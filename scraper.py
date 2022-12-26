import requests as rq
from bs4 import BeautifulSoup

def login():
    """
    prompts user with login information for owl and retrieves the assignments for each class that is favourited
    @return: list, each course with
    """
    # opens the western login for owl and prompts login
    details = {"eid": input("User: "),
               "pw": input("Pass: ")
               }
    with rq.session() as s:
        data = s.post("https://owl.uwo.ca/portal/xlogin", data=details)

        # use bs4 to find links to all favourited sites
        soup = BeautifulSoup(data.text, 'html.parser')
        div_classes = soup.find_all('a', class_="link-container", href=True)
        for course in div_classes:
            fav_urls.append(course['href'])
        fav_urls.pop(0)  # first link should be home, which isn't a class

        # go through each url in courses and find assignments and add them to a dictionary
        course_dic = {}
        for course in fav_urls:
            find_assignments(course, soup, course_dic)

def find_assignments(url, soup, results):
    """
    takes an url for an owl page and finds all the assignments and adds them to results
    @param url: url for owl course
    @param soup: bs4 object
    @param results: dictionary to collect assignments
    """


