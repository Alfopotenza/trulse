import selenium.webdriver as webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
import time

_url = 'https://cryptonews.com/it/news/lintelligenza-artificiale-di-chatgpt-ha-previsto-il-prezzo-di-bitcoin-nel-2025/'

#FUNZIONI PER ANALIZZARE UN TESTO
def scrape_website(url):
    print("Launching chrome browser")

    chrome_driver_path = './chromedriver.exe'
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)

    try:
        driver.get(url)
        print("Page loaded...")
        html = driver.page_source
        time.sleep(5)

        return html
    finally:
        driver.quit()
def extract_body_content(html_content):
    soup = BeautifulSoup(html_content , 'html.parser')
    body_content = soup.body
    if body_content:
        return str(body_content)
    else:
        return ""
def clean_body_content(body_content):
    soup = BeautifulSoup(body_content , 'html.parser')
    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()

    #if no text was found between '\n', remove it#
    cleaned_content = soup.get_text(separator="\n")
    cleaned_content = '\n'.join(line.strip() for line in cleaned_content.splitlines() if line.strip())

    return cleaned_content

def split_dom_content(dom_content, max_length = 6000):
    return [
        dom_content[i: i + max_length] for i in range(0, len(dom_content), max_length)
    ]

print(f"scraped website: {scrape_website(_url)}"
      f"body of website: {extract_body_content(scrape_website(_url))}"
      f"cleaned website: {clean_body_content(extract_body_content(scrape_website(_url)))}")