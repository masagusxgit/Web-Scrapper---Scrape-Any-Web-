import requests
from lxml import html
import csv
import time
from urllib.parse import urljoin

class WebScraper:
    def __init__(self, base_url):
        self.base_url = base_url
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

    def get_page_content(self, url):
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            return html.fromstring(response.content)
        except Exception as e:
            print(f"Error fetching page {url}: {str(e)}")
            return None

    def extract_data(self, tree, xpaths):
        data = {}
        for field, xpath in xpaths.items():
            try:
                elements = tree.xpath(xpath)
                if elements:
                    if field == 'url_gambar':
                        # Handle relative URLs for images
                        data[field] = urljoin(self.base_url, elements[0])
                    else:
                        data[field] = elements[0].strip() if isinstance(elements[0], str) else elements[0].text_content().strip()
                else:
                    data[field] = ''
            except Exception as e:
                print(f"Error extracting {field}: {str(e)}")
                data[field] = ''
        return data

    def scrape_articles(self, article_urls, xpaths, output_file):
        results = []
        
        for url in article_urls:
            print(f"Scraping: {url}")
            tree = self.get_page_content(url)
            
            if tree is not None:
                data = self.extract_data(tree, xpaths)
                data['url'] = url
                results.append(data)
                
                # Add a small delay to be respectful to the server
                time.sleep(2)

        # Save to CSV
        if results:
            fieldnames = ['judul', 'konten', 'kategori', 'url', 'tanggal_terbit', 'penulis', 'url_gambar']
            with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(results)
            print(f"Data saved to {output_file}")
        else:
            print("No data was collected")

def main():
    # Example usage
    base_url = "https://example.com"  # Replace with your target website
    
    # Define your XPath expressions
    xpaths = {
        'judul': '//h1[@class="article-title"]/text()',  # Adjust these XPaths according to your target website
        'konten': '//div[@class="article-content"]//text()',
        'kategori': '//div[@class="category"]/text()',
        'tanggal_terbit': '//span[@class="publish-date"]/text()',
        'penulis': '//span[@class="author-name"]/text()',
        'url_gambar': '//div[@class="article-image"]//img/@src'
    }
    
    # Get number of articles to scrape from user
    num_articles = int(input("Enter the number of articles to scrape: "))
    
    # In a real implementation, you would need to generate or provide the article URLs
    article_urls = [f"{base_url}/article/{i}" for i in range(num_articles)]  # Replace with actual URL generation logic
    
    scraper = WebScraper(base_url)
    scraper.scrape_articles(article_urls, xpaths, 'scraped_articles.csv')

if __name__ == "__main__":
    main()
