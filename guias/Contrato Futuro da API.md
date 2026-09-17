---
tags:
  - guia
  - api
  - contratos
---
# Guia: Especificação e Contrato da Futura API (Django REST Framework)

Este documento projeta antecipadamente os endpoints, modelos ORM e serializers que o backend **`api-flashmind`** (em Django REST Framework) fornecerá para atender o aplicativo **`app-flashmind`**.

---

## 🔐 Módulo de Autenticação (`/api/auth/`)

Gerenciado com `djangorestframework-simplejwt` e Custom User Model.

| Método | Rota | Descrição | Permissão | Payload / Resposta |
|---|---|---|---|---|
| `POST` | `/api/auth/register/` | Cadastro de novo estudante | `AllowAny` | Req: `{ email, password, name }`<br>Res: `UserSerializer` |
| `POST` | `/api/auth/token/` | Login com email e senha | `AllowAny` | Req: `{ email, password }`<br>Res: `{ access, refresh }` |
| `POST` | `/api/auth/token/refresh/` | Renovação do access token | `AllowAny` | Req: `{ refresh }`<br>Res: `{ access, refresh }` |
| `GET` | `/api/auth/me/` | Perfil do usuário logado | `IsAuthenticated` | Res: `UserSerializer` |

---

## 🗂️ Módulo de Decks (`/api/decks/`)

Implementado via `DeckViewSet(viewsets.ModelViewSet)`.

| Método | Rota | Descrição | Permissão | Payload / Resposta |
|---|---|---|---|---|
| `GET` | `/api/decks/` | Lista baralhos do usuário | `IsAuthenticated` | Res: `List[DeckSummarySerializer]` |
| `POST` | `/api/decks/` | Cria novo baralho | `IsAuthenticated` | Req: `CreateDeckSerializer`<br>Res: `DeckDetailSerializer` |
| `GET` | `/api/decks/{id}/` | Detalhes com flashcards | `IsAuthenticated` | Res: `DeckDetailSerializer` |
| `PUT` / `PATCH` | `/api/decks/{id}/` | Atualiza título/descrição | `IsAuthenticated` | Req: `UpdateDeckSerializer`<br>Res: `DeckDetailSerializer` |
| `DELETE` | `/api/decks/{id}/` | Remove baralho (soft delete) | `IsAuthenticated` | Res: `204 No Content` |

---

## 🗃️ Módulo de Flashcards (`/api/flashcards/`)

| Método | Rota | Descrição | Permissão | Payload / Resposta |
|---|---|---|---|---|
| `POST` | `/api/decks/{deck_id}/flashcards/` | Adiciona cartão a um baralho | `IsAuthenticated` | Req: `CreateFlashcardSerializer`<br>Res: `FlashcardSerializer` |
| `PUT` / `PATCH` | `/api/flashcards/{id}/` | Atualiza pergunta/resposta | `IsAuthenticated` | Req: `UpdateFlashcardSerializer`<br>Res: `FlashcardSerializer` |
| `DELETE` | `/api/flashcards/{id}/` | Remove um cartão | `IsAuthenticated` | Res: `204 No Content` |
| `POST` | `/api/flashcards/{id}/review/` | Registra avaliação (SRS) | `IsAuthenticated` | Req: `{ rating: "forgot" \| "difficult" \| "easy" }`<br>Res: `ReviewResultSerializer` |

---

## 🏆 Módulo de Progresso e Gamificação (`/api/progress/`)

| Método | Rota | Descrição | Permissão | Payload / Resposta |
|---|---|---|---|---|
| `GET` | `/api/progress/` | Retorna XP, nível e streak | `IsAuthenticated` | Res: `UserProgressSerializer` |
| `GET` | `/api/progress/calendar/` | Dias com estudo para heatmap | `IsAuthenticated` | Query: `?year=2026&month=9`<br>Res: `List[Date]` |
| `POST` | `/api/progress/sync/` | Sincroniza revisões offline | `IsAuthenticated` | Req: `BatchReviewSyncSerializer`<br>Res: `SyncSummarySerializer` |

---

## 📐 Modelos Django ORM Projetados (`apps/*/models.py`)

### 1. `apps.authentication.models.User`
- `id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)`
- `email = models.EmailField(unique=True, db_index=True)`
- `name = models.CharField(max_length=150)`
- `created_at = models.DateTimeField(auto_now_add=True)`
- `updated_at = models.DateTimeField(auto_now=True)`
- `deleted_at = models.DateTimeField(null=True, blank=True)`

### 2. `apps.decks.models.Deck`
- `id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)`
- `user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="decks")`
- `title = models.CharField(max_length=100)`
- `description = models.CharField(max_length=300, blank=True, default="")`
- `created_at = models.DateTimeField(auto_now_add=True)`
- `updated_at = models.DateTimeField(auto_now=True)`
- `deleted_at = models.DateTimeField(null=True, blank=True)`

### 3. `apps.decks.models.Flashcard`
- `id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)`
- `deck = models.ForeignKey(Deck, on_delete=models.CASCADE, related_name="flashcards")`
- `question = models.TextField()`
- `answer = models.TextField()`
- `review_step = models.PositiveSmallIntegerField(default=0)`
- `times_reviewed = models.PositiveIntegerField(default=0)`
- `next_review_at = models.DateTimeField(db_index=True)`
- `last_reviewed_at = models.DateTimeField(null=True, blank=True)`
- `created_at = models.DateTimeField(auto_now_add=True)`
- `updated_at = models.DateTimeField(auto_now=True)`
- `deleted_at = models.DateTimeField(null=True, blank=True)`

### 4. `apps.progress.models.UserProgress`
- `id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)`
- `user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="progress")`
- `total_xp = models.PositiveIntegerField(default=0)`
- `streak_days = models.PositiveIntegerField(default=0)`
- `best_streak = models.PositiveIntegerField(default=0)`
- `combo = models.PositiveIntegerField(default=0)`
- `last_study_date = models.DateField(null=True, blank=True)`
- `reviews_today = models.PositiveIntegerField(default=0)`
- `created_at = models.DateTimeField(auto_now_add=True)`
- `updated_at = models.DateTimeField(auto_now=True)`
- `deleted_at = models.DateTimeField(null=True, blank=True)`
