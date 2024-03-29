import json 
import text 
import datetime 
     
class Notes:
    textNote = text.TextNote
    def __init__(self, path: str = 'notes.json'):
        self.notes = {}
        self.path = path
        
    def notes_input(self, key, value, value_date):
        self.notes = {key:{value: value_date}}  
        
    def safe_notes(self, key):
        with open(self.path, "r", encoding='utf-8') as read_file:
            data = json.load(read_file)  
            data[key] = self.notes[key]
        with open(self.path, "w", encoding='utf8') as write_file:
            json.dump(data, write_file, ensure_ascii=False, indent=2)
            
    def read_notes(self):
        with open(self.path, "r", encoding='utf-8') as read_file:
            self.notes = json.load(read_file)  
            
    def write_notes(self):
        with open(self.path, "w", encoding='utf8') as write_file:
            json.dump(self.notes, write_file, ensure_ascii=False, indent=2)        
            
    def reserved_name(self,name):
        for item in self.notes:
            if item == name:
                return True
            False   
            
    def parse_int_date(self, value_date):
        date = value_date.split()
        list = date[0].split('-') + date[1].split(':')
        res = ''
        for item in list:
            res += item 
        return int(res) 
    
    def get_value_date(self, item):
            n = {}
            n = self.notes[item]
            for i in self.notes[item]:
                n = self.notes[item]
                return n[i]
                        
    def roker(self):
        res = {} 
        for item in self.notes:
            val_res = {}
            n = {}
            
            for i in self.notes[item]:
                n = self.notes[item]
                key = item
                value = i
                val_res[key] = value
                res[n[i]] = val_res       
        return res 
    
    def notes_for_edit(self, id):
        num = 1 
        for item in self.notes:
            if num == id:
                new_name = input('Введите новое название заметки или ENTER если оставить без изменений: ')
                if new_name == '':
                    new_content = input('Введите новый текст заметки или ENTER если оставить без изменений: ')
                    if new_content == '':
                        return self.notes
                    today = str(datetime.datetime.today())
                    date = today[:-7]
                    self.notes[item] = {new_content: date}
                    return self.notes
                else:
                    new_content = input('Введите новый текст заметки или ENTER если оставить без изменений: ')
                    if new_content == '':
                        for i in self.notes[item]:
                            new_content = i
                        key = new_name
                        today = str(datetime.datetime.today())
                        date = today[:-7]
                        self.notes[key] = {new_content: date}
                        return self.notes
                    key = new_name
                    today = str(datetime.datetime.today())
                    date = today[:-7]
                    self.notes[key] = {new_content: date}
                    return self.notes  
            num += 1 
        return self.notes        
    
    def delete_notes(self, id):
        num = 1 
        for item in self.notes:
            if num == id:
                key = item
            num += 1    
        return key       
    
    def name_list(self):
        list_name = []
        list_name.append('* * * * * СПИСОК ЗАМЕТОК * * * * * *')
        for item in self.notes:
            list_name.append(item)
        return list_name    
                        
             
    
    
                   
                  
                    
                    
        
            
        
            
                   
                       
        