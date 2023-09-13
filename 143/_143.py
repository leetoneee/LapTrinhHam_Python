def main():
	n = int(input("Nhap n: "))

	s = 0
	i = 1
	while (i < n):
		if (n % i == 0):
			s = s + i
		i = i + 1
	if (s == n):
		print("Hoan thien")
	else:
		print("Ko hoan thien")

if __name__ == "__main__":
    main()