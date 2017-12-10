def main():
    list1 = [10, 20, 30, 20, 10, 10]

    print("list1: ", list1)

    # menghitung banyaknya elemen 10
    a = list1.count(10)
    # menghitung banyaknya elemen 20
    b = list1.count(20)
    # menghitung banyaknya elemen 30
    c = list1.count(30)

    print("\nlist1.count(10): ", a)
    print("list1.count(20): ", b)
    print("list1.count(30): ", c)

if __name__ == "__main__":
    main()
