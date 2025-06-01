from time import sleep

acai = 0
coxinha = 0
cachorroquente = 0
enrroladinho = 0
moneytotal = 0
moneytotalbackup = 0

while True:
    print("selecione um salgado:")
    print("1. açaí                                  R$15,90")
    print("2. coxinha                               R$04,99")
    print("3. cachorro quente                       R$10,99")
    print("4. enrroladinho                          R$07,89")

    print("5: sair")
    print("6: finalizar compra")
    print("7: personalizar menu")
    salgado = int (input())
    
    if salgado == 1:
        acai += int (input("quantos? "))
        moneytotalbackup = moneytotal
        moneytotal = acai
        moneytotal *= 15.90
        moneytotal += moneytotalbackup
        sleep(1)

    elif salgado == 2:
        coxinha += int (input("quantos? "))
        moneytotalbackup = moneytotal
        moneytotal = coxinha
        moneytotal *= 4.99
        moneytotal += moneytotalbackup
        sleep(1)

    elif salgado == 3:
        cachorroquente += int (input("quantos? "))
        moneytotalbackup = moneytotal
        moneytotal = cachorroquente
        moneytotal *= 10.99
        moneytotal += moneytotalbackup
        sleep(1)

    elif salgado == 4:
        enrroladinho += int (input("quantos? "))
        moneytotalbackup = moneytotal
        moneytotal = coxinha
        moneytotal *= 7.89
        moneytotal += moneytotalbackup
        sleep(1)

    elif salgado == 5:
        print("saindo...")
        sleep(1)
        exit()

    elif salgado == 6:
        print("açaí: ", acai)
        print("coxinha: ", coxinha)
        print("cachorro quente: ", cachorroquente)
        print("enrroladinho: ", enrroladinho)
        print(f"total a gastar: R${moneytotal:.2f}")
        if input("deseja finalizar?(s/n) ") == "s":
            print("espere por alguns minutos até que seja feito a sua comida...")
            sleep(1)
            exit()

    elif salgado == 7:
        print(" ╔════════════════════════════════╗ ")
        print(" ║ modo de personalizacão do menu ║ ")
        print(" ╚════════════════════════════════╝ ")
        print("digite o nome do salgado e em seguida coloque um preço")
