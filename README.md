# Mission-to-Mars
## Background
Robin, who loves astrology and wants to work for NASA one day, has decided to use a specific method of gathering the latest data: web scraping. Using this technique, she has the ability to pull data from multiple websites, store it in a database, then present the collected data in a central location: a webpage.
## Challenge
Robin’s web app is looking good and functioning well, but she wanted to add more polish to it. She had been admiring images of Mars’ hemispheres and realized that the site is scraping-friendly. She would like to adjust the current web app to include all four of the hemispheres images. This requires additional scraping code to pull the high-resolution images, updating Mongo to include the new data, and altering the design of her web app to accommodate these images.
## Resources
1. Splinter
2. Beautiful Soup
3. MongoDB
4. Flask
5. Chromedriver
6. HTML
## Instructions
1. Visit the Mars Hemispheres (Links to an external site.) web site to view the hemisphere images and use DevTools to find the proper elements to scrape.
2. Obtain high-resolution images for each of Mars's hemispheres.
3. Save both the image URL string (for the full-resolution image) and the hemisphere title (with the name).
4. Use a Python dictionary to store the data using the keys `img_url` and `title.`
5. Append the dictionary with the image URL string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.

