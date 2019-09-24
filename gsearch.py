import requests


def main():
    # 目標:　フリーワード検索の結果上位５件における必要情報を出力する
    # フォーマット　店名,URL,路線名駅名
    API_KEY = ''
    payload = {'keyid': API_KEY, 'freeword': 'ワイン', 'hit_per_page': 5}

    # ワイン -> 店名　URL
    url = 'https://api.gnavi.co.jp/RestSearchAPI/v3/'

    response = requests.get(url, params=payload)

    rest_list = response.json()['rest']

    for restaurant in rest_list:
        name = restaurant['name']
        rest_url = restaurant['url']
        line = restaurant['access']['line']
        station = restaurant['access']['station']

        print(f'{name},{rest_url},{line}{station}')


if __name__ == '__main__':
    main()
