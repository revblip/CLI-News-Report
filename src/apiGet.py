import requests
from bs4 import BeautifulSoup

class GetAPI:
    def __init__(self, base_url, whitelist):
        self.base_url = base_url
        self.whitelist = whitelist
        self.new_stories_url = "newstories.json"
        self.top_stories_url = ""


    """
    Return a list of story IDs from the 500 newest stories on hacker-news
    """
    def get_new_stories(self):
        url = f"{self.base_url}/{self.new_stories_url}"
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
    def get_story_dict(self):
        story_ids = self.get_new_stories()
        if story_ids:
            url = f"{self.base_url}/item/{story_ids[0]}.json"
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
    def get_story_content(self, info):
        if "url" not in info:
            return "No URL present"
        contentURL = info["url"]
        request = requests.get(contentURL)
        clean_text = ' '.join(BeautifulSoup(request.content, "html.parser").stripped_strings)
        return clean_text


    def get_story_data(self, info):
        title = info["title"]
        author = info["by"]
        date = info["time"]

        print(f"Title = {title}")
        print(f"Author = {author}")
        print(f"Date = {date} (unix time)")
