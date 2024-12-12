def fibonacci(n):
    fib_list = []
    a, b = 0, 1
    while a < n:
        fib_list.append(a)
        a, b = b, a + b
    return fib_list

# Nhập số n
n = int(input("Nhập số nguyên n: "))

# Tạo danh sách các số Fibonacci nhỏ hơn n
fibonacci_list = fibonacci(n)

# In danh sách Fibonacci
print(fibonacci_list)
print('Tran Quang Anh, 235752021610095')
