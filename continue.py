def main():
    for i in range(1,11):
        if i % 2 == 0:
            continue    # melanjutkan pengulangan untuk i berikutnya
        # baris dibawah ini hanya akan di ekseskusi
        # jika i bernilai ganjil
        print(i, end="\t")

if __name__ == "__main__":
    main()
