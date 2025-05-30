from time import sleep

acai = 0
coxinha = 0
cachorroquente = 0
enrroladinho = 0

while True:
    print("selecione um salgado:")
    print("1. acaí")
    print("2. coxinha")
    print("3. cachorro quente")
    print("4. enrroladinho")
    print("digite 'q' para sair e 'f' para finalizar")
    salgado = input()
    
    if salgado == 1:
        acai = input("quantos? ")
        sleep(1)

    elif salgado == 2:
        coxinha = input("quantos? ")
        sleep(1)

    elif salgado == 3:
        cachorroquente = input("quantos? ")
        sleep(1)

    elif salgado == 4:
        enrroladinho = input("quantos? ")
        sleep(1)

    elif salgado == "q":
        print("saindo...")
        sleep(1)
        exit()

    elif salgado == "f":
        print("acaí: ", acai)
        print("coxinha: ", coxinha)
        print("cachorro quente: ", cachorroquente)
        print("enrroladinho: ", enrroladinho)
        if input("deseja finalizar?(s/n)") == "s":
            print("espere por alguns minutos até que seja feito a sua comida...")
            sleep(1)
            exit()
