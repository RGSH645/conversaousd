def converter_dolar_para_real():
    cotaçao_dolar = 5.64
    dolares = float(input("Digite o valor em dolares (usd): "))
    reais = dolares * cotaçao_dolar
    print("----------------------------------------------------------------")
    print(f"{dolares} usd equivale a R$ {reais: .2f}")


def converter_real_para_dolar():
    cotaçao_dolar = 5.64
    reais  = float(input("Digite o valor em reais  (brl): "))
    dolares = reais / cotaçao_dolar
    print("----------------------------------------------------------------")
    print(f"{reais} brl equivale a US$ {dolares: .2f}")


def  menu():
    while True: 
        print("\nConversor de moedas")
        print("[1] Converter dolar para Real")
        print("[2] Converter Real para dolar")
        print("[0] Sair")
        opção = input("Escolha uma opção:")


        if opção == "1":
            converter_dolar_para_real()
        elif opção =="2":
            converter_real_para_dolar()
        elif opção == "0":
            print("Saindo...")
            break
        else:
            print("!!! opção invalida. tente novamente. !!!")
menu()