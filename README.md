This repo contains the code of the Trawler project web app. Here's an overview of the project.

# Trawler project overview

Reddit is a social news aggregation and discussion website among the most visited in the U.S and internationally according to [1]. Reddit’s areas of interests, called “subreddits”, like “WallStreetBets” and “Stocks” where participants post to discuss stock and option trading have become notoriously influential in the trading market, see [2]. The Trawler project looks to take these subreddits mentions of individual stocks and the stock market historical data to visualize reddit influence in the stock market.

A web scrapping script is used to scrape the text content of posts on WallStreetBets and Stocks subreddits, then an NLP script runs to count individual stocks mentions. The counts of the individual stock are then stored in the main database. In the same workflow Alpha Vintage API is contacted to obtained the stock market current stock information, which is stored in the same database. This data in combination with historical data from the subreddits is used to feed a Machine Learning script. A web app is used to connect to the main database and use the scripts results. The frontend of this web app consists on a webpage displaying data visualizations in the form of a table and a graph.


# Web app overview

The web app portion of the Trawler project resides in a remote server, it communicates to Siren through a remote connection to Siren’s MySql database. The webapp was designed as a Monolithic CRUD application.
Flask was chosen as the framework of the web app which is a lightweight and customizable solution for the requirements. A MVC (Model-View-Controller) architecture was used.

The models are created with the help of the SqlAlchemy package which acts as a ORM. In this case the models created are the Trawler and Predictions database tables. To be able to access the MySQL database remotely the PyMySQL package was used. The ApScheduler Python package was used to create a CRON job to create the json files used to populate the frontend. The views are part of the frontend which were developed using HTML, CSS and Javascript with the help of the Bootstrap and Plotly libraries. 
The backend of the application connects to the MySql database through a remote connection, the only operation performed is read.

The Web App starts with a Scheduler that runs daily. A function is called to connect to the remote MySQL database and query the data needed into Python objects that are used to get the table, graph and prediction data. This data is writing to 3 JSON files. 

Each time a client connects to the webpage the backend serves the frontend the previously mentioned 3 JSON files, then the JavaScript script uses the JSON files to create the table, the graph and the predictions elements of the webpage. These elements are created with the help of Bootstrap and the Plotly libraries.

The webpage consists of 3 main elements, these elements use the data from the JSON files. The first element is a table that displays 10 rows that represents unique stocks and columns that represent the Trawler table columns except the date column. The table is ordered by Mentions, meaning that the rows shown are the top 10 stocks by mentions. If the client selects any other column the table displays the top ten ordered by the selected columns value. 
The second element is a graph, this graph displays a time series of the last 6 months of the currently selected row in the table element. The time series x-axis is the date and the y-axis are the mentions and volume columns of that particular stock. 

The third element is a prediction section, in here the predictions JSON file data is displayed. In this case the volume prediction and volume confidence are used from the Predictions database table. When the prediction is 0, a red down arrow is displayed with a message saying that the stock value is predicted to go down with the respective confidence. When the prediction is 1 it displays a horizontal yellow line and a message that says that the stock value is predicted to stay the same with the respective confidence. When the prediction is 2 it displays a green upward arrow and a message saying that the stock is predicted to go up with the respective confidence.





