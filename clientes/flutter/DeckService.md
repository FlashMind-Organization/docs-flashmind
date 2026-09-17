---
tags:
  - service/flutter
  - controller/flutter
  - feature/decks
---
# Service: DeckService

Serviço reativo e gerenciador de estado central (`ChangeNotifier`) para toda a coleção de baralhos e cartões do usuário.

- **Arquivo no App**: [`lib/features/decks/services/deck_service.dart`](file:///home/jonas/Projects/flashmind/app-flashmind/lib/features/decks/services/deck_service.dart)
- **Domínio**: [[Gestão de Decks e Cartões]]

---

## 📋 Métodos e Capacidades

### 1. Leitura e Inicialização
- `init()`: Carrega baralhos persistidos via `DeckRepository`. Se não houver nada salvo, o repositório semeia os decks iniciais.
- `decks`: Retorna lista imutável (`List.unmodifiable(_decks)`).
- `getDecks()`: Garante inicialização antes de retornar.

### 2. Criação, Edição e Exclusão de Decks
- `createDeck({title, description})`: Cria instância de [[Deck]] com timestamp, persiste no repositório e emite `notifyListeners()`.
- `updateDeck(deck)`: Atualiza propriedades e sincroniza cache em memória.
- `deleteDeck(deck)`: Remove baralho da persistência e da memória.

### 3. Gestão de Flashcards
- `addFlashcard({deck, question, answer})`: Cria novo [[Flashcard]], persiste no baralho e notifica ouvintes.
- `updateFlashcard({deck, flashcard, question, answer})`: Altera conteúdo do cartão.
- `deleteFlashcard({deck, flashcard})`: Remove cartão específico do baralho.

### 4. Validações de Domínio
- `validateTitle(title)`: Valida tamanho (1 a 100 caracteres) e presença.
- `validateTitleUnique(title, {excludeDeckId})`: Garante unicidade case-insensitive entre baralhos.
- `validateDescription(desc)`: Valida limite de 300 caracteres.
- `validateFlashcardUnique({deck, question, answer, excludeId})`: Impede cartões duplicados no mesmo baralho.

---

## 👥 Quem Consome Este Serviço

- Injetado em: [[AppScope]]
- Consumido por: [[ReviewService]], [[DecksScreen]], [[DeckDetailsScreen]], [[CreateDeckScreen]], [[HomeScreen]]
- Repositório utilizado: [[DeckRepository]]
