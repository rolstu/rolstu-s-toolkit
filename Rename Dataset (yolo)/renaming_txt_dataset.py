import os

# Listen carefully, there are the path that you'll be defining
source_folder_path = 'folder/labels'
destination_folder_path = 'swap/folder/labels'

# I know you are laszy to create a folder on your own so here you go, a FUNCTION TO DO IT
os.makedirs(destination_folder_path, exist_ok=True)

# Define the mapping for replacements (only for the first number, i repeat again 'ONLY FIRST NUMBERS')
replacement_map = {
    '0': '1',
    '1': '4'
}

# Loop it babee
for filename in os.listdir(source_folder_path):
    if filename.endswith('.txt'):  # Only process text files, don't be oversmart and add other types of docs. Yolo loves .txt files remember that
        source_file_path = os.path.join(source_folder_path, filename)
        destination_file_path = os.path.join(destination_folder_path, filename)

        # Reading happens here
        with open(source_file_path, 'r') as file:
            lines = file.readlines()

        # Modify the first number of each line based on the replacement_map
        modified_lines = []
        for line in lines:
            parts = line.split(' ', 1)  # Split only on the first space, it's a smarter way
            if parts[0] in replacement_map:
                parts[0] = replacement_map[parts[0]]
            modified_line = ' '.join(parts)
            modified_lines.append(modified_line)

        # If you did the Read function then definetly you should write as well. Those are good manners (also it does the work for you lol)
        with open(destination_file_path, 'w') as file:
            file.write("\n".join(modified_lines) + "\n")

print(f"Modification complete. Files saved in {destination_folder_path}.")
