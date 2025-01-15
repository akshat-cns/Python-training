import requests

def fetch():
    url = "https://jsonplaceholder.typicode.com/posts"
    try:
        response = requests.get(url)  
        response.raise_for_status()  
        data = response.json()  
        
        print("Here are the first 3 posts:")
        for post in data[:3]:
            print(f"ID: {post['id']}, Title: {post['title']}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from the API: {e}")

if __name__ == "__main__":
    fetch()
