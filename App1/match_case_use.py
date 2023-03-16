while True:
    action = input("Type Add, Show, Edit, Complete, or Exit: ")
    action = action.strip()     # strips extra white space

    match action:
        case 'add'|'Add':
            new_task = input("Enter new task: ") + '\n'

            with open('../Files/ToDo.txt', 'r') as file:
                To_Do = file.readlines()

            To_Do.append(new_task)
            
            with open('../Files/ToDo.txt', 'w') as file:
                file.writelines(To_Do)

        case 'show'|'Show':

            with open('../Files/ToDo.txt', 'r') as file:
                To_Do = file.readlines()

            # shw_td = [item.strip('\n') for item in To_Do]
            
            for index, item in enumerate(To_Do):
                item = item.strip('\n')
                item = item.title()
                print(f"{index+1}-{item}")
        
        case 'edit'|'Edit':

            with open('../Files/ToDo.txt', 'r') as file:
                To_Do = file.readlines()

            number = input("Number of list item to edit: ")
            num = int(number) -1
            replace = input("Enter update to list item: ")
            To_Do[num] = replace + '\n'

            with open('../Files/ToDo.txt', 'w') as file:
                file.writelines(To_Do)

        case 'complete'|'Complete':

            with open('../Files/ToDo.txt', 'r') as file:
                To_Do = file.readlines()

            item = input("Enter number of completed item: ")
            completed = To_Do[int(item)-1]
            completed = completed.strip('\n')
            To_Do.pop(int(item)-1)
            print(f"Task: {completed}, was removed from the list.")

            with open('../Files/ToDo.txt', 'w') as file:
                file.writelines(To_Do)

        case 'exit':
            break


print("Go Be Productive!")