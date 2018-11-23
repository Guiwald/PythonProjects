from bs4 import BeautifulSoup
import csv
import re

# requests for fetching html of website
import requests

# Make the GET request to a URL
r = requests.get('https://en.wikipedia.org/wiki/List_of_urban_areas_in_the_Republic_of_Ireland_by_population')

# Extract the content
c = r.content

# Create a soup object
soup = BeautifulSoup(c, 'html.parser')

# Finding the data on the webpage
main_content  = soup.find('table', attrs = {'class': 'wikitable'})
content = main_content.find('tbody').text



print(content)

# Some Regex
city_pattern = re.compile(r'(?:[w\d]\n)([[A-Z][A-Za-z\s-]+?)(?:[\[\n])', flags = re.S)
county_pattern = re.compile(r'(?:[a-z\]]\n)([^\n]+?)(?:(?:\n\d+\,)|(?:\&))', flags = re.S)
# find all occurences of the pattern
city = city_pattern.findall(content)
county = county_pattern.findall(content)

#print(city)

print(city)
print(county)


for ci,co in zip(city,county):
# open a csv file
	with open('index.csv', mode='a') as csv_file:
        	writer = csv.writer(csv_file, delimiter=',')
        	writer.writerow([ci,co])




#with open('index.csv', mode='a') as csv_file:
#	writer = csv.writer(csv_file, delimiter=',')
#	writer.writerow(zip(city, county))


#f=open('index.csv','w')
#for i,j in zip(city,county):
#    f.write(str(i)+","+str(j))
#f.close()