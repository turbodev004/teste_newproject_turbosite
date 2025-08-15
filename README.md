# Sistema Bancário

Um sistema simples em Python para gerenciamento de contas bancárias, permitindo cadastro de usuários, depósitos, saques e consulta de saldo.

## Funcionalidades

- Cadastro de usuários com saldo inicial
- Depósito de valores
- Saque de valores (com verificação de saldo)
- Consulta de saldo atual
- Histórico de transações

## Como Executar

1. Certifique-se de ter Python 3.x instalado
2. Clone este repositório
3. Navegue até a pasta do projeto
4. Execute o sistema com o comando:

```bash
python banco/main.py
```

## Estrutura do Projeto

- `banco/`: Código-fonte do sistema bancário
  - `__init__.py`: Inicializador do pacote
  - `usuario.py`: Módulo de gerenciamento de usuários
  - `main.py`: Interface principal do sistema
- `memory-bank/`: Documentação do projeto

## Limitações Atuais

- Dados armazenados apenas em memória (perdidos ao encerrar o programa)
- Interface limitada a linha de comando