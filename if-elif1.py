def main():
    x = int(input("Masukkan bilangan bulat : "))
    
    # memeriksa nilai x
    if x > 0:
        print("%d adalah bilangan positif" % x)
    elif x == 0:
        print("%d adalah bilangan nol" % x)
    else:
        print("%d adalah bilangam negatif" % x)
        
if __name__ == "__main__":
    main()