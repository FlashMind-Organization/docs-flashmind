---
tags:
  - router/screen
  - feature/admin
---
# Tela: AdminDashboardScreen

Painel administrativo exclusivo para contas com papel de administrador (`role: admin`) (AC 9).

- **Arquivo no App**: [`lib/features/admin/screens/admin_dashboard_screen.dart`](file:///home/jonas/Projects/flashmind/app-flashmind/lib/features/admin/screens/admin_dashboard_screen.dart)
- **Domínio**: [[Persistência e Arquitetura]]

---

## 📱 Estrutura Visual e Componentes

1. **Card de Identidade Administrativa**:
   - Saudação personalizada, e-mail e badge destacado de "Administrador".
   - Escuta dinamicamente o `AuthService` via `ListenableBuilder` para refletir alterações de nome imediatamente.
2. **Visão Geral do Sistema**:
   - Painel com cartões de métricas estruturadas: status da API, segurança JWT, modo de acesso e versão.
3. **Ações Administrativas**:
   - Gerenciamento de usuários (estudantes cadastrados).
   - Métricas de retenção e relatórios SRS.
   - Acesso ao perfil através de navegação para a [[ProfileScreen]].
4. **Logout Administrativo**:
   - Botão de logout na AppBar e no rodapé da página, com diálogo de confirmação chamando `authService.logout()`.
