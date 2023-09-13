def DaoNguoc(nn):
	dn = 0
	t = nn
	while (t != 0):
		dv = t % 10
		dn = dn * 10 + dv
		t = t // 10
	return dn

def main():
	n = int(input("Nhap n: "))

	print("So dao nguoc:", DaoNguoc(n))

if __name__ == "__main__":
    main()