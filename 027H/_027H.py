def Tong(nn):
	s = 0
	i = 1
	while (i <= nn):
		s = s + i
		i = i + 1
	return s

def main():
	n = int(input("Nhap n: "))
	
	print("Tong la: ", Tong(n))

if __name__ == "__main__":
    main()