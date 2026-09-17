---
tags:
  - dominio
  - feature/decks
---
# Domínio: Gestão de Decks e Cartões

Este domínio é responsável pela estruturação do conhecimento no **FlashMind**. Ele gerencia os baralhos de estudo ([[Deck]]) e seus respectivos flashcards ([[Flashcard]]), incluindo regras de validação de duplicidade, cálculo de métricas de progresso e persistência.

---

## 🗂️ Modelo do Baralho ([[Deck]])

Cada baralho agrupa uma coleção de flashcards sobre um tópico específico:

```dart
class Deck {
  final String id;
  final String title;
  final String description;
  final List<Flashcard> flashcards;
  final DateTime createdAt;
  final DateTime updatedAt;
}
```

### Métricas Calculadas em Tempo Real:
- **`totalCards`**: Quantidade total de cartões no baralho.
- **`reviewedCards`**: Quantidade de cartões já revisados cujo próximo agendamento está no futuro (`card.nextReviewAt.isAfter(DateTime.now())`).
- **`progress`**: Percentual de conclusão e retenção (`reviewedCards / totalCards`), variando de 0.0 a 1.0.

---

## 🛡️ Regras de Validação e Integridade

O [[DeckService]] atua como guardião de integridade dos baralhos:

1. **Título Obrigatório e Limite**:
   - `validateTitle(title)`: Título não pode ser vazio e deve ter no máximo 100 caracteres.
2. **Unicidade de Baralhos**:
   - `validateTitleUnique(title, excludeDeckId)`: Não é permitido criar ou renomear um baralho para um nome já existente (comparação *case-insensitive* e com *trim*).
3. **Limite da Descrição**:
   - `validateDescription(desc)`: Máximo de 300 caracteres.
4. **Unicidade de Cartões dentro do Deck**:
   - `validateFlashcardUnique(deck, question, answer)`: Impede a inserção de cartões idênticos (mesma pergunta e mesma resposta) dentro do mesmo baralho.

---

## 📦 Decks Pré-carregados (Seed Inicial)

Para garantir que o usuário tenha conteúdo imediato sem precisar cadastrar tudo do zero, o repositório local carrega dados estáticos na primeira execução a partir de `decks_data.dart`:

| Deck Seed | Quantidade de Cartões | Assuntos Abordados |
|---|---|---|
| **SQL** | 12 | Comandos DDL, DML, JOINs, agregações, índices |
| **OOP (Orientação a Objetos)** | 10 | Encapsulamento, herança, polimorfismo, abstração, SOLID |
| **Linux** | 12 | Comandos básicos, permissões `chmod`/`chown`, processos, pipes |
| **Git** | 10 | Branching, commits, rebase vs merge, stash, cherry-pick |
| **Fundamentos de Programação** | 12 | Tipos de dados, estruturas de controle, complexidade de algoritmos |
| **Linux - Cenários Práticos** | 8 | Resolução de incidentes, análise de logs, uso de memória/disco |
| **SQL - Cenários de Negócio** | 8 | Queries complexas, relatórios financeiros, otimização de consultas |

---

## 🔗 Componentes e Telas Relacionados

- Telas:
  - [[DecksScreen]]: Listagem geral de baralhos com busca, filtros de status e resumo.
  - [[DeckDetailsScreen]]: Detalhes do baralho selecionado, estatísticas, lista de cartões e ações.
  - [[CreateDeckScreen]]: Formulário com validação para criação de novo baralho.
- Componentes Visuais:
  - `deck_list.dart`: Lista rolável de baralhos.
  - `deck_list_item.dart`: Card individual de cada baralho com barra de progresso.
  - `decks_summary.dart`: Card superior com contagem total de baralhos e cartões.
  - `create_deck_button.dart`: Ação rápida de criação.
  - `deck_states_help_bottom_sheet.dart`: Modal explicativo sobre estados dos cartões.
- Controllers e Serviços:
  - [[DeckService]]: Gerenciamento central e notificações de estado (`ChangeNotifier`).
  - `deck_details_controller.dart`: Controle de paginação e filtros na tela de detalhes.
  - `create_deck_controller.dart`: Gerenciamento do formulário de criação.
- Repositórios:
  - [[DeckRepository]]: Interface abstrata.
  - `local_deck_repository.dart`: Implementação com serialização JSON em `SharedPreferences`.
  - `in_memory_deck_repository.dart`: Implementação volátil para testes automatizados.
