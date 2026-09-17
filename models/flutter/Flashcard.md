---
tags:
  - model/flutter
  - feature/flashcards
  - srs
---
# Model: Flashcard

Representa um cartão de memorização individual contendo pergunta, resposta e o estado de agendamento na repetição espaçada.

- **Arquivo no App**: [`lib/features/flashcards/models/flashcard.dart`](file:///home/jonas/Projects/flashmind/app-flashmind/lib/features/flashcards/models/flashcard.dart)
- **Domínio**: [[Repetição Espaçada e Sessão]]

---

## 📋 Campos e Tipos

| Campo | Tipo | Descrição |
|---|---|---|
| `id` | `String` | Identificador único do cartão |
| `question` | `String` | Pergunta ou conceito frontal do cartão |
| `answer` | `String` | Resposta ou explicação no verso |
| `reviewStep` | `int` | Índice na escala de intervalos (0 a 9) |
| `timesReviewed` | `int` | Quantidade total de vezes que foi revisado |
| `nextReviewAt` | `DateTime` | Data e hora em que o cartão fica pendente para estudo |
| `lastReviewedAt` | `DateTime?` | Data e hora da última revisão realizada |

---

## 🧮 Getters e Estados do Cartão

```dart
// Verdadeiro quando a data agendada já passou ou é agora
bool get isDue => nextReviewAt.isBefore(DateTime.now());

// Cartão considerado dominado quando atinge o passo 5 (intervalo de 1 dia ou mais)
bool get isMastered => reviewStep >= 5;

// Cartão em fase ativa de aprendizado
bool get isInProgress => timesReviewed > 0 && !isMastered;
```

---

## 🔄 Métodos de Serialização

- `toJson()`: Converte campos e datas ISO 8601 em `Map<String, dynamic>`.
- `Flashcard.fromJson(Map<String, dynamic> json)`: Reconstrói o cartão a partir do storage.
- `copyWith(...)`: Cria cópia alterando propriedades específicas.

---

## 👥 Quem Consome Este Modelo

- **Serviços**: [[SpacedRepetitionService]], [[ReviewService]], [[DeckService]]
- **Telas**: [[FlashcardSessionScreen]], [[CreateFlashcardScreen]], [[EditFlashcardScreen]], [[DeckDetailsScreen]]
- **Widgets**: `flashcard_view.dart`, `session_progress.dart`
