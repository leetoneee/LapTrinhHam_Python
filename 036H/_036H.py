def LuyThua(xx, nn):
	t = 1
	i = 1
	while (i <= nn):
		t = t * xx
		i = i + 1
	return t

def main():
	x = float(input("Nhap x: "))
	n = int(input("Nhap n: "))

	print("Luy thua: ", LuyThua(x, n))

if __name__ == "__main__":
    main()
