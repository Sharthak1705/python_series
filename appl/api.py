import requests


def fetch():
    url = "https://api.freeapi.app/api/v1/public/cats/cat/random"
    response = requests.get(url)
    data = response.json()
    
    if data["success"] and "data" in data:
        user_data = data["data"]
        content = user_data["description"]
        return content
    else:
        raise Exception("Failed to fetch user data ")
def main():
    try:
       content =  fetch()
       print(f"Content: {content} ")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()