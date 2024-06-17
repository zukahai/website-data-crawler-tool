import requests
import csv

def call_api(page):
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
        "page": page,
        "per_page": 10,
        "lang": 2
    }


    response = requests.post(url, headers=headers, json=data, cookies={"referrer": referrer})

    # Print the response
    rp = response.json()['data']['list']['data']
    totalPage = response.json()['data']['list']['last_page'];
    isEnd = False if totalPage != page else True
    print(f"Page {page} / {totalPage}  done")
    return [rp, isEnd]
header = ['id', 'title', 'title_py', 'title_en', 'product_info', 'product_info_en', 'group_id', 'group_session_id', 'category_id', 'cur_category_name_en', 'cur_category_name', 'hall_id', 'cur_hall_name', 'area_id', 'area', 'area_en', 'cur_area_name', 'logo', 'bg_cover', 'pos_no', 'addr', 'desc', 'sort', 'delete_time', 'create_time', 'update_time', 'hsort']
data = [header]

for page in range(1, 100):
    rp = call_api(page)
    if rp[1]:
        break
    for item in rp:
        print(item)
        row = [
            item['id'],
            item['title'],
            item['title_py'],
            item['title_en'],
            item['product_info'],
            item['product_info_en'],
            item['group_id'],
            item['group_session_id'],
            item['category_id'],
            item['cur_category_name_en'],
            item['cur_category_name'],
            item['hall_id'],
            item['cur_hall_name'],
            item['area_id'],
            item['area'],
            item['area_en'],
            item['cur_area_name'],
            item['logo'],
            item['bg_cover'],
            item['pos_no'],
            item['addr'],
            item['desc'],
            item['sort'],
            item['delete_time'],
            item['create_time'],
            item['update_time'],
            item['sort']
        ]
        data.append(row)
    print(f"Page {page} done")
    


csv_file_path = 'exhibitorlist.imsinoexpo.cn.csv'

# Write data to CSV file
# Mở tệp CSV để ghi (nếu tệp không tồn tại, nó sẽ được tạo mới)
with open(csv_file_path, 'w', newline='', encoding='utf-8-sig') as csv_file:
    # Tạo một đối tượng CSV writer
    csv_writer = csv.writer(csv_file)

    # Ghi dữ liệu vào tệp CSV với header
    csv_writer.writerows(data)

print('Có ' + str(len(data) - 1) + ' dữ liệu')
print(f'Tệp CSV đã được ghi tại: {csv_file_path}')

print(f"Data written to {csv_file_path}")