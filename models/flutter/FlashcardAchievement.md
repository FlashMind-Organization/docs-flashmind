---
tags:
  - model/flutter
  - feature/flashcards
  - gamification
---
# Model: FlashcardAchievement

Representa uma conquista ou marco de desempenho alcançado pelo estudante durante a sessão de estudos.

- **Arquivo no App**: [`lib/features/flashcards/models/flashcard_achievement.dart`](file:///home/jonas/Projects/flashmind/app-flashmind/lib/features/flashcards/models/flashcard_achievement.dart)
- **Domínio**: [[Repetição Espaçada e Sessão]] e [[Gamificação e Progresso]]

---

## 📋 Estrutura e Prioridade

```dart
enum AchievementType {
  rank(1),
  level(2),
  bestStreak(3),
  streak(4),
  combo(5);

  final int priority;
  const AchievementType(this.priority);
}

class FlashcardAchievement {
  final AchievementType type;
  final String message;

  const FlashcardAchievement({required this.type, required this.message});
}
```

A prioridade define qual conquista tem precedência de exibição visual caso múltiplas sejam disparadas simultaneamente ao final de uma sessão.

---

## 👥 Quem Consome

- **Telas**: [[FlashcardSessionScreen]]
- **Widgets**: `achievement_banner.dart`
