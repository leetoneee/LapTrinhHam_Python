def main():
	a = float(input("Nhap a: "))
	b = float(input("Nhap b: "))

	if (a == 0):
		if (b == 0):
			print("VSN")
		else:
			print("VN")
	else:
		x = (-b) / a
		print(x)

if __name__ == "__main__":
    main()


