import asyncio
from crawl4ai import AsyncWebCrawler,BrowserConfig

async def main():
    url='https://www.wantgoo.com/stock/2330/technical-chart'

    browser_config = BrowserConfig(
        headless=False, 
    )   
    
    async with AsyncWebCrawler(config=browser_config) as crawler:
        
        result = await crawler.arun(
            url=url,
        )
        print(result.markdown) 

if __name__ == "__main__":
    asyncio.run(main())