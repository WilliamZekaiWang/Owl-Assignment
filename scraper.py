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
        fav_urls = find_assignment_url(soup.find_all('a', class_="link-container", href=True))
        print("Logged in and Courses Found")

        # go through each url in courses and find assignments and add them to a dictionary
        course_dic = {}
        for course in fav_urls:
            soup = BeautifulSoup(s.post(fav_urls[course]).text, 'html.parser')
            if "Assignments" in soup.text:
                course_dic.update({course: {}})
                url = soup.find('a', title="Assignments - For posting, submitting, and grading assignments online",
                                href=True)['href']
                soup = BeautifulSoup(s.post(url).text, 'html.parser')
                extract_assignment(soup.find('table', class_="table table-hover table-striped table-bordered assignmentsList").find_all('td'), course_dic[course])

        if course_dic:
            return course_dic
        else:
            print("No Favourited Classes have assignments")
            exit()

def find_assignment_url(html):
    """
    given html parsed form bs4 find the links for each favourited course and return them in a list
    @return: course_links, a dictionary {course name : course url}
    """
    course_links = {}
    for course in html:
        course_links.update({course['title']: course['href']})
    course_links.pop("Home")  # first link should be home, which isn't a class
    return course_links

def extract_assignment(html, dic):
    """

    @return:
    """
    current_assignment = ""
    for row in html:
        if row.find("a") != None:
            row = row.find("a")
            current_assignment = row.text.replace('\n', "").replace('\t','').strip()
            dic.update({current_assignment: []})
        else:
            dic[current_assignment].append(row.text.replace('\n', "").replace('\t','').strip())
    return dic