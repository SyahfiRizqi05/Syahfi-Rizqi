var =["Arsel", "Avivah", "Daiva", ["Wahyu", "Wibi"]]
def linearsearch(var,x):
    for l in range(len(var)):
        if type(var[l]) == list:
            hasil_x = linearsearch(var[l],x)
            if hasil_x == -1:
                return -1
            else:
                print(f'{x} ditemukan pada indeks {l} kolom {hasil_x}')
                exit()
        elif var[l] == x:
            return l
    return -1
# print(var)
# x = input('Masukan nama yang ingin dicari: ')
# hasil_y = linearsearch(var,x)
# if hasil_y == -1:
#     print(f'{x} ditemukan pada indeks {hasil_y}')
# else:
#     print(f'{x} ditemukan pada indeks {hasil_y}')

def jumpSearch (var, target , length) :
    langkah = length**0.5
    prev = 0
    for H in range(len(var)):
        if type(var[H]) == list:
            hasil_g = jumpSearch (var[int(H)],target,len(var[int(H)]))
            if hasil_g == -1:
                var[int(H)]="berhasil"
            else:
                print(target ,"ditemukan pada indeks", int(H) , "kolom", hasil_g)
                exit()


    while var[int (min(langkah, length) -1)] < target:
        prev = langkah
        langkah += length**0.5 
        if (prev >= length) :
            return -1
        
    while var[int (prev)]< target:
        prev += 1
        if prev == min(langkah, length) :
            return -1
    if var[int(prev)]== target:
        return int(prev)
    return -1


# length = len(var)
# print(f'Arsel','Avivah','Daiva','Wahyu','Wibi')
# target = str(input("masukan nama :"))
# hasil_x = jumpsearch(var,target, length)
# if hasil_x == -1:
#     print(target, 'tidak ada')
# else:
#     print(target,'ada di indeks ke',hasil_x)


while True:
    print("""
    |=================|
    1. linearsearch
    2. jumpSearch
    |=================|
    """)

    pilih = input("masukan no yang anda inginkan :")

    if pilih == "1" :
        print(var)
        x = input('Masukan nama : ')
        hasil_y = linearsearch(var,x)
        if hasil_y == -1:
            print(f'{x} ditemukan pada indeks {hasil_y}')
        else:
            print(f'{x} ditemukan pada indeks {hasil_y}')
        exit()

    elif pilih == "2" :
        print(var)
        length = len(var)
        # print(f'Arsel','Avivah','Daiva','Wahyu','Wibi')
        target = str(input("masukan nama :"))
        hasil_x = jumpSearch(var,target, length)
        if hasil_x == -1:
            print(target, 'tidak ada')
        else:
            print(target,'ada di indeks ke',hasil_x)
        exit()
