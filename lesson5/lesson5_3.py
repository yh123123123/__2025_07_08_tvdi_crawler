import asyncio
from crawl4ai import AsyncWebCrawler

async def main():
    #建立一個AsyncWebCrawler的實體
    async with AsyncWebCrawler() as crawler:
        #Run the crawler on a URL
        url='https://blockcast.it/2025/07/21/eths-most-hated-rally-could-trigger-331m-in-liquidations/'
        result = await crawler.arun(url=url)
        print(type(result))  #列印結果物件
        print("="*60)
        #result = await crawler.arun(url='https://crawl4ai.com', mode='markdown')
        #列印結果物件
        #列印取出的HTML內容
        #列印取出的結果
        # 列印抓取結果
        
        print(result.markdown)
        print("Markdown length:", len(result.markdown))
        #print(result.raw_markdown[:200])


#執行asyncio.run()
if __name__ == "__main__":
    asyncio.run(main())
#await main()