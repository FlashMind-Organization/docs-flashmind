---
tags:
  - model/flutter
  - feature/decks
---
# Model: Deck

Representa um baralho de estudo no aplicativo Flutter. Agrupa flashcards com tema comum e gerencia o cálculo de progresso de estudo.

- **Arquivo no App**: [`lib/features/decks/models/deck.dart`](file:///home/jonas/Projects/flashmind/app-flashmind/lib/features/decks/models/deck.dart)
- **Domínio**: [[Gestão de Decks e Cartões]]

---

## 📋 Campos e Tipos

| Campo | Tipo | Descrição |
|---|---|---|
| `id` | `String` | Identificador único (gerado via timestamp em microssegundos se nulo) |
| `title` | `String` | Título do baralho (máximo 100 caracteres) |
| `description` | `String` | Descrição opcional (máximo 300 caracteres) |
| `flashcards` | `List<Flashcard>` | Coleção de flashcards pertencentes ao baralho |
| `createdAt` | `DateTime` | Data e hora de criação |
| `updatedAt` | `DateTime` | Data e hora da última modificação |

---

## 🧮 Getters e Propriedades Computadas

```dart
int get totalCards => flashcards.length;

int get reviewedCards {
  final now = DateTime.now();
  return flashcards.where((card) => card.nextReviewAt.isAfter(now)).length;
}

double get progress {
  if (totalCards == 0) return 0;
  return reviewedCards / totalCards;
}
```

---

## 🔄 Métodos de Serialização e Cópia

- `toJson()`: Serializa o objeto e a lista de `Flashcard` em um `Map<String, dynamic>` para armazenamento no SharedPreferences.
- `Deck.fromJson(Map<String, dynamic> json)`: Desserializa o JSON tratando nulos e parsing de datas ISO 8601.
- `copyWith(...)`: Cria uma nova instância com campos modificados de forma imutável.

---

## 👥 Quem Consome Este Modelo

- **Serviços**: [[DeckService]], [[ReviewService]]
- **Repositórios**: [[DeckRepository]], `LocalDeckRepository`, `InMemoryDeckRepository`
- **Telas**: [[DecksScreen]], [[DeckDetailsScreen]], [[FlashcardSessionScreen]], [[HomeScreen]]
- **Widgets**: `deck_list_item.dart`, `decks_summary.dart`
