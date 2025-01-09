def display_data(data):
    if data:
        print("\nProcessed Data:")
        for line in data:
            print(line)
    else:
        print("No data to display.")  

def save_data(data, output_file):
    try:
        with open(output_file, 'w') as file:
            for line in data:
                file.write(line + '\n')  # Write each line to the file
        print(f"Data successfully saved to {output_file}.")
    except Exception as e:
        print(f"Error saving data: {e}") 