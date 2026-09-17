---
tags:
  - model/flutter
  - feature/progress
  - gamification
---
# Model: UserProgress

Entidade que encapsula todas as métricas de engajamento, gamificação, experiência acumulada e dias de estudo consecutivos do usuário.

- **Arquivo no App**: [`lib/core/progress/models/user_progress.dart`](file:///home/jonas/Projects/flashmind/app-flashmind/lib/core/progress/models/user_progress.dart)
- **Domínio**: [[Gamificação e Progresso]]

---

## 📋 Campos e Tipos

| Campo | Tipo | Descrição |
|---|---|---|
| `totalXp` | `int` | Total de pontos de experiência acumulados |
| `streakDays` | `int` | Sequência atual de dias consecutivos de estudo |
| `lastStudyDate` | `DateTime?` | Data do último estudo registrado |
| `combo` | `int` | Sequência consecutiva de avaliações fáceis na sessão atual |
| `bestStreak` | `int` | Recorde histórico de ofensiva em dias |
| `totalStudyDays` | `int` | Contagem total absoluta de dias únicos com estudo |
| `studyDays` | `List<DateTime>` | Lista de dias com estudo (usada no calendário e heatmaps) |
| `reviewsToday` | `int` | Quantidade de cartões revisados no dia corrente |

---

## 🧮 Lógica de Nível e Títulos

```dart
// Cálculo iterativo do nível a partir do XP acumulado
int get level {
  int l = 1;
  while (totalXp >= totalXpRequiredForLevel(l + 1)) {
    l++;
  }
  return l;
}

// XP ganho dentro do nível atual
int get currentLevelXp => totalXp - totalXpRequiredForLevel(level);

// XP que ainda falta para atingir o próximo nível
int get xpForNextLevel => xpRequiredForLevel(level) - currentLevelXp;

// Progresso percentual dentro do nível atual (0.0 a 1.0)
double get levelProgress => currentLevelXp / xpRequiredForLevel(level);

// Título de maestria
String get title {
  if (level >= 10) return 'Mestre';
  if (level >= 9) return 'Sábio';
  if (level >= 8) return 'Guardião';
  if (level >= 7) return 'Especialista';
  if (level >= 6) return 'Veterano';
  if (level >= 5) return 'Desbravador';
  if (level >= 4) return 'Explorador';
  if (level >= 3) return 'Praticante';
  if (level >= 2) return 'Aprendiz';
  return 'Iniciante';
}
```

---

## 👥 Quem Consome Este Modelo

- **Serviços / Controllers**: [[GamificationService]], [[UserProgressController]], [[ReviewService]]
- **Repositórios**: [[UserProgressRepository]], `LocalUserProgressRepository`
- **Telas**: [[HomeScreen]], [[StreakScreen]], [[FlashcardSessionScreen]]
- **Widgets**: `level_card.dart`, `stats_section.dart`, `streak_calendar.dart`
