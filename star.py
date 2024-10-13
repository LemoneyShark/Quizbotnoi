def main():
    # รับค่าจากผู้ใช้
    x = int(input("Enter a number: "))
    print_star_pattern(x)

def print_star_pattern(x):
    for i in range(1, 2*x):
        if i <= x:
            print("*" * i)
        else:
            print("*" * (2*x - i))

main()
