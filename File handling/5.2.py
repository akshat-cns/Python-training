import os

def merge_files(file_paths, output_file, remove_duplicates=False):
    merged_lines = []
    encountered_files = []
    
    for file_path in file_paths:
        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()
                print(f"Successfully read file: {file_path}")
                merged_lines.extend(lines)
                encountered_files.append(file_path)
        except FileNotFoundError:
            print(f"Error: File not found - {file_path}")
    
    # Optionally remove duplicate lines
    if remove_duplicates:
        merged_lines = list(dict.fromkeys(merged_lines))  # Maintain order & remove duplicates
    
    try:
        with open(output_file, 'w') as output:
            output.writelines(merged_lines)
        print(f"Merged files into: {output_file}")
    except IOError as e:
        print(f"Error: Could not write to output file {output_file} - {e}")


if __name__ == "__main__":
    
    input_files = ["file1.txt", "file2.txt", "missing_file.txt", "file3.txt"] #Example hai
    output_file = "merged_output.txt"
    
    merge_files(file_paths=input_files, output_file=output_file, remove_duplicates=True)
