n = int(input("Nhap n: "))

t = 1
i = 1
while (i <= n):
	t = t * i
	i = i + 1

print(n, end=''),
print("!=", t)