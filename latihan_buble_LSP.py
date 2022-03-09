def garis():
    print("----------")

#fungsi bubble sort ascending (dari kecil ke besar)
def sort_asc(array):
    n = len(array) #n itu adalah jumlah baris
    #perulangan pertama
    for i in range(n):
        #perulangan kedua
        for j in range (n-i-1):
            #membandingkan masing" elemen ke kanan
            if array [j] > array[j+1]:
                #jika lebih besar, tukar ke kiri
                array[j], array[j+1] = array[j+1], array[j]
    return array

#fungsi bubble sort descending (dari besar ke kecil)
def sort_desc(array):
    n = len(array) #n itu adalah jumlah baris
    #perulangan pertama
    for i in range(n):
        #perulangan kedua
        for j in range (n-i-1):
            #membandingkan masing" elemen ke kanan
            if array [j] < array[j+1]:
                #jika lebih besar, tukar ke kiri
                array[j], array[j+1] = array[j+1], array[j]
    return array

#fungsi rata rata
def rata_rata(angka):
    return sum(angka)/len(angka)

#input nilai
garis()
print("masukkan tiga buah nilai")
nilai_a = int(input("nilai a : "))
nilai_b = int(input("nilai b : "))
nilai_c = int(input("nilai c : "))
angka = [nilai_a, nilai_b, nilai_c]
garis()
print()

#nilai akhir
print("hasil akhir----")
print("urutan angka ascending : ", (sort_asc(angka)))
print("urutan angka descending : ", (sort_desc(angka)))
garis()
print()

#angka terbesar
print("angka terbesar : ",max(angka))

#angka terkecil
print("angka terkecil : ",min(angka))

#rata rata
print("rata rata : ",round(rata_rata(angka),2))

#jumlah angka
print("jumlah angka : ",sum(angka))



