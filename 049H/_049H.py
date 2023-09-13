def LietKeUocSo(nn):
	i = 1
	while (i <= nn):
		if (nn % i == 0):
			print(i, end=' ')
		i = i + 1

def main():
	n = int(input("Nhap n: "))

	LietKeUocSo(n)

if __name__ == "__main__":
    main()
