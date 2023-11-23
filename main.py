import menu
import termo
import word


def main():
    while True:
        op = menu.generate_menu("TERMO",["JOGAR","OPÇÕES","SAIR"])
        
        if op == 1:
            termo.new_game(termo.gamemode)
        elif op == 2:
            while True:
                op = menu.generate_menu("OPÇÕES",["MODO DE JOGO","REDEFINIR PALAVRAS","ADICIONAR PALAVRA","REMOVER PALAVRA","VOLTAR"])
                if op == 1:
                    while True:
                        op = menu.generate_menu("MODO DE JOGO",menu.gamemode_button(termo.gamemode))
                        if op >= 1 and op <= 3:
                            termo.gamemode = op
                        elif op == 4:
                            break
                elif op == 2:
                    word.reset_words()
                    menu.warning_menu("PALAVRAS REDEFINIDAS!", True)
                    input("> Aperte enter para continuar...")
                    
                elif op == 3:
                    menu.warning_menu("ADICIONAR PALAVRA!", True)
                    add = word.add_word()
                    if add == 1:
                        menu.warning_menu("PALAVRA ADICIONADA!")
                        input("> Aperte enter para continuar...")
                    elif add == 2:
                        menu.warning_menu("PALAVRA JÁ ADICIONADA!")
                        input("> Aperte enter para continuar...")
                    else:
                        menu.warning_menu("PALAVRA INVÁLIDA!")
                        input("> Aperte enter para continuar...")
                        
                elif op == 4:
                    menu.warning_menu("REMOVER PALAVRA!", True)
                    remove = word.remove_word()
                    if remove == True:
                        menu.warning_menu("PALAVRA REMOVIDA!")
                        input("> Aperte enter para continuar...")
                    else:
                        menu.warning_menu("PALAVRA NÃO ENCONTRADA!")
                        input("> Aperte enter para continuar...")
                        
                elif op == 5:
                    break
        elif op == 3:
            break

main()