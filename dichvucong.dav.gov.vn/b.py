import csv

# Dữ liệu mẫu
data = [
    ["SỐ GPLH", "NGÀY HẾT HẠN", "Tên nguyên liệu"],
    ["VD3-121-21", "2024-06-03T00:00:00+07:00", "Trazodone hydrochloride"],
    ["VD-28878-18", "2023-02-22T00:00:00+07:00", "Linezolid"],
    ["VD-31303-18", "2023-08-10T00:00:00+07:00", "Potassium Guaiacolsulfonate"],
    ["VD-16959-12", "2020-02-27T00:00:00+07:00", "Ascorbic acid 95% granulation"],
    ["VD-16959-12", "2020-02-27T00:00:00+07:00", "Ascorbic acid 95% granulation"]
]

# Tên file CSV
csv_file_path = "du_lieu_mau.csv"

# Ghi dữ liệu vào file CSV
with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    
    # Ghi dữ liệu vào file
    writer.writerows(data)

print(f"File CSV đã được tạo: {csv_file_path}")
