---
tags:
  - dominio
  - feature/home
  - ux
---
# Domínio: Experiência do Usuário e Home

Este domínio abrange a interface de entrada e acolhimento do estudante no **FlashMind**, servindo como centro de comando diário. É projetado com foco em clareza, ausência de atritos e motivação contínua.

---

## 🏠 Anatomia da Tela Principal ([[HomeScreen]])

A tela inicial reúne em uma única visão vertical os elementos essenciais para que o usuário saiba imediatamente o que fazer:

1. **Cabeçalho (`header_section.dart`)**:
   - Saudação personalizada de acordo com o período do dia (Bom dia, Boa tarde, Boa noite).
   - Botão de acesso rápido às configurações e temas via bottom sheet.
2. **Card de Nível (`level_card.dart`)**:
   - Indicador visual do nível do usuário, título de maestria (ex: "Desbravador"), barra animada de XP e cálculo exato de quanto falta para o próximo nível.
3. **Seção de Estatísticas Rápidas (`stats_section.dart`)**:
   - Cartões com números chave: revisões de hoje, ofensiva ativa e dias totais de estudo.
   - Toque no card de ofensiva navega diretamente para a [[StreakScreen]].
4. **Card de Frase Motivacional (`quote_card.dart`)**:
   - Seleção randômica ou rotativa de citações de pensadores e cientistas sobre aprendizado, disciplina e persistência (a partir de `quotes_data.dart`).
5. **Botão de Ação Primária (`start_button.dart`)**:
   - CTA destacado ("Revisar Agora" ou "Ver Baralhos"), direcionando para a sessão de revisão se houver cartões pendentes, ou para a [[DecksScreen]].
6. **Onboarding e Guias**:
   - Uso de `showcaseview` para instruir novos usuários sobre o funcionamento do aplicativo no primeiro acesso (`onboarding_tooltip.dart`).

---

## 🎨 Temas e Preferências Visuais

O app possui suporte nativo completo a **Modo Claro (Light)** e **Modo Escuro (Dark)**, gerenciado no topo da árvore de widgets em `main.dart` (`FlashcardApp`):

- **Paleta Primária**: Indigo (`#6366F1`), transmitindo foco, inteligência e modernidade.
- **Fundo Claro**: `#F6F7FB` com superfícies em branco puro (`#FFFFFF`) e bordas suaves (`#E4E4E7`).
- **Fundo Escuro**: `#0F1115` com cards em cinza escuro (`#18181B`) e bordas em cinza neutro (`#27272A`).
- **Persistência de Tema**: O índice do modo de tema escolhido (`ThemeMode.light`, `ThemeMode.dark`, `ThemeMode.system`) é gravado na chave `theme_mode` do `SharedPreferences`.

---

## ⚙️ Ações de Manutenção e Configurações

Através do `settings_bottom_sheet.dart`, o usuário pode:
- Alternar o tema da interface entre Claro, Escuro ou Seguir o Sistema.
- Consultar a versão e informações de desenvolvimento.
- **Resetar Dados Locais**: Permite limpar o armazenamento local para fins de testes ou recomeço dos estudos, reinicializando com os decks padrão.

---

## 🔗 Componentes e Telas Relacionados

- Telas:
  - [[HomeScreen]]: Dashboard principal.
  - [[DecksScreen]]: Navegação a partir da Home.
  - [[StreakScreen]]: Navegação a partir do card de ofensiva.
- Componentes Visuais:
  - `header_section.dart`: Saudação e botão de ajustes.
  - `level_card.dart`: Nível e barra de XP.
  - `stats_section.dart`: Métricas diárias.
  - `quote_card.dart`: Citações de aprendizado.
  - `start_button.dart`: Ação rápida.
  - `settings_bottom_sheet.dart`: Painel de configurações.
  - `stats_help_bottom_sheet.dart`: Modal de ajuda sobre o que cada métrica significa.
- Entidades: [[Quote]], `stats_data.dart`, [[UserProgress]]
