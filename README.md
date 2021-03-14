# Challenge - News Content Collect and Store

The goal of this coding challenge is to create a solution that crawls for articles from a news website, cleanses the response, stores it in a mongo database, then makes it available to search via an API.

## Frameworks/Libs used:
- Python3
- Scarpy (crawl the news websites)
- re (Regular expressions to remove HTML tags from parsed news)
- Flask (Python framework to build restful APIs)
- MongoDB Atlas (Non-SQL Database framework to store the data)


## Specifications
- At the beginning, a scrapy project has been created using "" command. This "articles" project will be the base scrapy project that can include several scarpy spiders. Each spider can be assigned to specific news website. For example, in our case here, only one spider has been created for the [theguardian.com](http://theguardian.com) website using the command "".
- Of course, we can extend the project in the future to add several spiders each one map to different news website.
- In the `parse()` function in the `TheguardianSpider()` class, we have to define how data should be parsed and cleaned.
- I used the `rss` version that is provided by `theguardian.com` instead of the default website since it will facilitate a lot while fetching, parsing and handling the data from the website. The `rss` version does not include Ads. or any unrelated items that will be take time to parse and eliminate. 
- After getting the required info like the article title, url, author, ..etc, we had to remove any of the HTML tags that might be embedded in the text. So, one of the popular and easy options in Python is the `re` library which stands to Regular Expressions. 
- After parsing and cleaning the fetched new data, we have to store them in someplace. Well, usually databases are used for such purpose. I have created a free account in [MongoDB Atlas](https://www.mongodb.com/cloud/atlas). After that, it is pretty straight forward to create a new database their.
- Returning back to the python code, in our spider, we can use `pymongo` lib which is a Python lib that is used to communicate between Python scripts and the MongoDB Atlas databases. 
- A client at the beginning has to be created by `MongoClient()` class that takes the `user_name`, `password`,  `cluster_name` and `database_name`.
- Please make sure for this step that the `user_name` and the `password` have been removed form the code and add as environment variables in the system (for security purposes), so if you intend to use the same code, please make sure to add yours.
- Finally to access those data form the database, a restful API has been created to `GET` those information. Since the  system isn't too complex, I decided to use `Flask` instead of `Django` framework for simplicity. So, a new API url has been created `http://localhost:8000/articles` which will return the data in `Json` format rendered in HTML view (just for better visualization).
- `Bouns Point`: a new rest API in Flask has been added to let the user fetch articles with specific keyword in order not read all the articles. The new API `http://127.0.0.1:8000/articles/<search_word>` for example if we want to search about `covid`, we can use `http://127.0.0.1:8000/articles/covid` url.

## Folder structure
- articles: includes the Scrapy project.
- flask_api_app: includes the Flask rest API app.
- .gitignore: git ignore file to remove unneeded files/folders from being committed by mistake.
- README: read me file that shows how the whole application is working 