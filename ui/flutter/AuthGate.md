---
tags:
  - router/gate
  - core/auth
---
# Widget: AuthGate

Ponto de entrada e roteamento condicional central do aplicativo FlashMind (AC 9). Determina se exibe a tela de carregamento/splash, o painel do administrador, ou a tela inicial (estudante autenticado ou visitante).

- **Arquivo no App**: [`lib/core/auth/widgets/auth_gate.dart`](file:///home/jonas/Projects/flashmind/app-flashmind/lib/core/auth/widgets/auth_gate.dart)
- **Domínio**: [[Persistência e Arquitetura]]

---

## 📱 Estrutura e Comportamento

1. **Escuta Reativa**:
   - Conecta-se ao `AuthService` via `ListenableBuilder` através de `AppScope.of(context).requireAuthService`.
2. **Carregamento / Splash**:
   - Enquanto `authService.isLoading == true`, renderiza uma tela de carregamento limpa com a logo do FlashMind e indicador de progresso.
3. **Roteamento por Papel**:
   - Se autenticado e `currentUser?.isAdmin == true`: Renderiza [[AdminDashboardScreen]].
   - Se autenticado e `role == 'user'`: Renderiza [[HomeScreen]].
   - Se não autenticado (Modo Visitante): Renderiza [[HomeScreen]] com isolamento local de dados.
