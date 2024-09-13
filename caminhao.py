from Veiculo import veiculo

class caminhao(veiculo):
    def __init__(self, marca, modelo, placa, ano, carga):
        super().__init__(marca, modelo, placa, ano)
        self.__carga = carga
    
    def __str__(self):
        retorno = super().__str__()
        
        return f'''{retorno}
 - Carga: {self.__carga}'''