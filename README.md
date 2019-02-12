# sedar-filings-csv-lister
Scrapes Financial Statement filings from Sedar into a .csv file

At run it asks for the filing date, after its done it exits.

If there was no filing for that day then it writes it into a file titled empty_ + the YYYYMM

All filings are saved into one .csv per month.

If you want to scrape different kind of filings from Sedar, just change document_selection=5 this line to the appropiate one.

![alt text](https://github.com/alternistom/sedar-filings-csv-lister/blob/master/screenshot_sedar.png)
