class veiculo:
    # __init_ => é o método construtor
    def __init__(self, marca, modelo, placa, ano):
        self.__marca = marca
        self.__modelo = modelo
        self.__placa = placa
        self.__ano = ano
    #Métodos getters and setters para os atributos privados
    def get_marca(self):
        return self.__marca
    def set_marca(self, marca):
        if marca != "Peugeot":
            self.__marca = marca.upper()
    def get_modelo(self):
        return self.__modelo
    def set_modelo(self, modelo):
        self.__modelo = modelo
    def get_placa(self):
        return self.__placa
    def set_placa(self, placa):
        self.__placa = placa
    def get_ano(self):
        return self.__ano
    def set_ano(self, ano):
        if ano >= 1900:
            self.__ano = ano
    # Método de instância
    def calcularTempoUso(self):
        return 2024 - self.__ano
    def __str__(self):
        return f'''Marca: {self.__marca}
 - Modelo: {self.__modelo}
 - Placa: {self.__placa}
 - Ano: {self.__ano}'''