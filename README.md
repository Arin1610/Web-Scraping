# Website Information Extractor

This Python script extracts various information from a list of websites and saves it to a CSV file. The information extracted includes social media links, tech stack, meta title, meta description, payment gateways, website language, and category of the website.

## Features

- Extracts social media links, tech stack, meta tags, payment gateways, language, and category from websites.
- Uses Selenium for dynamic web page rendering and Beautiful Soup for parsing HTML.
- Supports headless mode for scraping without a browser window.
- Saves extracted information to a CSV file for easy analysis.

## Requirements

- Python 3.x
- Selenium
- Beautiful Soup
- Chrome WebDriver (for Selenium)

## Installation

1. **Python 3.x**: If you don't have Python installed, download and install it from [the official Python website](https://www.python.org/downloads/).

2. **Selenium and Beautiful Soup**: Install the required Python packages using pip:

   ```bash
   pip install selenium beautifulsoup4
   ```

3. **Chrome WebDriver**: Download the appropriate Chrome WebDriver binary from [the ChromeDriver website](https://chromedriver.chromium.org/downloads) based on your Chrome browser version. Ensure the WebDriver binary is placed in a directory included in your system's PATH environment variable.

## Usage

1. **Clone the Repository**: Clone this repository or download the script (`app.py`) directly to your local machine.

2. **Modify the Website List**: Open the script (`app.py`) in a text editor and modify the `websites` list to include the URLs you want to scrape.

   ```python
   websites = [
       "https://example.com",
       "https://another-example.com",
       # Add more websites here
   ]
   ```

3. **Run the Script**: Open a terminal or command prompt, navigate to the directory containing the script, and execute the following command:

   ```bash
   python app.py
   ```

4. **Check Output**: Once the script finishes executing, you will find the extracted information saved in a file named `websites_info.csv` in the same directory as the script.

## Code Explanation

- **Importing Libraries**: The script imports necessary libraries including `requests`, `BeautifulSoup`, `csv`, `time`, `re`, and `Selenium`.

- **Setup Selenium WebDriver**: The script sets up Selenium WebDriver with Chrome for dynamic web page rendering in headless mode.

  ```python
  from selenium import webdriver
  from selenium.webdriver.chrome.service import Service
  from selenium.webdriver.chrome.options import Options
  
  chrome_options = Options()
  chrome_options.add_argument("--headless")
  chrome_options.add_argument("--disable-gpu")
  service = Service(executable_path="C:/WebDriver/bin/chromedriver.exe")
  driver = webdriver.Chrome(service=service, options=chrome_options)
  ```

- **Defining Functions**: Functions are defined to extract social media links, tech stack, meta tags, payment gateways, website language, and category from the HTML content of websites.

- **Extract Information**: The main function `extract_info` is defined to call these functions and compile the extracted information into a dictionary.

  ```python
  def extract_info(url):
      driver.get(url)
      content = driver.page_source
      soup = BeautifulSoup(content, 'html.parser')

      social_media_links = extract_social_media_links(soup)
      tech_stack = extract_tech_stack(soup)
      meta_title = extract_meta_title(soup)
      meta_description = extract_meta_description(soup)
      payment_gateways = extract_payment_gateways(content)
      website_language = extract_website_language(soup)
      category = extract_category(url)

      return {
          "url": url,
          "social_media_links": social_media_links,
          "tech_stack": tech_stack,
          "meta_title": meta_title,
          "meta_description": meta_description,
          "payment_gateways": payment_gateways,
          "website_language": website_language,
          "category": category
      }
  ```

- **Saving to CSV**: The script iterates through the list of websites, extracts information using the `extract_info` function, and saves the data to a CSV file.

  ```python
  with open('websites_info.csv', 'w', newline='', encoding='utf-8') as csvfile:
      fieldnames = ["url", "social_media_links", "tech_stack", "meta_title", "meta_description", "payment_gateways", "website_language", "category"]
      writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
      writer.writeheader()

      for site in websites:
          info = extract_info(site)
          writer.writerow(info)
          print(f"Extracted info for: {site}")
          print(info)
          time.sleep(2)
  ```

### Conclusion
This web scraping solution efficiently extracts valuable information from a list of websites and saves it into a CSV file. It demonstrates proficiency in using Python for web scraping, handling dynamic web content with Selenium, and parsing HTML with Beautiful Soup. The script is modular, easy to understand, and follows best coding practices, making it maintainable and extensible for future enhancements.