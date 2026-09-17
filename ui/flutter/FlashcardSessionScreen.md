---
tags:
  - router/screen
  - feature/flashcards
  - srs
---
# Tela: FlashcardSessionScreen

Tela principal do ciclo de estudo e repetição espaçada. Oferece a experiência tátil de virar os cartões e classificá-los para reagendamento.

- **Arquivo no App**: [`lib/features/flashcards/screens/flashcard_session_screen.dart`](file:///home/jonas/Projects/flashmind/app-flashmind/lib/features/flashcards/screens/flashcard_session_screen.dart)
- **Domínio**: [[Repetição Espaçada e Sessão]]

---

## 📱 Fluxo da Sessão

1. **Início da Sessão**:
   - A tela recebe a lista de cartões pendentes de revisão (`isDue`) do baralho selecionado.
   - Se não houver cartões pendentes, exibe o widget `empty_review_state.dart`.
2. **Visualização do Cartão (`FlashcardView`)**:
   - Apresenta inicialmente a pergunta frontal.
   - Ao tocar no cartão ou no botão "Virar Cartão", uma animação tridimensional (3D Flip com `Matrix4.identity()..rotateY(...)`) revela a resposta no verso.
3. **Avaliação (`AnswerButtons`)**:
   - Uma vez virado o cartão, os botões de resposta são exibidos:
     - **"Não sabia"** (`ReviewRating.forgot`) -> +5 XP
     - **"Difícil"** (`ReviewRating.difficult`) -> +10 XP
     - **"Fácil"** (`ReviewRating.easy`) -> +15 XP
4. **Processamento da Resposta**:
   - Dispara `ReviewService.reviewFlashcard(...)`.
   - Exibe a animação do XP ganho flutuando na tela (`XpGainLabel`).
   - Avança para o próximo cartão com animação suave.
5. **Encerramento da Sessão**:
   - Ao revisar o último cartão, renderiza a tela de congratulações com:
     - Total de cartões revisados
     - Total de XP acumulado na sessão
     - Banner comemorativo de conquistas (`AchievementBanner`)
     - Botão para retornar à Home ou aos Baralhos.

---

## 🔗 Dependências

- [[ReviewService]]: comanda o ciclo de revisão, recalcula intervalos e credita XP.
- [[SpacedRepetitionService]]: aplica a curva do esquecimento.
- [[GamificationService]]: calcula novos patamares de nível.
- Modelos: [[Deck]], [[Flashcard]], [[ReviewRating]], [[FlashcardAchievement]]
- Componentes Visuais:
  - `flashcard_view.dart`
  - `answer_buttons.dart`
  - `session_progress.dart`
  - `session_header.dart`
  - `xp_gain_label.dart`
  - `achievement_banner.dart`
  - `srs_help_bottom_sheet.dart`
