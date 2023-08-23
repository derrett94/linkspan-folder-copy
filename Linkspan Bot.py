import os
import shutil


# Define the options a user can select.
linkspan_options = ["Armadale", "Brodick", "Castlebay", "Colonsay", "Gourock",
                    "Kennacraig", "Lochboisdale", "Mallaig", "New Oban No 1",
                    "Oban No.2", "Port Ellen", "Tarbert Harris", "Tiree New",
                    "Wemyss Bay"]

# Show the user the list of options with a number for each.
print("Select the linkspan to be assessed:")
for index, linkspan in enumerate(linkspan_options, start=1):
    print(f"{index}. {linkspan}")


try:
    selection = int(input("Enter the number of the linkspan: ")) - 1
    if 0 <= selection < len(linkspan_options):
        selected_folder = linkspan_options[selection]
    else:
        print("Invalid selection.")
        exit(1)
except ValueError:
    print("Invalid input.")
    exit(1)

# Destination folder for the copied folder
destination_folder = input("Enter the destination folder path: ")

# Additional text to append
additional_text = "This text was added."

# Copy folder and contents
try:
    shutil.copytree(selected_folder, os.path.join(destination_folder, selected_folder))
    with open(os.path.join(destination_folder, selected_folder, "additional.txt"), "w") as f:
        f.write(additional_text)
    print("Folder copied successfully.")
except Exception as e:
    print(f"An error occurred: {e}")
