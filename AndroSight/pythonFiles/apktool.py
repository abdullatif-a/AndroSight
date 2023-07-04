import os
import subprocess


def run_apktool_command(folder_path):
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".apk"):
            try:
                apk_file_path = os.path.join(folder_path, file_name)
                output_folder = os.path.join(folder_path, "output")
                command = f"apktool d {apk_file_path} -o {output_folder}"
                subprocess.run(command, shell=True, check=True)
            except subprocess.CalledProcessError as e:
                print(f"Error executing command: {e}")


# path of the folder where apk files are stored
folder_path = 'PATH/TO/FOLDER'

# Run apktool command on APK file in the folder
run_apktool_command(folder_path)











