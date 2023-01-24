# create a class location with the following attributes
# cep, logradouro, complemento, bairro, localidade, uf ,ibge, gia, ddd, siafi

class Location (object):
    def __init__(self, cep, logradouro, complemento, bairro, localidade, uf, ibge, gia, ddd, siafi):
        self.cep = cep
        self.logradouro = logradouro
        self.complemento = complemento
        self.bairro = bairro
        self.localidade = localidade
        self.uf = uf
        self.ibge = ibge
        self.gia = gia
        self.ddd = ddd
        self.siafi = siafi

def to_json(location):
    json = {
        'cep': location.cep,
        'logradouro': location.logradouro,
        'complemento': location.complemento,
        'bairro': location.bairro,
        'localidade': location.localidade,
        'uf': location.uf,
        'ibge': location.ibge,
        'gia': location.gia,
        'ddd': location.ddd,
        'siafi': location.siafi
    }
    return json