def main():
	n = int(input("Nhap n: "))

	s = 0
	i = 2
	while (i <= n):
		s = (i + s)**(1 / i)
		i = i + 1

	print("Ket qua:", s)

if __name__ == "__main__":
    main()