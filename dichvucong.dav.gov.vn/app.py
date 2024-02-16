import requests
import csv
import json

def thuoc():
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
                str(item['soDangKy']), 
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

        print('Có ' + str(len(data) - 1) + ' dữ liệu')
        print(f'Tệp CSV đã được ghi tại: {csv_file_path}')

        print(f"Data written to {csv_file_path}")
    else:
        print(f"Request failed with status code: {response.status_code}")
        print(response.text)

def nguyen_lieu():
    url = "https://dichvucong.dav.gov.vn/api/services/app/soDangKy/GetAllPublicServerPaging"

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
        "x-xsrf-token": "6na7gCt_GM0yO7Qiv80SmWT1L0OEXP0TCKc5OAELQJm1WoJ9zZ6dT6QO6AJTNrrMiklT7jG0v9a2ZU_tou5S7DB4Ihw__QyR79AOxiDGO1c1"
    }

    data = {
        "SoDangKyThuoc": {},
        "KichHoat": True,
        "skipCount": 0,
        "maxResultCount": 200000,
        "sorting": None
    }

    # Thực hiện yêu cầu POST
    response = requests.post(url, json=data, headers=headers, cookies={"Cookie": "your_cookie_here"}, verify=False)

    # Kiểm tra nếu yêu cầu thành công (status code 200)
    if response.status_code == 200:
        # Phân tích cú pháp JSON response
        json_data = response.json()

        header = ['SỐ GPLH', 'Ngày hết hạn', 'Tên thuốc', 'HOẠT CHẤT', 'HÀM LƯỢNG',
                  'SỐ QUYẾT ĐỊNH', 'NĂM CẤP', 'ĐỢT CẤP', 'DẠNG BÀO CHẾ', 'QUY CÁCH ĐÓNG GÓI',
                  'TIÊU CHUẨN', 'TUỔI THỌ', 'TÊN CÔNG TY', 'NƯỚC', 'ĐỊA CHỈ', 'TÊN CÔNG TY', 'NƯỚC', 'ĐỊA CHỈ',
                  'TÀI LIỆU']
        data = [header]

        for item in json_data['result']['items']:
            row = [
                str(item['soDangKy']),
                item['thongTinDangKyThuoc']['ngayHetHanSoDangKy'],
                item['tenThuoc'],
                item['thongTinThuocCoBan']['hoatChatChinh'],
                item['thongTinThuocCoBan']['hamLuong'],
                item['thongTinDangKyThuoc']['soQuyetDinh'],
                item['thongTinDangKyThuoc']['ngayCapSoDangKy'],
                item['thongTinDangKyThuoc']['dotCap'],
                item['thongTinThuocCoBan']['dangBaoChe'],
                item['thongTinThuocCoBan']['dongGoi'],
                item['thongTinThuocCoBan']['tieuChuan'],
                item['thongTinThuocCoBan']['tuoiTho'],
                item['congTyDangKy']['tenCongTyDangKy'],
                item['congTyDangKy']['nuocDangKy'],
                item['congTyDangKy']['diaChiDangKy'],
                item['congTySanXuat']['tenCongTySanXuat'],
                item['congTySanXuat']['nuocSanXuat'],
                item['congTySanXuat']['diaChiSanXuat'],
                'https://dichvucong.dav.gov.vn/ViewTaiLieu/Index?SoDangKyId=' + str(item['id']),
            ]
            data.append(row)

        csv_file_path = 'nguyenlieu.csv'

        # Write data to CSV file
        # Mở tệp CSV để ghi (nếu tệp không tồn tại, nó sẽ được tạo mới)
        with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
            # Tạo một đối tượng CSV writer
            csv_writer = csv.writer(csv_file)

            # Ghi dữ liệu vào tệp CSV với header
            csv_writer.writerows(data)
        print('Có ' + str(len(data) - 1) + ' dữ liệu')
        print(f'Tệp CSV đã được ghi tại: {csv_file_path}')

        print(f"Data written to {csv_file_path}")
    else:
        print(f"Request failed with status code: {response.status_code}")
        print(response.text)

def congbotaduocvonang():
    url = "https://dichvucong.dav.gov.vn/api/services/app/congBoTaDuocVoNang/getAllServerPaging"

    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "vi,en-US;q=0.9,en;q=0.8",
        "content-type": "application/json;charset=UTF-8",
        "sec-ch-ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"YaBrowser\";v=\"24.1\", \"Yowser\";v=\"2.5\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "x-requested-with": "XMLHttpRequest",
        "x-xsrf-token": "nQfvmy6ai7ofMlH5BA-NhQw0aVV_GetzbMBh4yGI9DXUoitytnEYFT0uLd1WM29-yrNx7wiQYNOpGWXzkDP8w83cdksQvmGsIyFUR_TLU801"
    }

    data = {
        "keyword": None,
        "filterByIsActive": True,
        "skipCount": 0,
        "maxResultCount": 200000,
        "sorting": None
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        # Xử lý dữ liệu ở đây, ví dụ:
        json_data = response.json()

        header = ['SỐ ĐĂNG KÝ LƯU HÀNH', 'NGÀY HẾT HIỆU LỰC SỐ ĐĂNG KÝ', 'TÊN TÁ DƯỢC, VỎ NANG'
                  'TÊN CƠ SỞ SẢN XUẤT', 'NƯỚC SẢN XUẤT', 'TIÊU CHUẨN CHẤT LƯỢNG']
        data = [header]

        for item in json_data['result']['items']:
            row = [
                item['soDangKyLuuHanh'],
                item['ngayHetHieuLucSDK'],
                item['tenTaDuocVoNang'],
                item['tenCoSoSanXuat'],
                item['nuocSanXuat'],
                item['tieuChuanChatLuong'],
            ]
            data.append(row)

        csv_file_path = 'congbotaduocvonang.csv'

        # Write data to CSV file
        # Mở tệp CSV để ghi (nếu tệp không tồn tại, nó sẽ được tạo mới)
        with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
            # Tạo một đối tượng CSV writer
            csv_writer = csv.writer(csv_file)

            # Ghi dữ liệu vào tệp CSV với header
            csv_writer.writerows(data)
        print('Có ' + str(len(data) - 1) + ' dữ liệu')
        print(f'Tệp CSV đã được ghi tại: {csv_file_path}')

        print(f"Data written to {csv_file_path}")
    else:
        print("Yêu cầu không thành công. Mã trạng thái:", response.status_code)



if __name__ == "__main__":
    thuoc()
    nguyen_lieu()
    congbotaduocvonang()
