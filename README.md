# Teste técnico backend python pleno

---

Neste repositório você encontra o teste técnico para a vaga de Desenvolvedor(a) Python pleno
da [Sales Sense](http://salessense.com.br)!
Você provavelmente chegou aqui através da indicação da empresa após passar pelas outras etapas do processo seletivo.
Se este não for o seu caso e mesmo assim você implementar alguma solução para este exercício, ele não será avaliado.

Você devera efetuar um fork deste repositório em seu Github, e tera o prazo estipulado a seguir para conclusão.
Após a conclusão, informar a pessoa da Sales Sense que contatou você para ser feita a avaliação. 

---

### PROBLEMA

A empresa análise de dados Sense Inc tem trabalhado para popular uma base de dados global para seus clientes.

Atualmente eles necessitam de informacoes de enderecos e cidades para utlizar em relatorios.

---

### SOLUÇÃO

Para auxiliar a Sense Inc, você deve desenvolver uma API que consulte e grave em uma tabela do banco de dados
as informacoes do endereco de um determinado CEP que sera recebido pela sua API.

Para isso, foram passados alguns requisitos técnicos:

* A API deve ser desenvolvida utilizando um dos seguintes frameworks web de sua preferencia:
    * FastAPI
    * Flask
    * Django
* Deve possuir um endpoint que receba um CEP, efetue a consulta no ViaCep e cadastre no banco 
* Deve utilizar a API [ViaCEP](https://viacep.com.br) para consultar um Cep recebido
* Utilizar banco de dados PostgreSQL em Docker para gravar as seguintes informacoes:
    * Cep consultado
    * UF
    * Localidade
    * Logradouro
    * Data e hora da consulta
* Deve possuir um endpoint para consultar todos os CEPs ja cadastrados no banco de dados

```
GET /api/localidades/
```

Esse endpoint deverá apresentar os dados no seguinte formato:

```json
 {
  "localidades": [
    {
      "cep": "01001-000",
      "uf": "SP",
      "localidade": "São Paulo",
      "logradouro": "Praça da Sé",
      "data_consulta": "2023-01-11T17:36:13Z"
    },
    {
      "cep": "32310-210",
      "uf": "MG",
      "localidade": "Contagem",
      "logradouro": "Avenida José Faria da Rocha",
      "data_consulta": "2023-01-10T12:14:25Z"
    }
  ]
}
```

Esse endpoint deverá possuim um parametro opcional para filtrar somente as localidades de uma determinada UF:


```
GET /api/localidades/?uf=SP
```

Neste exemplo o endpoint deverá apresentar os dados no seguinte formato:

```json
 {
  "localidades": [
    {
      "cep": "01001-000",
      "uf": "SP",
      "localidade": "São Paulo",
      "logradouro": "Praça da Sé",
      "data_consulta": "2023-01-11T17:36:13Z"
    }
  ]
}
```

Alguns exemplos de CEP:
* 89110-110
* 97542-460
* 88010-907
* 49075-975


---

### AVALIAÇÃO

Iremos seguir as orientacoes que estiverem no README.md do seu fork para subir o projeto e efetuar testes.

Serao avaliados os seguintes pontos:
* Organização do projeto
* Legibilidade do código
* Boas práticas de programação
* Se as funcionalidades descritas nos requisitos técnicos estão funcionando


### PRAZO

3 dias a partir da data combinada para aplicacao do teste
