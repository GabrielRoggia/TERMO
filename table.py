import os
import menu
from unidecode import unidecode


def quadrant(tables,title = "TERMO", clean = True):
    if clean == True:
        os.system('cls') or None
    print("\t"+"{:^53}".format(title))
    top = "\t{:^}".format(menu.top_left_cornor+(menu.horizontal_line*3+menu.t_line)*4+menu.horizontal_line*3+menu.top_right_cornor)
    text_format = "\t"+menu.vertical_line+"{:^}"+menu.vertical_line+"{:^}"+menu.vertical_line+"{:^}"+menu.vertical_line+"{:^}"+menu.vertical_line+"{:^}"+menu.vertical_line
    mid = "\t{:^}".format(menu.left_t_line+(menu.horizontal_line*3+menu.cross_line)*4+menu.horizontal_line*3+menu.rigt_t_line)
    bot = "\t{:^}".format(menu.botton_left_cornor+(menu.horizontal_line*3+menu.inverse_t_line)*4+menu.horizontal_line*3+menu.botton_right_cornor)
    
    
    
    print(top,"\t", top)
    for i in range(len(tables[0])):
        print(text_format.format(tables[0][i][0],tables[0][i][1],tables[0][i][2],tables[0][i][3],tables[0][i][4]),"\t", text_format.format(tables[1][i][0],tables[1][i][1],tables[1][i][2],tables[1][i][3],tables[1][i][4]))
        if i != len(tables[0])-1:
            print(mid,"\t", mid)
    print(bot,"\t",bot)
    
    if len(tables) > 2:
        print("\n\n")
        print(top,"\t", top)
        for i in range(len(tables[2])):
            print(text_format.format(tables[2][i][0],tables[2][i][1],tables[2][i][2],tables[2][i][3],tables[2][i][4]),"\t", text_format.format(tables[3][i][0],tables[3][i][1],tables[3][i][2],tables[3][i][3],tables[3][i][4]))
            if i != len(tables[2])-1:
                print(mid,"\t", mid)
        print(bot,"\t",bot)
        
           
def generate_table(tentatives):
    table=[]
    for i in range(tentatives):
        table.append([])
        for j in range(5):
            table[i].append(print_color("d"," "))
    
    return table

def print_table(table, clean = True):
    if clean == True:
        os.system('cls') or None
    print("\t\t\t{:^21}".format("TERMO"))
    print("\t\t\t{:^}".format(menu.top_left_cornor+(menu.horizontal_line*3+menu.t_line)*4+menu.horizontal_line*3+menu.top_right_cornor))
    
    text_format = "\t\t\t"+menu.vertical_line+"{:^}"+menu.vertical_line+"{:^}"+menu.vertical_line+"{:^}"+menu.vertical_line+"{:^}"+menu.vertical_line+"{:^}"+menu.vertical_line
    for line in range(len(table)):
        print(text_format.format(table[line][0],table[line][1],table[line][2],table[line][3],table[line][4]))
        if line != len(table)-1:
            print("\t\t\t{:^}".format(menu.left_t_line+(menu.horizontal_line*3+menu.cross_line)*4+menu.horizontal_line*3+menu.rigt_t_line)) 
    print("\t\t\t{:^}".format(menu.botton_left_cornor+(menu.horizontal_line*3+menu.inverse_t_line)*4+menu.horizontal_line*3+menu.botton_right_cornor))
       
def print_color(color,letter):
    
    if color == "y":
        return f"\033[43m {letter} \033[0m"
    elif color == "g":
        return f"\033[42m {letter} \033[0m"
    elif color == "d":
        return f"\033[40m {letter} \033[0m"
    elif color == "r":
        return f"\033[41m {letter} \033[0m"
    elif color == "tr":
        return f"\033[91m{letter}\033[0m"
    
def mark_letters(sorted_word, guess_word):
    mark_word = ["","","","",""]
    word_list = list(unidecode(sorted_word))

    for i in range (len(mark_word)):
        if unidecode(guess_word[i]) == unidecode(sorted_word[i]):
            mark_word[i] = print_color("g",guess_word[i])
            word_list.remove(unidecode(sorted_word[i]))
            
    for i in range (len(mark_word)):
        if unidecode(guess_word[i]) in word_list and mark_word[i] == "":
            mark_word[i] = print_color("y",guess_word[i])
    
    for i in range (len(mark_word)):
        if mark_word[i] == "": 
            mark_word[i] = print_color("d",guess_word[i])
            
    return mark_word