import asyncio
from crawl4ai import (AsyncWebCrawler,
                      CrawlerRunConfig,
                      DefaultMarkdownGenerator,
                      PruningContentFilter)

async def main():
    #建立爬蟲執行的設定配置
    run_config = CrawlerRunConfig(
        markdown_generator=DefaultMarkdownGenerator(
            content_filter = PruningContentFilter(
                threshold = 0.6,  # 提高閾值，更嚴格的過濾
                threshold_type = "fixed",
                min_word_threshold = 50  # 最少字數要求
            )
        ),
 
        # 移除不必要的元素
        excluded_tags=['nav', 'footer', 'header', 'aside', 'form'],
        # 專門針對文章內容的CSS選擇器（可選）
        css_selector='article, .content, .post-content, .entry-content, main'
    )

    #建立一個AsyncWebCrawler的實體
    async with AsyncWebCrawler() as crawler:
        url = 'https://blockcast.it/2025/07/21/eths-most-hated-rally-could-trigger-331m-in-liquidations/'
        output_file = 'result.md'

        try:
            result = await crawler.arun(
                url=url,
                config=run_config,
                output_filename=output_file  # 這只是參數，不會自動存檔！
            )
        except Exception as e:
            print(f"❌ 爬蟲執行錯誤：{e}")
            return

        if result and result.markdown:
            print("✅ 擷取成功，儲存中...")
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(result.markdown)
            print(f"✅ Markdown 已儲存至 {output_file}")
            print("Markdown 頭部預覽：\n", result.markdown[:300])
        else:
            print("⚠️ 沒有擷取到有效內容。")
        #print(type(result))  #列印結果物件
        #print("="*60)
        #result = await crawler.arun(url='https://crawl4ai.com', mode='markdown')
        #列印結果物件
        #列印取出的HTML內容
        #列印取出的結果
        # 列印抓取結果
        
        print(result.markdown)
        print("Markdown length:", len(result.markdown))
        #print(f"結果已儲存至 {output_file}")
        #print(result.raw_markdown[:200])


#執行asyncio.run()
if __name__ == "__main__":
    asyncio.run(main())
#await main()