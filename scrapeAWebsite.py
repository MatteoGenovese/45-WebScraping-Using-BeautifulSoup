from bs4 import BeautifulSoup
import requests

# get the website html
response = requests.get("https://news.ycombinator.com/news")
soup = BeautifulSoup(response.text, "html.parser")

# find articles and subtexts
articles = [a for a in soup.find_all(name="tr", class_="athing")]
subTexts = [a for a in soup.select("tr .subtext")]

# Select more specifically
articleTitles = [a.select(".titleline a")[0].get_text() for a in articles]
articleLinks = [l.find_next("a", rel="noreferrer").get("href") for l in articles]
articlePoints = [int(a.select(".score")[0].get_text().split(" ")[0] if len(a.select(".score")) > 0 else 0) for a in subTexts]

# calculate maximum points article
largestNumber = max(articlePoints)
largestIndex = articlePoints.index(largestNumber)

# Display it on screen
print(articleTitles[largestIndex])
print(articleLinks[largestIndex])

