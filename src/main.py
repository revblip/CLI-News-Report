import requests
from bs4 import BeautifulSoup

base_url = "https://hacker-news.firebaseio.com/v0/"

"""
Return a list of story IDs from the 500 newest stories on hacker-news
"""
def get_new_stories():
    url = f"{base_url}/newstories.json"
    response = requests.get(url)
    if response.status_code == 200:
        ids = response.json()
        return ids
    else:
        print("Failed to retrieve data")

"""
Get information about a story given its ID
Returns a dictionary
"""
def get_story_dict():
    story_ids = get_new_stories()
    if story_ids:
        url = f"{base_url}/item/{story_ids[0]}.json"
        response = requests.get(url)
        if response.status_code == 200:
            info = response.json()
            return info
        else:
            print("Failed to retrieve data")

"""
Get the html from the url given and convert it into clean text
Returns a string
"""
def get_story_content(info):
    if "url" not in info:
        return "No URL present"
    contentURL = info["url"]
    request = requests.get(contentURL)
    clean_text = ' '.join(BeautifulSoup(request.content, "html.parser").stripped_strings)
    return clean_text


def get_story_data(info):
    title = info["title"]
    author = info["by"]
    date = info["time"]

    print(f"Title = {title}")
    print(f"Author = {author}")
    print(f"Date = {date} (unix time)")


def main():
    new_story_ids = get_new_stories()
    if new_story_ids:
        print(new_story_ids[0])
    print(get_story_dict())
    print("\n")
    print(get_story_content(get_story_dict()))
    print("\n")
    get_story_data(get_story_dict())


if __name__ == "__main__":
    main()
