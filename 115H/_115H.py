def TinhAn(nn):
	if (nn == 0):
		return -1
	if (nn == 1):
		return 3
	att = -1
	at  = 3
	i = 2
	while (i <= nn):
		ahh = 5 * at + 6 * att
		i += 1
		att = at
		at = ahh
	return ahh


def main():
	n = int(input("Nhap n: "))

	print("Ket qua:", TinhAn(n))

if __name__ == "__main__":
    main()