import text
import model

def main_menu(t): 
    textNote = text.TextNote
    
    for n, item in enumerate(t):
        if n == 0:
            print(item)
        else:
            print(f'\t {n}. {item}')
    while True:
        choice = input(textNote.main_menu_choice)
        if choice.isdigit() and 0 < int(choice) < len(t):
            return int(choice)
        print(f'Введите число от 1 до {len(t) - 1}')  
        
def print_message(message: str):
    print('\n' + '=' * len(message))
    print(message)
    print('=' * len(message) + '\n')  
    
def print_notes(data):  
    for item in data:
        print(item, sep='\n')
        n = {}
        for i in data[item]:
            n = data[item]
            print(i, n[i])
        print('-------------------------------------------------------') 
            
def print_sorted(dict1,list1):
    for i in list1:
        print(i, sep='\n')
        n = {}
        for item in dict1[i]:
            n = dict1[i]
            print(item, n[item], sep='    ')
        print('-------------------------------------------------------')    

def print_notes_id(data):
    id = 1
    for item in data:
        print(id, item, sep='. ')
        id += 1
 
def print_notes_for_edit(data, id):
    num = 1 
    for item in data:
        if num == id:
            print(item, sep='\n')
            n = {}
            for i in data[item]:
                n = data[item]
                print(i, n[i], sep='    ')
        num += 1     
                  
                
                    
                
                