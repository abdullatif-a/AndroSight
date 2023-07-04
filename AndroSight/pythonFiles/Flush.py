import os


def delete_files_in_folder(folder_path):
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):
            os.remove(file_path)


# path of the folder where apk files are stored
folder_path = 'PATH/TO/FOLDER'

# Call the function to delete files in the folder
delete_files_in_folder(folder_path)
