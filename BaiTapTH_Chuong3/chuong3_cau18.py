def hinh1(n):
    # Hình vuông rỗng
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()


def hinh2(n):
    # Tam giác vuông rỗng (vuông góc dưới-phải)
    for i in range(1, n+1):
        for j in range(1, n+1):
            if j == n or i == n or j == n-i+1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def hinh3(n):
    width = 2 * n - 1
    upper = []

    # phần trên (n-1 dòng)
    for i in range(1, n):
        line = [' '] * width
        line[0] = '*'
        if i >= 2:
            line[i - 1] = '*'
        upper.append(''.join(line))

    # in phần trên
    for ln in upper:
        print(ln)

    # dòng giữa đầy sao
    print('*' * width)

    # phần dưới = phản chiếu ngang
    for ln in reversed(upper):
        print(ln[::-1])


def menu():
    while True:
        print("\n--- MENU ---")
        print("1. Hình vuông rỗng")
        print("2. Tam giác vuông rỗng (vuông góc dưới-phải)")
        print("3. Hình đặc biệt")
        print("0. Thoát")

        chon = input("Chọn hình: ")
        if chon == '0':
            break
        n = int(input("Nhập n: "))

        if chon == '1':
            hinh1(n)
        elif chon == '2':
            hinh2(n)
        elif chon == '3':
            hinh3(n)
        else:
            print("Lựa chọn không hợp lệ!")
# chạy menu
menu()