---
tags:
  - repository/flutter
  - feature/decks
---
# Repository: DeckRepository

Interface abstrata que define o contrato de persistência e recuperação de baralhos e cartões.

- **Arquivo no App**: [`lib/features/decks/repositories/deck_repository.dart`](file:///home/jonas/Projects/flashmind/app-flashmind/lib/features/decks/repositories/deck_repository.dart)
- **Domínio**: [[Gestão de Decks e Cartões]] e [[Persistência e Arquitetura]]

---

## 📋 Contrato Abstrato

```dart
abstract class DeckRepository {
  Future<List<Deck>> getDecks();
  Future<void> createDeck(Deck deck);
  Future<void> updateDeck(Deck deck);
  Future<void> deleteDeck(Deck deck);
  Future<void> addFlashcard(Deck deck, Flashcard flashcard);
  Future<void> deleteFlashcard(Deck deck, Flashcard flashcard);
}
```

---

## 🛠️ Implementações Atuais

1. **`LocalDeckRepository`** (`local_deck_repository.dart`):
   - Grava a lista de baralhos codificada como JSON no `SharedPreferences` (chave `'decks'`).
   - Se for a primeira inicialização (chave vazia), injeta automaticamente os 7 baralhos padrão de `decks_data.dart`.
2. **`InMemoryDeckRepository`** (`in_memory_deck_repository.dart`):
   - Mantém uma lista `List<Deck>` volátil em memória RAM.
   - Usado em testes unitários e de widget para máxima velocidade e isolamento.

---

## 🚀 Evolução Futura (Dual-DataSource)

Com a chegada da API (`api-flashmind`), esta interface será mantida, mas a implementação passará a delegar para um `LocalDataSource` ou `RemoteDataSource` com base no `AppConfig.useRemoteBackend`. Veja mais em [[Plano de Transição para a API]].
