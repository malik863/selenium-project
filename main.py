from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize WebDriver (e.g., Chrome)
driver = webdriver.Chrome()  # Make sure you have 'chromedriver' in your PATH

# Navigate to the website
driver.get("http://books.toscrape.com/")

# Find all book elements on the page
books = driver.find_elements(By.CLASS_NAME, "product_pod")

# Iterate through each book and extract the desired information
for book in books:
    # Extract the title
    title = book.find_element(By.TAG_NAME, "h3").find_element(By.TAG_NAME, "a").get_attribute("title")
    
    # Extract the price
    price = book.find_element(By.CLASS_NAME, "price_color").text
    
    # Extract the availability
    availability = book.find_element(By.CLASS_NAME, "instock").text.strip()
    
    # Extract the rating (as a word, e.g., "Three", "Five")
    rating_class = book.find_element(By.CLASS_NAME, "star-rating").get_attribute("class")
    rating = rating_class.split()[-1]  # Extract rating from class name (e.g., "star-rating Three" -> "Three")

    # Print the extracted information
    print(f"Title: {title}")
    print(f"Price: {price}")
    print(f"Availability: {availability}")
    print(f"Rating: {rating}")
    print("-" * 40)

# Close the WebDriver
driver.quit()
