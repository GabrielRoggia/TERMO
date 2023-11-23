import table
import word
from unidecode import unidecode

gamemode = 1


def new_game(gamemode):
    tryes = []
    count = 0
    letters  = ["\t\t\t",'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P',"\n\t\t\t ",
                    'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L',"\n\t\t\t  ",
                        'Z', 'X', 'C', 'V', 'B', 'N', 'M']
    
    if gamemode == 1:
       
        tentatives = 6
        sorted_word = word.random_word(1)
        new_table = table.generate_table(tentatives)
        
        table.print_table(new_table)
        print("\n")
        
        while True:
            word.print_letters(letters)
            guess_word = word.get_guess_word(tryes)
            letters = word.used_letters(letters, guess_word)
                    
            new_table[count] = table.mark_letters(sorted_word[0], guess_word)
            table.print_table(new_table)
            print("\n")
            tentatives -= 1
            count += 1
            
            if unidecode(guess_word) == unidecode(sorted_word[0]):
                print("{:^}".format(f"Você ganhou! a palavra era {sorted_word[0]}!"))
                word.used_words(sorted_word[0].lower())
                break
            elif tentatives == 0:
                print("{:^}".format(f"Você perdeu! a palavra era {sorted_word[0]}!"))
                break
            
        input("\n> Aperte enter para voltar...")
        
    elif gamemode == 2:
        
        win = [False, False]
        tentatives = 7
        sorted_word = word.random_word(2)
        tables = [table.generate_table(tentatives),table.generate_table(tentatives)]
        
        table.quadrant(tables, "DUETO!")
        print("\n")
        
        while True:
            
            word.print_letters(letters)
            guess_word = word.get_guess_word(tryes)
            letters = word.used_letters(letters, guess_word)
            
            if win[0] != True:
                tables[0][count] = table.mark_letters(sorted_word[0], guess_word)
            if win[1] != True:
                tables[1][count] = table.mark_letters(sorted_word[1], guess_word)
            
            tentatives -= 1
            count += 1

            if unidecode(guess_word) == unidecode(sorted_word[0]):
                win[0] = True
                word.used_words(sorted_word[0].lower())

            if unidecode(guess_word) == unidecode(sorted_word[1]):
                win[1] = True
                word.used_words(sorted_word[1].lower())
            
            table.quadrant(tables, "DUETO!")
            print("\n")
            
            if win[0] == True and win[1] == True:
                print("{:^}".format(f"Você ganhou! as palavras eram {sorted_word[0]} e {sorted_word[1]}!"))
                break
            elif tentatives == 0:
                print("{:^}".format(f"Você perdeu! as palavras eram {sorted_word[0]} e {sorted_word[1]}!"))
                break
        
        input("\n> Aperte enter para voltar...")
            
    elif gamemode == 3:
        
        win = [False, False, False, False]
        tentatives = 9
        sorted_word = word.random_word(4)
        tables = [table.generate_table(tentatives),table.generate_table(tentatives),table.generate_table(tentatives),table.generate_table(tentatives)]
        
        table.quadrant(tables, "QUARTETO!")
        print("\n")
        
        while True:
            
            word.print_letters(letters)
            guess_word = word.get_guess_word(tryes)
            letters = word.used_letters(letters, guess_word)
            
            if win[0] != True:
                tables[0][count] = table.mark_letters(sorted_word[0], guess_word)
            if win[1] != True:
                tables[1][count] = table.mark_letters(sorted_word[1], guess_word)
            if win[2] != True:
                tables[2][count] = table.mark_letters(sorted_word[2], guess_word)
            if win[3] != True:
                tables[3][count] = table.mark_letters(sorted_word[3], guess_word)
            
            tentatives -= 1
            count += 1

            if unidecode(guess_word) == unidecode(sorted_word[0]):
                win[0] = True
                word.used_words(sorted_word[0].lower())
            if unidecode(guess_word) == unidecode(sorted_word[1]):
                win[1] = True
                word.used_words(sorted_word[1].lower())
            if unidecode(guess_word) == unidecode(sorted_word[2]):
                win[2] = True
                word.used_words(sorted_word[2].lower())
            if unidecode(guess_word) == unidecode(sorted_word[3]):
                win[3] = True
                word.used_words(sorted_word[3].lower())
            
            table.quadrant(tables, "QUARTETO!")
            print("\n")
            
            if win[0] == True and win[1] == True and win[2] == True and win[3] == True:
                print("{:^}".format(f"Você ganhou! as palavras eram {sorted_word[0]} , {sorted_word[1]} , {sorted_word[2]} e {sorted_word[3]}!"))
                break
            elif tentatives == 0:
                print("{:^}".format(f"Você perdeu! as palavras eram {sorted_word[0]} , {sorted_word[1]} , {sorted_word[2]} e {sorted_word[3]}!"))
                break
        input("\n> Aperte enter para voltar...")