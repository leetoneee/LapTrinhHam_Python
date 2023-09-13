def main():
	n = int(input("Nhap n: "))

	flag = 1
	t = n
	while (t != 0):
		dv = t % 10
		if (dv % 2 == 0):
			flag = 0
		t = t // 10
	if (flag):
		print("Toan le")
	else:
		print("Ko toan le")

if __name__ == "__main__":
    main()


