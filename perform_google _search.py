from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# Step 1: Set up the WebDriver using the correct installation
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run headless (optional)

# Step 2: Correctly initialize the WebDriver with the ChromeDriverManager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# Step 3: Perform a Google search
def perform_google_search(query):
    driver.get("https://www.google.com/")
    
    # Wait for the page to load
    time.sleep(2)
    
    # Find the search box and type the query
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)
    
    # Wait for results to load
    time.sleep(3)

# Step 4: Extract the top results
def extract_top_results():
    results = []
    
    # Find all the search result elements
    search_results = driver.find_elements(By.CSS_SELECTOR, 'div.g')

    for result in search_results:
        # Extract the title
        title_element = result.find_element(By.CSS_SELECTOR, 'h3')
        if title_element:
            title = title_element.text
        
        # Extract the link
        link_element = result.find_element(By.TAG_NAME, 'a')
        link = link_element.get_attribute('href')

        # Extract the description/snippet
        try:
            description_element = result.find_element(By.CSS_SELECTOR, 'div.VwiC3b')
            description = description_element.text if description_element else 'No description available'
        except:
            description = 'No description available'

        results.append({
            'title': title,
            'link': link,
            'description': description
        })
    
    return results

# Step 5: Define the main function
def main():
    query = "Who was the first person stepped first on moon?"
    
    # Perform the search
    perform_google_search(query)
    
    # Extract and print top search results
    results = extract_top_results()
    
    for i, result in enumerate(results):
        print(f"Result {i + 1}:")
        print(f"Title: {result['title']}")
        print(f"Link: {result['link']}")
        print(f"Description: {result['description']}\n")
    
    # Close the browser
    driver.quit()

# Step 6: Run the script
if __name__ == "__main__":
    main()
