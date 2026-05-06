import os
import shutil

def automate_files():
    
    input_file = "data.txt"
    output_file = "processed_data.txt"
    renamed_file = "final_report.txt"
    target_folder = "archive_folder"
    temp_file = "temp_to_delete.txt"

    try:
       
        print("Starting file operations...")
        
       
        if not os.path.exists(input_file):
            
            with open(input_file, "w") as f:
                f.write("User ID, Name, Status\n101, Shaik Sadik, Active")

        
        with open(input_file, "r") as f:
            content = f.read()
            print(f"Read successful. Content: {content}")

       
        with open(output_file, "w") as f:
            f.write(f"PROCESSED DATA:\n{content.upper()}")
            print(f"Write successful. Created '{output_file}'.")

        
        if os.path.exists(renamed_file):
            os.remove(renamed_file)
        
        os.rename(output_file, renamed_file)
        print(f"Rename successful: '{output_file}' -> '{renamed_file}'.")

       
        if not os.path.exists(target_folder):
            os.makedirs(target_folder)
            print(f"Created folder: '{target_folder}'.")

        
        shutil.move(renamed_file, os.path.join(target_folder, renamed_file))
        print(f"Move successful: '{renamed_file}' moved to '{target_folder}'.")

        
        with open(temp_file, "w") as f:
            f.write("This file will be deleted.")
        
        if os.path.exists(temp_file):
            os.remove(temp_file)
            print(f"Delete successful: '{temp_file}' has been removed.")

        print("\nAll automation tasks completed successfully!")

    except FileNotFoundError:
        print("Error: The specified file was not found.")
    except PermissionError:
        print("Error: You do not have permission to modify these files.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    automate_files()