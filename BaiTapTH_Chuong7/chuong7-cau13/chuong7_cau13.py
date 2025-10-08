from xml.dom.minidom import parse

# Đọc danh sách nhóm thiết bị
def doc_nhom_thiet_bi():
    tree = parse("nhomthietbi.xml")
    root = tree.documentElement
    nhoms = root.getElementsByTagName("nhom")
    ds_nhom = []
    for n in nhoms:
        ma = n.getElementsByTagName("ma")[0].childNodes[0].data
        ten = n.getElementsByTagName("ten")[0].childNodes[0].data
        ds_nhom.append({"ma": ma, "ten": ten})
    return ds_nhom

# Đọc danh sách thiết bị
def doc_thiet_bi():
    tree = parse("ThietBi.xml")
    root = tree.documentElement
    tbs = root.getElementsByTagName("thietbi")
    ds_tb = []
    for tb in tbs:
        manhom = tb.getAttribute("manhom")
        ma = tb.getElementsByTagName("ma")[0].childNodes[0].data
        ten = tb.getElementsByTagName("ten")[0].childNodes[0].data
        ds_tb.append({"manhom": manhom, "ma": ma, "ten": ten})
    return ds_tb

# Hiển thị danh sách nhóm thiết bị
def hien_thi_nhom():
    ds_nhom = doc_nhom_thiet_bi()
    print("\n--- DANH SÁCH NHÓM THIẾT BỊ ---")
    for n in ds_nhom:
        print(f"Mã: {n['ma']}\tTên: {n['ten']}")

# Hiển thị toàn bộ thiết bị
def hien_thi_thiet_bi():
    ds_tb = doc_thiet_bi()
    print("\n--- DANH SÁCH THIẾT BỊ ---")
    for tb in ds_tb:
        print(f"Mã: {tb['ma']}\tTên: {tb['ten']}\tThuộc nhóm: {tb['manhom']}")

# Lọc thiết bị theo nhóm
def loc_theo_nhom():
    manhom = input("\nNhập mã nhóm cần lọc (vd: n1, n2, n3): ")
    ds_tb = doc_thiet_bi()
    print(f"\n--- DANH SÁCH THIẾT BỊ THUỘC NHÓM {manhom} ---")
    found = False
    for tb in ds_tb:
        if tb["manhom"] == manhom:
            print(f"{tb['ma']} - {tb['ten']}")
            found = True
    if not found:
        print("Không có thiết bị nào thuộc nhóm này.")

# Tìm nhóm có nhiều thiết bị nhất
def nhom_nhieu_thiet_bi():
    ds_tb = doc_thiet_bi()
    thong_ke = {}
    for tb in ds_tb:
        manhom = tb["manhom"]
        thong_ke[manhom] = thong_ke.get(manhom, 0) + 1
    max_sl = max(thong_ke.values())
    print("\n--- NHÓM CÓ NHIỀU THIẾT BỊ NHẤT ---")
    for nhom, sl in thong_ke.items():
        if sl == max_sl:
            print(f"Nhóm {nhom} có {sl} thiết bị")

# Menu chương trình
def main():
    while True:
        print("\n===== QUẢN LÝ THIẾT BỊ (XML) =====")
        print("1. Hiển thị danh sách nhóm thiết bị")
        print("2. Hiển thị toàn bộ thiết bị")
        print("3. Lọc thiết bị theo nhóm")
        print("4. Xuất nhóm có nhiều thiết bị nhất")
        print("0. Thoát")

        chon = input("Chọn chức năng: ")
        if chon == "1":
            hien_thi_nhom()
        elif chon == "2":
            hien_thi_thiet_bi()
        elif chon == "3":
            loc_theo_nhom()
        elif chon == "4":
            nhom_nhieu_thiet_bi()
        elif chon == "0":
            print("Kết thúc chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    main()