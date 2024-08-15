from bs4 import BeautifulSoup
import requests
import html5lib

url = "https://www.paradigmshift.com.pk"
data = requests.get(url)
html_content = data.text
soup = BeautifulSoup(html_content, 'html.parser')

# print(html_content[:500])

links = soup.find_all('a')

for link in links:
    print(link.text)

# for link in soup.find_all('a', href=True):
#     print(link.get('href'))

# for link in soup.find_all('img'):
#     print(link)
#     print(link.get('src'))

# url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/HTMLColorCodes.html"

# data = requests.get(url).text
# soup = BeautifulSoup(data, 'html5lib')
# table = soup.find('table')

# for rows in table.find_all('tr'):
#     cols = row.find_all('td')
#     color_name = cols[2].string
#     color_code = cols[3].text
#     print("{}--->{}".format(color_name, color_code))
