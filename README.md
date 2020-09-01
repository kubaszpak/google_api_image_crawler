# google_api_image_crawler

Google image scraper with Google Search Engine API

<br>

## Description

---

<br>

Application used for scraping Images from google images after having searched a given phrase.<br>

This program uses google api, so before running it you must get your own using the link below.<br>

Get an API key here: [Custom Search JSON API](developers.google.com/custom-search/v1/introduction)

## Usage

---

<br>
Fistly run:<br><br>

        pip install google-api-python-client

After you had possesed the api_key from the Description section you should run:<br><br>

        python update_key.py {api_key}

That will update the api_key.ini config file and make the application usable. Next step is to simply run:<br><br>

        python crawler.py {searched_phrase}

If you would like to search a phrase consisting of several words use an uncderscore instead of a space.

Update:
Now you can also specify larger number of photos to download by adding a second argument like this (Note: number has to be divisible by 10):
  
  <br>



        python crawler.py {searched_phrase} {number_of_photos}

## Example

---

After running<br><br>

        python crawler.py youtube

in directory images there has been created a new directory called youtube. In the screenshot you can see the tree of this project and the first picture that popped up after running this script.<br><br>
![](git_images/youtube.png)
