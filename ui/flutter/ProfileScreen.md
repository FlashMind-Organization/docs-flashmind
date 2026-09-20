---
tags:
  - router/screen
  - core/auth
---
# Tela: ProfileScreen

Tela de visualização, edição de dados cadastrais e encerramento de sessão do usuário ativo (AC 6, AC 7, AC 8).

- **Arquivo no App**: [`lib/core/auth/screens/profile_screen.dart`](file:///home/jonas/Projects/flashmind/app-flashmind/lib/core/auth/screens/profile_screen.dart)
- **Domínio**: [[Persistência e Arquitetura]]

---

## 📱 Estrutura Visual e Componentes

1. **Cabeçalho de Identidade**:
   - Avatar com inicial em destaque e badge de papel: "Estudante" ou "Administrador".
2. **Edição de Perfil (AC 7)**:
   - Permite alterar Nome e E-mail, sincronizando via `authService.updateProfile(...)`.
   - Trata erros de duplicidade de e-mail com a mensagem amigável "Este e-mail já está em uso.".
3. **Segurança e Alteração de Senha (AC 8)**:
   - Botão para abrir o diálogo modal `ChangePasswordDialog`, solicitando senha atual e nova senha.
4. **Encerramento de Sessão (AC 6)**:
   - Botão de logout com confirmação em diálogo de alerta, chamando `authService.logout()` e limpando a pilha de navegação até a tela inicial.
