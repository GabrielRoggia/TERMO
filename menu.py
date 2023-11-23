import os
import table
import termo
import menu

top_left_cornor = u'\u2554'
top_right_cornor = u'\u2557'
horizontal_line = u'\u2550'
vertical_line = u'\u2551'
rigt_t_line = u'\u2563'
left_t_line = u'\u2560'
botton_left_cornor = u'\u255A'
botton_right_cornor = u'\u255D'
cross_line = u'\u256C'
t_line = u'\u2566'
inverse_t_line = u'\u2569'

def generate_menu(title, op_list):
    while True:
        try:
            os.system('cls') or None
            space = 25
            header = "{:^"+str(space)+"}"
            text = "{:<"+str(space)+"}"
            print("\n"+top_left_cornor+horizontal_line*space+top_right_cornor)
            print(vertical_line+header.format(title)+vertical_line)
            print(left_t_line+horizontal_line*space+rigt_t_line)
            print(vertical_line+" "*space+vertical_line)
            for i in range(len(op_list)):
                if i == len(op_list) - 1:
                    print(vertical_line+" "*space+vertical_line)
                print(vertical_line+text.format(f"  {(i+1)}-{op_list[i]}")+vertical_line)
            print(botton_left_cornor+horizontal_line*space+botton_right_cornor)

            option = int(input("> Digite uma opção:"))

            return option
        
        except ValueError:
            pass
        except BaseException as error:
            print(table.print_color("tr","[ERROR]")+" Aconteceu um erro:", error)
            print(menu.horizontal_line*40)
    
    
    
def gamemode_button(gamemode):
    
    if termo.gamemode == 1:
        classic = table.print_color("d","OFF")+table.print_color("g","ON")
        duet = table.print_color("r","OFF")+table.print_color("d","ON")
        quartet = table.print_color("r","OFF")+table.print_color("d","ON")
    elif termo.gamemode == 2:
        classic = table.print_color("r","OFF")+table.print_color("d","ON")
        duet = table.print_color("d","OFF")+table.print_color("g","ON")
        quartet = table.print_color("r","OFF")+table.print_color("d","ON")
    elif termo.gamemode == 3:
        classic = table.print_color("r","OFF")+table.print_color("d","ON")
        duet = table.print_color("r","OFF")+table.print_color("d","ON")
        quartet = table.print_color("d","OFF")+table.print_color("g","ON")
    
    buttons = ["CLASSICO   "+classic+" ","DUETO      "+duet+" ","QUARTETO   "+quartet+" ","VOLTAR"]
    return buttons 

def warning_menu(text, clean = False):
    if clean == True:
        os.system('cls') or None
        
    space = 25
    header = "{:^"+str(space)+"}"
    
    print(top_left_cornor+horizontal_line*space+top_right_cornor)
    print(vertical_line+header.format(text)+vertical_line)
    print(botton_left_cornor+horizontal_line*space+botton_right_cornor)