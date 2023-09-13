def bcnn(aa, bb):
	m = abs(aa)
	n = abs(bb)
	while (m * n != 0):
		if (m > n):
			m = m - n
		else:
			n = n - m
	return int(abs(aa * bb) / (m + n))

def main():
	a = int(input("Nhap a: "))
	b = int(input("Nhap b: "))

	print("Ket qua:", bcnn(a, b))

if __name__ == "__main__":
    main()