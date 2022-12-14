# cnab_parser

***

## Descrição

### O que é o cnab?

O CNAB (Centro Nacional de Automação Bancária) é uma ferramenta padrão da FEBRABAN (Federação Brasileira de Bancos). Ela é utilizada tanto para a remessa quanto para o retorno de informações sobre clientes para as empresas que utilizam este tipo de serviço.

### Como funciona o CNAB?

A utilização do CNAB alimenta os bancos de dados das empresas e faz com que estes estejam constantemente atualizados em relação aos recebimentos. Além disso, existe a baixa automática dos títulos devido ao padrão de comunicação. O que melhora as atividades e o dia a dia. Uma vez que não é necessário digitar cada boleto que foi compensado.

### O que é o projeto cnab_parser?

O cnab_parser é um projeto desenvolvido em Python, cuja proposta é lidar com o upload de um arquivo CNAB preenchido com dados de movimentações financeiras de várias lojas. A aplicação deve receber um arquivo cnab por formulário, em formato .txt, tratar os dados e popular o banco de dados de forma automática. Para testar a aplicação, um arquivo teste estará localizado na raiz do projeto.

***

## Documentação

>### Preparando o ambiente local para rodar a aplicação

>#### Requisitos: Python 3.0+ instalado

1. Clonar o repositório: `git clone git@github.com:hiquebarros/cnab_parser.git`

2. Criar ambiente virtual: `python -m venv venv`

3. Ativar ambiente virtual: 
   
   - Linux: `source venv/bin/activate`

   - Windows: `.\venv\Scripts\activate`

4. Instalar dependencias localmente: `pip install -r requirements.txt`

5. Rodar as migrações e criar o banco de dados de desenvolvimento: `python manage.py migrate`
6. Subir o servidor: `python manage.py runserver`
   
Pronto, sua aplicação já deve estar pronta para ser utilizada.

![Server running!](https://cdn.discordapp.com/attachments/892221831514308678/1027711728793948170/unknown.png)

>### Utilizando o cnab_parser

- `http://localhost:8000/api/cnab/`
  
![cnab url](https://cdn.discordapp.com/attachments/892221831514308678/1027719068620443731/cnab_url.png)

Essa rota disponibiliza um formulário para ser feito o upload do arquivo CNAB. Após feito o upload, será criada uma pasta /media na raiz do repositório, onde serão guardados todos os arquivos. Ao mesmo tempo que guarda os arquivos, a aplicação já interpreta e popula o banco de dados com as remessas parseadas.

- `http://localhost:8000/api/cnab/NOME DA LOJA/`

![cnab url](https://cdn.discordapp.com/attachments/892221831514308678/1027719562646536273/unknown.png)

Essa rota disponibiliza a lista de transferências de uma loja específica. A url recebe como paramêtro o nome da loja, que deve ser escrito da mesma forma que se encontra no CNAB.



 
 








