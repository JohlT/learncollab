def get_To_Do(local_read='ToDo.txt'):
    """Reads to-do list file and grabs the contents"""
    with open(f'../Files/{local_read}', 'r') as file_local:
        td_list = file_local.readlines() 
    return td_list


def store_To_Do(td_arg, local_write='ToDo.txt'):
    """writes adjusted list to the to-do text file."""
    with open(f'../Files/{local_write}', 'w') as file:
        file.writelines(td_arg)

