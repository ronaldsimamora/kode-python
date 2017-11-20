def main():
    # menampilkan judul program
    print("Nilai Maksimum dari Tiga Bilangan")
    
    # meminta user memasukkan tiga bilangan
    a = int(input("Masukkan bilangan ke-1\t: "))
    b = int(input("Masukkan bilangan ke-2\t: "))
    c = int(input("Masukkan bilangan ke-3\t: "))
    
    # menentukan nilai maksimum menggunakan CARA II
    if a > b and a > c:
        maks = a
    else:
        if b > a and b > c:
            maks = b
        else:
            maks = c
            
    # menampilkan nilai maksimum
    print("\nNilai maksimum adalah %d" % maks)
    
if __name__ == "__main__":
    main()