def main():
    # membuka file
    f = open(r"data.txt", "r")
    
    # membaca data di dalam file
    # tanpa menentukan jumlah byte
    s = f.read(11)
    
    print("DATA: ")
    print(s)
    
    # menutup file
    f.close()
    
if __name__ == "__main__":
    main()