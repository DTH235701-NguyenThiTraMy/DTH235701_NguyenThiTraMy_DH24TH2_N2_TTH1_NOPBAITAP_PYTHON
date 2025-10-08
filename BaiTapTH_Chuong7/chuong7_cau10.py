import json
import os

FILENAME = "sinhvien.json"

def save_to_file(data):
    with open(FILENAME, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print("Đã lưu dữ liệu vào file JSON.")

def load_from_file():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def them_sv(ds):
    ma = input("Nhập mã sinh viên: ")
    ten = input("Nhập tên sinh viên: ")
    namsinh = input("Nhập năm sinh: ")
    malop = input("Nhập mã lớp: ")
    ds.append({"ma": ma, "ten": ten, "namsinh": namsinh, "malop": malop})
    print("Đã thêm sinh viên.")

def sua_sv(ds):
    ma = input("Nhập mã sinh viên cần sửa: ")
    for sv in ds:
        if sv["ma"] == ma:
            sv["ten"] = input("Tên mới (Enter để giữ nguyên): ") or sv["ten"]
            sv["namsinh"] = input("Năm sinh mới (Enter để giữ nguyên): ") or sv["namsinh"]
            sv["malop"] = input("Mã lớp mới (Enter để giữ nguyên): ") or sv["malop"]
            print("Đã cập nhật thông tin sinh viên.")
            return
    print("Không tìm thấy sinh viên.")

def xoa_sv(ds):
    ma = input("Nhập mã sinh viên cần xóa: ")
    for sv in ds:
        if sv["ma"] == ma:
            ds.remove(sv)
            print("Đã xóa sinh viên.")
            return
    print("Không tìm thấy sinh viên.")

def tim_sv(ds):
    kw = input("Nhập tên hoặc mã sinh viên cần tìm: ").lower()
    found = [sv for sv in ds if kw in sv["ten"].lower() or kw in sv["ma"].lower()]
    if found:
        for sv in found:
            print(sv)
    else:
        print("Không tìm thấy sinh viên.")

def sapxep_sv(ds):
    ds.sort(key=lambda x: x["ten"].lower())
    print("Đã sắp xếp danh sách theo tên.")

def xem_ds(ds):
    print("\nDanh sách sinh viên:")
    for sv in ds:
        print(f"{sv['ma']} - {sv['ten']} - {sv['namsinh']} - {sv['malop']}")

def main():
    ds = load_from_file()
    while True:
        print("\n=== MENU QUẢN LÝ SINH VIÊN ===")
        print("1. Thêm sinh viên")
        print("2. Sửa sinh viên")
        print("3. Xóa sinh viên")
        print("4. Tìm kiếm sinh viên")
        print("5. Sắp xếp sinh viên")
        print("6. Xem danh sách")
        print("7. Lưu file JSON")
        print("8. Thoát")
        chon = input("Chọn chức năng (1-8): ")

        if chon == "1": them_sv(ds)
        elif chon == "2": sua_sv(ds)
        elif chon == "3": xoa_sv(ds)
        elif chon == "4": tim_sv(ds)
        elif chon == "5": sapxep_sv(ds)
        elif chon == "6": xem_ds(ds)
        elif chon == "7": save_to_file(ds)
        elif chon == "8":
            print("Kết thúc chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ.")

if __name__ == "__main__":
    main()
