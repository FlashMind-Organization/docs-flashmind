---
tags:
  - service/flutter
  - srs
  - feature/flashcards
---
# Service: SpacedRepetitionService

Implementação pura do algoritmo de repetição espaçada no Flutter, sem dependências de UI.

- **Arquivo no App**: [`lib/features/flashcards/services/spaced_repetition_service.dart`](file:///home/jonas/Projects/flashmind/app-flashmind/lib/features/flashcards/services/spaced_repetition_service.dart)
- **Domínio**: [[Repetição Espaçada e Sessão]]
- **Guia Detalhado**: [[Algoritmo SRS e Gamificação]]

---

## 📋 Escala de Intervalos

```dart
static const reviewIntervals = [
  Duration(minutes: 1),
  Duration(minutes: 5),
  Duration(minutes: 15),
  Duration(hours: 1),
  Duration(hours: 6),
  Duration(days: 1),
  Duration(days: 3),
  Duration(days: 7),
  Duration(days: 15),
  Duration(days: 30),
];
```

---

## ⚙️ Método: `reviewCard(Flashcard card, ReviewRating rating)`

Modifica o estado interno da entidade [[Flashcard]]:
1. Incrementa `card.timesReviewed++`.
2. Registra `card.lastReviewedAt = DateTime.now()`.
3. Ajusta `reviewStep` de acordo com a nota:
   - `forgot`: `reviewStep = 0`
   - `difficult`: `reviewStep = max(0, reviewStep - 2)`
   - `easy`: `reviewStep = min(9, reviewStep + 1)`
4. Recalcula `nextReviewAt = DateTime.now().add(reviewIntervals[card.reviewStep])`.

---

## 👥 Quem Consome

- [[ReviewService]]
- Testes automatizados em `test/features/flashcards/`
