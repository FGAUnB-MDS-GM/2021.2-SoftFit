# Visão do Produto e Projeto

## Histórico de Revisão

| Data       | Versão | Descrição | Autor |
| :---       | :----: | :-------- | :---: |
| 31/01/2022 | 1.0    |  Primeira versão do documento. Em que todos os quadros, tanto de problema, quanto de produto foram preenchidos. A metodologia escolhida e suas justificativas também são adicionadas pela primeira vez no documento. As lições aprendidas da Unidade 1 são descritas nessa versão do documento. | Victor Hugo Oliveira Leão; Felipe Alef Pereira Rodrigues |
| 08/02/2022 | 1.1 | Correção de ajustes apontados pelo professor nos quesitos: O problema; Objetivos do Produto; Como está organizado o time de desenvolvimento?; É importante ter uma especificação e um projeto (design) bem detalhados antes de passar para a implementação - talvez por motivos contratuais? | Victor Hugo Oliveira Leão; Felipe Alef Pereira Rodrigues |
| 14/02/2022 | 2.0 | Adição de novos tópicos (Escopo do Produto e Visão Geral do Projeto), para as entregas da Unidade 2 em diante. Primeira versão dos requisitos funcionais e não-funcionais. | Victor Hugo Oliveira Leão; Marcos Well Neres Silva Pereira |
| 20/02/2022 | 2.1 | Correção de ajustes acerca dos requisitos funcionais e não-funcionais. Adição dos tópicos: Organização do Projeto; Planejamento das Fases e/ou Iterações do Projeto; Matriz de Comunicação; Gerenciamento de Riscos | Victor Hugo Oliveira Leão |
| 20/02/2022 | 2.2 | Ajuste nos requisitos não-funcionais; Adição das lições aprendidas na Unidade 2; Correção de como as iterações do projeto serão feitas (Releases ao invés de Sprints) | Victor Hugo Oliveira Leão |
| 07/03/2022 | 2.3 | Correção de ajustes apontados pelo professor: adição da imagem do Canvas MVP; Datas das entregas previstas; Ajustes de alguns RFs | Victor Hugo Oliveira Leão |
| 06/04/2022 | 3.0 | Adição das lições aprendidas nas unidades 3 e 4; Documentação da dinâmica de programação em duplas | Victor Hugo Oliveira Leão |

## 1. Visão Geral do Produto

### 1.1 Declaração do Problema

|                                | 	                                                                                     |
| :----------------------------: | :------------------------------------------------------------------------------------ |
| O problema                     |  É a falta de organização no gerenciamento das questões humanas no que convém a academias.        |
| Afeta                          |  O administrador, os alunos e os profissionais (professores/Personal Trainers).       |
| Cujo Impacto é                 |  Para o administrador: a falta de concentração dos dados financeiros e de controle de frequência de seus alunos matriculados em uma única plataforma; a dificuldade de comunicação imediata e automática de avisos para com os alunos. Para os alunos: terem suas avaliações e treinos registrados em fichas físicas, que podem ser facilmente perdidas ou danificadas; a necessidade de se dirigir a uma unidade física da academia para resolver problemas financeiros ou solucionar dúvidas ou consultas simples. Para os profissionais: não possuírem sua rotina e ferramentas de gerenciamento e auxílio de alunos em um único lugar.                                                                     |
| Uma solução de sucesso seria   |  Um software em que os alunos pudessem administrar seus treinos e avaliações, resolver questões que envolvam seu estado financeiro e entrar em contato com a academia. Para o administrador, uma solução de sucesso seria aquela em que os principais dados dos alunos e professores estiverem concentrados e que o possibilitaria com poucos cliques enviar avisos para os alunos por e-mail. Já para os professores, ter sua rotina em uma única tela juntamente com a possibilidade de auxiliar os alunos de forma on-line.                                                               |

### 1.2 Declaração de Posição do Produto

|              |                 																						  |
| :--------    | :------ 																						  |
| Para         | Academias       																							|
| Que          | Buscam uma solução em que possam realizar o gerenciamento de questões humanas e entregarem uma experiência digital aos alunos e professores 																						   |
| O SoftFit    | É uma aplicação Web responsiva																			   |
| Que          | Entrega soluções digitais para as 3 partes: administrador, aluno e professor.                                                                                                                 |
| Ao contrário | Das academias tradicionais em que: Os dados, treinos e avaliações do aluno são disponíveis de forma física; Os alunos precisam se locomover até uma unidade física para solucionar problemas financeiros e tirarem dúvidas; Os professores só conseguem criar e administrar treinos se estiverem com os alunos ao seu lado; Os administradores não tem os principais dados dos alunos concentrados e com a disponibilidade de entrarem em contato de forma imediata e automática acerca de avisos importantes; |
Nosso Produto  | Possui as seguintes funções: Para o **administrador**, há a disposição dos dados, tanto pessoais e financeiros, quanto de frequência de seus alunos matriculados. Além disso, o administrador também consegue enviar avisos importantes e entrar em contato por e-mail com os frequentadores da academia; Para os **alunos**, haverá seus treinos e avalições (medidas) em uma única página (com a possibilidade de vídeos demonstrativos), também é possível entrar em contato com a academia por e-mail e chats para poderem tirar suas dúvidas e controlarem seu estado financeiro; Para os **professores** terão sua rotina disposta e ferramentas de criação e auxílio de treinos a partir dos dados dos alunos. |

### 1.3 Objetivos do Produto

Os objetivos do produto são os seguintes:
* Entregar para os **alunos** da academia: 
	* Seus treinos e medidas/avaliações em uma única plataforma;
	* Uma área em que eles possam ver e controlar seu estado financeiro;
	* A possibilidade de entrar em contato com a academia de forma digital (por e-mail ou chatbots).
* Entregar para os **professores** da academia:
	* Uma tela em que suas rotinas estão cadastradas;
	* Uma plataforma em que se é possível montar os treinos dos alunos de forma totalmente digital.
* Entregar para o **administrador** da academia:
	* Um sistema em que os principais dados dos alunos, juntamente com o controle de frequência de cada um deles, estão concentrados.
	* Uma aplicação que envia mensagens por e-mail para os alunos de forma automática e personalizada.

### 1.4 Escopo do Produto

#### 1.4.1 Requisitos Funcionais

|  N° | Versão | Requisito | Prioridade |
|:--: | :----: | :-------: | :--------: |
| RF1 |   1.0  | O **aluno** deve ser capaz de consultar todas as fichas de treino atribuídas a ele. | Alta |
| RF2 |   1.0  | O **aluno** deve poder informar seus objetivos na academia. | Alta |
| RF3 |   1.0  | O **aluno** deve ser capaz de mandar uma mensagem para a academia pelo sistema. | Média |
| RF4 |   1.0  | O **aluno** deve ser capaz de visualizar o resultado de suas avaliações físicas. | Média |
| RF5 |   1.0  | O **aluno** deve ser capaz de filtrar suas avaliações físicas por período. | Baixa |
| RF6 |   1.0  | O **aluno** deve ser capaz de consultar seu estado financeiro. | Alta |
| RF7 |   1.0  | O **aluno** deve poder visualizar suas frequências na academia (dias em que ele foi na academia e dias que não). | Baixa |
| RF8 |   1.0  | O **aluno** deve ser capaz de filtrar suas frequências por mês. | Baixa |
| RF9 |   1.0  | O **administrador** deve ser capaz de realizar o cadastro de um novo aluno. | Alta |
| RF10 |   1.0  | O **administrador** deve ser capaz de realizar o cadastro de um novo professor. | Alta |
| RF11 |   1.0  | O **administrador** deve poder visualizar a situação financeira de cada aluno. | Alta |
| RF12 |   1.0  | O **administrador** deve ser capaz de filtrar os alunos por situação financeira, nas seguintes categorias: em dia ou inadimplente. | Média |
| RF13 |   1.0  | O **administrador** deve poder consultar o controle de frequência de cada aluno. | Alta |
| RF14 |   1.0  | O **administrador** deve ser capaz de buscar os alunos por nome. | Média |
| RF15 |   1.0  | O **administrador** deve poder enviar e-mails personalizados (por nome do aluno) para cada aluno acerca de sua situação financeira ou frequência. | Alta |
| RF16 |   1.0  | O **administrador** deve ser capaz de visualizar cada professor e os alunos atrelados a ele. | Média |
| RF17 |   1.0  | O **administrador** deve ser capaz de filtrar os professores por nome. | Baixa |
| RF18 |   1.0  | Os **professores** devem ser capazes de visualizar as avaliações físicas e os objetivos de cada aluno. | Alta |
| RF19 |   1.0  | Os **professores** devem poder montar os treinos personalizados para cada aluno. | Alta |
| RF20 |   1.0  | Os **professores** devem ser capazes de buscar os alunos por nome. | Média |
| RF21 |   1.0  | Os **professores** devem ser capazes de filtrar os alunos por objetivos na academia. | Baixa |
| RF23 |   1.0  | Os **professores** devem poder visualizar sua rotina. | Alta |
| RF24 |   1.0  | Os **professores** devem ser capazes de visualizar os alunos atrelados a eles. | Média |
| RF25 |   1.0  | O **aluno** deve ser capaz de realizar login com seus dados cadastrais preenchidos pelo administrador. | Alta |
| RF26 |   1.0  | O **professor** deve ser capaz de realizar login com seus dados cadastrais preenchidos pelo administrador. | Alta |
| RF27 |   1.0  | O **administrador** deve ser capaz de realizar login com seus dados cadastrais. | Alta |

**Legenda**:
* Prioridade Alta: São os requisitos necessários para que os objetivos do produto sejam cumpridos.
* Prioridade Média: São os requisitos que complementam os requisitos de prioridade alta, mas não são essenciais para o funcionamento do sistema.
* Prioridade Baixa: São os requisitos que facilitam e incrementam o uso do sistema, mas que sem eles, o produto funciona e entrega o necessário.

#### 1.4.2 Requisitos Não-Funcionais

* **Requisitos de Utilidade:**
	* Todas as documentações do sistema devem estar disponíveis na GitPages do repositório.
* **Requisitos de Implementação:**
	* O sistema deve ser desenvolvido na linguagem Python com o framework Django.
	* O versionamento do sistema deve ser feito pelo GitHub.
	* Caso o produto tenha andamento após o fim da disciplina, o sistema deve seguir a Lei Geral de Proteção de Dados (Lei nº 13.709/2018 – “LGPD”).
* **Requisitos de Desempenho:**
	* O sistema SoftFit deverá estar disponível durante os horários de funcionamento da academia.
* **Requisitos de Suportabilidade:**
	* O sistema deve ser uma aplicação web responsiva.
	* O sistema deve ser acessível nos seguintes navegadores: Microsoft Edge, Google Chrome, Firefox, Safari e Opera.

Todos os requisitos não-funcionais possuem alta prioridade, isto é, são necessários para o funcionamento do produto cumprindo todos seus objetivos.

### 1.5 Minímo Produto Viável (MVP)

![Canvas MVP](../mvp.jpg "Canvas MVP")
Melhor visualização em: [Canvas MVP - Miro](https://miro.com/app/board/uXjVOL8m7cA=/?invite_link_id=174921709773)

## 2. Abordagem de Desenvolvimento de Software 

### 2.1 Metodologia

Para o estabelecimento da metodologia de desenvolvimento de software, algumas questões foram previamente respondidas: 

* Questões Técnicas:
	* **Qual é o tamanho do sistema que está sendo desenvolvido?** Relativamente extenso, uma vez que envolve funções para o aluno, o professor e o administrador da academia. 
	* **Que tipo de sistema está sendo desenvolvido?** Aplicação Web responsiva. 
	* **Qual a vida útil prevista para o sistema?** 4 meses (tempo da disciplina).
	* **O sistema está sujeito a controle externo?** Sim, o dono/administrador da academia adquiriria o software, logo o produto não estaria somente sob influência dos desenvolvedores.

* Questões Humanas:
	* **Qual é o nível de competência dos projetistas e programadores do time de desenvolvimento?** A princípio, todos que compõem o time possuem um nível de competência igualmente básico-intermediário. 
	* **Como está organizado o time de desenvolvimento?** O time de desenvolvimento está organizado entre Product Owner (PO), que será responsável por fazer a ponte entre o time de desenvolvimento e o produto desejado e definido pelo escopo, e desenvolvedores, aqueles que construirão de fato o software a partir do que é conversado e determinado com o PO.
	* **Quais são as tecnologias disponíveis para apoiar o desenvolvimento do sistema?** Trello, Discord, Microsoft Teams e GitHub.  

* Questões Organizacionais: 
	* **É importante ter uma especificação e um projeto (design) bem detalhados antes de passar para a implementação - talvez por motivos contratuais?** Apesar do escopo do produto definido inicialmente, a equipe, durante o desenvolvimento do sistema, vai trabalhar de forma direta e muito conectada com os requisitos, havendo a possibilidade de mudanças e alterações no meio da implementação. Dessa forma, não será necessário ter previamente uma especificação e um projeto (design) bem detalhados.
	* **É realista uma estratégia de entrega incremental, na qual o software é entregue aos clientes ou outros stakeholders e um rápido feedback é obtido?** Considerando que teremos um Product Owner, isto é, alguém que trabalharia analisando as entregas do grupo e ver se está de acordo com o pensado, é sim realista. 
	* **Os representantes do cliente estarão disponíveis e dispostos a participar do time de desenvolvimento?** Basicamente, a equipe terá um “representante de cliente”, então sim. 
	* **Existem questões culturais que possam afetar o desenvolvimento do sistema?** Não. 

A partir das respostas desenvolvidas, considera-se que por não haver uma necessidade da criação de documentos formais sendo criados dentro das atividades e, uma vez que os requisitos e o projeto serão desenvolvidos conjuntamente, uma **abordagem ágil** seja ideal.  

Sendo assim, a metodologia ágil **Kanban** foi escolhida a partir dos seguintes motivos:
1. Seguir uma filosofia contínua de desenvolvimento e entrega e, portanto, admitir uma maior flexibilidade e leveza para os desenvolvedores; 
1. Ter uma organização visível clara que possibilita ao grupo, sem a necessidade de reunião constantes, entender os processos e em que etapa o desenvolvimento está como um todo; 
1. Por não ter a necessidade de uma divisão de funções específicas, o grupo pode, como um todo, se auto-organizar e trabalhar com maior autonomia;
1. A priorização de atividades é bem intuitiva com o quadro e com a limitação de WIP (trabalhos em andamento).

Dessa forma, apesar dos horários rígidos que os integrantes do grupo, como alunos, possam ter, com o Kanban, o grupo pode trabalhar de forma ágil, mas sem a necessidade de comprometimentos diários de horários.

### 2.2 Processo e Procedimentos

|    Atividade         | Objetivo  |  Papel  |       Método        | Ferramenta |
| :------------------- | :-------: | :-----: | :----------------:  | :--------: |
| Criar quadro Kanban  |  Organizar o quadro que a equipe utilizará para se orientar durante o desenvolvimento    |       Product Owner e Equipe de Desenvolvimento        |     Requisitos – Em desenvolvimento - Entregue       | ZenHub |
| Criar Canvas MVP  |  Definir o Minímo Produto Viável e criar seu quadro Canvas  | Product Owner e Equipe de Desenvolvimento | Canvas MVP | Miro |
| Estabelecer o prazo de entregas  |  Organizar os requisitos a serem entregues em relação ao tempo    |             Product Owner e Equipe de Desenvolvimento              |      Analisar datas da disciplina com os requisitos definidos      | ZenHub |
| Estabelecer escopo do produto  |  Definir as características que devem estar presentes no produto de software    |               Product Owner e Equipe de Desenvolvimento                 | SAFe  | SAFe |
| Estudar tecnologias  |  Adquirir o conhecimento necessário para o desenvolvimento do sistema   |                      Equipe de Desenvolvimento                        |      Individual (Cada integrante seguirá o método de estudo que achar mais eficiente)      | Materiais Digitais |
| Definir design das interfaces  |  Criar um modelo das interfaces que serão desenvolvidas    |       Product Owner e Equipe de Desenvolvimento         |     Pesquisa de mercado e Boas práticas de UI e UX.       | Canva |
| Codificação das Interfaces (Front-End)  | Desenvolver as telas que os usuários do sistema terão acesso   | Equipe de Desenvolvimento | Seguir o design das interfaces feito previamente  | HTML5/CSS3 |
| Codificação das funções do sistema (Back-End)  |  Desenvolver as funcionalidades do programa em si    |  Equipes de Desenvolvimento     |      Desenvolvimento dos requisitos definidos no escopo do produto.       | Python e Django |
| Tornar o produto responsivo  |  Tornar o produto utilizável tanto no desktop, quanto no dispositivo móvel    |       Desenvolvedor       |     Utilização do PWA       | PWA |
| Realizar Versionamento  |  Acompanhar o progresso do projeto    |           Equipe de Desenvolvimento           |      Controlar as versões no GitHub       | GitHub |
| Realizar Teste Unitário  |  Encontrar possíveis falhas no software    |  Desenvolvedor  |     Criação de classes de teste       | PyUnit |
| Realizar Refatoração  |  Melhorar a qualidade do código    |                Equipe de Desenvolvimento                 | Extração de método, extração de classe, renomeação de método, classe ou variável, extração de interface  | GitHub |
| Entregar produto final  |  Entregar o software em funcionamento para o cliente final    |                Product Owner e Equipe de Desenvolvimento                  | Hospedagem do produto final na Internet  | GitPages |

## 3. Visão Geral do Projeto

### 3.1 Organização do Projeto

| Papel | Atribuições | Responsável | Participantes |
| :---: | :---------- | :---------: | :------------ |
| Desenvolvedor | Codificação, realizar testes unitários, refatoração, versionamento. | Victor | Luan, Marcos, Arthur |
| Product Owner | Desenvolver escopo do produto/product backlog, organizar sprints, validar entregas.  | Felipe | Victor, Luan, Marcos |

### 3.2 Planejamento das Fases e/ou Iterações do Projeto

| Release | Entregas Feitas | Data Prevista de Entrega | 
| :----: | :---------------- | :--------------------:  |
| Release 1 | Documento de Visão do Produto e Projeto. | 03/02/2022 |
| Release 2 | Product Backlog; Documento de Visão do Produto e Projeto Ampliada; Canvas MVP; e Kanban do Projeto. | 24/02/2022 |
| Release 3 | Modelo de Classes de Produto; Modelo de Arquitetura (Visão Lógica); e Protótipos de Interface. | 17/03/2022 |
| Release 4 | Itens de Cadastro e Login que compõem o MVP (Após Prototipação, Codificação, Teste, Revisão e Pedidos de Mudança). | 24/03/2022 |
| Release 5 | Interfaces de Cadastro e Login para os itens desenvolvidos. | 28/03/2022 |
| Release 6 | Itens de Gerenciamento de Treinos que compõem o MVP (Após Prototipação, Codificação, Teste, Revisão e Pedidos de Mudança). | 04/04/2022 |
| Release 7 | Interfaces de Gerenciamento de Treinos para os itens desenvolvidos. | 08/04/2022 |
| Release 8 | Itens de Administração que compõem o MVP (Após Prototipação, Codificação, Teste, Revisão e Pedidos de Mudança). | 15/04/2022 |
| Release 9 | Interfaces de Administração para os itens desenvolvidos. | 18/04/2022 |
| Release 10 | MVP concluído. | 20/04/2022 |
| Release 11 | Produto de Software Final. | 25/04/2022 |

### 3.3 Matriz de Comunicação

| Descrição | Área/Envolvidos | Periodicidade | Produtos Gerados |
| :-------- | :-------------: | :-----------: | :--------------- |
| Acompanhamento das atividades que estão em desenvolvimento, das que ainda estão pendentes e revisar as feitas desde a última reunião. Esse acompanhamento será feito, principalmente, levando em conta o quadro Kanban da equipe. | Equipe do Projeto | Semanal | Ata de Reunião e </br > Relatório de situação da release e do projeto. | 
| Comunicar situação do projeto e </br > Feedback do encaminhamento do projeto. | Equipe do projeto e Professor | Semanal | Ata de Reunião e </br > Relatório de situação do projeto | 

### 3.4 Gerenciamento de Riscos

| Risco | Ação para mitigar |
| :---- | :---------------- |
| Remoção da disciplina por algum aluno. | Manter uma comunicação efetiva entre todos os membros para que se possam ajudar constantemente e manter um ambiente saudável para todos. |
| Horários da equipe serem inflexíveis. | Buscar maximizar o tempo gasto em reuniões, para que os integrantes do grupo possam trabalhar de forma autônoma e remota no projeto com excelência. |
| Não conseguir entregar o MVP. | Organizar as sprints para que o Mínimo Produto Viável seja completamente desenvolvido a tempo. |
| Dificuldade com as tecnologias necessárias. | A equipe dedicar parte do seu tempo na Sprint 3 para estudar o máximo possível de todas as tecnologias que serão usadas durante o desenvolvimento do projeto. |

### 3.5 Critérios de Replanejamento
(Descrever os critérios de replanejamento que serão utilizados, caso seja necessário realizá-lo no projeto)

## 4. Lições Aprendidas

### 4.1 Unidade 1

A unidade 1 trouxe diversas lições e aprendizados no que convém ao começo de um projeto e conceitos iniciais de Engenharia de Software. Entretanto, podemos destacar dois pontos que tiveram maior impacto no grupo como um todo:
1. Primeiramente, a lição referente à escolha da metodologia de desenvolvimento de software. As questões levantadas por Sommerville ajudaram de forma substancial na determinação da abordagem ágil para a realização do projeto, uma vez que a equipe, a priori, não sabia como justificar de forma correta a escolha de uma abordagem e não de outra. 
1. O esclarecimento do que é o Product Owner, quais são suas funções e características também teve grande impacto no grupo, uma vez que pudemos escolher um integrante para trabalhar na função de P.O., o que acreditamos que será de grande ajuda durante todo o projeto. 

### 4.2 Unidade 2

A unidade 2 trouxe diversas lições e aprendizados no que convém a Engenharias de Requisitos, desenvolvimento do Product Backlog e MVP. Entretanto, podemos destacar os seguintes pontos que tiveram maior impacto no grupo como um todo:
1. Primeiramente, a utilização do Framework SAFe, que, a princípio, trouxe dúvidas de como deveria ser destrinchado e organizado. Todavia, após explicações específicas do professor e de um estudo mais focado, o grupo pôde entender e aplicar a organização de épicos, features e histórias de usuário.
1. Conjuntamente com o primeiro ponto, as histórias de usuário foram um grande aprendizado dessa unidade no que convém a entender um software e como ele será desenvolvido, uma vez que trouxe uma visão mais simplificada e palpável das funcionalidades de um sistema.
1. Finalmente, podemos mencionar a estrutura de Canvas MVP para o desenvolvimento do Minímo Produto Viável. O quadro Canvas, com suas divisões de persona, jornada, proposta, funcionalidades, custo e cronograma, resultado esperado e métricas, ajudou a equipe a desenvolver o escopo aquele que será o primeiro produto a ser desenvolvido.

### 4.3 Unidade 3

A unidade 3 foi muito edificante no que convém ao começo propriamente dito da construção do software. Sendo assim, podemos destacar os seguintes pontos como lições aprendidas:
1. Primeiramente, o entendimento da arquitetura que será seguida durante toda a programação do projeto é de extrema importância para que o produto seja consistente durante seu desenvolvimento e para que toda a equipe entenda onde e como serão feitas as partes do software.
1. A construção do famoso diagrama de classes também é importante para saber como serão feitas as classes do projeto e entender os principais objetos e seus métodos que compõem o software como um todo.
1. Finalmente, a definição de um padrão de design do projeto traz, assim como a definição da arquitetura, um entendimento geral de como o software deve ser desenvolvido para todos os integrantes do grupo.

### 4.4 Unidade 4

A unidade 4 foi basicamente mão na massa, mas ainda assim trouxe algumas lições:
1. Primeiramente, a definição de um backlog das releases que serão entregues ajuda substancialmente a organização de como o produto será desenvolvido, a divisão de duplas para trabalho e os prazos de entrega.
1. Além disso, a programação em duplas também foi efetiva para que não houvessem sobrecarregamento dos desenvolvedores, além de que o ditado "duas cabeças pensando é melhor que uma" foi bem aplicado durante as dinâmicas.

### 4.5 Unidade 5

## 5. Documentação Dinâmica em Duplas

### Release 4: Felipe e Victor
Para o desenvolvimento da Release 4, o Felipe e o Victor se reuniram para que, a partir de uma prévia pesquisa de templates de front-end aplicáveis para a arquitetura e framework selecionados (Django), pudesse ser implementada a base html para todas as telas do projeto.</br>
Dessa forma, em uma reunião de aproximadamente 3 horas, o Victor programou o código enquanto o Felipe deu direcionamentos e pesquisou formas de resolver erros que apareceram.</br>
O motivo da escolha da dupla para essa release foi: o Felipe já tinha uma ideia de qual template usar e como implementá-lo em Django e o Victor se dispôs em entender como aplicar a base em todas as telas para que outras duplas a serem formadas pudessem também desenvolver a partir dela sem muitos problemas.

### Release 5: Victor e Marcos
Para o desenvolvimento da Release 5, o Victor e o Marcos se juntaram para que pudesse ser codificadas as histórias: **H02** (Administrador Consultar Estado Financeiro), **H18** (Cadastrar Professores) e **H19** (Cadastrar Alunos).</br>
Primeiramente, houve uma reunião de aproximadamente 2 horas para a criação dos modelos de classes a partir do diagrama de classes desenvolvido na Unidade 3. Nessa reunião, o Marcos programou o código enquanto o Victor ajudou no entendimento da disposição de certas classes e seus tipos.</br>
Em uma segunda reunião mais longa, foi desenvolvida as telas e funções de cadastro de aluno e de professor. Além disso, também foi criada a tela inicial do administrador com a listagem dos principais dados dos alunos (Estado Financeiro incluso) e dos professores. Nessa reunião, o Victor ficou no desenvolvimento de código enquanto o Marcos auxiliou na manipulação dos dados e modelos feitos nas funções que estavam sendo criadas.</br>
O motivo da escolha da dupla para essa release foi: o Marcos havia estudado acerca da criação de modelos e funções de cadastro, já o Victor quis ajudar principalmente na implementação da base html e entender a implementação do projeto em Django na prática.

### Release 6: Luan e Arthur

### Release 7: Victor e Luan


## 6. Referências Bibliográficas

* Sommerville, Ian Engenharia de software/ Ian Sommerville; tradução Luiz Cláudio Queiroz; revisão técnica Fábio Levy Siqueira. -- 10. ed. -- São Paulo: Pearson Education do Brasil, 2018. Título original: Software engineering ISBN 978-65-5011-048-2 1. Engenharia de software I. Siqueira.
