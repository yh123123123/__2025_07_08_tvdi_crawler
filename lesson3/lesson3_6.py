import json
from pprint import pprint
import argparse

class Site:
    def __init__(self, sitename, county,aqi,pollutant, status, pm2_5,pm2_5_avg,latitude,longitude,datacreationdate):
        self.sitename = sitename
        self.county = county
        self.aqi = aqi
        self.pollutant = pollutant
        self.status = status
        self.pm2_5 = pm2_5
        self.pm2_5_avg = pm2_5_avg
        self.latitude = latitude
        self.longitude = longitude
        self.datacreationdate = datacreationdate


def parse_sites_from_json(json_file):
    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)
    site_list = []
    for sitename in data['records']:
        site = Site(
            sitename=sitename['sitename'],
            county=sitename['county'],
            aqi=sitename['aqi'],
            pollutant=sitename['pollutant'],
            status=sitename['status'],
            pm2_5=sitename['pm2.5'],
            pm2_5_avg=sitename['pm2.5_avg'],
            latitude=sitename['latitude'],
            longitude=sitename['longitude'],
            datacreationdate=sitename['datacreationdate']
        )
        site_list.append(site)
    return site_list


# --- 以下是主要修改的部分 ---

def main():
    # 1. 建立命令列參數解析器
    parser = argparse.ArgumentParser(description='依縣市名稱查詢空氣品質指標 (AQI) 資料。')
    
    # 2. 新增 --county 參數
    #    required=True 表示此為必填參數
    #    help 提供使用者操作說明
    parser.add_argument('--county', type=str, required=True, help='請輸入要查詢的縣市名稱 (例如: 臺北市, 高雄市)')
    
    # 3. 解析使用者從命令列輸入的參數
    args = parser.parse_args()
    
    # 從解析結果中取得縣市名稱
    target_county = args.county
    
    # 載入並解析所有站點資料
    try:
        sites = parse_sites_from_json('aqx_p_488.json')
    except FileNotFoundError:
        print("錯誤: 找不到 'aqx_p_488.json' 檔案。請確保此檔案與程式在同一個目錄下。")
        return # 找不到檔案就結束程式

    # 4. 過濾並顯示指定縣市的資料
    print(f"\n查詢 {target_county} 的空氣品質資料：")
    print("====================================")
    
    found_sites = []
    for site in sites:
        # 檢查站點的縣市是否符合使用者輸入的縣市
        if site.county == target_county:
            found_sites.append(site)

    if not found_sites:
        print(f"找不到縣市 '{target_county}' 的相關資料，請確認縣市名稱是否正確。")
    else:
        # 為了避免重複印出同一時間點的資料，只顯示最新的資料
        latest_data = {}
        for site in found_sites:
            # 如果站點名稱還沒紀錄，或此筆資料比已紀錄的更新，就取代它
            if site.sitename not in latest_data or site.datacreationdate > latest_data[site.sitename].datacreationdate:
                latest_data[site.sitename] = site
        
        for site in latest_data.values():
            pollutant_info = site.pollutant if site.pollutant else '無'
            print(f"站點: {site.sitename:<6} AQI: {site.aqi:<3} | 狀態: {site.status:<4} | PM2.5: {site.pm2_5:<3} | 主要污染物: {pollutant_info:<10} | 更新時間: {site.datacreationdate}")


# 確保此腳本是直接執行，而非被其他程式引用
if __name__ == '__main__':
    main()
