# Padrões do Sistema

## Padrões Arquiteturais

### Programação Orientada a Objetos (POO)
O sistema utiliza o paradigma de Programação Orientada a Objetos, com classes bem definidas para representar entidades como Usuário e Conta.

### Modelo de Domínio Simples
Implementação de um modelo de domínio simples, onde as entidades do sistema bancário são representadas por classes com comportamentos e atributos específicos.

## Padrões Lógicos

### Validação de Dados
Implementação de validações para garantir a integridade dos dados, como verificação de saldo suficiente para saques.

### Encapsulamento
Utilização de encapsulamento para proteger os dados internos das classes, expondo apenas métodos controlados para manipulação.

## Padrões de Design

### Single Responsibility Principle (SRP)
Cada classe tem uma única responsabilidade bem definida, facilitando a manutenção e evolução do código.

### Interface Simples
Interface de linha de comando com menu interativo para facilitar a navegação e uso do sistema.

## Decisões Técnicas Importantes

1. **Armazenamento em Memória**
   - Decisão: Armazenar dados apenas em memória durante a execução do programa.
   - Justificativa: Simplificar a implementação inicial (MVP) sem necessidade de configurar banco de dados.
   - Implicação: Os dados são perdidos ao encerrar o programa.

2. **Validação de Operações Financeiras**
   - Decisão: Implementar validações rigorosas para operações financeiras.
   - Justificativa: Garantir a integridade dos dados financeiros e prevenir operações inválidas.
   - Implicação: Maior segurança nas operações, mas com código adicional para validações.

3. **Estrutura Modular**
   - Decisão: Organizar o código em módulos separados por responsabilidade.
   - Justificativa: Facilitar manutenção e permitir expansão futura do sistema.
   - Implicação: Melhor organização do código e possibilidade de reutilização de componentes.