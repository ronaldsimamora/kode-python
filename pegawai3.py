while True:
    nama = input("Nama\t: ")
    if not nama:
        break
    alamat = input("Alamat\t: ")
    hobi = input("Hobi\t: ")
    print("Nama\t: ", nama)
    print("Alamat\t: ", alamat)
    if hobi:
        print("Hobi\t: ", hobi)
    else:
        print("Sebaiknya hobi diisi")
