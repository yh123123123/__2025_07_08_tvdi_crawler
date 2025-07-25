import asyncio
from crawl4ai import AsyncWebCrawler,BrowserConfig, CacheMode,CrawlerRunConfig,JsonCssExtractionStrategy

async def main():

    url='https://www.wantgoo.com/stock/2317/technical-chart'

    browser_config = BrowserConfig(
        headless=False 
    ) 

    stock_schema = {
        "name": "StockInfo",
        "baseSelector": "main.main",  # 從整個頁面開始選擇
        "fields": [
            {
                "name":"日期時間",
                "selector":"time.last-time#lastQuoteTime",
                "type":"text"
            },
            {
                "name": "股票號碼",
                "selector": "span.astock-code[c-model='id']", # 假設股票代碼在這個選擇器下
                "type": "text"
            },
            {
                "name": "股票名稱",
                "selector": "h3.astock-name[c-model='name']",  # 假設股票名稱在這個選擇器下
                "type": "text"
            },
            {
                "name": "即時價格",
                "selector":"div.quotes-info div.deal",
                "type": "text"

            },
            {
                "name": "漲跌",
                "selector":"div.quotes-info span.chg[c-model='change']",
                "type": "text"
            },
            {
                "name": "漲跌百分比",
                "selector":"div.quotes-info span.chg-rate[c-model='changeRate']",
                "type": "text"
            },
            {
                "name": "開盤價",
                "selector":"div.quotes-info #quotesUl span[c-model-dazzle='text:open,class:openUpDn']",
                "type": "text"
            },
            {
                "name": "最高價",
                "selector":"div.quotes-info #quotesUl span[c-model-dazzle='text:high,class:highUpDn']",
                "type": "text"

            },
            {
                "name": "成交量(張)",
                "selector":"div.quotes-info #quotesUl span[c-model='volume']",
                "type": "text" 
            },
            {
                "name": "最低價",
                "selector":"div.quotes-info #quotesUl span[c-model-dazzle='text:low,class:lowUpDn']",
                "type": "text" 
            },
            {
                "name": "前一日收盤價",
                "selector":"div.quotes-info #quotesUl span[c-model='previousClose']",
                "type": "text" 
            }

        ]
    }

    run_config=CrawlerRunConfig(
        wait_for_images=True,
        scan_full_page=True,
        scroll_delay=0.5,
        #想要在class="my-drawer-toggle-btn"的元素點擊
        cache_mode=CacheMode.BYPASS,
        extraction_strategy=JsonCssExtractionStrategy(stock_schema),
        verbose=True
    )
    async with AsyncWebCrawler(config=browser_config) as crawler:
        
        result = await crawler.arun(
            url=url,
            config=run_config
        )
        #print(result.markdown)
        print(result.extracted_content)  

if __name__ == "__main__":
    asyncio.run(main())