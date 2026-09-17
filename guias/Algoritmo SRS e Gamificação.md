---
tags:
  - guia
  - srs
  - gamification
---
# Guia: Algoritmo SRS e Sistema de Gamificação

Este guia aprofunda a implementação matemática e a lógica de regras de negócio por trás da repetição espaçada e da gamificação no **FlashMind**.

---

## 1. Algoritmo de Repetição Espaçada (SRS)

A classe [[SpacedRepetitionService]] é o motor que calcula quando um cartão deve ser revisitado.

### 1.1 Tabela de Intervalos Fixos

O sistema adota uma escala exponencial de 10 passos:

```dart
static const reviewIntervals = [
  Duration(minutes: 1),   // Passo 0
  Duration(minutes: 5),   // Passo 1
  Duration(minutes: 15),  // Passo 2
  Duration(hours: 1),     // Passo 3
  Duration(hours: 6),     // Passo 4
  Duration(days: 1),      // Passo 5 -> isMastered = true
  Duration(days: 3),      // Passo 6
  Duration(days: 7),      // Passo 7
  Duration(days: 15),     // Passo 8
  Duration(days: 30),     // Passo 9
];
```

### 1.2 Transições de Estado por Avaliação

Para cada avaliação submetida pelo estudante:

```dart
card.timesReviewed++;
card.lastReviewedAt = DateTime.now();

switch (rating) {
  case ReviewRating.forgot:
    // Erro crítico: reinicia a curva do zero
    card.reviewStep = 0;
    break;

  case ReviewRating.difficult:
    // Dificuldade média: recua 2 passos para reforço
    card.reviewStep = max(0, card.reviewStep - 2);
    break;

  case ReviewRating.easy:
    // Sucesso: avança para o próximo patamar de retenção
    if (card.reviewStep < reviewIntervals.length - 1) {
      card.reviewStep++;
    }
    break;
}

card.nextReviewAt = DateTime.now().add(reviewIntervals[card.reviewStep]);
```

---

## 2. Sistema de Gamificação e Recompensas

A classe [[GamificationService]] gerencia a economia de experiência (XP) e a consistência do usuário.

### 2.1 Matriz de XP por Desempenho

| Ação / Avaliação | XP Base Concedido | Impacto no Combo |
|---|---|---|
| `ReviewRating.forgot` | **5 XP** | Reseta combo para 0 |
| `ReviewRating.difficult` | **10 XP** | Mantém combo atual |
| `ReviewRating.easy` | **15 XP** | Incrementa combo (+1) |

> **Nota**: O método `applyReview` aceita um parâmetro opcional `customXp` para cenários futuros onde bônus de eventos ou cartas raras concedam recompensas especiais.

### 2.2 Curva de Nível (Progressão Aritmética)

A progressão não é linear nem puramente exponencial; ela cresce de forma sustentável para manter o engajamento:

- **XP necessário para subir do nível $N$ para o nível $N+1$**:
  $$XP_{\text{necessário}}(N) = 100 + (N - 1) \times 50$$

- **Exemplos práticos de evolução**:
  - Do Nível 1 para o 2: precisa de **100 XP** (~7 cartões fáceis)
  - Do Nível 2 para o 3: precisa de **150 XP** (~10 cartões fáceis)
  - Do Nível 3 para o 4: precisa de **200 XP** (~13 cartões fáceis)
  - Do Nível 4 para o 5: precisa de **250 XP** (~17 cartões fáceis)

### 2.3 Cálculo Inteligente de Ofensiva (*Streak*)

O algoritmo compara a data atual com `lastStudyDate` normalizadas em ano, mês e dia (desconsiderando horas e minutos):

```dart
final today = DateTime(now.year, now.month, now.day);
final lastDay = DateTime(last.year, last.month, last.day);

if (lastDay != today) {
  final isConsecutive = lastDay.add(const Duration(days: 1)) == today;
  streakDays = isConsecutive ? streakDays + 1 : 1;
  lastStudyDate = today;
  combo = 0;
  reviewsToday = 1;
} else {
  reviewsToday++; // Já estudou hoje, apenas acumula revisões do dia
}
```

Isso garante que:
- Múltiplas sessões no mesmo dia somem no total diário de revisões sem inflar a contagem de dias de ofensiva.
- Estudar em dias subsequentes (ex: terça às 23h e quarta às 08h) conte como 2 dias de ofensiva.
- Perder um dia inteiro sem estudar resete a ofensiva para 1 no próximo dia estudado.
