---
tags:
  - router/screen
  - feature/progress
  - gamification
---
# Tela: StreakScreen

Tela detalhada dedicada ao monitoramento da ofensiva diária, consistência de estudos e calendário de frequência.

- **Arquivo no App**: [`lib/features/progress/screens/streak_screen.dart`](file:///home/jonas/Projects/flashmind/app-flashmind/lib/features/progress/screens/streak_screen.dart)
- **Domínio**: [[Gamificação e Progresso]]

---

## 📱 Estrutura Visual

1. **Card de Destaque da Ofensiva**:
   - Ícone de fogo animado / destacado.
   - Número atual de dias consecutivos (`streakDays`).
   - Mensagem de incentivo e recorde histórico (`bestStreak`).
2. **Calendário Mensal (`StreakCalendar`)**:
   - Visualização dos dias do mês atual.
   - Destaque visual colorido nos dias em que houve ao menos uma sessão registrada (`studyDays`).
   - Identificação do dia de hoje e status da ofensiva de hoje.
3. **Resumo Numérico de Consistência**:
   - Total absoluto de dias estudados desde o início.
   - Maior sequência contínua de dias.

---

## 🔗 Dependências

- `StreakController`: coordena os meses exibidos no calendário e formatação de datas.
- [[UserProgressController]]: provê os dados em tempo real de [[UserProgress]].
- Widget filho: `streak_calendar.dart`.
