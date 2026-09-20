---
tags:
  - router/screen
  - core/auth
---
# Tela: LoginScreen

Tela de autenticação e login de usuários existentes no FlashMind (AC 4).

- **Arquivo no App**: [`lib/core/auth/screens/login_screen.dart`](file:///home/jonas/Projects/flashmind/app-flashmind/lib/core/auth/screens/login_screen.dart)
- **Domínio**: [[Persistência e Arquitetura]]

---

## 📱 Estrutura Visual e Componentes

1. **Formulário de Acesso**:
   - Campo de e-mail com validação estrita de formato (`^[^\s@]+@[^\s@]+\.[^\s@]+$`).
   - Campo de senha com alternância de visibilidade (ícone de olho).
2. **Tratamento Seguro de Erros (AC 4)**:
   - Erros HTTP 401 exibem mensagem genérica amigável ("E-mail ou senha inválidos."), prevenindo a enumeração de usuários.
3. **Ações de Navegação**:
   - Botão "Cadastre-se": Navega para [[RegisterScreen]] e preenche o e-mail automaticamente no retorno.
   - Botão "Continuar como visitante": Permite utilizar o aplicativo localmente sem autenticação.
   - Ao autenticar com sucesso, retorna para a tela anterior ou roteia para o [[AuthGate]].
