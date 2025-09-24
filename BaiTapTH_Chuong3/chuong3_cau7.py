import datetime

# Nhập ngày/tháng/năm
day = int(input("Nhập ngày: "))
month = int(input("Nhập tháng: "))
year = int(input("Nhập năm: "))

try:
    today = datetime.date(year, month, day)
    next_day = today + datetime.timedelta(days=1)

    print("Ngày vừa nhập là:", today.strftime("%d/%m/%Y"))
    print("Ngày kế tiếp là:", next_day.strftime("%d/%m/%Y"))
except ValueError:
    print("Ngày tháng năm không hợp lệ!")
