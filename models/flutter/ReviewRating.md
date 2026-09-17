---
tags:
  - model/flutter
  - enum/flutter
  - srs
---
# Enum: ReviewRating

Classificação atribuída pelo usuário ao avaliar sua retenção durante uma sessão de estudo.

- **Arquivo no App**: [`lib/features/flashcards/models/review_rating.dart`](file:///home/jonas/Projects/flashmind/app-flashmind/lib/features/flashcards/models/review_rating.dart)
- **Domínio**: [[Repetição Espaçada e Sessão]]

---

## 📋 Valores e Rótulos

```dart
enum ReviewRating { forgot, difficult, easy }
```

| Valor do Enum | Rótulo da Interface (`label`) | Efeito no SRS | Ganho de XP | Cor Típica |
|---|---|---|---|---|
| `forgot` | **"Não sabia"** | Reseta o passo para 0 (1 min) | +5 XP | Vermelho / Amber |
| `difficult` | **"Difícil"** | Recua 2 passos: `max(0, step - 2)` | +10 XP | Laranja / Amarelo |
| `easy` | **"Fácil"** | Avança 1 passo: `min(9, step + 1)` | +15 XP | Verde / Indigo |

---

## 👥 Quem Consome Este Enum

- **Serviços**: [[SpacedRepetitionService]], [[GamificationService]], [[ReviewService]]
- **Telas e Widgets**: [[FlashcardSessionScreen]], `answer_buttons.dart`
