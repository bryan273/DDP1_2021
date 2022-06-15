print('Selamat datang di Kalkulator IPK!')

# Menggunakan while loop untuk mengecek apakah jumlah matkul yang diinput sesuai kriteria
# Apabila kurang dari 0 , maka user harus menginput nilai kembali yang valid
# Jika matkul nya 0 , maka tidak ada matkul yg diambil dan program langsung berhenti
# Selebihnya bila > 0 , maka loop berhenti dan lanjut ke statement berikutnya
while True:
    # Menerima input user untuk jumlah matkul
    jumlah_matkul=int(input('Masukkan jumlah mata kuliah: '))
    if jumlah_matkul==0:
        print('Tidak ada mata kuliah yang diambil.')
        exit()
    elif jumlah_matkul<0:
        continue
    else:
        break

# Assign variabel yang akan kita butuhkan untuk perhitungan nanti    
jumlah_semua_mutu=0
jumlah_mutu_lulus=0
sks_lulus=0
sks_tidak_lulus=0

# Menggunakan for loop sebanyak jumlah matkul yang diambil
for loop in range(jumlah_matkul):

    # Menerima input user berupa nama matkul dengan formatting untuk menentukan jumlah matkul ke berapa
    # Dan juga menerima input berupa jumlah sks dengan formatting nama matkulnya apa
    nama_matkul=input(f'Masukkan nama mata kuliah ke-{loop+1}: ')
    jumlah_sks=int(input(f'Masukkan jumlah SKS {nama_matkul} : '))

    # Menggunakan loop untuk mengecek nilai matkul , kalau kurang dari 0 nilainya tetap di-looping
    # Dan selain itu break dari loop
    while True:
        # Input nilai_matkul dalam bentuk float karena memungkinkan inputan ada koma
        nilai_matkul=float(input('Masukkan nilai yang kamu dapatkan: '))
        if nilai_matkul<0:
            print('Nilai yang kamu masukkan tidak valid')
            continue
        else : 
            break
    
    # Menggunakan condition untuk mengonversi nilai matkul menjadi bobot dan
    # Menentukan jumlah sks matkul yang lulus atau tidak sesuai dengan kriteria yang sudah ditentukan
    if 0<=nilai_matkul<40:
        bobot=0.00
        sks_tidak_lulus+=jumlah_sks
    elif 40<=nilai_matkul<55:
        bobot=1.00
        sks_tidak_lulus+=jumlah_sks
    else:
        # Memakai nested condition khusus untuk nilai matkul yang membuat lulus sks ,
        # Supaya bisa menspesifikan mutu hanya untuk jumlah mutu matkul yang lulus
        if 55<=nilai_matkul<60:
            bobot=2.00
            sks_lulus+=jumlah_sks
        elif 60<=nilai_matkul<65:
            bobot=2.30
            sks_lulus+=jumlah_sks
        elif 65<=nilai_matkul<70:
            bobot=2.70
            sks_lulus+=jumlah_sks
        elif 70<=nilai_matkul<75:
            bobot=3.00
            sks_lulus+=jumlah_sks
        elif 75<=nilai_matkul<80:
            bobot=3.30
            sks_lulus+=jumlah_sks
        elif 80<=nilai_matkul<85:
            bobot=3.70
            sks_lulus+=jumlah_sks
        elif nilai_matkul>=85:
            bobot=4.00
            sks_lulus+=jumlah_sks
        # Menjumlahkan total mutu sks yang lulus
        jumlah_mutu_lulus+=bobot*jumlah_sks
    
    # Menjumlahkan total mutu sks yang lulus maupun yang tidak lulus
    mutu=bobot*jumlah_sks
    jumlah_semua_mutu+=mutu
    print()

# Ketika Loop Selesai
# Menjumlahkan total sks yang diambil dari yg lulus + tidak lulus
total_sks=sks_lulus+sks_tidak_lulus

# Membuat condition jika total semua sks atau total sks lulus tidak 0 
# Maka dicari IPT atau IPK menggunakan rumus yang ditentukan
# Tetapi jika 0 , maka IPT atau IPK tetap 0 , dan tidak dimasukkan ke rumus
# Untuk menghindari terjadinya division by zero error
IPT,IPK=0,0
if total_sks!=0:
    IPT=jumlah_semua_mutu/total_sks
if sks_lulus!=0:
    IPK=jumlah_mutu_lulus/sks_lulus

# Print dengan formatting dan juga kata kata yang telah ditentukan
print('Jumlah SKS lulus :' ,sks_lulus ,'/', total_sks)
print('Jumlah mutu lulus:', f'{jumlah_mutu_lulus:.2f}' ,'/', f'{jumlah_semua_mutu:.2f}')
print('Total IPK kamu adalah' ,f'{IPK:.2f}')
print('Total IPT kamu adalah', f'{IPT:.2f}')

