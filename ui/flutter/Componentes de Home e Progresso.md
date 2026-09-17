---
tags:
  - component/flutter
  - feature/home
  - feature/progress
---
# Componentes: Home e Progresso

Componentes reutilizáveis utilizados no dashboard inicial e nas telas de acompanhamento de ofensiva.

- **Diretórios no App**:
  - [`lib/features/home/widgets/`](file:///home/jonas/Projects/flashmind/app-flashmind/lib/features/home/widgets/)
  - [`lib/features/progress/widgets/`](file:///home/jonas/Projects/flashmind/app-flashmind/lib/features/progress/widgets/)
- **Domínios**: [[Experiência do Usuário e Home]] e [[Gamificação e Progresso]]

---

## 🧩 Catálogo de Componentes

### 1. `LevelCard` (`level_card.dart`)
- **Papel**: Renderiza o cartão de nível do usuário.
- **Detalhes**:
  - Badge circular com o número do nível (ex: "Lv. 3").
  - Título correspondente ao patamar (ex: "Praticante").
  - Barra de progresso percentual e contagem "XP: 140 / 200".

### 2. `StatsSection` (`stats_section.dart`)
- **Papel**: Grade de 3 cartões compactos:
  - *Revisões Hoje*: quantidade de cards revisados no dia atual.
  - *Ofensiva*: dias consecutivos de estudo (ao clicar, abre a [[StreakScreen]]).
  - *Total de Dias*: histórico acumulado de consistência.

### 3. `QuoteCard` (`quote_card.dart`)
- **Papel**: Card estético com ícone de aspas contendo uma citação motivacional e o nome do pensador.

### 4. `StartButton` (`start_button.dart`)
- **Papel**: Botão primário com ícone de reprodução/estudo para acionar a revisão do dia.

### 5. `HeaderSection` (`header_section.dart`)
- **Papel**: Saudação de boas-vindas e acesso ao painel de configurações.

### 6. `SettingsBottomSheet` (`settings_bottom_sheet.dart`)
- **Papel**: Modal de opções contendo:
  - Alternância de tema claro/escuro.
  - Informações de versão.
  - Botão de reset de dados para testes.

### 7. `StreakCalendar` (`streak_calendar.dart`)
- **Papel**: Widget da [[StreakScreen]] que renderiza o grid mensal de dias com preenchimento colorido para as datas presentes na lista `studyDays`.
