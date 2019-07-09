# theGuardianNews 
This is a Scrapy project to scrape news from https://www.theguardian.com/ (英国卫报).

This project uses **Mongodb** as database.

## Extracted data
This project extracts news, combined with title, time, category, tags and content. The extracted data looks like this sample:<br />
{<br />
&emsp;"title": "Indonesia: 193m people, 17,000 islands, one big election. Here's what you need to know", <br />
&emsp;"time": "Mon 15 Apr 2019 ", <br />
&emsp;"category": "World", <br />
&emsp;"tags": "Indonesia,Asia Pacific,Joko Widodo,explainers", <br />
&emsp;"content": "A nation made up of 17,000 islands ..."<br />
}

## Spiders
This project contains two spiders and you can list them using the list command:

`$ scrapy list`

> news

You can learn more about the spiders by going through [my blog]('https://stardust567.github.io/post/b2a.html').

## Running the spiders
You can run a spider using the scrapy crawl command, such as:

`$ scrapy crawl news`

