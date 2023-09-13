def ktChinhPhuong(nn):
	flag = 0
	i = 1
	while (i <= nn):
		if (i * i == nn):
			flag = 1
		i = i + 1
	return flag

def main():
	n = int(input("Nhap n: "))

	if (ktChinhPhuong(n) == 1):
		print("Chinh phuong")
	else:
		print("Ko chinh phuong")

if __name__ == "__main__":
    main()

