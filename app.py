import csv
from urllib.parse import urlparse
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

# Configure Selenium WebDriver
chrome_options = Options()
chrome_options.add_argument("--headless")  # Ensure GUI is off

# Set path to chromedriver as per your configuration
webdriver_service = Service('C:/Users/LENOVO/anaconda3/Lib/site-packages/typings/selenium/webdriver/chrome/chromedriver.exe')

# Initialize the driver
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

# Function to extract information from a website
def extract_info(url):
    info = {
        "url": url,
        "social_media_links": [],
        "tech_stack": [],
        "meta_title": "",
        "meta_description": "",
        "payment_gateways": [],
        "website_language": "",
        "category": ""
    }
    
    try:
        # Get page content
        driver.get(url)
        content = driver.page_source
        soup = BeautifulSoup(content, 'lxml')

        # Extract social media links
        social_media_platforms = ["facebook", "twitter", "instagram", "linkedin", "pinterest", "youtube"]
        for link in soup.find_all('a', href=True):
            href = link['href']
            if any(platform in href for platform in social_media_platforms):
                info["social_media_links"].append(href)

        # Extract meta title
        if soup.title:
            info["meta_title"] = soup.title.string

        # Extract meta description
        description = soup.find('meta', attrs={"name": "description"})
        if description and description.get("content"):
            info["meta_description"] = description["content"]

        # Extract tech stack (simplified for illustration)
        scripts = [script['src'] for script in soup.find_all('script', src=True)]
        if any("wp-content" in script for script in scripts):
            info["tech_stack"].append("WordPress")
        if any("jquery" in script for script in scripts):
            info["tech_stack"].append("jQuery")
        if any("react" in script for script in scripts):
            info["tech_stack"].append("React")
        if any("vue" in script for script in scripts):
            info["tech_stack"].append("Vue.js")
        if any("angular" in script for script in scripts):
            info["tech_stack"].append("Angular")

        # Detect payment gateways
        content_str = str(content).lower()
        if "paypal" in content_str:
            info["payment_gateways"].append("PayPal")
        if "stripe" in content_str:
            info["payment_gateways"].append("Stripe")
        if "razorpay" in content_str:
            info["payment_gateways"].append("Razorpay")

        # Extract website language
        html_tag = soup.find('html')
        if html_tag and html_tag.get("lang"):
            info["website_language"] = html_tag["lang"]

        # Determine category based on URL or meta keywords
        parsed_url = urlparse(url)
        domain = parsed_url.netloc.lower()
        if "news" in domain or any(keyword in content_str for keyword in ["news", "media"]):
            info["category"] = "News"
        elif "shop" in domain or any(keyword in content_str for keyword in ["shop", "store", "cart"]):
            info["category"] = "E-commerce"
        elif "blog" in domain or any(keyword in content_str for keyword in ["blog", "post", "article"]):
            info["category"] = "Blog"
        elif "edu" in domain or any(keyword in content_str for keyword in ["education", "course", "university", "school"]):
            info["category"] = "Education"
        elif "health" in domain or any(keyword in content_str for keyword in ["health", "medical", "hospital"]):
            info["category"] = "Health"
        elif "tech" in domain or any(keyword in content_str for keyword in ["tech", "software", "app"]):
            info["category"] = "Technology"
        elif "sport" in domain or any(keyword in content_str for keyword in ["sport", "team", "league"]):
            info["category"] = "Sports"
        elif "entertainment" in domain or any(keyword in content_str for keyword in ["movie", "music", "show"]):
            info["category"] = "Entertainment"
        elif "food" in domain or any(keyword in content_str for keyword in ["food", "recipe", "restaurant"]):
            info["category"] = "Food"
        elif "travel" in domain or any(keyword in content_str for keyword in ["travel", "tourism", "destination"]):
            info["category"] = "Travel"
        elif "finance" in domain or any(keyword in content_str for keyword in ["finance", "investment", "bank"]):
            info["category"] = "Finance"
        elif "fashion" in domain or any(keyword in content_str for keyword in ["fashion", "clothing", "style"]):
            info["category"] = "Fashion"
        elif "automotive" in domain or any(keyword in content_str for keyword in ["automotive", "car", "vehicle"]):
            info["category"] = "Automotive"
        else:
            info["category"] = "Other"

    except Exception as e:
        print(f"Error extracting information from {url}: {e}")
    
    return info

# List of 100 websites to scrape
websites = [
    "https://www.python.org",
    "https://www.djangoproject.com",
    "https://www.paypal.com",
    "https://stripe.com",
    "https://razorpay.com",
    "https://www.shopify.com",
    "https://www.wordpress.com",
    "https://www.medium.com",
    "https://www.facebook.com",
    "https://twitter.com",
    "https://www.wikipedia.org",
    "https://www.github.com",
    "https://www.stackoverflow.com",
    "https://www.reddit.com",
    "https://www.bbc.com",
    "https://www.cnn.com",
    "https://www.nytimes.com",
    "https://www.theguardian.com",
    "https://www.techcrunch.com",
    "https://www.wired.com",
    "https://www.huffpost.com",
    "https://www.bloomberg.com",
    "https://www.forbes.com",
    "https://www.wsj.com",
    "https://www.cnet.com",
    "https://www.theverge.com",
    "https://www.engadget.com",
    "https://www.ted.com",
    "https://www.imdb.com",
    "https://www.amazon.com",
    "https://www.ebay.com",
    "https://www.alibaba.com",
    "https://www.netflix.com",
    "https://www.disneyplus.com",
    "https://www.hulu.com",
    "https://www.spotify.com",
    "https://www.apple.com",
    "https://www.microsoft.com",
    "https://www.google.com",
    "https://www.yahoo.com",
    "https://www.bing.com",
    "https://www.linkedin.com",
    "https://www.instagram.com",
    "https://www.pinterest.com",
    "https://www.tumblr.com",
    "https://www.quora.com",
    "https://www.yelp.com",
    "https://www.tripadvisor.com",
    "https://www.airbnb.com",
    "https://www.booking.com",
    "https://www.expedia.com",
    "https://www.khanacademy.org",
    "https://www.coursera.org",
    "https://www.udemy.com",
    "https://www.edx.org",
    "https://www.duolingo.com",
    "https://www.codecademy.com",
    "https://www.pluralsight.com",
    "https://www.academia.edu",
    "https://www.researchgate.net",
    "https://www.nationalgeographic.com",
    "https://www.sciencemag.org",
    "https://www.nature.com",
    "https://www.newscientist.com",
    "https://www.sciencedaily.com",
    "https://www.livescience.com",
    "https://www.space.com",
    "https://www.espn.com",
    "https://www.nba.com",
    "https://www.nfl.com",
    "https://www.mlb.com",
    "https://www.nhl.com",
    "https://www.fifa.com",
    "https://www.olympic.org",
    "https://www.formula1.com",
    "https://www.motogp.com",
    "https://www.nascar.com",
    "https://www.healthline.com",
    "https://www.webmd.com",
    "https://www.mayoclinic.org",
    "https://www.cdc.gov",
    "https://www.who.int",
    "https://www.nih.gov",
    "https://www.nhs.uk",
    "https://www.cancer.org",
    "https://www.diabetes.org",
    "https://www.heart.org",
    "https://www.unicef.org",
    "https://www.un.org",
    "https://www.worldbank.org",
    "https://www.imf.org",
    "https://www.redcross.org",
    "https://www.doctorswithoutborders.org",
    "https://www.amnesty.org",
    "https://www.greenpeace.org",
    "https://www.wwf.org",
    "https://www.savethechildren.org",
    "https://www.plan-international.org",
    "https://www.oxfam.org",
    "https://www.hrw.org"
]


# Extract info and save to CSV
with open('websites_info.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ["url", "social_media_links", "tech_stack", "meta_title", "meta_description", "payment_gateways", "website_language", "category"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    
    for url in websites:
        info = extract_info(url)
        writer.writerow(info)
