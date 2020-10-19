
<h1>Web-Scrapping-using-scrapy(Python)</h1>

<p>Web scraping has become an effective way of extracting information from the web for decision making and analysis. 
It has become an essential part of the data science toolkit. Data scientists should know how to gather data from web pages and store that data in different formats for further analysis.
Scrapy is a Python framework for web scraping that provides a complete package for developers without worrying about maintaining code.</p>

<h2>Creating a Scrapy project and Custom Spider</h2>
<p>Web scraping can be used to make an aggregator that you can use to compare data. For example, you want to buy a tablet, and you want to compare products and prices together you can crawl your desired pages and store in an excel file. Here you will be scraping aliexpress.com for tablets information.

Now, you will create a custom spider for the same page. First, you need to create a Scrapy project in which your code and results will be stored. Write the following command in the command line or anaconda prompt.</p>

<b>scrapy startproject simple_crawler</b>

This will create a hidden folder in your default python or anaconda installation. simple_crawler will be the name of the folder. You can give any name.



<p>Here I scraped  data for all products from the men's shoes section using Python from  https://matchesfashion.com . The data  collected is  for Germany (Deutschland).
The output is in the  .csv file with the following column headers.
<ul>
 <li>Name: the name or the title of the product</li>
 <li>Brand: the brand name of the product</li>
 <li>Price: the price of the product</li>
 <li>Image Url: the url of the product image</li>
 <li>Product Url: the url of the product page</li>
 </ul>
 We can scrape more data if we want to from the website.
 Scrapy handles all the heavy load of coding for you, from creating project files and folders till handling duplicate URLs it helps you get heavy-power web scraping in minutes and provides you support for all common data formats that you can further input in other programs.
 This project will surely help you understand Scrapy and its framework and what you can do with it. To become a master in Scrapy, you will need to go through all the fantastic functionalities it has to provide, but this tutorial has made you capable of scraping groups of web pages in an efficient way.</p>
