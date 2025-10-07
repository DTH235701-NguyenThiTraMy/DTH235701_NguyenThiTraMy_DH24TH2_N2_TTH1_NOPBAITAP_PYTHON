def oscillate(start, end):
    for i in range(start, end):
        yield i
        yield -i

# Test
for n in oscillate(-3, 5):
    print(n, end=' ')
print()
