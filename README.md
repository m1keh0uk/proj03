# eBay DL

This script (`ebay_dl.py`) scrapes eBay search results for product listings based on a search term and number of pages.

It collects:
- item name
- price
- shipping cost
- whether it has free returns
- item condition (new/used)
- how many have been sold

You can save the output as a `.json` file by default, or as a `.csv` file using the `--csv` flag.

## How to Run

### Basic Search
Enter this command into terminal. Replace (search term) with desired ebay serch word:

python ebay_dl.py (search term) 

ex: python ebay_dl.py 'lebron'

### Change Page Numbers
Add additional argument to select how many pages of ebay to collect from. Optional argument, defaults to 10 pages.

python ebay_dl.py (search term) --pg_num=(number of pages)

ex: python ebay_dl.py 'lebron' --pg_num=4

### Change format to CSV
Add --csv flag to change output from JSON to CSV

python ebay_dl.py (search term) --pg_num=(number of pages) --csv

ex: python ebay_dl.py 'lebron'  --pg_num=4 --csv

## Course Project

https://github.com/mikeizbicki/cmc-csci040/tree/2025spring/project_03_webscraping