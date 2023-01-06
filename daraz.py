import requests
from bs4 import BeautifulSoup
import csv


# Open a CSV file for writing

with open('scraped_data2.csv', 'w', encoding='utf-8') as csv_file:
    # Create a CSV writer
    writer = csv.writer(csv_file)
    writer.writerow(['name', 'link', 'Price', 'image_link'])
# Make a request to the website
    URL = "https://www.sastodeal.com/sd-fast/food-essentials/rice-rice-products.html"
    page = requests.get(URL)

    # Parse the HTML content of the page

    soup = BeautifulSoup(page.content, "html.parser")

    # Find all the product containers on the page
    product_containers = soup.find_all("div", class_="product-item-info")

    # For each product container, extract the category, product name, link, price, and image link
    for container in product_containers:
        # category = container.find("div", class_="category").text
        name = container.find("a", class_="product-item-link").text
        link = container.find("a", class_="product-item-link")["href"]
        price = container.find("span", class_="price").text
        image_link = container.find("img")["src"]

        # Print the information for each product
        # print(f"Category: {category}")
        print(f"Name: {name}")
        print(f"Link: {link}")
        print(f"Price: {price}")
        print(f"Image Link: {image_link}")
        writer.writerow([name, link, price, image_link])



        # Write the header row

