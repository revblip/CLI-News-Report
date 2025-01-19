import requests

base_url = "https://hacker-news.firebaseio.com/v0/"

# Store a list of story IDs from the 500 newest stories on hacker-news
def get_new_stories():
    url = f"{base_url}/newstories.json"
    response = requests.get(url)
    if response.status_code == 200:
        ids = response.json()
        return ids
    else:
        print("Failed to retrieve data")

def main():
    new_story_ids = get_new_stories()
    if new_story_ids:
        print(new_story_ids[0])

if __name__ == "__main__":
    main()
