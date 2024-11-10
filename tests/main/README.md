# Descrição do Projeto

Este projeto tem como objetivo uma automacão ao site do instagram. Ele segue uma arquitetura modular e escalável, com separação clara entre as regras de negócios, a apresentação da interface do usuário e o gerenciamento das tarefas dinâmicas.

## Estrutura do Projeto

A estrutura do projeto foi organizada para garantir uma boa separação de responsabilidades, modularidade e coesão com base em meus estudos e conhecimentos adquiridos no meu tempo de estudo em desenvolvimento de software utilizando **Python** como minha principal linguagem e assim busquei quais melhores técnicas e estruturas utilizar com a linguagem. A seguir, detalho o papel de cada pasta e módulo dentro da aplicação:

### src
- **factory**: Contém as fábricas de regras e a lógica central de criação.
  - **rules**: Contém as classes de regras de negócio, tanto abstratas quanto concretas.
      >__\_\_init\_\___.__py__: Classes concretas `produtos concretos do Padrão Factory`
       <br>__abs__.__py__: classes abstratas `produtos abstrados do padrão Factory` 
  - **core**: Contém a classe Handler, que controla o estado e a execução das regras.
  - **factory.py**: Implementação da fábrica abstrata, responsável pela criação das instâncias.
  - **__\_\_init\_\___.py**: Contém a Factory concreta, que organiza o fluxo de criação de objetos.

### template
- **template/__\_\_init\_\___.py**: Contém a classe Template, que gerencia os layouts e a execução das tarefas nos menus.
- **main_template.py**: Layout para o menu principal.
- **tasks_template.py**: Layout para o menu de tarefas.

### utils
- **utils/__\_\_init\_\___.py**: Contém funções utilitárias para tarefas comuns, como ler arquivos ou gerar valores aleatórios.

### __\_\_main\_\___.py
- O ponto de entrada do código, responsável pela execução do fluxo principal da aplicação.

### __\_\_init\_\___.py
 - Gerencia os dados apresentados e enviados pelo cliente, tem uma classe Schema que é consumida através template de forma eficaz através de arquivo \`\_\_main\_\_.py\` ponto de união entre as regras e o front-end

### Considerações sobre Design e Padrões

#### Separação de Preocupações
A separação de preocupações entre a lógica de negócios (regras) e a apresentação (templates) foi bem definida, garantindo que cada módulo tenha uma responsabilidade clara e isolada.

#### Padrões de Design
O sistema utiliza os seguintes padrões de design:
- **Factory**: Para a criação de objetos de regras e templates.
- **Facade**: Para simplificar a interface entre o cliente e o sistema, escondendo a complexidade interna.
  
#### Handler (Possível Anti-padrão)
O uso do Handler com descritor e meta-classe pode ser considerado um anti-padrão, mas foi escolhido para permitir um controle mais granular sobre o estado e a execução das regras. Cada regra é aplicada dinamicamente nas classes abstratas, e o Handler gerencia os atributos de estado e a saída. Esse design proporciona uma boa organização para escalar e manter o código no futuro.

## Como Usar

1. Clone o repositório.
2. Execute o código em `__main__.py` para iniciar a execução.
3. Explore as fábricas de regras e templates para personalizar o comportamento da aplicação.

## Possíveis Melhorias

Embora a arquitetura esteja sólida, existem algumas áreas para melhorias, como:
- A substituição do **Handler** por um design mais convencional para aplicar as metaclasses e descritores e assim um melhor controle de estado e saída.
- Adicionar testes unitários.
- Implementar um sistema de logs para monitoramento da execução.

## Conclusão

O design modular e a aplicação de padrões de design garantem que o código seja fácil de escalar e manter. A estrutura de fábricas, templates e regras oferece uma base sólida para o desenvolvimento de novos recursos.

