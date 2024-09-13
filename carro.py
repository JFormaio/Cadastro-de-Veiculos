from Veiculo import veiculo
class carro(veiculo):
    def __init__(self, marca, modelo, placa, ano, n_portas):
        super().__init__(marca, modelo, placa, ano)
        self.__n_portas = n_portas
    #Override - Sobrescrever o método __str__()
    def __str__(self):
        retorno = super().__str__()
        return f'''{retorno}
 - Nº de Portas: {self.__n_portas}'''