def main():
	n = int(input("Nhap n: "))

	flag = 0
	i = 1
	while (i <= n):
		if (i * i == n):
			flag = 1
		i = i + 1
	if (flag == 1):
		print("Chinh phuong")
	else:
		print("Ko chinh phuong")

if __name__ == "__main__":
    main()
