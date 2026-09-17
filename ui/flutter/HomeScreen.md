---
tags:
  - router/screen
  - feature/home
---
# Tela: HomeScreen

Ponto focal e dashboard de entrada do aplicativo FlashMind. Exibe a saúde do aprendizado diário, ofensiva ativa, nível e botão de ação rápida.

- **Arquivo no App**: [`lib/features/home/screens/home_screen.dart`](file:///home/jonas/Projects/flashmind/app-flashmind/lib/features/home/screens/home_screen.dart)
- **Domínio**: [[Experiência do Usuário e Home]]

---

## 📱 Estrutura Visual e Componentes

1. **`HeaderSection`**:
   - Mensagem de saudação de acordo com a hora local.
   - Ícone de engrenagem que abre o `SettingsBottomSheet`.
2. **`LevelCard`**:
   - Mostra o nível atual do estudante, título de maestria (ex: "Desbravador"), XP acumulado e barra percentual até o próximo nível.
3. **`StatsSection`**:
   - Três cartões informativos:
     - Revisões feitas hoje
     - Dias de ofensiva atual (ao tocar, navega para a [[StreakScreen]])
     - Total de dias de estudo acumulados
4. **`QuoteCard`**:
   - Exibe citação reflexiva aleatória sobre foco e estudo.
5. **`StartButton`**:
   - Botão de ação principal. Se houver baralhos com cartões pendentes de revisão (`card.isDue`), inicia imediatamente a revisão ou direciona para a [[DecksScreen]].

---

## 🔗 Dependências e Serviços

- Acessa [[AppScope]] para obter:
  - `userProgressController`: escuta via `ListenableBuilder` para atualizar o card de nível e estatísticas instantaneamente.
  - `deckService`: escuta mudanças no total de baralhos e cartões pendentes.
- Navegação:
  - Para [[DecksScreen]] via `Navigator.push(...)`.
  - Para [[StreakScreen]] via toque no card de ofensiva.
  - Para `SettingsBottomSheet` via modal inferior.
