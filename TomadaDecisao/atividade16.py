ip=input("Digite um [IP] válido: ")
octeto=int((ip[0]+ip[1]+ip[2]))
if(0<=octeto<=127):
    print("IP classe [A]")
else:
    if(128<=octeto<=191):
        print("IP classe [B]")
    else:
        if(192<=octeto<=223):
            print("IP classe [C]")
        else:
            if(224<=octeto<=239):
                print("IP classe [D]")
            else:
                if(240<=octeto<=255):
                    print("IP classe [E]")
                else:
                    print("IP Inválido")