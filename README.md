For AGIHouseSF Hackathon

We store all the info about our social network in local DB

Then we can ask it questions like: "who in my network is investing in Seed Stage AI companies?" 
Or
"Who in my network just left a company in the last couple months" 

It can also recommend quick 5m tasks to help empower your network like
"I noticed in your network your friend Jim mentioned they are leaving their space company to start something new, and your friend Helen invests in ambitious founders, you should intro them: here are the two emails."

# Design:
- Scraping. Linkedin. Messenger. anywhere else. A mix of public facing data, and private dms
	[ ] todo design ingestion interface so ppl can write their own scrapers ezpz
- Database: SEt of all the people, their public facing network info, and a dump of private DMs
	[ ] todo design DB schema to work generically with many frontends/ingestion patterns
- AI layer: can query DB for insights
- Frontend: Some local app or streamlit thing or react app or CLI to visualize insights

# How to contribute
3 Major chunks of code, each should be able to run standalone as mini projects you can hack on. Kyle Morris will orchestrate the DB layer + make things speak nicely to eachother.

## Scraping
If you want to write a scraper add a file or function to /scrapers that you could run standalone to fetch a bunch of useful info, such as linkedin dms, or facebook profile info. Make sure you figure out the auth, test it so it works reliably

## AI Layer: 
If you want to try writing your own query logic add a file to the /query directory that reads the Database and then outputs stuff, can just be in CLI for now

## Frontend
If you want to try some frontend, go to /frontend and make your own subdirectory. For eg., /frontend/python_cli if you want to try a CLI or /frontend/nextapp if you want to try a jsx app, or /frontend/streamlit if you want a streamlit app. Make sure you don't break the other frontends with yours

### Adding Data: 

How to use: 
- create a new database: run `python src/db_create_collection.py`, type CREATE 
- Reset (erase) database: run `python src/db_create_collection.py`, type RESET. then run `python src/db_create_collection.py` again, and type CREATE

- add data:  run `python src/main.py`
- query data: run `python src/db_query_data.py`
- to run the local chromadb server, run `python src/main.py`

Main functions to update: 
- chunk_long_document (if you want a different chunking algorithm)
- chunk_long_document

*Notes on adding data*
- Right now, we add each one in the same main.py. There's something about the chroma client that gets reset and so doesn't put it in the same spot. 