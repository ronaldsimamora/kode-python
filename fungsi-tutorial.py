import datetime as dt

def getisoformat(date):
    return dt.date.isoformat(date)

def day(date):
    datestr = getisoformat(date)
    return int(datestr[8:])

def month(date):
    datestr = getisoformat(date)
    return int(datestr[5:7])

def year(date):
    datestr = getisoformat(date)
    return int(datestr[:4])

def main():
    sekarang = dt.date.today()
    print(getisoformat(sekarang))
    print("Hari\t: %d" % day(sekarang))
    print("Bulan\t: %d" % month(sekarang))
    print("Tahun\t: %d" % year(sekarang))
    
if __name__ == "__main__":
    main()