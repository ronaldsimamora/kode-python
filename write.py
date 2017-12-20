def main():
    # membuka file
    f = open(r"data.txt", "w")
    
    # menulis data kedalam file
    f.write("Pemrograman Python\n")
    f.write("2015")
    
    # menutup file
    f.close()
    
if __name__ == "__main__":
    main()