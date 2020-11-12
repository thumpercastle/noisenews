import scrapy
from ..items import NoisenewsItem

# TODO: Develop this spider to grab more items from the page. It only grabs a handful at the moment.

class BBCSpider(scrapy.Spider):

    name = "bbcspider"
    start_urls = [
        "https://www.bbc.co.uk/news/science_and_environment",
        "https://www.bbc.co.uk/news/technology",
        "https://www.bbc.co.uk/news/entertainment_and_arts"
    ]

    def parse(self, response):

        items = NoisenewsItem()
        # Note this is not scraping all items, but just the static items at the top of the news page.
        headline = response.xpath("//h3[contains(@class, 'gs-c-promo-heading')]/text()").getall()
        subheading = response.xpath("//p[contains(@class, 'gs-c-promo-summary')]/text()").getall()
        link_ending = response.xpath("//div/a[contains(@class, 'gs-c-promo-heading')]").css('a::attr(href)').getall()
        link = ["http://www.bbc.co.uk" + item for item in link_ending]

        for i in range(len(headline)-1):

            items["headline"] = headline[i]
            items["subheading"] = subheading[i]
            items["url"] = link[i]
            yield items