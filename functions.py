import os
import json

class Functions:
    @staticmethod
    def find_vue_files(directory):
        """
        Finds Vue files in a directory and its subdirectories.

        Args:
            directory: Path of the directory to be searched.

        Returns:
            List of paths of the found Vue files.
        """
        vue_files = []
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith('.vue'):
                    file_path = os.path.join(root, file)
                    vue_files.append(file_path)
        return vue_files


    @staticmethod
    def save_files_to_json(vue_files, json_file_name):
        """
        Saves the paths of Vue files to a JSON file.

        Args:
            vue_files: List of paths of the Vue files.
            json_file_name: Name of the JSON file to be created.
        """
        data = {'VUE_FILES': vue_files}
        json_data = json.dumps(data, indent=4)
        with open(json_file_name, 'w', encoding='utf-8') as json_file:
            json_file.write(json_data)


    @staticmethod
    def extract_strings_for_translation(vue_files_paths):
        """
        Extracts strings for translation from Vue files.

        Args:
            vue_files_paths: List of paths of the Vue files.

        Returns:
            - List of strings for translation found in the Vue files.
            - List of files that do not contain the '$t(' pattern.
        """
        strings_for_translation = []
        files_without_pattern = []

        for file_path in vue_files_paths:
            with open(file_path, 'r', encoding='utf-8') as vue_file:
                lines = vue_file.readlines()
                found_pattern = False
                for line in lines:
                    start_index = line.find('$t(')
                    if start_index != -1:
                        found_pattern = True
                        end_index = line.find(')', start_index)
                        if end_index != -1:
                            string = line[start_index + 4:end_index]
                            strings_for_translation.append(string)
                if not found_pattern:
                    files_without_pattern.append(file_path)
        return strings_for_translation, files_without_pattern


    @staticmethod
    def save_strings_to_json(strings, json_file_name):
        """
        Saves the strings for translation to a JSON file.

        Args:
            strings: List of strings for translation.
            json_file_name: Name of the JSON file to be created.
        """
        data = {'TRANSLATED_STRINGS': strings}
        json_data = json.dumps(data, indent=4, ensure_ascii=False)
        with open(json_file_name, 'w', encoding='utf-8') as json_file:
            json_file.write(json_data)


    @staticmethod
    def save_files_without_pattern(files_without_pattern, json_file_name):
        """
        Saves the files that do not contain the '$t(' pattern to a JSON file.

        Args:
            files_without_pattern: List of paths of the files that do not contain the pattern.
            json_file_name: Name of the JSON file to be created.
        """
        data = {'NON_T_FILES': files_without_pattern}
        json_data = json.dumps(data, indent=4, ensure_ascii=False)
        with open(json_file_name, 'w', encoding='utf-8') as json_file:
            json_file.write(json_data)