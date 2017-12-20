def main():
    # membuka file
    f = open(r"data.txt")
    
    # menggunakan file
    print("Nama file\t: ", f.name)
    print("Tertutup? ", f.closed)
    print("Mode akses: ", f.mode)
    
    # menutup file
    f.close()
    
    print("\nSetelah ditutup")
    print("Tertutup?\t: ", f.closed)
    
if __name__ == "__main__":
    main()