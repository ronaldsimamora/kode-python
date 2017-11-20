import copy

def filetolist(filename):
    templist = []
    try:
        f = open(filename)
        for line in f:
            templist.append(line)
    except IOError as e:
        print(e)
        sys.exit(1)
    return templist

def printlist(li):
    for e in li:
        print(e, end="")

def main():
    phonebook = filetolist("data.txt")

    sortedlist = sorted(copy.deepcopy(phonebook))

    print("Sebelum diurutkan")
    printlist(phonebook)

    print("\nSetelah diurutkan")
    printlist(sortedlist)

if __name__ == "__main__":
    main()
