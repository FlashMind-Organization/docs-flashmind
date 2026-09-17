---
tags:
  - dominio
  - feature/flashcards
  - srs
---
# Domínio: Repetição Espaçada e Sessão de Estudo

Este domínio é o coração pedagógico do **FlashMind**. Ele implementa um algoritmo adaptado de repetição espaçada (inspirado no Leitner System e SuperMemo SM-2 simplificado), proporcionando revisão no momento ótimo da curva do esquecimento de Ebbinghaus.

---

## 📚 Como Funciona o Algoritmo de SRS

O serviço responsável é o [[SpacedRepetitionService]]. Ele opera baseado em **Passos de Revisão (`reviewStep`)** que mapeiam para intervalos de tempo pré-fixados:

```text
Passo 0: 1 minuto
Passo 1: 5 minutos
Passo 2: 15 minutos
Passo 3: 1 hora
Passo 4: 6 horas
Passo 5: 1 dia       ← Card considerado 'Dominado' (isMastered)
Passo 6: 3 dias
Passo 7: 7 dias
Passo 8: 15 dias
Passo 9: 30 dias
```

### Avaliação do Usuário ([[ReviewRating]])

Ao revisar a resposta de um flashcard, o usuário escolhe entre três opções:

| Classificação | Valor Interno | Efeito no `reviewStep` | Efeito no Agendamento | XP Ganho |
|---|---|---|---|---|
| **Não sabia** | `forgot` | Volta para `0` | Reagendado para daqui a 1 min | **+5 XP** (Zera combo) |
| **Difícil** | `difficult` | Recua 2 passos: `max(0, step - 2)` | Reagendado com intervalo reduzido | **+10 XP** (Mantém combo) |
| **Fácil** | `easy` | Avança 1 passo: `min(9, step + 1)` | Reagendado para o próximo intervalo maior | **+15 XP** (Incrementa combo) |

---

## 🔄 Ciclo de Vida do Cartão

Um cartão ([[Flashcard]]) transita entre 3 estados semânticos:

1. **Novo (New)**: `timesReviewed == 0` (nunca revisado).
2. **Em Aprendizado (isInProgress)**: `timesReviewed > 0 && reviewStep < 5`.
3. **Dominado (isMastered)**: `reviewStep >= 5` (alcançou intervalo de 1 dia ou mais).

A propriedade `isDue` determina se o cartão está pronto para ser revisado:
```dart
bool get isDue => nextReviewAt.isBefore(DateTime.now());
```

---

## 🧩 Orquestração da Sessão

A tela [[FlashcardSessionScreen]] comanda o fluxo de estudo:
1. Filtra os cartões do baralho que estão pendentes (`card.isDue`).
2. Exibe o cartão com animação 3D de flip (Frente: pergunta / Verso: resposta).
3. Ao avaliar, aciona [[ReviewService#reviewFlashcard]].
4. O `ReviewService` orquestra:
   - Recálculo de `nextReviewAt` e `reviewStep` via [[SpacedRepetitionService]].
   - Persistência das alterações via [[DeckService]].
   - Cálculo de XP, nível e streak via [[GamificationService]].
   - Atualização reativa de progresso via [[UserProgressController]].
5. Ao concluir todos os cartões, exibe tela de encerramento com estatísticas da sessão e [[FlashcardAchievement]].

---

## 🔗 Componentes e Telas Relacionados

- Tela principal: [[FlashcardSessionScreen]]
- Telas de edição: [[CreateFlashcardScreen]], [[EditFlashcardScreen]]
- Componentes visuais:
  - `flashcard_view.dart` (Card flip animado)
  - `answer_buttons.dart` (Botões de Não sabia, Difícil, Fácil)
  - `session_progress.dart` (Barra de progresso de cartões concluídos)
  - `session_header.dart` (Contador e botão de sair)
  - `xp_gain_label.dart` (Animação de XP flutuante)
  - `achievement_banner.dart` (Banner comemorativo de maestria)
  - `srs_help_bottom_sheet.dart` (Guia explicativo sobre a curva de repetição)
- Entidades: [[Flashcard]], [[ReviewRating]], [[FlashcardAchievement]]
- Serviços: [[ReviewService]], [[SpacedRepetitionService]], [[GamificationService]]
