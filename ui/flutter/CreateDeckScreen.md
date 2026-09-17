---
tags:
  - router/screen
  - feature/decks
---
# Tela: CreateDeckScreen

Formulário para cadastro de um novo baralho de flashcards com validações em tempo real.

- **Arquivo no App**: [`lib/features/decks/screens/create_deck_screen.dart`](file:///home/jonas/Projects/flashmind/app-flashmind/lib/features/decks/screens/create_deck_screen.dart)
- **Domínio**: [[Gestão de Decks e Cartões]]

---

## 📱 Campos do Formulário e Validações

1. **Campo Título (`TextFormField`)**:
   - Obrigatório.
   - Máximo de 100 caracteres.
   - Validação assíncrona de unicidade através de `DeckService.validateTitleUnique`.
2. **Campo Descrição (`TextFormField`)**:
   - Opcional.
   - Máximo de 300 caracteres.
3. **Botão Salvar Baralho**:
   - Valida o formulário.
   - Invoca `DeckService.createDeck(...)`.
   - Fecha a tela retornando para a lista de baralhos com feedback de sucesso.

---

## 🔗 Dependências

- `CreateDeckController`: controlador de validações e estado do formulário.
- [[DeckService]]: responsável pela persistência do novo baralho.
