# import httpx
# import asyncio
# from parsel import Selector
#
#
# class AsyncScraper:
#     TARGET_URL = "https://kg.akipress.org/?from=portal&place=menu"
#     LINK_XPATH = '//div[@class="elem"]/div[@class="title"]/a/@href'
#     HEADERS = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0',
#         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
#         'Accept-Language': 'en-US,en;q=0.7,ja;q=0.3',
#         'Accept-Encoding': 'gzip, deflate, br',
#         'DNT': '1',
#         'Connection': 'keep-alive',
#         'Upgrade-Insecure-Requests': '1',
#         'Sec-Fetch-Dest': 'document',
#         'Sec-Fetch-Mode': 'navigate',
#         'Sec-Fetch-Site': 'same-site',
#         'Sec-Fetch-User': '?1',
#         'TE': 'trailers'
#     }
#
#     def __init__(self):
#         self.found_links = []
#
#     async def parse_data(self):
#         async with httpx.AsyncClient(headers=self.HEADERS) as client:
#             async for page in self.async_generator(limit=4):
#                 await self.get_url(client,
#                                    url=self.TARGET_URL.format(page=page))
#
#     async def get_url(self, client, url):
#         response = await client.get(url)
#         await self.scrape_links(content=response.text, client=client)
#
#     async def scrape_links(self, content, client):
#         tree = Selector(text=content)
#         links = tree.xpath(self.LINK_XPATH).extract()
#         for link in links:
#             if len(self.found_links) >= 4:
#                 break
#             await self.scrape_detail(client=client, link=link)
#
#         # async for link in self.async_generator_detail(links=links):
#         #     await self.scrape_detail(client=client, link=link)
#         #     print(links)
#
#     async def scrape_detail(self, client, link):
#         response = await client.get(link)
#         self.found_links.append(response.url)
#         print(response.url)
#
#     async def async_generator(self, limit):
#         for page in range(1, limit):
#             yield page
#
#     async def async_generator_detail(self, links):
#         for page in links:
#             yield page
#
#     def get_response_urls(self):
#         return self.found_links
#
# # if __name__ == "__main__":
# #     scraper = AsyncScraper()
# #     asyncio.run(scraper.parse_data())
# #     scraper.get_response_urls()