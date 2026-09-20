---
tags:
  - router/screen
  - core/auth
---
# Tela: RegisterScreen

Tela de registro de novas contas de estudantes no FlashMind (AC 1, AC 2).

- **Arquivo no App**: [`lib/core/auth/screens/register_screen.dart`](file:///home/jonas/Projects/flashmind/app-flashmind/lib/core/auth/screens/register_screen.dart)
- **Domínio**: [[Persistência e Arquitetura]]

---

## 📱 Estrutura Visual e Componentes

1. **Formulário de Cadastro**:
   - Nome completo (obrigatório, trim).
   - E-mail (formato válido, sem espaços).
   - Senha (mínimo de 6 caracteres).
   - Confirmação de senha (deve coincidir exatamente com a senha informada).
2. **Tratamento de Duplicidade (AC 2)**:
   - Se a API retornar erro de validação (HTTP 400) no campo `email`, exibe feedback explícito e amigável: "Este e-mail já está cadastrado.".
3. **Navegação**:
   - Botão de retorno e link "Entrar" direcionam para a [[LoginScreen]].
   - Ao concluir o cadastro, retorna à tela de login preenchendo o e-mail cadastrado e exibindo mensagem de sucesso.
