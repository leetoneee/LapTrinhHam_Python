def Tinh(nn):
	s = 0
	i = 2
	while (i <= nn):
		s = (i + s)**(1 / i)
		i = i + 1
	return s

def main():
	n = int(input("Nhap n: "))

	print("Ket qua:", Tinh(n))

if __name__ == "__main__":
    main()
