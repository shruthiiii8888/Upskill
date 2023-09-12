import os
import shutil

# Function to categorize and organize files
def organize_files(directory):
    file_types = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif'],
        'Documents': ['.pdf', '.docx', '.txt'],
        'Videos': ['.mp4', '.avi', '.mkv'],
        'Others': []
    }

    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            file_extension = os.path.splitext(filename)[1].lower()

            target_folder = None
            for folder, extensions in file_types.items():
                if file_extension in extensions:
                    target_folder = folder
                    break

            if target_folder is None:
                target_folder = 'Others'

            target_folder_path = os.path.join(directory, target_folder)
            if not os.path.exists(target_folder_path):
                os.makedirs(target_folder_path)

            source_path = os.path.join(directory, filename)
            destination_path = os.path.join(target_folder_path, filename)

            shutil.move(source_path, destination_path)
            print(f"Moved '{filename}' to '{target_folder}'")

# Specify the directory to organize
directory_to_organize = 'OneDrive/Documents/front'

# Call the function to organize files
organize_files(directory_to_organize)
