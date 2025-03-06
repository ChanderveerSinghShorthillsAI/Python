from bs4 import BeautifulSoup
import requests

# Load the local HTML file
with open("Sample.html", "r", encoding="utf-8") as file:
    html_content = file.read()

# Create BeautifulSoup object
soup = BeautifulSoup(html_content, "html.parser")

# 1. Getting the title of the page
title = soup.title.text
print("Page Title:", title)

# 2. Finding all links (anchor tags)
links = soup.find_all("a")
for link in links:
    print("Link:", link.get("href"))

# 3. Finding all paragraphs
paragraphs = soup.find_all("p")
for para in paragraphs:
    print("Paragraph:", para.text)

# 4. Extracting a table
tables = soup.find_all("table")
for table in tables:
    rows = table.find_all("tr")
    for row in rows:
        cols = row.find_all("td")
        print("Row Data:", [col.text for col in cols])

# 5. Extracting elements by class name
divs = soup.find_all("div", class_="content-section")
for div in divs:
    print("Div Content:", div.text)

# 6. Extracting elements by ID
special_div = soup.find(id="special-div")
if special_div:
    print("Special Div Content:", special_div.text)

# 7. Navigating the HTML Tree
body = soup.body
print("Body Content:", body.text)

# 8. Extracting images
images = soup.find_all("img")
for img in images:
    print("Image Source:", img.get("src"))

# 9. Extracting text from a specific tag
description = soup.find("meta", attrs={"name": "description"})
if description:
    print("Meta Description:", description.get("content"))

# 10. Scraping using CSS selectors
title_via_selector = soup.select("title")[0].text
print("Title via CSS Selector:", title_via_selector)

# 11. Extracting form data
forms = soup.find_all("form")
for form in forms:
    print("Form Action:", form.get("action"))
    inputs = form.find_all("input")
    for input_tag in inputs:
        print("Input Field:", input_tag.get("name"))

# Change all <span> tags to <div> tags
for tag in soup.find_all("span"):
    tag.name = "div"
            
# Modify element attributes
for img in soup.find_all("img"):
    img["alt"] = "Updated Image"
            
# Save the modified HTML to a new file
with open("modified.html", "w", encoding="utf-8") as modified_file:
    modified_file.write(str(soup))

# OUTPUT
    
# Page Title: Sample Web Page
# Link: https://example.com
# Paragraph: This is a paragraph with some example link.
# Paragraph: Another paragraph inside a div.
# Paragraph: Content inside a special div with ID.
# Row Data: []
# Row Data: ['Alice', '25']
# Row Data: ['Bob', '30']
# Div Content: 
# Another paragraph inside a div.

# Special Div Content: 
# Content inside a special div with ID.

# Body Content: 
# Welcome to Web Scraping
# This is a paragraph with some example link.

# Another paragraph inside a div.


# Content inside a special div with ID.



# Name
# Age


# Alice
# 25


# Bob
# 30










# Image Source: image1.jpg
# Image Source: image2.jpg
# Meta Description: This is a sample HTML page for web scraping.
# Title via CSS Selector: Sample Web Page
# Form Action: submit.php
# Input Field: username
# Input Field: password
# Input Field: None
