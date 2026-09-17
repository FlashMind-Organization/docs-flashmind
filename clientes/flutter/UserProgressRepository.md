---
tags:
  - repository/flutter
  - feature/progress
---
# Repository: UserProgressRepository

Contrato abstrato para persistência e recuperação do progresso, XP e histórico de ofensiva do estudante.

- **Arquivo no App**: [`lib/core/progress/repositories/user_progress_repository.dart`](file:///home/jonas/Projects/flashmind/app-flashmind/lib/core/progress/repositories/user_progress_repository.dart)
- **Domínio**: [[Gamificação e Progresso]] e [[Persistência e Arquitetura]]

---

## 📋 Contrato Abstrato

```dart
abstract class UserProgressRepository {
  Future<UserProgress?> getProgress();
  Future<void> saveProgress(UserProgress progress);
}
```

---

## 🛠️ Implementações Atuais

1. **`LocalUserProgressRepository`** (`local_user_progress_repository.dart`):
   - Grava e lê o objeto [[UserProgress]] codificado em JSON no `SharedPreferences` (chave `'user_progress'`).
2. **`InMemoryUserProgressRepository`** (`in_memory_user_progress_repository.dart`):
   - Mantém o objeto em memória para suíte de testes.

---

## 👥 Quem Consome

- [[UserProgressController]]
