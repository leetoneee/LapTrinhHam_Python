def GiaiBacNhat(aa, bb):
	if (aa == 0):
		if (bb == 0):
			print("VSN")
		else:
			print("VN")
	else:
		x = (-bb) / aa
		print(x)
def main():
	a = float(input("Nhap a: "))
	b = float(input("Nhap b: "))

	GiaiBacNhat(a, b)

if __name__ == "__main__":
    main()
