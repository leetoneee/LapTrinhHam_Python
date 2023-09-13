def GiaiThua(nn):
	t = 1
	i = 1
	while (i <= nn):
		t = t * i
		i = i + 1
	return t

def main():
	n = int(input("Nhap n: "))


	print(n, end=''),
	print("!=", GiaiThua(n))

if __name__ == "__main__":
    main()