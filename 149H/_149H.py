def ucln(aa, bb):
	m = abs(aa)
	n = abs(bb)
	while (m * n != 0):
		if (m > n):
			m = m - n
		else:
			n = n - m
	return m + n

def main():
	a = int(input("Nhap a: "))
	b = int(input("Nhap b: "))

	print("Ket qua:", ucln(a, b))

if __name__ == "__main__":
    main()
