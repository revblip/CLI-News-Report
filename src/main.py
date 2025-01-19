import requests
from bs4 import BeautifulSoup

base_url = "https://hacker-news.firebaseio.com/v0/"

# Return a list of story IDs from the 500 newest stories on hacker-news
def get_new_stories():
    url = f"{base_url}/newstories.json"
    response = requests.get(url)
    if response.status_code == 200:
        ids = response.json()
        return ids
    else:
        print("Failed to retrieve data")

# Get information about a story given its ID
# Returns a dictionary
def get_story():
    story_ids = get_new_stories()
    if story_ids:
        url = f"{base_url}/item/{story_ids[0]}.json"
        response = requests.get(url)
        if response.status_code == 200:
            info = response.json()
            return info
        else:
            print("Failed to retrieve data")


def main():
    new_story_ids = get_new_stories()
    if new_story_ids:
        print(new_story_ids[0])
    print(get_story())
    testurl = "https://www.economist.com/finance-and-economics/2025/01/16/the-traitors-a-reality-tv-show-offers-a-useful-economics-lesson"
    r = requests.get(testurl)
    # Simplify the html of a given web page to just the readable text
    clean_text = ' '.join(BeautifulSoup(r.content, "html.parser").stripped_strings)

    print(clean_text)

if __name__ == "__main__":
    main()
