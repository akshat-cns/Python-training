def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = file.readlines()  
        return [line.strip() for line in data]  # Remove extra spaces 
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return []  
    except Exception as e:
        print(f"Error reading file: {e}")
        return []  