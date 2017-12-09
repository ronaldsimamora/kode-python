import random

def main():
    # mengambil bilangan acak dari 1 sampai 100
    print("random.randrange(1, 100): ", random.randrange(1, 100))

    # mengambil bilangan acak dari 1 sampai 1000
    print("\nrandom.randrange(1, 1000): ", random.randrange(1, 1000))

    # mengambil bilangan acak dari -100 samppai 0
    print("\nrandom.randrange(-100, 0): ", random.randrange(-100, 0))

if __name__ == "__main__":
    main()
