---
tags:
  - core/app
  - di/flutter
---
# Cliente Flutter: AppScope

Mecanismo central de injeção de dependências do aplicativo, implementado como um `InheritedWidget` de alta performance sem bibliotecas externas.

- **Arquivo no App**: [`lib/core/app_scope.dart`](file:///home/jonas/Projects/flashmind/app-flashmind/lib/core/app_scope.dart)
- **Domínio**: [[Persistência e Arquitetura]]

---

## 📋 Responsabilidades

1. Prover instâncias únicas de serviços essenciais para toda a sub-árvore de widgets:
   - `deckService`: [[DeckService]]
   - `userProgressController`: [[UserProgressController]]
   - `reviewService`: [[ReviewService]]
2. Disponibilizar o método de conveniência estático `AppScope.of(context)`.
3. Determinar se os filhos precisam ser reconstruídos (`updateShouldNotify`).

---

## 💻 Código de Referência

```dart
class AppScope extends InheritedWidget {
  final DeckService deckService;
  final UserProgressController userProgressController;
  final ReviewService reviewService;

  const AppScope({
    super.key,
    required this.deckService,
    required this.userProgressController,
    required this.reviewService,
    required super.child,
  });

  static AppScope of(BuildContext context) {
    final scope = context.dependOnInheritedWidgetOfExactType<AppScope>();
    assert(scope != null, 'No AppScope found in context');
    return scope!;
  }

  @override
  bool updateShouldNotify(AppScope oldWidget) {
    return deckService != oldWidget.deckService ||
        userProgressController != oldWidget.userProgressController ||
        reviewService != oldWidget.reviewService;
  }
}
```

---

## 👥 Telas que Acessam o AppScope

Praticamente todas as telas do aplicativo usam `AppScope.of(context)`:
- [[HomeScreen]] (lê progresso, XP e decks)
- [[DecksScreen]] e [[DeckDetailsScreen]] (lê e comanda o DeckService)
- [[FlashcardSessionScreen]] (usa o ReviewService)
- [[StreakScreen]] (lê histórico de ofensiva)
