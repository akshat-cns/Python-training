import csv

def read_sales_data(filename):
    sales_data = []
    try:
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                sales_data.append({
                    "product": row["Product"],
                    "quantity": int(row["Quantity"]),
                    "price": float(row["Price"])
                })
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except KeyError as e:
        print(f"Error: Missing column in the file: {e}")
        return None
    except ValueError:
        print("Error: Invalid data format in the file.")
        return None
    return sales_data


def generate_report(sales_data):
    total_sales = 0
    product_sales = {}

    for item in sales_data:
        product = item["product"]
        revenue = item["quantity"] * item["price"]
        total_sales += revenue

        if product in product_sales:
            product_sales[product] += revenue
        else:
            product_sales[product] = revenue
    if sales_data:
        average_sales = total_sales / len(sales_data) 
    else:
        0
    
    if product_sales:
        top_selling_product = max(product_sales, key=product_sales.get)
    else:
        None

    return {
        "total_sales": total_sales,
        "average_sales": average_sales,
        "top_selling_product": top_selling_product,
        "top_selling_revenue": product_sales.get(top_selling_product, 0) if top_selling_product else 0
    }


def main():
    filename = input("Enter the CSV file name: ")
    sales_data = read_sales_data(filename)
    report = generate_report(sales_data)
    
    print(f"Total Sales: ${report['total_sales']:.2f}")
    print(f"Average Sales: ${report['average_sales']:.2f}")
    print(f"Top-Selling Product: {report['top_selling_product']} (${report['top_selling_revenue']:.2f})")


if __name__ == "__main__":
    main()