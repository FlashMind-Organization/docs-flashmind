---
tags:
  - model/flutter
  - feature/home
---
# Model: Quote

Representa uma citação inspiradora ou reflexão sobre aprendizagem, foco e consistência.

- **Arquivo no App**: [`lib/features/home/models/quote.dart`](file:///home/jonas/Projects/flashmind/app-flashmind/lib/features/home/models/quote.dart)
- **Domínio**: [[Experiência do Usuário e Home]]

---

## 📋 Campos

```dart
class Quote {
  final String text;    // Texto da citação
  final String author;  // Autor / pensador

  const Quote({required this.text, required this.author});
}
```

O conjunto de citações é fornecido estaticamente em `quotes_data.dart`, trazendo frases de autores como Albert Einstein, Confúcio, Benjamin Franklin e James Clear.

---

## 👥 Quem Consome

- **Telas**: [[HomeScreen]]
- **Widgets**: `quote_card.dart`
