def filter_data(data, keyword):
    return [line for line in data if keyword.lower() in line.lower()]  # Filter by keyword

def transform_data(data, transformation_func):
    return [transformation_func(line) for line in data]  # Apply the transformation function
