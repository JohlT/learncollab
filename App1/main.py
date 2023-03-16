import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)
while True:
    action = input("Type Add, Show, Edit, Complete, or Exit: ")
    action = action.strip()     # strips extra white space
    
    if action.startswith('add'):
    
        new = action[4:]
        
        To_Do = functions.get_To_Do()
        
        To_Do.append(new + '\n')
            
        functions.store_To_Do(To_Do)
        

    elif action.startswith('show'):
    
        To_Do = functions.get_To_Do()

        # shw_td = [item.strip('\n') for item in To_Do]
            
        for index, item in enumerate(To_Do):
            item = item.strip('\n')
            item = item.title()
            print(f"{index+1}-{item}")

    elif action.startswith('edit'):

        try:    
            number = action[5:]

            To_Do = functions.get_To_Do()
           
            num = int(number) - 1 
            replace = input("Enter update to list item: ")
            To_Do[num] = replace + '\n'

            functions.store_To_Do(To_Do)
            

        except ValueError:
            print('Your command is not valid')
            continue


    elif action.startswith('complete'):
        try:
            item = action[9:]

            To_Do = functions.get_To_Do()            

            completed = To_Do[int(item)-1]
            completed = completed.strip('\n')
            completed = completed.capitalize()
            To_Do.pop(int(item)-1)
            print(f"{completed} was removed from the list.")

            functions.store_To_Do(To_Do)
            

        except IndexError:
            print("There is no item with that number")
            continue

    elif action.startswith('exit'):
        break

    else:
        print('Action Invalid. Please try again')



print("Go Be Productive!")
