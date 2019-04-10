EXTRACT:
Using Pandas, we pulled data from 3 CSVs, which had 58 similar columns. Two of the three CSVs had a column for the IRS990 form, which we dropped from the Pandas dataframe.

TRANSFORM:
Looking through each of the columns, we decided to drop all the tax information for all of the museums. We were specifically interested in categorizing by museums by location, and segmented them by region 

We realized that the two zip code columns in the original were mislabeled. ZIPCODE-5 and ZIPCODE were actually switched. The common zip code had entries such as 90036-8675 and the ZIPCODE-5 column only had entries with clean, six-digit zips. So we switched the names and, ultimately, decided to drop the zip code column with the four-digit extension.  

Make sure to create a config.py file and add it to your .gitignore prior to uploading. Here’s what you need:

password = “ “
username = “ “
host = “ “ 
database = “ “ 

These fields are required and will be pulled when you load the data into the database.

LOAD:
run schema.sql in a SQL client interface application 

CONTRIBUTORS:
Ramon Gomez
Pavel Altukhov
Charlotte Acevedo

DATA SOURCES:
https://www.imls.gov/research-evaluation/data-collection/museum-universe-data-file 

PARSED AND CLEANED UP DIDN’T END UP USING
https://github.com/MuseumofModernArt/collection 
https://github.com/tategallery/collection 
https://github.com/cooperhewitt/collection 
http://www.penn.museum/collections/data.php 
https://www.rijksmuseum.nl/en/api 
https://www.brooklynmuseum.org/opencollection/api/ 
https://medium.com/@blprnt/a-sort-of-joy-1d9d5ff02ac9 


SIGNIFICANT FILES/FOLDERS:
main.py
extract.py
transform.py
loader.py
schema.sql
us_museums_final.csv

SUMMARY:
By creating the IMLS data files into a database we have created a skeleton for organizing American museums and libraries collection’s into one, massive database. Uses for this database as is are searching institution by location such as zip code, coordinates, or region. 
