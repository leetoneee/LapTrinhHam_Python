def TonTaiChan(nn):
	flag = 0
	t = nn
	while (t != 0):
		dv = t % 10
		if (dv % 2 == 1):
			flag = 1
		t = t // 10
	return flag

def main():
	n = int(input("Nhap n: "))

	if (TonTaiChan(n) == 1):
		print("Ton tai.")
	else:
		print("Ko ton tai.")

if __name__ == "__main__":
    main()