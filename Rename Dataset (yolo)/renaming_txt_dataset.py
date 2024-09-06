import os

# Define the source and destination folders
source_folder_path = 'folder/labels'
destination_folder_path = 'swap/folder/labels'

# Create the destination folder if it doesn't exist
os.makedirs(destination_folder_path, exist_ok=True)

# Define the mapping for replacements (only for the first number)
replacement_map = {
    '0': '1',
    '1': '4'
}

# Loop over all files in the source folder
for filename in os.listdir(source_folder_path):
    if filename.endswith('.txt'):  # Only process text files
        source_file_path = os.path.join(source_folder_path, filename)
        destination_file_path = os.path.join(destination_folder_path, filename)

        # Read the contents of the file
        with open(source_file_path, 'r') as file:
            lines = file.readlines()

        # Modify the first number of each line based on the replacement_map
        modified_lines = []
        for line in lines:
            parts = line.split(' ', 1)  # Split only on the first space
            if parts[0] in replacement_map:
                parts[0] = replacement_map[parts[0]]
            modified_line = ' '.join(parts)
            modified_lines.append(modified_line)

        # Write the modified lines to a new file in the destination folder
        with open(destination_file_path, 'w') as file:
            file.write("\n".join(modified_lines) + "\n")

print(f"Modification complete. Files saved in {destination_folder_path}.")
