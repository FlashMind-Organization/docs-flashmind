---
tags:
  - router/screen
  - feature/flashcards
---
# Tela: CreateFlashcardScreen

Formulário para inclusão de um novo flashcard dentro de um baralho selecionado.

- **Arquivo no App**: [`lib/features/flashcards/screens/create_flashcard_screen.dart`](file:///home/jonas/Projects/flashmind/app-flashmind/lib/features/flashcards/screens/create_flashcard_screen.dart)
- **Domínio**: [[Gestão de Decks e Cartões]]

---

## 📱 Estrutura do Formulário

1. **Campo Pergunta (Frente)**:
   - `TextFormField` multilinhas.
   - Validação de preenchimento obrigatório.
2. **Campo Resposta (Verso)**:
   - `TextFormField` multilinhas com suporte a explicações detalhadas ou blocos de código/conceitos.
   - Validação de preenchimento obrigatório.
3. **Validação de Duplicidade**:
   - `DeckService.validateFlashcardUnique`: impede cadastrar exatamente o mesmo par pergunta/resposta no baralho.
4. **Ação de Salvar**:
   - Invoca `DeckService.addFlashcard(...)`.
   - Fecha a tela e retorna à tela anterior com notificação de sucesso.

---

## 🔗 Dependências

- `CreateFlashcardController`
- [[DeckService]]
- Entidades: [[Deck]], [[Flashcard]]
