# Contexto do Produto

## Funcionalidades

### Cadastro de Usuários
- Criação de novos usuários com informações básicas
- Atribuição de saldo inicial

### Gerenciamento de Saldo
- Consulta de saldo atual
- Atualização automática após operações

### Operações Financeiras
- Depósito: adicionar valores à conta
- Saque: retirar valores da conta (com verificação de saldo suficiente)

## Casos de Uso

1. **Cadastro de Novo Usuário**
   - O usuário fornece seus dados
   - O sistema registra o usuário e inicializa o saldo

2. **Depósito**
   - O usuário seleciona a opção de depósito
   - Informa o valor a ser depositado
   - O sistema atualiza o saldo

3. **Saque**
   - O usuário seleciona a opção de saque
   - Informa o valor a ser sacado
   - O sistema verifica se há saldo suficiente
   - Se houver, realiza o saque e atualiza o saldo

## Exemplos Práticos

```python
# Exemplo de uso do sistema
usuario = CadastrarUsuario("João Silva", 1000.0)  # Cadastra usuário com saldo inicial de R$ 1000
usuario.depositar(500.0)  # Deposita R$ 500, saldo atualizado para R$ 1500
usuario.sacar(200.0)  # Saca R$ 200, saldo atualizado para R$ 1300
print(usuario.consultar_saldo())  # Exibe: R$ 1300
```

## Escopo Atual e Planejado

### Escopo Atual (MVP)
- Interface via terminal/console
- Armazenamento em memória (durante execução)
- Operações básicas: cadastro, depósito, saque e consulta

### Escopo Planejado (Futuro)
- Interface gráfica
- Persistência de dados em arquivo ou banco de dados
- Múltiplas contas por usuário
- Transferências entre contas
- Histórico de transações