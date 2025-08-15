# Contexto Tecnológico

## Stack Tecnológica

### Linguagens
- **Python 3.x**: Linguagem principal de desenvolvimento

### Bibliotecas
- **Biblioteca Padrão Python**: Utilização apenas de módulos da biblioteca padrão para simplicidade
  - `os`: Para operações relacionadas ao sistema operacional
  - `datetime`: Para registro de data e hora das transações

## Estrutura do Projeto

```
teste_newproject_turbosite/
├── memory-bank/           # Documentação do projeto
├── banco/                 # Código-fonte do sistema bancário
│   ├── __init__.py        # Inicializador do pacote
│   ├── usuario.py         # Módulo de gerenciamento de usuários
│   ├── conta.py           # Módulo de gerenciamento de contas
│   └── main.py            # Ponto de entrada da aplicação
└── README.md              # Documentação geral do projeto
```

## Interações entre Componentes

1. **Módulo Usuario**: Responsável pelo gerenciamento de informações dos usuários
   - Armazena dados pessoais
   - Associa usuários às suas contas

2. **Módulo Conta**: Gerencia as operações financeiras
   - Controla saldo
   - Implementa operações de depósito e saque
   - Valida operações financeiras

3. **Módulo Main**: Interface principal do sistema
   - Apresenta menu de opções
   - Coordena interações entre os módulos
   - Gerencia o fluxo da aplicação

## Configurações

### Variáveis de Ambiente
O sistema não utiliza variáveis de ambiente na versão atual (MVP).

### Configurações de Desenvolvimento
- **Ambiente de Desenvolvimento**: Qualquer IDE ou editor de texto com suporte a Python
- **Versionamento**: Git para controle de versão
- **Testes**: Testes manuais via interface de linha de comando