import os
import csv

webshell_extensions = ['.php', '.asp', '.jsp'] 
webshell_keywords = ['system', 'shell_exec', 'eval']

def detect_webshell(root_dir):
    with open('webshell_detection_results.csv', mode='w', newline='') as csv_file:
        fieldnames = ['File Path', 'Keywords Found']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for root, dirs, files in os.walk(root_dir):
            for file in files:
                file_path = os.path.join(root, file)
                file_extension = os.path.splitext(file_path)[1]
                if file_extension in webshell_extensions:
                    try:
                        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                            file_contents = f.read()
                            keywords_found = []
                            for keyword in webshell_keywords:
                                if keyword in file_contents:
                                    keywords_found.append(keyword)
                            if keywords_found:
                                writer.writerow({'File Path': file_path, 'Keywords Found': ', '.join(keywords_found)})
                    except Exception as e:
                        print(f"Error reading file {file_path}: {e}")

detect_webshell('/var/www/')  # specify the root directory of the web server
