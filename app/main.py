# app/main.py

# Import required libraries
from fastapi import FastAPI
from bs4 import BeautifulSoup
from database import get_connection  # MySQL connection function

# Initialize FastAPI app
app = FastAPI()

# API endpoint to scrape data and save to MySQL
@app.get("/scrape")
def scrape():
    """
    Scrape user data from demo.html and save to MySQL database.
    Returns the scraped data as JSON.
    """

    # Step 1: Read the demo HTML file
    with open("demo.html", "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")

    # Step 2: Find all user blocks in HTML
    users = soup.find_all("div", class_="user")

    # Step 3: Connect to MySQL
    conn = get_connection()
    cursor = conn.cursor()

    result = []

    # Step 4: Loop through each user and extract data
    for user in users:
        name = user.find("span", class_="name").text.strip()
        email = user.find("span", class_="email").text.strip()
        phone = user.find("span", class_="phone").text.strip()
        location = user.find("span", class_="location").text.strip()

        # Step 5: Insert data into MySQL table
        cursor.execute(
            "INSERT INTO users (name, email, phone, location) VALUES (%s, %s, %s, %s)",
            (name, email, phone, location)
        )

        # Step 6: Save data for API response
        result.append({
            "name": name,
            "email": email,
            "phone": phone,
            "location": location
        })

    # Step 7: Commit changes and close connection
    conn.commit()
    cursor.close()
    conn.close()

    # Step 8: Return scraped data as JSON
    return result
