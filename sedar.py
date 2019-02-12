from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import urllib.request
import random

import ssl
ssl._create_default_https_context = ssl._create_unverified_context


print(" _____ _____ ____  _____ _____    ____  _____ _ _ _ _____ __    _____ _____ ____  _____ _____ ")
print("|   __|   __|    \|  _  | __  |  |    \|     | | | |   | |  |  |     |  _  |    \|   __| __  |")
print("|__   |   __|  |  |     |    -|  |  |  |  |  | | | | | | |  |__|  |  |     |  |  |   __|    -|")
print("|_____|_____|____/|__|__|__|__|  |____/|_____|_____|_|___|_____|_____|__|__|____/|_____|__|__|")
print(" v.1.3")
print("")
print(" last updated on:      Jan-14-2019")  
print(" initially created on: Jun-20-2017")                                                        
print("")

# This is our base URL
base_url = "http://sedar.com/FindMFDocuments.do?lang=EN&page_no="
# Some days have multiple pages, some don't, but they all have a first one
page = 1
# URL continued...
base_url_2 = "&company_search=All+%28or+type+a+name%29&document_selection=5&FromDate="
# We ask for the day
day = input("► Which day would you like to scrape? ")
# URL snipet
url_part_2 = "&FromMonth="
# We ask for the month
month = input("► Which month? ")
# Still URL
url_part_3 = "&FromYear="
# We ask for the year
year = input("► Which year? ")
# Giving someone space is always healthy
print("")
# Since the from and to is the same we won't ask for more values
url_part_4 = "&ToDate="
# day here again
url_part_5 = "&ToMonth="
# month here again
url_part_6 = "&ToYear="
# year here again
url_part_7 = "&Variable=FilingDate"

# For filename we need two digit for month and day, but URL only one, therefore:
if len(day) == 1:
	day_fn = "0" + day
else:
	day_fn = day

if len(month) == 1:
	month_fn = "0" + month
else:
	month_fn = month

# If this goes False the script will stop, when there are no other pages we kill the process
multiple_pages = True

while multiple_pages is True:
	
	# By your power combined, I am Captain Planet!
	fund_url = base_url + str(page) + base_url_2 + str(day) + url_part_2 + str(month) + url_part_3 + str(year) + url_part_4 + str(day) + url_part_5 + str(month) + url_part_6 + str(year) + url_part_7
	
	# Giving the indication that the script is indeed alive
	print("Now collecting data from page: " + str(page) + " for " + str(year) + "|" + str(month) + "|" + str(day) +  " Please wait...")
	my_url = str(fund_url)

	# This needed for some pages against the 403 error
	req = urllib.request.Request(my_url, headers={'User-Agent': 'Mozilla/5.0'})
	page_html = urllib.request.urlopen(req).read()

	# We locate the table
	page_soup = soup(page_html, "html.parser")
	table = page_soup.findAll("table")
	
	# We locate the lines
	filings = table[2].findAll("tr", {"class":"rt"})
	# With this counter we will cycle through all lines on a page
	col_cnt = 0
	
	# We use this string to check if it's an empty/last page or not
	# results = table[1].findAll("br")
	results = table[1].findAll("td")
	search_results = results[2]
	stripped_search_results = search_results.text.replace("\n", "").replace("\r", "").strip()
		
	if stripped_search_results == "Search results      0-0":
		if page != 1:
			break
		multiple_pages = False
		print("No holdings for this day!")
		filename = "empty_SEDAR_" + year + month_fn + ".csv"
		f = open(filename, "a")
		f.close
		break
		
   #filename = "SEDAR_" + year + month_fn + day_fn + ".csv"
	filename = "SEDAR_" + year + month_fn + ".csv"
	f = open(filename, "a")
	headers = "who, status, doc_type, filing_date, company, link_to_doc, link_to_fund\n"
	if page == 1:
		f.write(headers)
		
		
	for row in filings:
		first_col = filings[col_cnt].findAll("td")
		
		company_from_col = first_col[0]
		company_text = company_from_col.text.replace(",", "").strip()
		
		date_from_col = first_col[1]
		date_text = date_from_col.text.replace(",", "").strip()
				
		doc_type_from_col = first_col[3]
		doc_type_text = doc_type_from_col.text.replace(",", "").strip()
		# if doc_type_text == "AB Form 13-501F5 (Investment Fund - Participation Fee)":
		
		link_from_col = first_col[3]
		link_text = link_from_col.a["title"]
		
		fundlink_from_col = first_col[0]
		fundlink_text = fundlink_from_col.a["href"]
			
		f.write("," + "," + doc_type_text + "," + date_text + "," + company_text + "," + "http://sedar.com/GetFile.do?&lang=EN" + link_text + "," + "http://sedar.com" + fundlink_text + "\n")
		
		col_cnt = col_cnt + 1
		
	f.close
			
	page = page + 1

Goodbyemsg = random.randint(1, 10)

print("")

if Goodbyemsg == 1:
	print("But man is not made for defeat. A man can be destroyed but not defeated. - Ernest Hemingway")
elif Goodbyemsg == 2:
	print("When you reach the end of your rope, tie a knot in it and hang on. - Franklin D. Roosevelt")
elif Goodbyemsg == 3:
	print("Learning never exhausts the mind. - Leonardo da Vinci")
elif Goodbyemsg == 4:
	print("There is no charm equal to tenderness of heart. - Jane Austen")
elif Goodbyemsg == 5:
	print("Lord, make me an instrument of thy peace. Where there is hatred, let me sow love. - Francis of Assisi")
elif Goodbyemsg == 6:
	print("Keep your face always toward the sunshine - and shadows will fall behind you. - Walt Whitman")
elif Goodbyemsg == 7:
	print("Happiness can exist only in acceptance. - George Orwell")
elif Goodbyemsg == 8:
	print("I have not failed. I've just found 10,000 ways that won't work. - Thomas A. Edison")
elif Goodbyemsg == 9:
	print("Whoever is happy will make others happy too. - Anne Frank")
elif Goodbyemsg == 10:
	print("Tell me and I forget. Teach me and I remember. Involve me and I learn. - Benjamin Franklin")
