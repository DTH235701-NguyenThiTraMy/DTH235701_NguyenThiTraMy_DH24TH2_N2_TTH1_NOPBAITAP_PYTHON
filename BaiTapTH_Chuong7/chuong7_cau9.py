import os

# Đường dẫn file lưu dữ liệu
FILENAME = "products.txt"

# -các hàm lưu và đọc file-
def save_to_file(products):
    with open(FILENAME, "w", encoding="utf-8") as f:
        for p in products:
            line = f"{p['id']},{p['name']},{p['price']},{p['category']}\n"
            f.write(line)
    print("Đã lưu dữ liệu vào file!")

def load_from_file():
    products = []
    if not os.path.exists(FILENAME):
        return products
    with open(FILENAME, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split(",")
            if len(parts) == 4:
                products.append({
                    "id": parts[0],
                    "name": parts[1],
                    "price": float(parts[2]),
                    "category": parts[3]
                })
    return products

# các hàm chức năng
def add_product(products):
    id = input("Nhập mã sản phẩm: ")
    name = input("Nhập tên sản phẩm: ")
    price = float(input("Nhập đơn giá: "))
    category = input("Nhập mã danh mục: ")
    products.append({"id": id, "name": name, "price": price, "category": category})
    print("Đã thêm sản phẩm thành công!")

def edit_product(products):
    id = input("Nhập mã sản phẩm cần sửa: ")
    for p in products:
        if p["id"] == id:
            print("Sản phẩm hiện tại:", p)
            p["name"] = input("Tên mới: ") or p["name"]
            p["price"] = float(input("Giá mới: ") or p["price"])
            p["category"] = input("Danh mục mới: ") or p["category"]
            print("Đã cập nhật sản phẩm!")
            return
    print("Không tìm thấy mã sản phẩm!")

def delete_product(products):
    id = input("Nhập mã sản phẩm cần xóa: ")
    for p in products:
        if p["id"] == id:
            products.remove(p)
            print("Đã xóa sản phẩm!")
            return
    print("Không tìm thấy mã sản phẩm!")

def search_product(products):
    keyword = input("Nhập từ khóa cần tìm (tên hoặc mã): ").lower()
    found = [p for p in products if keyword in p["id"].lower() or keyword in p["name"].lower()]
    if not found:
        print("Không tìm thấy sản phẩm nào!")
    else:
        print("Kết quả tìm kiếm:")
        display_products(found)

def sort_products(products):
    print("1. Sắp xếp theo tên\n2. Sắp xếp theo giá")
    choice = input("Chọn kiểu sắp xếp: ")
    if choice == "1":
        products.sort(key=lambda x: x["name"].lower())
    elif choice == "2":
        products.sort(key=lambda x: x["price"])
    else:
        print("Lựa chọn không hợp lệ!")
    print("Đã sắp xếp danh sách!")

def display_products(products):
    print("\nDanh sách sản phẩm:")
    print("{:<10} {:<20} {:<10} {:<10}".format("Mã", "Tên", "Giá", "Danh mục"))
    print("-" * 50)
    for p in products:
        print("{:<10} {:<20} {:<10} {:<10}".format(p["id"], p["name"], p["price"], p["category"]))
    print("-" * 50)

# menu chính
def main():
    products = load_from_file()
    while True:
        print("\n=== MENU QUẢN LÝ SẢN PHẨM ===")
        print("1. Thêm sản phẩm")
        print("2. Sửa sản phẩm")
        print("3. Xóa sản phẩm")
        print("4. Tìm kiếm sản phẩm")
        print("5. Sắp xếp sản phẩm")
        print("6. Hiển thị danh sách")
        print("7. Lưu file")
        print("8. Thoát")
        choice = input("Chọn chức năng (1-8): ")

        if choice == "1":
            add_product(products)
        elif choice == "2":
            edit_product(products)
        elif choice == "3":
            delete_product(products)
        elif choice == "4":
            search_product(products)
        elif choice == "5":
            sort_products(products)
        elif choice == "6":
            display_products(products)
        elif choice == "7":
            save_to_file(products)
        elif choice == "8":
            print("Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    main()