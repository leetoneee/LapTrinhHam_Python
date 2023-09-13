def ktDang2m(nn):
	flag = 1
	t = nn
	while (t > 1):
		du = t % 2
		if (du != 0):
			flag = 0
		t = t // 2
	return flag

def main():
	n = int(input("Nhap n: "))
	
	if (ktDang2m(n) == 1):
		print("La dang")
	else:
		print("Ko la dang")

if __name__ == "__main__":
    main()