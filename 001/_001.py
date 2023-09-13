from math import sqrt

def main():
    print("Diem thu nhat:")
    x1 = float(input("Nhap hoanh do: "))
    y1 = float(input("Nhap tung do: "))
    print("Diem thu hai:")
    x2 = float(input("Nhap hoanh do: "))
    y2 = float(input("Nhap tung do: "))

    kc = sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1))

    print("Diem thu nhat:")
    print("Hoanh do: ", x1)
    print("Tung do: ", y1)
    print("Diem thu hai:")
    print("Hoanh do: ", x2)
    print("Tung do: ", y2)
    print("Khoang cach: ", kc)
    
if __name__ == "__main__":
    main()