import pandas as pd
import os
import shutil

class DataChecker:
    def __init__(self, excel_file, txt_folder, output_folder):
        self.df = pd.read_excel(excel_file)
        self.txt_folder = txt_folder
        self.output_folder = output_folder

    def check_data(self):
        for index, row in self.df.iterrows():
            name = row['Name']
            address = row['Address']
            other_data = row['other_data']

            matching_files = [file for file in os.listdir(self.txt_folder) if name in file]

            if not matching_files:
                print(f"No matching TXT file found for {name}")
                continue

            for file_name in matching_files:
                file_path = os.path.join(self.txt_folder, file_name)

                with open(file_path, 'r', encoding='utf-8') as txt_file:
                    txt_content = txt_file.read()
                    if address in txt_content and other_data in txt_content:
                        print(f"Data for {name} found in {file_name}")
                    else:
                        print(f"Data for {name} not found in {file_name}")
                        self.move_to_not_found(file_path)

    def move_to_not_found(self, file_path):
        not_found_folder = os.path.join(self.output_folder, "not_found_folder_name")
        os.makedirs(not_found_folder, exist_ok=True)

        shutil.move(file_path, os.path.join(not_found_folder, os.path.basename(file_path)))
