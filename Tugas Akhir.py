import pandas as pd
#Irfan M Zein = 222410102015
#Rasthian Restu Fende Dwiki Darmawan = 222410102085

print("="*80)
print("SELAMAT DATANG DI BITCOUNT")
print("Aplikasi yang dapat memudahkan anda untuk memaksimalkan\nlahan yang anda punya sebagai lahan pertanian")
jumlah_kebun = int(input("\nMasukkan Jumlah lahan yang anda Miliki = \n"))

print("="*80)

for i in range(jumlah_kebun): # menentukan banyaknya atau batasan tanaman yang bisa ditanam di setiap lahan
    i+=1
    nama_jenis = str(input("masukkan nama tanaman yang anda tanam = "))
    luas_setiap_kebun = int(input(f"\nmasukkan luas lahan ke {i} anda (m^2)= "))
    jarak_1 = float(input("masukkan jarak lebar antar tanaman (cm)= "))
    jarak_2 = float(input("masukkan jarak panjang antar tanaman (cm)= "))
    jarak_1 = jarak_1/100
    jarak_2 = jarak_2/100
    jarak = jarak_1*jarak_2
    jumlah_tanaman_yang_bisa_ditanam  = luas_setiap_kebun/jarak 
    jumlah_tanaman_yang_bisa_ditanam  = int(jumlah_tanaman_yang_bisa_ditanam )
    print(f"jumlah tanaman {nama_jenis} yang anda bisa tanam adalah {jumlah_tanaman_yang_bisa_ditanam } ")
    jumlah_jenis_tanaman  = int(input(f"masukkan jumlah jenis tanaman {nama_jenis} yang anda akan tanam = "))
    print("") 
    print("="*80) 
    jenis_tanaman  = []
    jumlah_bibit_tanaman = []
    list_keterangan_kebun = []
    nama_tanaman = []
    for u in range(jumlah_jenis_tanaman ):# menginputkan jenis dan jumlah bibit dari setiap jenis
        u+=1
        jenis = str(input(f"\nmasukkan jenis {nama_jenis} ke {u} = "))
        jumlah_bibit_setiap_tanaman = int(input(f"masukkan jumlah bibit {nama_jenis} {jenis} yang akan di tanam = "))
        jumlah_bibit_tanaman.append(jumlah_bibit_setiap_tanaman)
        seed_left = jumlah_tanaman_yang_bisa_ditanam  - sum(jumlah_bibit_tanaman)
        
        if seed_left <= 0 : # jika jumlah bibit melebihi batasan tanaman yang bisa di tanam
            seed_left = seed_left*-1
            jenis_tanaman.append(jenis)
            jumlah_bibit_tanaman.remove(jumlah_bibit_setiap_tanaman)
            lahan_yang_tersisa = jumlah_tanaman_yang_bisa_ditanam  - sum(jumlah_bibit_tanaman)
            jumlah_bibit_tanaman.append(lahan_yang_tersisa)
            list_keterangan_kebun.append(i)
            nama_jenis.append(nama_tanaman)
            lahan_yang_tersisa = 0
            if seed_left > 0 :
                print(f"jumlah bibit {nama_jenis} {jenis} terlalu banyak sehingga lebih {seed_left} bibit\n")
            break
        list_keterangan_kebun.append(i)
        nama_jenis.append(nama_tanaman)
        jenis_tanaman.append(jenis)
        lahan_yang_tersisa = jumlah_tanaman_yang_bisa_ditanam  - sum(jumlah_bibit_tanaman)
        print(f"lahan yang tersisa {lahan_yang_tersisa}\n")
       
        
    print("=======================================================================================")
    for idx , o in enumerate(jumlah_bibit_tanaman): # memberikan informasi yang akan ditanam dari setiap jenis dan jumlah
        idx1 = idx+1
        print(f"jumlah tanaman jenis ke {idx1} bisa ditanam sebanyak {o} bibit {jenis_tanaman [idx]}")
    if lahan_yang_tersisa > 0 :   # jika lahan masih tersisa maka akan diberi informasi
        print(f"\njumlah lahan yang tersisa untuk ditanam adalah {lahan_yang_tersisa} ")
    print(f"di kebun ke {i}\n")
    print("="*80)
    print("")
        
    listjumlah = {
    'nama'  : nama_tanaman,
    'jenis' : jenis_tanaman ,
    'jumlah bibit' : jumlah_bibit_tanaman,
    'keterangan kebun' : list_keterangan_kebun}
    data1 = pd.DataFrame(listjumlah)
    print(f"{data1}\n")
    
    
    keterangan = str(input("apakah anda ingin menyimpan data di atas ? y/n = ")) # menambahkan jumlah data ke dalam csv
    if keterangan == "y":
        data1.to_csv('tugas akhir.csv', mode='a', index=False)
    elif keterangan == "n":
        break
    
print("")
print("="*80)   
keterangan_awal = str(input("apakah anda ingin melihat isi database ? y/n = \n")) # melihat data yang ada di csv

if keterangan_awal == "y":
    keterangan_awal = pd.read_csv('tugas akhir.csv')
    print(keterangan_awal)
else:
    print()
