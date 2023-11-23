import random
from unidecode import unidecode
import menu
import table

def get_guess_word(tryes):
    while True:
        try:
            guess_word = verify_word(input("> Digite uma palavra:").upper().strip())
            
            if guess_word == False:
                raise ValueError
            elif guess_word in tryes:
                raise AssertionError
            else:
                tryes.append(guess_word)
            
            return guess_word 
    
        except ValueError:
            print(table.print_color("tr","[ERROR]")+" Palavra invalida!")
            print(menu.horizontal_line*61)
        except AssertionError:
            print(table.print_color("tr","[ERROR]")+" Palavra já utilizada!!")
            print(menu.horizontal_line*61)
        except BaseException as error:
            print(table.print_color("tr","[ERROR]")+"Aconteceu um erro:", error)
            print(menu.horizontal_line*61)
        
           
                
def random_word(num):
    file_words = open("all_words.txt", "r", encoding="utf8")
    file_used_words = open("used_words.txt", "r", encoding="utf8")
    
    words_lines = file_words.readlines()
    used_lines = file_used_words.readlines()
    words = []
    
    for i in range(num):
        sorted_word = words_lines[random.randint(0,len(words_lines)-1)]
        while sorted_word in used_lines and sorted_word in words and len(sorted_word) == 5:
            sorted_word = words_lines[random.randint(0,len(words_lines)-1)]
        words.append(sorted_word.upper().replace("\n",""))
    
    file_words.close()
    file_used_words.close()
    
    return words

def verify_word(guess_word):
    file_words = open("dict5.txt", "r", encoding="utf8")
    words_lines = file_words.readlines()
    file_words.close()
    
    for i in range(len(words_lines)):
        word = words_lines[i].replace("\n","").upper()
        if unidecode(guess_word) == unidecode(word):
            return word
        
    
    return False

def used_words(word):
    file_used_words = open("used_words.txt", "a+", encoding="utf8")
    file_used_words.write(word+"\n")
        
    file_used_words.close()

def reset_words():
    file_used_words = open("used_words.txt", "w", encoding="utf8")
    file_used_words.write("")
    
    file_used_words.close()
    
def add_word():
    numbers = ["0","1","2","3","4","5","6","7","8","9"]
    word = input("> Digite a palavra:").strip().lower()
    
    file_words = open("all_words.txt", "r", encoding="utf8")
    file_words2 = open("dict5.txt", "r", encoding="utf8")
    words_lines = file_words.read()
    words_lines2 = file_words2.read()
    file_words.close()
    file_words2.close()
    
    for letter in word:
        if letter in numbers:
            return 0
        
    if len(word) != 5:
        return 0
    
    elif unidecode(word) in unidecode(words_lines).replace("\n","").lower():
        return 2
    
    else:
        file_words = open("all_words.txt", "a+", encoding="utf8")
        file_words.write(word+"\n")
        file_words.close()
        if unidecode(word) not in unidecode(words_lines2).replace("\n","").lower():
            file_words2 = open("dict5.txt", "a+", encoding="utf8")
            file_words2.write(word+"\n")
            file_words2.close()
        return 1
    
def remove_word():
    
    word = input("> Digite a palavra:").strip().lower()
    aux = False
    file_words = open("all_words.txt", "r", encoding="utf8")
    file_words2 = open("dict5.txt", "r", encoding="utf8")
    words_lines = file_words.readlines()
    words_lines2 = file_words2.readlines()
    file_words.close()
    file_words2.close()
    
    for i in range(len(words_lines)):
        if unidecode(word) == unidecode(words_lines[i].replace("\n","").lower()):
            words_lines.pop(i)
            aux = True
            
            file_words = open("all_words.txt", "w", encoding="utf8")      
            for i in range(len(words_lines)):
                file_words.write(words_lines[i])
            
            file_words.close()
            break
                
    for i in range(len(words_lines2)):
        if unidecode(word) == unidecode(words_lines2[i].replace("\n","").lower()):
            words_lines2.pop(i)
            aux = True
            
            file_words2 = open("dict5.txt", "w", encoding="utf8")      
            for i in range(len(words_lines2)):
                file_words2.write(words_lines2[i])
                
            file_words2.close()
            break
            
    
    return aux

def used_letters(letters, word):
    
    for i in range(len(letters)):
        for j in range(len(word)):
            if letters[i] == unidecode(word[j]):
                letters[i] = table.print_color("tr", letters[i])
    
    return letters
    
def print_letters(letters):
    
    for i in range(len(letters)):
        print(letters[i], end = " ")
    print()
    print(menu.horizontal_line*61)
    
    
        
    
        
    