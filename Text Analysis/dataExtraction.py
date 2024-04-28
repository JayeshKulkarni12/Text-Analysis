import pandas as pd
from bs4 import BeautifulSoup
import requests
import os

# Read the Excel file
input_file = "Input.xlsx"
df = pd.read_excel(input_file)

# Function to extract article text from URL
def extract_article_text(url, url_id):
    # Send a GET request to the URL
    response = requests.get(url)
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    # Find the article title
    title = soup.find('title').text.strip()
    # Find the article text
    article_text = ""
    for paragraph in soup.find_all('p'):
        article_text += paragraph.get_text() + "\n"
    
    # Save the extracted text to a file
    filename = f"{output_directory}/{url_id}.txt"
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(title + "\n\n")
        file.write(article_text)

# Specify the desired output directory
output_directory = "C:/Users/jayes/Desktop/extracted_articles"

# Create the output directory if it doesn't exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Extract article text for each URL
for index, row in df.iterrows():
    url_id = row['URL_ID']
    url = row['URL']
    extract_article_text(url, url_id)
    print(f"Article text extracted for {url_id}")

print("Extraction completed.")


