def fibonacci_gen(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

for num in fibonacci_gen(10):
    print(num)
    
    
def read_large_file(file_name):
    with open(file_name, "r") as file:
        # Read the file line by line
        for line in file:
            # Yield each line to the caller
            yield line

# Usage
for line in read_large_file("large_file.log"):
    # Process each line
    print(line)  # or any other processing


import requests
from bs4 import BeautifulSoup

def get_articles(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    for article in soup.find_all('article'):
        yield article.get_text()

# Use the generator to process one article at a time
for article_text in get_articles("https://example-news-site.com/news"):
    process(article_text)  # hypothetical processing function
