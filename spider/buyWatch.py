from json import JSONDecodeError

import requests

from datetime import datetime
from requests.adapters import HTTPAdapter
import time


def queryQuote(a, b):
    cookie = "" #登陆苹果官网后的cookie
    headers = {
        'authority': 'www.apple.com.cn',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'sec-ch-ua': '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
        'accept': '*/*',
        'x-requested-with': 'XMLHttpRequest',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.apple.com.cn/shop/buy-watch/apple-watch-nike/45mm-gps-starlight-aluminium-anthracite-black-sport-band-onesize',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
        'cookie': cookie
    }

    params = {
        'mt': 'regular',
        'option.0': 'MKNW3CH/A,ML8C3FE/A',
        'parts.0': 'Z0YQ',
        'searchNearby': True,
        'store': 'R471', #此处我用的是杭州西湖店
        '_': int(time.time())
    }
    models = [{
        "key": "Z0YQ",
        "describe": "星光色铝金属表壳；Nike 运动表带"
    }, {
        "key": "MKNC3CH/A",
        "describe": "午夜色铝金属表壳；Nike 运动表带"
    }
    ]
    for model in models:
        params['parts.0'] = model["key"]
        try:
            requestSession = requests.session()
            requestSession.mount('http://', HTTPAdapter(max_retries=3))
            requestSession.mount('https://', HTTPAdapter(max_retries=3))
            response = requestSession.get(
                'https://www.apple.com.cn/shop/fulfillment-messages', headers=headers, params=params)
        except requests.exceptions.RequestException as e:
            print(e)
            print(time.strftime('%Y-%m-%d %H:%M:%S'))
        if response.status_code != 200:
            print(f"Query failed: {response.text}")
            push(f"Query failed: {response.text}")

        try:
            response.json()
        except JSONDecodeError as e:
            print(f"JSONDecodeError!!! {e}")
            push(f"JSONDecodeError!!! {e}")

        json_data = response.json()
        # print(json.dumps(json_data, indent=4))
        stores = json_data["body"]["content"]["pickupMessage"]["stores"]
        print("\n\n\n" + "All stores quote:" + model["describe"])

        timestamp = int(time.time())
        for idx, item in enumerate(stores):
            if idx < 2:
                quote = item["partsAvailability"][model["key"]
                                                  ]["pickupSearchQuote"]
                msg = item["storeName"] + ": " + quote
                if quote != "不可取货" or timestamp % 1800 == 0:
                    print(msg)
                    msg = "GOT ⌚!!!\n" + \
                        item["storeName"] + ": " + \
                        model["describe"] + " " + quote
                    # push to tg
                    push(msg)
                else:
                    print(time.strftime('%H:%M:%S' , time.localtime(time.time()))+">>>>>>>"+msg)
                    # push(msg)


def push(text):
    tgbotWebhook = "https://api.telegram.org/bot<tg机器人的token>/sendMessage?chat_id=<tg的chat_id>&text=" + text
    try:
        requests.post(tgbotWebhook)
    except requests.exceptions.ConnectionError as e:
        print(text)
        print(e)
        print(time.strftime('%Y-%m-%d %H:%M:%S'))
        while(1):
            result = queryQuote("a", "b")


if __name__ == '__main__':
    startTime = time.time()
    while(1):
        result = queryQuote("a", "b")
