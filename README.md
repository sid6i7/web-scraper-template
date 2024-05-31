# Source
Following steps and ideas are from [Jovian](https://jovian.com/).

https://jovian.ai/aakashns/python-web-scraping-project-guide

Do checkout their courses!

# Web Scraping
Web scraping is the process of extracting and parsing data from websites in an automated fashion using a computer program. It's a useful technique for creating datasets for research and learning.

# Steps to Build a Web Scraper
1. **Pick a website and describe your objective**

    - Browse through different sites and pick on to scrape. Check the "Project Ideas" section for inspiration.
    - Identify the information you'd like to scrape from the site. Decide the format of the output CSV file.
    - Summarize your project idea and outline your strategy in a Juptyer notebook. Use the "New" button above.


2. **Use the requests library to download web pages**

    - Inspect the website's HTML source and identify the right URLs to download.
    - Download and save web pages locally using the `requests` library.
    - Create a function to automate downloading for different topics/search queries.


3. **Use Beautiful Soup to parse and extract information**

    - Parse and explore the structure of downloaded web pages using Beautiful soup.
    - Use the right properties and methods to extract the required information.
    - Create functions to extract from the page into lists and dictionaries.
    - (Optional) Use a REST API to acquire additional information if required.


4. **Create CSV file(s) with the extracted information**

    - Create functions for the end-to-end process of downloading, parsing, and saving CSVs.
    - Execute the function with different inputs to create a dataset of CSV files.
    - Verify the information in the CSV files by reading them back using [Pandas](https://pandas.pydata.org).


5. **Document and share your work**

    - Add proper headings and documentation in your Jupyter notebook.

# Project Ideas
1. **Dataset of Books (Amazon)**: Create a dataset of popular books in different genres by scraping the site: https://www.amazon.in/gp/bestsellers/books/ 


2. **Dataset of Quotes (BrainyQuote)**: Create a dataset of quotes for different tags/topics by scraping the site :https://www.brainyquote.com/topics


3. **Dataset of Movies (TMDb)**: The Movie Database (TMDb) contains information about thousands of movies from around the world: https://www.themoviedb.org/movie . Can you scape the site to create a dataset of movies containing information like title, release date, cast, etc. ? You can also create datasets of movie actors/actresses/directors using this site.


4. **Dataset of TV Shows (TMDb)**: The Movie Database (TMDb) contains information about thousands of TV shows from around the world: https://www.themoviedb.org/tv . Can you scape the site to create a dataset of TV shows containing information like title, release date, cast, crew, etc. ? You can also create datasets of TV actors/actresses/directors using this site.


5. **Collections of Popular Repositories (GitHub)**: Scape GitHub collections ( https://github.com/collections ) to create a dataset of popular repositories organized by different use cases.


6. **Dataset of Books (BooksToScrape)**: Create a dataset of popular books in different genres by scraping the site *Books To Scrape*: http://books.toscrape.com


7. **Dataset of Quotes (QuotesToScrape)**: Create a dataset of popular quotes for different tags by scraping the site *Quotes To Scrape*: http://quotes.toscrape.com


8. **Scrape a User's Repositories (GitHub)**: Given someone's GitHub username, can you scrape their GitHub profile to create a list of their repositories with information like repository name, no. of stars, no. of forks, etc.?


9. **Scrape User's Reviews (ConsumerAffairs)**: Consumeraffairs contains reviews about thousands of brands: https://www.consumeraffairs.com/. Can you scrape any category from the site to create a dataset of Reviews containing information like Title, Rating, Reviews and toll-free number etc.?


10. **Songs Dataset (AZLyrics)**: Create a dataset of songs by scraping AZLyrics: https://www.azlyrics.com/f.html . Capture information like song title, artist name, year of release and lyrics URL. 


11. **Scrape a Popular Blog**: Create a dataset of blog posts on a popular blog e.g. https://m.signalvnoise.com/search/ . The dataset can contain information like the blog title, published date, tags, author, link to blog post, etc.


12. **Weekly Top Songs (Top 40 Weekly)**: Create a dataset of the top 40 songs of each week in a given year by scraping the site https://top40weekly.com . Capture information like song title, artist, weekly rank, etc.


**NOTE**: Websites with dynamic content cannot be scraped using BeautifulSoup. One way to scrape dynamic website is by using Selenium.