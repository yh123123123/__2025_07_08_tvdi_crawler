import asyncio
from crawl4ai import AsyncWebCrawler,CrawlerRunConfig,CacheMode
from crawl4ai.extraction_strategy import JsonCssExtractionStrategy
import json

def process_data(datas):
    for item in datas:
        print(item)

async def main():
    
    url = 'https://rate.bot.com.tw/xrt?Lang=zh-TW'
    schema = {
        "name":"台幣匯率",
        "baseSelector": "table[title='牌告匯率'] tr",
        #"baseSelector": "#ie11andabove > div > table > tbody > tr",
        "fields":[
            {
                "name": "幣別",
                "selector": 'td[data-table="幣別"] div.hidden-phone.print_show.xrt-cur-indent',
                "type":"text"
            },
            {
                "name":"現金匯率_本行買入",
                "selector":'[data-table="本行現金買入"]',
                "type":"text"
            },
            {
                "name":"現金匯率_本行賣出",
                "selector":'[data-table="本行現金賣出"]',
                "type":"text"
            },
            {
                "name":"即期匯率_本行買入",
                "selector":'[data-table="本行即期買入"]',
                "type":"text"
            },
            {
                "name":"即期匯率_本行賣出",
                "selector":'[data-table="本行即期賣出"]',
                "type":"text"
            }
        ]
    }

    #CrawlerRunConfig實體
    run_config = CrawlerRunConfig(
        cache_mode = CacheMode.BYPASS,
        extraction_strategy=JsonCssExtractionStrategy(schema=schema)
    )

    #建立一個AsyncWebCrawler的實體
    async with AsyncWebCrawler() as crawler:
        #Run the crawler on a URL
        result = await crawler.arun(
            url=url,
            config=run_config
        )
        #print(type(result.extracted_content)) 
        #print(result.extracted_content)
        datas=json.loads(result.extracted_content)
        process_data(datas)

        
        

if __name__ == "__main__":
    asyncio.run(main())