# Khai báo biến
i1, i2, i3 = 2, 5, -3
d1, d2, d3 = 2.0, 5.0, -0.5

# Định nghĩa các biểu thức trong dictionary
expressions = {
    "a": "i1 + (i2 * i3)",
    "b": "i1 * (i2 + i3)",
    "c": "i1 / (i2 + i3)",
    "d": "i1 // (i2 + i3)",
    "e": "i1 / i2 + i3",
    "f": "i1 // i2 + i3",
    "g": "3 + 4 + 5 / 3",
    "h": "3 + 4 + 5 // 3",
    "i": "(3 + 4 + 5) / 3",
    "j": "(3 + 4 + 5) // 3",
    "k": "d1 + (d2 * d3)",
    "l": "d1 + d2 * d3",
    "m": "d1 / d2 - d3",
    "n": "d1 / (d2 - d3)",
    "o": "d1 + d2 + d3 / 3",
    "p": "(d1 + d2 + d3) / 3",
    "q": "d1 + d2 + (d3 / 3)",
    "r": "3 * (d1 + d2) * (d1 - d3)"
}

# Tính và in kết quả
for key, expr in expressions.items():
    result = eval(expr)  # dùng eval() để tính toán từ chuỗi
    print(f"({key}) {expr} = {result}")
