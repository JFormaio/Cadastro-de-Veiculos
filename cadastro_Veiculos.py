from Carro import carro
from Moto import moto
from Caminhao import caminhao
from Veiculo import veiculo
#BD em memória
listaveiculos = [
    carro("Hyundai", "HB20", "ABC", 2023, 4),
    moto("Yamaha", "Lander", "DEF", 2008, 250),
    caminhao("Volvo", "FH540", "GHI", 2015, 80)
]

def cadastrar():
    print("Qual o tipo de Veículo: (1) Carro - (2) Moto - (3) Caminhão")
    tipo = input()
    print("Digite a Marca:")
    marca = input()
    print("Digite o Modelo:")
    modelo = input()
    print("Digite a Placa:")
    placa = input()
    print("Digite o Ano:")
    ano = input()
    if tipo == "1":
        nPortas = input("Digite o número de Portas: ")
        veiculoAdd = carro(marca, modelo ,placa, ano, nPortas)
    elif tipo == "2":
        cilindradas = input("Digite as Cilindradas: ")
        veiculoAdd = moto(marca, modelo, placa, ano, cilindradas)
    elif tipo == "3":
        capCarga = input("Digite a capacidade de Carga: ")
        veiculoAdd = caminhao(marca, modelo, placa, ano, capCarga)
    listaveiculos.append(veiculoAdd)

def listar():
    if len(listaveiculos) == 0:
        print ("Não existem veículos cadastrados")
    else:
        i = 1
        for veiculo in listaveiculos:
            print(f"Veículo: {i}")
            print(f" - {veiculo}")
            i += 1

def excluir():
    listar()
    print("Digite a Placa que deseja excluir")
    placa = input()
    encontrou = False
    for veiculo in listaveiculos:
        if veiculo.get_placa() == placa:
            listaveiculos.remove(veiculo)
            encontrou = True
            break
    if encontrou:
        print("Veículo excluído")
    else:
        print("Veículo não encontrado")


while True:
    print("Escolha uma das Opções:")
    print("1 - Cadastrar Veículo")
    print("2 - Listar Veículos")
    print("3 - Excluir Veículo")
    print("0 - SAIR")
    opcao = input()
    try:
        opcao = int(opcao)
    except:
        print("Opção Inválida")
    if opcao == 1:
        cadastrar()
    elif opcao == 2:
        listar()
    elif opcao == 3:
        excluir()
    elif opcao == 0:
        break
    else:
        print("Opção Inválida")