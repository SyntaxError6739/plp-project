def modify_content(content):
    # Function to modify the content (you can customize this logic)
    return content.upper()

def main():
    try:
        # Ask user for the input file name
        input_file = input("Enter the name of the file to read from: ")
        with open(input_file, 'r') as file:
            content = file.read()
        
        # Modify the content
        modified_content = modify_content(content)

        # Ask user for the output file name
        output_file = input("Enter the name of the new file to write to: ")
        with open(output_file, 'w') as file:
            file.write(modified_content)
        
        print("Content has been successfully modified and written to the new file.")

    except FileNotFoundError:
        print("Error: The file does not exist. Please check the file name and try again.")
    except IOError:
        print("Error: Unable to read/write the file. Please ensure you have the necessary permissions.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
