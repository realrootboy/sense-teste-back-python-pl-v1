/* CREATE A TABLE WITH cep AS primary key, logradouro, complemento, bairro, localidade, uf, ibge, gia, ddd, siafi as attributes*/
CREATE TABLE IF NOT EXISTS locations (
    cep varchar(10) NOT NULL,
    logradouro varchar(255) NOT NULL,
    complemento varchar(255) NOT NULL,
    bairro varchar(255) NOT NULL,
    localidade varchar(255) NOT NULL,
    uf varchar(2) NOT NULL,
    ibge varchar(255) NOT NULL,
    gia varchar(255) NOT NULL,
    ddd varchar(255) NOT NULL,
    siafi varchar(255) NOT NULL,
    PRIMARY KEY (cep)
);
