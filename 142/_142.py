def main():
	n = int(input("Nhap n: "))

	dn = 0
	t = n
	while (t != 0):
		dv = t % 10
		dn = dn * 10 + dv
		t = t // 10

	print("So dao nguoc:", dn)

if __name__ == "__main__":
    main()
