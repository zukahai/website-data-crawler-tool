import requests
import csv
import json

url = "https://dichvucong.dav.gov.vn/api/services/app/nguyenLieuLamThuoc/GetAllServerPaging"

headers = {
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-language": "vi,en-US;q=0.9,en;q=0.8",
    "cache-control": "no-cache",
    "content-type": "application/json",
    "expires": "Sat, 01 Jan 2000 00:00:00 GMT",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"118\", \"YaBrowser\";v=\"23.11\", \"Not=A?Brand\";v=\"99\", \"Yowser\";v=\"2.5\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "x-requested-with": "XMLHttpRequest",
    "x-xsrf-token": "Y9hConk6zCbnSaDdufevLyOJwmlB5nTSygcLdNiGbzKtR8OFPeR_q9Rjm8yL-JVT9sCHgwVv3zBI8Oc64hwHgG9TlSf0KGCc7sUXaFdWlLA1"
}

data = {
    "isActive": True,
    "ngayHetHanSoDangKyTu": None,
    "ngayHetHanSoDangKyToi": None,
    "ngayKyCongVanTu": None,
    "ngayKyCongVanToi": None,
    "skipCount": 0,
    "maxResultCount": 200000,
    "sorting": None
}

response = requests.post(url, json=data, headers=headers, cookies={"Cookie": "your_cookie_here"}, verify=False)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    json_data = response.json()

    # print(json.dumps(json_data, indent=2))

    header = ['SỐ GPLH', 'NGÀY HẾT HẠN', "Tên nguyên liệu", "PHÂN LOẠI", "TIÊU CHUẨN", 
              "CƠ SỞ SẢN XUẤT NGUYÊN LIỆU", "NƯỚC SẢN XUẤT NGUYÊN LIỆU", "ĐỊA CHỈ CƠ SỞ SẢN XUẤT NGUYÊN LIỆU", "PHẢI CẤP PHÉP NHẬP KHẨU"]
    data = [header]

    for item in json_data['result']['items']:
        row = [
            item['soDangKy'], 
            item['ngayHetHanSoDangKy'], 
            item['tenNguyenLieu'],
            item['phanLoai'],
            item['tieuChuanChatLuongNguyenLieu'],
            item['tenCoSoSanXuatNguyenLieu'],
            item['nuocSanXuatNguyenLieu'],
            item['diaChiCoSoSanXuatNguyenLieu'],
            item['isPhaiCapPhepNhapKhau'],
        ]
        data.append(row)

    csv_file_path = 'data.csv'

    # Write data to CSV file
    # Mở tệp CSV để ghi (nếu tệp không tồn tại, nó sẽ được tạo mới)
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
        # Tạo một đối tượng CSV writer
        csv_writer = csv.writer(csv_file)

        # Ghi dữ liệu vào tệp CSV với header
        csv_writer.writerows(data)

    print(f'Tệp CSV đã được ghi tại: {csv_file_path}')

       

    print(f"Data written to {csv_file_path}")
else:
    print(f"Request failed with status code: {response.status_code}")
    print(response.text)
