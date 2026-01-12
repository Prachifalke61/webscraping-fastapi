from fastapi import FastAPI
from bs4 import BeautifulSoup
from database import get_connection

app = FastAPI()

@app.get("/scrape")
def scrape():
    with open("demo.html", "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")

    users = soup.find_all("div", class_="user")

    conn = get_connection()
    cursor = conn.cursor()

    result = []

    for user in users:
        name = user.find("span", class_="name").text
        email = user.find("span", class_="email").text
        phone = user.find("span", class_="phone").text
        location = user.find("span", class_="location").text

        cursor.execute(
            "INSERT INTO users (name, email, phone, location) VALUES (%s, %s, %s, %s)",
            (name, email, phone, location)
        )

        result.append({
            "name": name,
            "email": email,
            "phone": phone,
            "location": location
        })

    conn.commit()
    cursor.close()
    conn.close()

    return result
