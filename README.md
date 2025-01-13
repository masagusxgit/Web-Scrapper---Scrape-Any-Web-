# Web-Scrapper---Scrape-Any-Web-
# Python Web Scraper with XPath

A flexible and robust web scraper built in Python that extracts article data using XPath selectors. This scraper is designed to collect the following information from articles:
- Title
- Content
- Category
- URL
- Publication Date
- Author
- Image URL

## Features

- XPath-based data extraction
- CSV output format
- Configurable number of articles to scrape
- Built-in rate limiting
- Error handling
- Relative URL resolution for images
- User-Agent rotation to prevent blocking

## Requirements

### Python Version
- Python 3.7 or higher

### Required Modules
```bash
pip install requests lxml
```

Or install using requirements.txt:
```bash
pip install -r requirements.txt
```

## Installation

1. Clone the repository or download the script
2. Install the required dependencies
3. Adjust the XPath expressions to match your target website

## Usage

1. Update the XPath expressions in the script to match your target website's HTML structure:
```python
xpaths = {
    'judul': '//h1[@class="article-title"]/text()',
    'konten': '//div[@class="article-content"]//text()',
    'kategori': '//div[@class="category"]/text()',
    'tanggal_terbit': '//span[@class="publish-date"]/text()',
    'penulis': '//span[@class="author-name"]/text()',
    'url_gambar': '//div[@class="article-image"]//img/@src'
}
```

2. Set your target website's base URL:
```python
base_url = "https://example.com"  # Replace with your target website
```

3. Run the script:
```bash
python web_scraper.py
```

4. Enter the number of articles you want to scrape when prompted

The script will create a CSV file named 'scraped_articles.csv' containing the extracted data.

## Output Format

The script generates a CSV file with the following columns:
- judul (Title)
- konten (Content)
- kategori (Category)
- url
- tanggal_terbit (Publication Date)
- penulis (Author)
- url_gambar (Image URL)

## Important Notes

- Be respectful of the website's robots.txt file
- The script includes a 2-second delay between requests to avoid overwhelming the server
- Make sure you have permission to scrape the target website
- Adjust the User-Agent header if needed
- Consider implementing proxy rotation for large-scale scraping

## Error Handling

The scraper includes error handling for:
- Failed HTTP requests
- Invalid XPath expressions
- Missing data
- Network connectivity issues

## Customization

You can customize the scraper by:
- Adjusting the delay between requests
- Modifying the User-Agent header
- Adding proxy support
- Implementing custom data processing
- Adding additional data fields to extract

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is open source and available under the MIT License.
