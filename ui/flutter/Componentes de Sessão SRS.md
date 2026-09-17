---
tags:
  - component/flutter
  - feature/flashcards
  - srs
---
# Componentes: Sessão SRS

Componentes visuais e interativos especializados na sessão de estudo e repetição espaçada.

- **Diretório no App**: [`lib/features/flashcards/widgets/`](file:///home/jonas/Projects/flashmind/app-flashmind/lib/features/flashcards/widgets/)
- **Domínio**: [[Repetição Espaçada e Sessão]]

---

## 🧩 Catálogo de Componentes

### 1. `FlashcardView` (`flashcard_view.dart`)
- **Papel**: Cartão com animação de flip tridimensional (`Transform` com matriz de perspectiva `rotateY`).
- **Estados**:
  - Frente: texto da pergunta, etiqueta de "Pergunta", ícone de toque para virar.
  - Verso: texto da resposta, etiqueta de "Resposta", cores de contraste aprimoradas.

### 2. `AnswerButtons` (`answer_buttons.dart`)
- **Papel**: Barra inferior com os 3 botões de avaliação:
  - Vermelho: "Não sabia" (`ReviewRating.forgot`)
  - Amarelo: "Difícil" (`ReviewRating.difficult`)
  - Indigo/Verde: "Fácil" (`ReviewRating.easy`)
- **Visibilidade**: Exibido somente após o cartão ser virado para o verso.

### 3. `SessionProgress` (`session_progress.dart`)
- **Papel**: Barra linear de progresso no topo da tela mostrando o percentual da sessão concluído (ex: "4 de 12 cartões").

### 4. `SessionHeader` (`session_header.dart`)
- **Papel**: Botão de fechar/sair da sessão, nome do baralho atual e botão de ajuda com o modal de SRS.

### 5. `XpGainLabel` (`xp_gain_label.dart`)
- **Papel**: Efeito visual de micro-recompensa: exibe um rótulo animado com "+15 XP" ou "+10 XP" subindo e desaparecendo suavemente na tela após a avaliação.

### 6. `AchievementBanner` (`achievement_banner.dart`)
- **Papel**: Banner festivo comemorando marcos como novo nível, novo recorde de ofensiva ou combo estendido.

### 7. `EmptyReviewState` (`empty_review_state.dart`)
- **Papel**: Ilustração e mensagem encorajadora quando todos os cartões do baralho já foram revisados e estão em dia.

### 8. `SrsHelpBottomSheet` (`srs_help_bottom_sheet.dart`)
- **Papel**: Explicação pedagógica para o usuário sobre a curva do esquecimento e como os botões influenciam os intervalos.
