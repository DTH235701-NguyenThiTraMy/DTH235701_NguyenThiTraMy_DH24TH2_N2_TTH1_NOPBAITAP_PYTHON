import csv
import random

FILENAME = "dulieu_ngau_nhien.csv"

# Hàm 1: Tạo file CSV gồm 10 dòng, mỗi dòng 10 số ngẫu nhiên cách nhau bằng dấu ";"
def tao_file_csv():
    with open(FILENAME, mode="w", newline="") as file:
        writer = csv.writer(file, delimiter=';')
        for _ in range(10):
            dong = [random.randint(1, 100) for _ in range(10)]
            writer.writerow(dong)
    print(f"✅ Đã tạo file {FILENAME} với 10 dòng dữ liệu ngẫu nhiên.")

# Hàm 2: Đọc file CSV và xuất tổng giá trị của mỗi dòng
def doc_va_tinh_tong():
    try:
        with open(FILENAME, mode="r") as file:
            reader = csv.reader(file, delimiter=';')
            print("\n📄 Tổng giá trị các phần tử trên mỗi dòng:")
            for i, row in enumerate(reader, start=1):
                so = [int(x) for x in row if x.strip() != ""]
                print(f"Dòng {i}: {so} → Tổng = {sum(so)}")
    except FileNotFoundError:
        print("⚠️ File chưa tồn tại, vui lòng tạo trước!")

# --- Chương trình chính ---
def main():
    while True:
        print("\n=== CHƯƠNG TRÌNH XỬ LÝ CSV FILE ===")
        print("1. Tạo file CSV ngẫu nhiên (10 dòng, 10 số)")
        print("2. Đọc file CSV và tính tổng từng dòng")
        print("3. Thoát")
        chon = input("Chọn chức năng (1-3): ")

        if chon == "1":
            tao_file_csv()
        elif chon == "2":
            doc_va_tinh_tong()
        elif chon == "3":
            print("Kết thúc chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    main()
