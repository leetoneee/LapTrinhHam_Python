def ktDoiXung(nn):
	dn = 0
	t = nn
	while (t != 0):
		dv = t % 10
		dn = dn * 10 + dv
		t = t // 10
	if (dn == nn):
		return 1
	return 0

def main():
	n = int(input("Nhap n: "))

	if (ktDoiXung(n) == 1):
		print("La doi xung")
	else:
		print("Ko doi xung")

if __name__ == "__main__":
    main()


