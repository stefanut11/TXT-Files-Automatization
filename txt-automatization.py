import os
import shutil

folder_path = '/path/to/folder'
extension = '.txt'
prefix = 'image_'

files = os.listdir(folder_path)

for file in files:
    if file.endswith(extension):
        shutil.move(os.path.join(folder_path, file), target_folder)

        
print("The .txt files was moved with success.")
