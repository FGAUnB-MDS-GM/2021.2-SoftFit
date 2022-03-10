# Arquitetura do Projeto

## Histórico de Revisão

| Data       | Versão | Descrição | Autor |
| :---       | :----: | :-------- | :---: |
| 10/03/2022 | 1.0 | Primeira versão do documento, em que se encontra uma explicação da arquitetura escolhida (MTV) pelo grupo. | Victor, Felipe, Marcos e Luan |

## Arquitetura MTV

Uma vez que o projeto será uma aplicação Web desenvolvida em **Python**, usando o Framework **Django**, a arquitetura escolhida e que será seguida é a proposta pelo Django: MTV (Model, Template e View). É bem similar à famosa MVC (Model, View, Controller).

### Model

A **Model** se refere ao mapeamento do banco de dados para o projeto. É nela que se realiza a modelagem de dados e como eles são armazenados no banco.

### Template

A **Template** se responsabiliza pelas páginas em que os dados serão visualizados pelo usuário. 
É nessa camada que se encontra os arquivos HTML que serão mostrados pelo navegador. Basicamente, o "Front-End" da aplicação.

### View

A **View** possui a lógica de negócio. A partir de parâmetros/request recebidos, a View aplica sua lógica e retorna as informações necessárias.

## Funcionamento da Arquitetura

Todas as 3 partes da arquitetura são interligadas e igualmente importante para o funcionamento completo do projeto. 
O Django trabalha com requisições e respostas. Ao haver uma atualização ou mudança na Template, é enviada uma solicitação para o servidor por meio da View. Ao receber uma solicitação, a lógica da aplicação é acionada e a URL é verificada e, uma vez validada, um status http é retornado e a Template renderiza o solicitado no HTML.
O funcionamento da arquitetura pode ser entendido pela seguinte imagem:

![Visualização MTV](../_media/mtv.png "Funcionamento MTV")