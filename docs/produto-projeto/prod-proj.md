# Visão do Produto e Projeto

## Histórico de Revisão

| Data       | Versão | Descrição | Autor |
| :---       | :----: | :-------- | :---: |
| 31/01/2022 | 1.0    |  Primeira versão do documento. Em que todos os quadros, tanto de problema, quanto de produto foram preenchidos. A metodologia escolhida e suas justificativas também são adicionadas pela primeira vez no documento. As lições aprendidas da Unidade 1 são descritas nessa versão do documento. | Victor Hugo Oliveira Leão; Felipe Alef Pereira Rodrigues |
| 08/02/2022 | 1.1 | Correção de ajustes apontados pelo professor nos quesitos: O problema; Objetivos do Produto; Como está organizado o time de desenvolvimento?; É importante ter uma especificação e um projeto (design) bem detalhados antes de passar para a implementação - talvez por motivos contratuais? | Victor Hugo Oliveira Leão; Felipe Alef Pereira Rodrigues |
| 14/02/2022 | 2.0 | Adição de novos tópicos (Escopo do Produto e Visão Geral do Projeto), para as entregas da Unidade 2 em diante. Primeira versão dos requisitos funcionais e não-funcionais. | Victor Hugo Oliveira Leão; Marcos Well Neres Silva Pereira |

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

| Versão | Requisito | Prioridade |
| :----: | :-------: | :--------: |
|   1.0  | O **aluno** deve ser capaz de consultar todas as fichas de treino atribuídas a ele. | Alta |
|   1.0  | O **aluno** deve poder informar e alterar seus objetivos na academia. | Alta |
|   1.0  | O **aluno** deve ser capaz de mandar uma mensagem para a academia pelo sistema. | Média |
|   1.0  | O **aluno** deve ser capaz de visualizar o resultado de suas avaliações físicas. | Média |
|   1.0  | O **aluno** deve ser capaz de filtrar suas avaliações físicas por período. | Baixa |
|   1.0  | O **aluno** deve ser capaz de consultar seu estado financeiro. | Alta |
|   1.0  | O **aluno** deve poder visualizar suas frequências na academia (dias em que ele foi na academia e dias que não). | Baixa |
|   1.0  | O **aluno** deve ser capaz de filtrar suas frequências por mês. | Baixa |
|   1.0  | O **administrador** deve ser capaz de realizar o cadastro de um novo aluno. | Alta |
|   1.0  | O **administrador** deve ser capaz de realizar o cadastro de um novo professor. | Alta |
|   1.0  | O **administrador** deve poder visualizar a situação financeira de cada aluno. | Alta |
|   1.0  | O **administrador** deve ser capaz de filtrar os alunos por situação financeira (em dia ou inadimplente). | Média |
|   1.0  | O **administrador** deve poder consultar o controle de frequência de cada aluno. | Alta |
|   1.0  | O **administrador** deve ser capaz de buscar os alunos por nome. | Média |
|   1.0  | O **administrador** deve poder enviar e-mails personalizados (por nome do aluno) para cada aluno acerca de sua situação financeira ou frequência. | Alta |
|   1.0  | O **administrador** deve ser capaz de visualizar cada professor e os alunos atrelados a ele. | Média |
|   1.0  | O **administrador** deve ser capaz de filtrar os professores por nome. | Baixa |
|   1.0  | Os **professores** devem ser capazes de visualizar as avaliações físicas e os objetivos de cada aluno. | Alta |
|   1.0  | Os **professores** devem poder montar os treinos personalizados para cada aluno. | Alta |
|   1.0  | Os **professores** devem ser capazes de buscar os alunos por nome. | Média |
|   1.0  | Os **professores** devem ser capazes de filtrar os alunos por objetivos na academia. | Baixa |
|   1.0  | Os **professores** devem poder visualizar sua rotina. | Alta |
|   1.0  | Os **professores** devem ser capazes de visualizar os alunos atrelados a eles. | Média |

**Legenda**:
* Prioridade Alta: São os requisitos necessários para que os objetivos do produto sejam cumpridos.
* Prioridade Média: São os requisitos que complementam os requisitos de prioridade alta, mas não são essenciais para o funcionamento do sistema.
* Prioridade Baixa: São os requisitos que facilitam e incrementam o uso do sistema, mas que sem eles, o produto funciona e entrega o necessário.

#### 1.4.2 Requisitos Não-Funcionais

1. O sistema SoftFit deverá estar disponível durante os horários de funcionamento da academia.
1. O sistema deve ser desenvolvido na linguagem Python com o framework Django.
1. O sistema deve ser uma aplicação web responsiva.
1. O versionamento do sistema deve ser feito pelo GitHub.
1. Todas as documentações do sistema devem estar disponíveis na GitPages do repositório.
1. Caso o produto tenha andamento após o fim da disciplina, o sistema deve seguir a Lei Geral de Proteção de Dados (Lei nº 13.709/2018 – “LGPD”).

### 1.5 Minímo Produto Viável (MVP)

Forneça uma lista de requisitos (funcionais e não-funcionais) mínimos (derivadas do escopo geral do produto) que o produto deve possuir para que possa ser lançado.

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
| Criar quadro Kanban  |  Organizar o quadro que a equipe utilizará para se orientar durante o desenvolvimento    |       Product Owner e Equipe de Desenvolvimento        |     Requisitos – Em desenvolvimento - Entregue       | Trello |
| Estabelecer o prazo de entregas  |  Organizar os requisitos a serem entregues em relação ao tempo    |             Product Owner e Equipe de Desenvolvimento              |      Analisar datas da disciplina com os requisitos definidos      | Trello |
| Estabelecer escopo do produto  |  Definir as características que devem estar presentes no produto de software    |               Product Owner e Equipe de Desenvolvimento                 | EAP – Estrutura Analítica de Projeto  | Trello |
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
(Apresentada a divisão de atribuições e responsabilidades entre os membros do projeto, sem qualquer relação de hierarquia ou grau de importância. Todos os integrantes são igualmente importantes e responsáveis pelo sucesso do projeto)

### 3.2 Planejamento das Fases e/ou Iterações do Projeto
(Registrar o projeto, as fases de seu ciclo de vida e suas iterações, especificando suas datas de início e de fim, bem como os produtos a serem gerados)

### 3.3 Matriz de Comunicação
(Esta seção descreve a estratégia de comunicação adotada para monitoramento do progresso do projeto. Identificar a periodicidade de reuniões e o envio dos relatórios exigidos pelo processo e opcionalmente outros relatórios exigidos pelo cliente)

### 3.4 Gerenciamento de Riscos
(Para o Gerenciamento de Riscos devem ser realizadas tarefas, como:   

Identificar todos os riscos possíveis e detectáveis em cada fase do projeto;  

Executar as ações para mitigar os riscos que tenham um alto grau de exposição ao risco caso este ocorra na Lista de Riscos do Projeto; 

Fazer uma revisão da lista dos riscos periodicamente, com o propósito de averiguar uma possível incidência de um risco e ver se há outros riscos ainda não relatados; 

Em caso de confirmação de um risco previsto, agir no sentido de contingenciá-lo conforme programado; 

Registrar os riscos no Painel de Controle do Projeto e no Plano do Projeto (Riscos iniciais);)

### 3.5 Critérios de Replanejamento
(Descrever os critérios de replanejamento que serão utilizados, caso seja necessário realizá-lo no projeto)

## 4. Lições Aprendidas

### 4.1 Unidade 1

A unidade 1 trouxe diversas lições e aprendizagens no que convém ao começo de um projeto e conceitos iniciais de Engenharia de Software. Entretanto, podemos destacar dois pontos que tiveram maior impacto no grupo como um todo:
1. Primeiramente, a lição referente à escolha da metodologia de desenvolvimento de software. As questões levantadas por Sommerville ajudaram de forma substancial na determinação da abordagem ágil para a realização do projeto, uma vez que a equipe, a priori, não sabia como justificar de forma correta a escolha de uma abordagem e não de outra. 
1. O esclarecimento do que é o Product Owner, quais são suas funções e características também teve grande impacto no grupo, uma vez que pudemos escolher um integrante para trabalhar na função de P.O., o que acreditamos que será de grande ajuda durante todo o projeto. 

### 4.2 Unidade 2
### 4.3 Unidade 3
### 4.4 Unidade 4
### 4.5 Unidade 5

## 5. Referências Bibliográficas

* Sommerville, Ian Engenharia de software/ Ian Sommerville; tradução Luiz Cláudio Queiroz; revisão técnica Fábio Levy Siqueira. -- 10. ed. -- São Paulo: Pearson Education do Brasil, 2018. Título original: Software engineering ISBN 978-65-5011-048-2 1. Engenharia de software I. Siqueira.