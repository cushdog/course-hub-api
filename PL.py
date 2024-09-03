import requests
from bs4 import BeautifulSoup

def make_prairielearn_request():
    url = "https://us.prairielearn.com/pl"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": "https://us.prairielearn.com/",
        "Referrer-Policy": "strict-origin-when-cross-origin",
        # add the cookie header
        "Cookie": "xsrf=2|a237b5e0|3cf767745aedc1ce76ea3269a11fdec3|1724780297; prairielearn_session=wM-6RRvAsfcBX9Sasoc10GBz5e9uVOHG.v1P1irxEh5qQHNc6vfK2X9977GER9TIaQxveOdXWRJU; pl2_session=wM-6RRvAsfcBX9Sasoc10GBz5e9uVOHG.v1P1irxEh5qQHNc6vfK2X9977GER9TIaQxveOdXWRJU; AWSALB=t/peB2B7Hbj+wPlacOfUP1AZHO8omY0z2OTtDkFe0peextUBe5RyCSANEq+rI9QGxrhs7bpeRy+sylCUHixjVoT7y/Cfg4ErJvTBwfbS6uDcc9DIfTpLK8wfgZfAex5NHnWhIMUyFlvevqT9ywW1B06CCUcXen3le0gCRqmQ12bSLSEa455CJ18u0SNj56fDIhcNMRmfTquDrxOb+mXSFBl0VhJ/8R27Nvj86HZIUJ/kVRw4EH1c/Z96A8IXrL8=; AWSALBCORS=t/peB2B7Hbj+wPlacOfUP1AZHO8omY0z2OTtDkFe0peextUBe5RyCSANEq+rI9QGxrhs7bpeRy+sylCUHixjVoT7y/Cfg4ErJvTBwfbS6uDcc9DIfTpLK8wfgZfAex5NHnWhIMUyFlvevqT9ywW1B06CCUcXen3le0gCRqmQ12bSLSEa455CJ18u0SNj56fDIhcNMRmfTquDrxOb+mXSFBl0VhJ/8R27Nvj86HZIUJ/kVRw4EH1c/Z96A8IXrL8="
    }
    
    try:
        response = requests.get(url, headers=headers)
        
        print(f"Request URL: {url}")
        print(f"Request Method: GET")
        print(f"Status Code: {response.status_code} {response.reason}")

        return response.content
        
    except requests.RequestException as e:
        print(f"An error occurred: {e}")

def retrieve_courses():

    response = make_prairielearn_request()

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response, 'html.parser')

    # Find all <a> tags with href attributes that contain "/pl/course_instance/"
    course_instance_links = soup.find_all('a', href=True)

    # Extract the instance numbers from the href attributes
    instance_numbers = []
    for link in course_instance_links:
        href = link['href']
        if "/pl/course_instance/" in href:
            instance_number = href.split('/')[-1]
            if (instance_number.isdigit()):
                instance_numbers.append(instance_number)

    # Return the list of instance numbers
    return instance_numbers

def retrieve_all():
    courses = retrieve_courses()
    assignments = []
    for course in courses:
        print(retrieve_assignments(course))
        assignments.append(retrieve_assignments(course))
    return assignments

def retrieve_assignments(instance_id):

    courses = retrieve_courses()

    assignments = []

    # Define the URL
    url = f"https://us.prairielearn.com/pl/course_instance/{instance_id}/assessments"

    # Define headers
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "en-US,en;q=0.9",
        "cookie": "_xsrf=2|a237b5e0|3cf767745aedc1ce76ea3269a11fdec3|1724780297; prairielearn_session=wM-6RRvAsfcBX9Sasoc10GBz5e9uVOHG.v1P1irxEh5qQHNc6vfK2X9977GER9TIaQxveOdXWRJU; pl2_session=wM-6RRvAsfcBX9Sasoc10GBz5e9uVOHG.v1P1irxEh5qQHNc6vfK2X9977GER9TIaQxveOdXWRJU; AWSALB=m7bHiTajGhwQ6926L3wf2KI3DRhfC0vEWEFsRm4GThuLAyxIwRjkbzVTBrRPoTteVyoOvxFwZGd4WOdguXnNa2yrcDuRdHjAwGD7/qec0sYhn0yEInUcMC/Iv8ev/qjOxWSNRSWq7U73Y07d9pEXa6wrnFr40pLUtipy6ca+vNzlfgepGj32XtoS63qxT1wo+MJILBdvliMnB5UVXkQXnVdnnCxeKkPKlD2zPnmXJAVsEktH3Dnj1cqrS2j1w00=; AWSALBCORS=m7bHiTajGhwQ6926L3wf2KI3DRhfC0vEWEFsRm4GThuLAyxIwRjkbzVTBrRPoTteVyoOvxFwZGd4WOdguXnNa2yrcDuRdHjAwGD7/qec0sYhn0yEInUcMC/Iv8ev/qjOxWSNRSWq7U73Y07d9pEXa6wrnFr40pLUtipy6ca+vNzlfgepGj32XtoS63qxT1wo+MJILBdvliMnB5UVXkQXnVdnnCxeKkPKlD2zPnmXJAVsEktH3Dnj1cqrS2j1w00=",
        "dnt": "1",
        "priority": "u=0, i",
        "referer": "https://us.prairielearn.com/",
        "sec-ch-ua": '"Not;A=Brand";v="24", "Chromium";v="128"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"macOS"',
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
    }

    # Send the GET request
    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:

        # Parse the HTML content with BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all table row tags
        table_rows = soup.find_all('tr')

        # Loop through each row and extract relevant information
        for row in table_rows:
            try:
                # Extract the first cell's content (e.g., badge text "S1")
                badge = row.find('span', class_='badge').get_text(strip=True)
            except AttributeError:
                badge = "N/A"

            try:
                # Extract the link text, stripping extra spaces
                link_text = row.find('a').get_text(strip=True)
            except AttributeError:
                link_text = "N/A"

            try:
                # Extract the "None" or other text in the third column
                status_text = row.find_all('td')[2].get_text(strip=True)
            except (AttributeError, IndexError):
                status_text = "N/A"

            try:
                # Extract the progress percentage text (e.g., "0%")
                progress_text = row.find('div', class_='progress-bar').get_text(strip=True)
            except AttributeError:
                progress_text = "N/A"

            # Print or store the extracted information
            print(f"Badge: {badge}")
            print(f"Link Text: {link_text}")
            print(f"Status: {status_text}")
            print(f"Progress: {progress_text}")
            print("-------------")

            # Store the information in a dictionary
            assignment = {
                "badge": badge,
                "link_text": link_text,
                "status": status_text,
                "progress": progress_text
            }

            # Add the assignment to the assignments list
            assignments.append(assignment)
        return assignments
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")

print(retrieve_all())

