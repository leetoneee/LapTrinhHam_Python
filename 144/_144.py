def main():
	n = int(input("Nhap n: "))

	dem = 0
	i = 1
	while (i <= n):
		if (n % i == 0):
			dem += 1
		i = i + 1
	if (dem == 2):
		print("Nguyen to")
	else:
		print("Ko nguyen to")

if __name__ == "__main__":
    main()
