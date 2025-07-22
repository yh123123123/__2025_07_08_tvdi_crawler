import asyncio
from crawl4ai import AsyncWebCrawler

async def main():
    #建立一個AsyncWebCrawler的實體
    async with AsyncWebCrawler() as crawler:
        #Run the crawler on a URL
        result = await crawler.arun(url='https://crawl4ai.com')
        print(result)  #列印結果物件
        print("="*60)
        #result = await crawler.arun(url='https://crawl4ai.com', mode='markdown')
        #列印結果物件
        #列印取出的HTML內容
        #列印取出的結果
        #print(result.markdown)
        print(result.markdown[:300])

#執行asyncio.run()
if __name__ == "__main__":
    asyncio.run(main())
#await main()