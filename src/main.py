from apiGet import GetAPI
import sys

# base url for hacker news api
base_url = "https://hacker-news.firebaseio.com/v0/"

# whitelist of websites that can be used.
# include all websites of type blog / article
whitelist = []

def print_new_story(node, story_ids, keyword=None):
    title = node.get_story_data(node.get_story_dict())
    if keyword:
        if keyword.lower() in title.lower():
            print("Keyword is in title")
    print(f"TEST {title}")
    if story_ids:
        print(story_ids[0])
    print(node.get_story_dict())
    print("\n")
    print(node.get_story_content(node.get_story_dict()))
    print("\n")
    node.get_story_data(node.get_story_dict())


def main():
    node = GetAPI(base_url, whitelist)

    # Explain program usage if no args are given
    if len(sys.argv) == 1:
        print()
        print("        Welcome to your CLI news report.\n")
        print("        You can grab a hackernews article from their top, best,")
        print("        or new articles by using the corrosponding arguments")
        print("        when calling this program.\n")
        print("        In addition, you can enter any number of keywords after")
        print("        that as additional arguments to further refine your search.\n")


    # Choose between new, top, and best stories with no keyword
    if len(sys.argv) == 2:
        print(f"First argument: {sys.argv[1]}")
        if sys.argv[1] == "new":
            print_new_story(node, node.get_new_stories())
        if sys.argv[1] == "best":
            print_new_story(node, node.get_best_stories())
        if sys.argv[1] == "top":
            print_new_story(node, node.get_top_stories())
    print()

    # Choose between new, top, and best stories with keyword
    if len(sys.argv) == 3:
        print(f"First argument: {sys.argv[1]}")
        if sys.argv[1] == "new":
            print_new_story(node, node.get_new_stories(), sys.argv[2])
        if sys.argv[1] == "best":
            print_new_story(node, node.get_best_stories(), sys.argv[2])
        if sys.argv[1] == "top":
            print_new_story(node, node.get_top_stories(), sys.argv[2])
    print()


if __name__ == "__main__":
    main()
