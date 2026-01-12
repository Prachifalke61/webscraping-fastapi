from bs4 import BeautifulSoup

with open("demo.html", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")

users = soup.find_all("div", class_="user")

for user in users:
    name = user.find("span", class_="name").text
    email = user.find("span", class_="email").text
    phone = user.find("span", class_="phone").text
    location = user.find("span", class_="location").text

    print(name, email, phone, location)
