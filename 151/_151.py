n = int(input("Nhap n: "))

flag = 1
t = n
while (t > 1):
	du = t % 2
	if (du != 0):
		flag = 0
	t = t // 2
	
if (flag == 1):
	print("La dang")
else:
	print("Ko la dang")
