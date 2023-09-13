def ktNguyenTo(nn):
	dem = 0
	i = 1
	while (i <= nn):
		if (nn % i == 0):
			dem += 1
		i = i + 1
	if (dem == 2):
		return 1
	return 0

def main():
	n = int(input("Nhap n: "))

	if (ktNguyenTo(n) == 1):
		print("Nguyen to")
	else:
		print("Ko nguyen to")

if __name__ == "__main__":
    main()
