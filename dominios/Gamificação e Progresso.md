---
tags:
  - dominio
  - feature/progress
  - gamification
---
# Domínio: Gamificação e Progresso

O domínio de gamificação do **FlashMind** transforma o estudo repetitivo em um hábito consistente, estimulando a disciplina diária através de pontuação de experiência (XP), progressão de níveis, combos de acertos e controle contínuo de ofensivas (*streaks*).

---

## 🎮 O Modelo de Progresso ([[UserProgress]])

O estado de progresso do usuário contém as seguintes métricas fundamentais:

```dart
class UserProgress {
  final int totalXp;               // XP acumulado em toda a jornada
  final int streakDays;            // Dias consecutivos de estudo ativos
  final DateTime? lastStudyDate;   // Última data em que houve revisão
  final int combo;                 // Acertos fáceis consecutivos na sessão
  final int bestStreak;            // Maior sequência histórica de dias
  final int totalStudyDays;        // Total absoluto de dias com estudo
  final List<DateTime> studyDays;  // Histórico de datas registradas (para calendário)
  final int reviewsToday;          // Total de cartões revisados no dia atual
}
```

---

## 📈 Curva de Níveis e Progressão de XP

A progressão de nível segue uma progressão aritmética onde cada nível sucessivo exige mais esforço:

- **Fórmula de XP para o nível seguinte**:
  $$\text{xpRequiredForLevel}(N) = 100 + (N - 1) \times 50$$
  - Nível 1: 100 XP
  - Nível 2: 150 XP
  - Nível 3: 200 XP
  - Nível 4: 250 XP
  - Nível 5: 300 XP

- **Total acumulado necessário para alcançar o nível $N$**:
  $$\text{totalXpRequired}(N) = (N - 1) \times (100 + (N - 2) \times 25)$$
  - Nível 1: 0 XP
  - Nível 2: 100 XP
  - Nível 3: 250 XP
  - Nível 4: 450 XP
  - Nível 5: 700 XP

### Títulos de Maestria por Nível:
| Nível | Título Exibido |
|---|---|
| Nível 1 | **Iniciante** |
| Nível 2 | **Aprendiz** |
| Nível 3 | **Praticante** |
| Nível 4 | **Explorador** |
| Nível 5 | **Desbravador** |
| Nível 6 | **Veterano** |
| Nível 7 | **Especialista** |
| Nível 8 | **Guardião** |
| Nível 9 | **Sábio** |
| Nível 10+ | **Mestre** |

---

## 🔥 Regras de Ofensiva (*Streak*) e Combos

O cálculo de ofensiva é realizado pelo [[GamificationService#applyReview]]:

1. **Mesmo Dia**:
   - Se `lastStudyDate` for igual ao dia de hoje, a ofensiva se mantém inalterada e o contador `reviewsToday` é incrementado.
2. **Dia Consecutivo**:
   - Se o último dia de estudo foi exatamente ontem (`lastDay.add(Duration(days: 1)) == today`), a ofensiva aumenta em 1 (`streakDays++`).
3. **Quebra de Sequência**:
   - Se houver mais de 1 dia de hiato entre o último estudo e hoje, a ofensiva reinicia em `1`.
4. **Recorde (*Best Streak*)**:
   - Se o `streakDays` atual ultrapassar o `bestStreak`, o novo recorde é persistido imediatamente.
5. **Combos**:
   - Cada resposta **Fácil** incrementa o combo (`combo++`).
   - Respostas **Difícil** mantêm o combo.
   - Respostas **Não sabia** zeram o combo.

---

## 🔗 Componentes e Telas Relacionados

- Telas:
  - [[StreakScreen]]: Tela dedicada à visualização do histórico de estudo e recordes.
  - [[HomeScreen]]: Exibição do card de nível, barra de progresso, ofensiva e métricas do dia.
- Componentes Visuais:
  - `streak_calendar.dart`: Renderização do calendário mensal marcando os dias em que houve estudo.
  - `level_card.dart`: Exibição de nível atual, título, XP restante e barra percentual.
  - `stats_section.dart`: Grid com cartões revisados hoje, streak e taxa de retenção.
- Controllers e Serviços:
  - [[UserProgressController]]: Gerencia o estado e notificações de mudança de progresso.
  - [[GamificationService]]: Lógica matemática pura de XP, streak e combos.
  - `streak_controller.dart`: Controlador para navegação e filtros do calendário.
- Repositórios:
  - [[UserProgressRepository]]: Interface abstrata de persistência de progresso.
  - `local_user_progress_repository.dart`: Armazenamento em `SharedPreferences`.
  - `in_memory_user_progress_repository.dart`: Armazenamento volátil para testes.
