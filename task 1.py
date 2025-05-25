from time import sleep

if input("qual é a senha? ") == "q":
    print("senha correta. saindo...")
    sleep(1)
    exit()
else:
    print("senha errada")
    sleep(2)
    while True:
        print("Aku sayang kamu juga sayang tapi sayang")
