---
tags:
  - api
  - status/planejamento
---
# Visão Geral da API Futura (`api-flashmind`)

> **Status Atual**: Em fase de planejamento arquitetural. O desenvolvimento do backend será iniciado após a consolidação das rotinas mobile do Flutter.

Para garantir que a API nasça padronizada e com máxima sinergia com o `app-flashmind`, todas as especificações de rotas, serializers DRF, modelos Django ORM e estratégias de sincronização estão mapeadas nos guias:

- [[Plano de Transição para a API]] — Roteiro de migração para o padrão Dual-DataSource
- [[Contrato Futuro da API]] — Especificação de endpoints, rotas de auth, decks, flashcards e progresso

---

## 🏛️ Stack Escolhida para `api-flashmind`

- **Linguagem**: Python 3.11+ gerenciado com [`uv`](https://docs.astral.sh/uv/)
- **Framework Web**: **Django 5** com **Django REST Framework (DRF)**
- **Painel Administrativo**: Django Admin nativo (`/admin/`) para auditoria e gestão de conteúdo
- **Autenticação**: JWT via `djangorestframework-simplejwt` (Access Token + Refresh Token)
- **Banco de Dados**: PostgreSQL em produção / SQLite local em desenvolvimento
- **Migrações**: Sistema nativo de migrações do Django (`makemigrations` / `migrate`)
- **Testes**: `pytest-django` com fixtures e `APIClient` do DRF

---

## 📂 Estrutura Alvo de Diretórios (Padrão ECC Django)

```text
api-flashmind/
├── manage.py              # Script de gerenciamento do Django
├── pyproject.toml         # Dependências gerenciadas via uv
├── Dockerfile             # Multi-stage container
├── docker-compose.yml     # PostgreSQL + Redis + API
├── config/                # Núcleo de configuração do Django
│   ├── settings/
│   │   ├── base.py        # Configurações compartilhadas
│   │   ├── development.py # Debug, SQLite/PostgreSQL local
│   │   └── production.py  # Segurança estrita, SSL, env vars
│   ├── urls.py            # Roteamento global de URLs
│   └── wsgi.py
└── apps/                  # Apps desacoplados por domínio
    ├── authentication/    # Custom User, SimpleJWT (login, refresh, me)
    ├── decks/             # Models Deck, Flashcard, Serializers, ViewSets
    └── progress/          # UserProgress, cálculo de streaks, histórico de revisões
```
