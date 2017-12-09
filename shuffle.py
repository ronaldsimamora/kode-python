import random

def main():
    li1 = [50, 30, 10, 20, 40]
    li2 = ["Joni", "Arif", "Ridho", "Awan"]

    # menampilkan nilai list sebelum diacak
    print("Sebelum diacak")
    print("li1: ", li1)
    print("li2: ", li2)

    # mengacak urutan list
    random.shuffle(li1)
    random.shuffle(li2)

    # menampilkan nilai list setelah diacak
    print("Setelah diacak")
    print("li1: ", li1)
    print("li2: ", li2)

if __name__ == "__main__":
    main()
