import view
import text
import model
import datetime
import json

textNote = text.TextNote
view.print_message(textNote.welcome)

def start_app():        
    pb = model.Notes()  
    while True:
        choice = view.main_menu(textNote.main_menu)
        match choice:
            case 1:
                name = input(textNote.notes_name)
                today = str(datetime.datetime.today())
                date = today[:-7]
                pb.read_notes()
                if len(pb.notes) == 0: 
                    content = input(textNote.notes_content) 
                    pb.notes_input(name, content, date)
                    pb.write_notes()
                else: 
                    if pb.reserved_name(name): 
                        view.print_message(textNote.reserved_name)
                        name = input("Введите другое название: ")
                    content = input(textNote.notes_content)
                    pb.notes_input(name, content, date)  
                    pb.safe_notes(name)
            case 2:
                while True:
                    pb.read_notes()
                    if len(pb.notes) == 0: 
                        view.print_message(textNote.empty_notes)
                        break
                    else:    
                        choice1 = view.main_menu(textNote.sub_menu)
                    
                        if choice1 == 1:
                            view.print_notes(pb.notes)
                            break
                        if choice1 == 2:
                            dict_roker = pb.roker()
                            sort_list = sorted(dict_roker)
                            view.print_sorted(dict_roker, sort_list)
                            break
                        else:
                            view.print_message(textNote.error_num)
                        
            case 3:
                pb.read_notes()
                len_dict = len(pb.notes)
                if len(pb.notes) == 0: 
                    view.print_message(textNote.empty_notes)
                    
                else:
                    choice_edit = view.main_menu(textNote.edit_menu)
                    if choice_edit == 1:
                        id = view.main_menu(pb.name_list())      
                        view.print_notes_for_edit(pb.notes, id)
                        del_dict = pb.delete_notes(id)
                        pb.notes_for_edit(id)
                        if len(pb.notes) > len_dict:
                            del pb.notes[del_dict]
                            pb.write_notes()
                    elif choice_edit == 2:
                        id = view.main_menu(pb.name_list())      
                        view.print_notes_for_edit(pb.notes, id)
                        del_dict = pb.delete_notes(id)
                        choice_del = input(textNote.del_num)
                        if choice_del == '1':
                            print(del_dict, pb.notes[del_dict], ' Удалено')
                            del pb.notes[del_dict]
                            pb.write_notes()
                                        
            case 4:
                view.print_message(textNote.good_bay)
                break
            