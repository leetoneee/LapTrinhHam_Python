def ktHoanThien(nn):
	s = 0
	i = 1
	while (i < nn):
		if (nn % i == 0):
			s = s + i
		i = i + 1
	if (s == nn):
		return 1
	return 0

def main():
	n = int(input("Nhap n: "))

	if (ktHoanThien(n) == 1):
		print("Hoan thien")
	else:
		print("Ko Hoan thien")

if __name__ == "__main__":
    main()
