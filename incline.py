"""
Web scraper script to extract information from a GitHub organization's members page.

This script sends an HTTP GET request to the GitHub organization's members page and
scrapes the profile picture, name, and username of each member.

Author: Your Name
"""

import requests
from bs4 import BeautifulSoup

# URL of the GitHub organization's members page
URL = 'https://github.com/orgs/inclineteam/people'

# Send an HTTP GET request to the URL with a timeout
response = requests.get(URL, timeout=10)

# Parse the HTML content of the page using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all elements with the class 'member-list-item' (organization members)
member_elements = soup.find_all(class_='member-list-item')

# Extract and print profile picture, name, and username
for member_element in member_elements:
    # Extract profile picture URL
    img_element = member_element.find('img', class_='avatar')
    profile_picture = img_element['src'] if img_element else 'No profile picture'
    
    # Extract name
    name_element = member_element.find(class_='user-full-name')
    name = name_element.get_text().strip() if name_element else 'No name'
    
    # Extract username
    username_element = member_element.find(class_='user-mention')
    username = username_element.get_text().strip() if username_element else 'No username'
    
    print(f"Name: {name}")
    print(f"Username: {username}")
    print(f"Profile Picture URL: {profile_picture}")
    print()
