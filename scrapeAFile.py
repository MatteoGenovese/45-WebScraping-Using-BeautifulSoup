from bs4 import BeautifulSoup

with open("website.html") as website:
    contents = website.read()

soup = BeautifulSoup(contents, 'html.parser')

# print(soup.title.string)
# print(soup.title.string)
# print(soup.prettify())
# print(soup.a)

# print all p texts
allPsText = soup.find_all(name="p")
for p in allPsText:
    print(p.get_text())

# print all a href
allAs = soup.find_all(name="a")
for a in allAs:
    print(a.get("href"))

# print all h1 with id=name
heading = soup.find_all(name="h1", id="name")
for h in heading:
    print(h.get_text())

# print all h1 with class=heading
heading2 = soup.find_all(name="h3", class_="heading")
for h in heading2:
    print(h.get_text())

# find nested tags with css selectors
companyUrl = soup.select_one("p a")
print(companyUrl.get("href"))

headings = soup.select(".heading")
print(headings)