import requests
from bs4 import BeautifulSoup

# Set the base URL of the website
base_url = "http://books.toscrape.com/catalogue/category/books_1/"

# Set the initial page number to 1
page_number = 1

# Set a flag to indicate when to stop scraping
done = False

# Scrape until we reach the last page
while not done:
    # Construct the URL for the current page
    url = base_url + "page-" + str(page_number) + ".html"

    # Make a request to the website
    response = requests.get(url)

    # Parse the HTML content
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all the h3 elements on the page (these contain the book titles)
    titles = soup.find_all("h3")

    # Iterate over the titles
    for title in titles:
        # Get the text of the title
        title_text = title.text

        # Check if the title starts with 'm' or 's', and if its length is between 10 and 20 characters
        if (title_text[0].lower() == 'm' or title_text[0].lower() == 's') and 10 <= len(title_text) <= 20:
            print(title_text)

    # Check if there is a next page
    next_page = soup.find(class_="next")

    # If there is no "next" button, we've reached the last page
    if next_page is None:
        done = True
    else:
        # Increment the page number
        page_number += 1
