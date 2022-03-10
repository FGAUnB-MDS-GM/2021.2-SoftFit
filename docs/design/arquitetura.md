# Arquitetura do Projeto

## Histórico de Revisão

| Data       | Versão | Descrição | Autor |
| :---       | :----: | :-------- | :---: |
| 10/03/2022 | 1.0 | Primeira versão do documento, em que se encontra uma explicação da arquitetura escolhida (MTV) pelo grupo. | Victor, Felipe, Marcos e Luan |

## Arquitetura MTV

Uma vez que o projeto será uma aplicação Web desenvolvida em **Python**, usando o Framework **Django**, a arquitetura escolhida e que será seguida é a proposta pelo Django: MTV (Model, Template e View). A arquitetura acontece como mostrado na figura 1:
![Arquitetura MTV](../_media/django.png "Arquitetura MTV")

### Model

A **Model** se refere ao mapeamento do banco de dados para o projeto. É nela que se realiza a modelagem de dados e como eles serão armazenados no banco.
O arquivo responsável pela implementação da Model é o **models.py**.

### Template

A **Template** se responsabiliza pelas apresentação das páginas em si para o usuário, em que ele pode interagir, trocar informações de dados (tanto recebendo dados de input, quanto gerando dados de output) ou somente visualizar a aplicação.
É nessa camada que se encontra os arquivos **.html** que serão mostrados pelo navegador. Basicamente, é o "Front-End" da aplicação.

### View

A **View** possui a lógica de negócio. A partir de parâmetros/request recebidos pelo arquivo **urls.py**, a View aplica sua lógica e retorna as informações necessárias. Diferentemente da arquitetura MVC em que a View seria como os dados são mostrados, na MTV, a View apresenta quais dados serão apresentados.
O arquivo que faz as implementações responsáveis pela View é o **views.py**.

## Funcionamento da Arquitetura

Todas as 3 partes da arquitetura são interligadas e igualmente importante para o funcionamento completo do projeto. 
O Django trabalha com requisições e respostas. Ao haver uma atualização ou mudança na Template, é enviada uma solicitação para o servidor por meio da View. Ao receber uma solicitação, a lógica da aplicação é acionada e a URL é verificada e, uma vez validada, um status http é retornado e a Template renderiza o solicitado no HTML.
O funcionamento da arquitetura pode ser entendido pela figura 2:

![Visualização MTV](../_media/mtv.png "Funcionamento MTV")

## Fontes
1. Figura 1: https://pythonacademy.com.br/blog/desenvolvimento-web-com-python-e-django-introducao
1. Figura 2: https://diandrasilva.medium.com/como-funciona-a-arquitetura-mtv-django-86af916f1f63