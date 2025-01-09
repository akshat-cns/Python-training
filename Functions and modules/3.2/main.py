import fetch
import process
import report

def main():
    # Step 1: Fetch the data from a file
    file_path = 'input_data.txt'  
    data = fetch.read_file(file_path)  
    
    if not data: # Step 2: Process the data
    keyword = 'important' 
    filtered_data = process.filter_data(data, keyword)  
    
    transformed_data = process.transform_data(filtered_data, lambda x: x.upper())

    # Step 3: Report the results
    report.display_data(transformed_data)  

if __name__ == "__main__":
    main()  