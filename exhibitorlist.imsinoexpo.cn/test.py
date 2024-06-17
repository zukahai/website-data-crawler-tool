import requests

url = "https://exhibitorlist.imsinoexpo.cn/front/index/index"
headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "vi,en-US;q=0.9,en;q=0.8",
    "content-type": "application/json",
    "sec-ch-ua": "\"Chromium\";v=\"122\", \"Not(A:Brand\";v=\"24\", \"YaBrowser\";v=\"24.4\", \"Yowser\";v=\"2.5\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin"
}
referrer = "https://exhibitorlist.imsinoexpo.cn/front/index.html?uri=cphipmecchina2024shanghai&session=&lan=EN"
data = {
    "uri": "cphipmecchina2024shanghai",
    "session": "",
    "keyword": "",
    "cate_id": [],
    "hall_id": [],
    "area": [],
    "page": 1,
    "per_page": 10,
    "lang": 2
}

response = requests.post(url, headers=headers, json=data, cookies={"referrer": referrer})

print(response.json())
