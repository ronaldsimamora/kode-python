def main():
    # membuka file
    f = open(r"data.txt", "r")
    
    # membaca seluruh baris, dan menampungnya
    # kedalam objek list
    data = f.readlines()
    
    print(data)
    
    # menutup file
    f.close()
    
if __name__ == "__main__":
    main()