---
tags:
  - service/flutter
  - gamification
  - feature/progress
---
# Service: GamificationService

Serviço imutável e funcional com a lógica matemática de concessão de XP, cálculo de ofensiva e streaks diários.

- **Arquivo no App**: [`lib/core/progress/services/gamification_service.dart`](file:///home/jonas/Projects/flashmind/app-flashmind/lib/core/progress/services/gamification_service.dart)
- **Domínio**: [[Gamificação e Progresso]]
- **Guia Detalhado**: [[Algoritmo SRS e Gamificação]]

---

## 📋 Métodos

### 1. `xpForRating(ReviewRating rating) -> int`
- `forgot`: 5 XP
- `difficult`: 10 XP
- `easy`: 15 XP

### 2. `applyReview(UserProgress progress, ReviewRating rating, {required DateTime now, int? customXp}) -> UserProgress`
Calcula uma **nova instância** de [[UserProgress]] com:
- `totalXp`: incrementado pelo XP obtido.
- `streakDays`: incrementado se for dia consecutivo; mantido se já estudou hoje; resetado para 1 se houve quebra de mais de 1 dia.
- `bestStreak`: atualizado se a ofensiva atual bater o recorde anterior.
- `combo`: incrementado no `easy`, zerado no `forgot`.
- `studyDays`: data de hoje adicionada à lista caso ainda não estivesse presente.
- `reviewsToday`: contador do dia incrementado.

---

## 👥 Quem Consome

- [[ReviewService]]
- Testes unitários em `test/core/progress/gamification_service_test.dart`
