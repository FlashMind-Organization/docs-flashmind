---
tags:
  - controller/flutter
  - gamification
  - feature/progress
---
# Controller: UserProgressController

Gerenciador de estado reativo (`ChangeNotifier`) responsável por manter em memória e persistir o estado do usuário ([[UserProgress]]).

- **Arquivo no App**: [`lib/core/progress/controllers/user_progress_controller.dart`](file:///home/jonas/Projects/flashmind/app-flashmind/lib/core/progress/controllers/user_progress_controller.dart)
- **Domínio**: [[Gamificação e Progresso]]

---

## 📋 Responsabilidades

1. Inicialização (`init()`): Carrega o progresso salvo via [[UserProgressRepository]]. Se não existir, inicia com progresso padrão (0 XP, nível 1).
2. Fornecimento do estado atual: `progress` retorna a instância de [[UserProgress]].
3. Atualização e Notificação (`setProgress(updatedProgress)`):
   - Atualiza o estado em memória.
   - Persiste no repositório de forma assíncrona.
   - Emite `notifyListeners()` para reconstruir widgets inscritos (`HomeScreen`, `LevelCard`, etc.).

---

## 👥 Quem Consome

- Injetado em: [[AppScope]]
- Consumido por: [[ReviewService]], [[HomeScreen]], `level_card.dart`, `stats_section.dart`, [[StreakScreen]]
- Repositório utilizado: [[UserProgressRepository]]
