from apiGet import GetAPI

# base url for hacker news api
base_url = "https://hacker-news.firebaseio.com/v0/"

# whitelist of websites that can be used.
# include all websites of type blog / article
whitelist = []

def main():

    node = GetAPI(base_url, whitelist)

    new_story_ids = node.get_new_stories()
    if new_story_ids:
        print(new_story_ids[0])
    print(node.get_story_dict())
    print("\n")
    print(node.get_story_content(node.get_story_dict()))
    print("\n")
    node.get_story_data(node.get_story_dict())


if __name__ == "__main__":
    main()
