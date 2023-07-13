while True:
    Castanho = input("O seu(ua) personagem possui algo castanho ou marrom? (olho, cabelo e pele)\n")

    if Castanho == "s":
        Gênero = input("O seu(ua) personagem é do sexo masculino?\n")

        if Gênero == "s":
            Pele_Escura = input("O seu personagem possui pele escura?\n")

            if Pele_Escura == "n":
                Barba = input("O seu personagem possui barba?\n")

                if Barba == "s":
                    Ruivo = input("O seu personagem possui pelos ruivos?\n")

                    if Ruivo == "s":
                        print("O seu personagem é o Daniel\n")
                    else:
                        print("O seu personagem é o Ricardo\n")
                else:
                    Olho_Azul = input("O seu personagem possui olhos azuis?\n")

                    if Olho_Azul == "s":
                        print("O seu personagem é o Francisco\n")
                    else:
                        print("O seu personagem é o Rodrigo\n")
            else:
                Acessório = input("O seu personagem está usando algum acessório?\n")

                if Acessório == "s":
                    Boca_Aberta = input("O seu personagem está com a boca aberta ou sorrindo?\n")

                    if Boca_Aberta == "s":
                        print("O seu personagem é o Gabriel\n")
                    else:
                        print("O seu personagem é o Robson\n")
                else:
                    print("O seu personagem é o Marcelo\n")
        else:
            Pele_Escura = input("A sua personagem possui pele escura?\n")

            if Pele_Escura == "s":
                Brinco_Rosa = input("A sua personagem está usando um brinco rosa?\n")

                if Brinco_Rosa == "n":
                    print("A sua personagem é a Nathalia\n")
                else:
                    Olho_Verde = input("A sua personagem possui olhos verdes?\n")

                    if Olho_Verde == "s":
                        print("A sua personagem é a Karina\n")
                    else:
                        print("A sua personagem é a Gisele\n")
            else:
                Usa_Brinco = input("A sua personagem está usando um brinco?\n")

                if Usa_Brinco == "s":
                    print("A sua personagem é a Mariana\n")
                else:
                    Loira = input("A sua personagem possui pelos loiros?\n")

                    if Loira == "s":
                        print("A sua personagem é a Paula\n")
                    else:
                        print("A sua personagem é a Julia\n")
    else:
        Gênero = input("O seu(ua) personagem é do sexo masculino?\n")

        if Gênero == "s":
            Olho_Preto = input("O seu personagem possui olhos pretos?\n")

            if Olho_Preto == "s":
                Acessório = input("O seu personagem está usando algum acessório?\n")

                if Acessório == "n":
                    print("O seu personagem é o Renato\n")
                else:
                    Cabelo = input("O seu personagem possui cabelo?\n")

                    if Cabelo == "s":
                        print("O seu personagem é o João\n")
                    else:
                        print("O seu personagem é o Felipe\n")
            else:
                Acessório_Cabeca = input("O seu personagem está usando algum acessório na cabeça?\n")

                if Acessório_Cabeca == "n":
                    print("O seu personagem é o Bruno\n")
                else:
                    Loiro = input("O seu personagem possui pelos loiros?\n")

                    if Loiro == "s":
                        print("O seu personagem é o Eduardo\n")
                    else:
                        print("O seu personagem é o Pedro\n")
        else:
            Boca_Aberta = input("A sua personagem está com a boca aberta ou sorrindo?\n")

            if Boca_Aberta == "s":
                Ruiva = input("A sua personagem possui pelos ruivos?\n")

                if Ruiva == "s":
                    print("A sua personagem é a Aline\n")
                else:
                    Olho_Azul = input("A sua personagem possui olho azul?\n")

                    if Olho_Azul == "s":
                        print("A sua personagem é a Marta\n")
                    else:
                        print("A sua personagem é a Juliana\n")
            else:
                Loira = input("A sua personagem possui pelos loiros?\n")

                if Loira == "s":
                    print("A sua personagem é a Erica\n")
                else:
                    print("A sua personagem é a Sônia\n")

    jogar_novamente = input("Deseja jogar novamente?\n")
    if jogar_novamente == "n":
        break
