# Mengimport modul random
import random

print("Halo, selamat datang di Mathbot")

# Define suatu fungsi yang mengambil parameter berupa nomor perintah yang akan diambil
# Tujuannya untuk menge-print perintah "piih mode x" dengan x sesuai nomor perintah yang diambil
# Menggunakan dictionary karena bisa assign key dan value ,cocok untuk memilih nilai x sesuai nomor perintah
# Jika nomor perintah 4 , print suatu kalimat dan program selesai
# Jika nomor perintah ada diantara 1,2,3 maka output pilih mode
def perintah(nomor_perintah):
    dictionary={1:'Penjumlahan',2:'Pengurangan',3:'Campur',4:'Akhiri Program'}
    if nomor_perintah==4:
        print('Terima kasih telah bermain kuis ini. Sampai jumpa lagi!')
        exit()
    elif nomor_perintah in [1,2,3] :
        print(f"Baik, pilih mode {dictionary[nomor_perintah]} ya, sekarang pilih jenis kuis apa?")
        
# Define fungsi dengan parameter jenis kuis yang akan diambil
# Tujuannya untuk memberi output soal operasi matematika dan mengembalikan nilai jawaban benarnya
# Menggunakan random.randint(0,10) untuk memilih angka random 0<= n <= 10
# Menggunakan dictionary supaya bisa menspesifikasikan operator yang dipakai sesuai dengan jenis kuisnya
# Menggunakan random.choice untuk memilih random operator untuk campuran nanti apakah + atau -
# Menggunakan max min , supaya jika pengurangan angka pertama selalu lebih besar dari angka kedua
# Sehingga pengurangan tidak mungkin minus
# Membuat formula untuk operasi yang akan dilakukan dan fungsi eval() supaya bisa mengubah
# String operator / int menjadi bisa di evaluate hasilnya kemudian di return untuk mendapat hasilnya
def kuis(jenis_kuis):
    number_1=random.randint(0,10)
    number_2=random.randint(0,10)
    operator={1:'+',2:'-',3:random.choice(['+','-'])}
    bigger_number=max(number_1,number_2)
    smaller_number=min(number_1,number_2)

    formula=str(bigger_number)+operator[nomor_perintah]+str(smaller_number)

    print("Berapa",bigger_number,operator[nomor_perintah],smaller_number,'?')
    return eval(formula)

# Menggunakan loop terluar untuk memilih mode yang akan dipilih user
while True:
    # Menggunakan loop supaya input user bisa diulang jika nilai yang dimasukkan tidak valid
    while True:
        # Memakai try , except supaya jika inputnya berupa string dan error
        # Masuk ke except dan memberi output tidak valid jika perintahnya string
        try:
            print('Pilih Mode:')
            print('1. Penjumlahan')
            print('2. Pengurangan')
            print('3. Campur')
            print('4. Akhiri program\n')

            # Nomor perintah harus integer dan di antara 1 dan 4 (inklusif) sesudah itu keluar dari loop
            # Bila perintahnya integer tetapi di luar kondisi itu tidak valid
            # Bila perintahnya string error , dan masuk ke except juga memberi output tidak valid
            nomor_perintah=int(input('Masukkan perintah: '))
            print()
            if nomor_perintah in [1,2,3,4]:
                break
            else: 
                print('Program tidak mengenali perintah yang dimasukkan. Silakan memilih dari')
                print('perintah yang tersedia.\n')

        except:
            print('\nProgram tidak mengenali perintah yang dimasukkan. Silakan memilih dari')
            print('perintah yang tersedia.\n')

    # Memanggil fungsi perintah , untuk memberi output pemilihan mode sesuai nomor perintah yang diinput
    perintah(nomor_perintah)

    # Menggunakan inner loop pertama untuk memilih jenis kuis dari user
    while True:
        # Menerima input berupa jenis kuis yang akan diambil dan dipadukan dengan beberapa kondisi
        # Bila inputnya integer dan diluar range 1 sampai 4 , maka jawaban tidak valid dan looping ulang
        # Bila inpuntya string , dan karena diconvert ke int menjadi error maka memakai try and except
        # Dan Bila error masuk ke except dan print tidak valid inputnya , dan looping untuk input ulang
        # Bila inputnya int dan antara 1<=n<=4 maka lanjut dan break dari loop
        while True:
            print('Pilih kuis:')
            print('1. Kuis Lepas')
            print('2. Kuis 5')
            print('3. Ganti mode')
            print('4. Akhiri Program\n')

            try:
                jenis_kuis=int(input("Masukkan jenis kuis: "))
                if jenis_kuis in [1,2,3,4]:
                    break
                else:
                    print('\nProgram tidak mengenali perintah yang dimasukkan. Silakan memilih dari')
                    print('perintah yang tersedia.\n')
            except:
                print('\nProgram tidak mengenali perintah yang dimasukkan. Silakan memilih dari')
                print('perintah yang tersedia.\n')
                continue

        if jenis_kuis==1:
            # Jika jenis kuis adalah 1 , maka masuk ke dalam inner loop ke 2 untuk memeriksa jawaban
            # Memakai while karena , sebelum user memberi perintah spesifik , loop akan terus berjalan
            while True:
                print()
                # Memanggil fungsi untuk memberi output soal dan mendapat hasil yg benar diassign ke 'hasil'
                hasil=kuis(jenis_kuis)

                # Menerima jawaban dari user
                jawaban=input("Jawab: ")

                # Menggunakan try dan except , karena jika jawaban user berupa string maka bila
                # Diconvert ke int akan error dan masuk ke except
                try:
                    # Memakai kondisi , jika input user akhiri kuis , maka inner loop 2 berhenti
                    # Dan kembali di inner loop 1 , Jika jawaban user = jawaban hasil yang benar
                    # Memberi output hore benar , yang lainnya kurang tepat dan memberi hasil yang benar
                    if jawaban=='akhiri kuis':
                        print()
                        break
                    elif int(jawaban)==hasil:
                        print('Hore benar!')
                    else:
                        print('Masih kurang tepat, ya. Jawabannya adalah',hasil)
                # Jika input tidak dapat diconvert menjadi int dan error , maka output
                # Jawaban tidak valid 
                except:
                    print('Jawaban tidak valid, hanya menerima jawaban bilangan bulat.')

        # Kondisi kedua , jika jenis kuis 2       
        elif jenis_kuis==2:
            skor=0

            # Memakai for loop untuk menspesifikan 5 loop
            for loop in range(1,6):
                # Memakai formatting untuk menspesifikan pertanyaan ke berapa
                print()
                print(f'Pertanyaan {loop}:',end=' ')
                hasil=kuis(jenis_kuis)
                jawaban=input("Jawab: ")

                # Memakai try dan except dengan tujuan yang sama seperti di kondisi jenis kuis 1
                try:
                    if int(jawaban)==hasil:
                        print('Hore benar!')
                        # Jika benar skor bertambah 20
                        skor+=20
                    else:
                        print('Masih kurang tepat, ya. Jawabannya adalah',hasil)
                except:
                    print('Jawaban tidak valid, hanya menerima jawaban bilangan bulat.')
            else:
                # Setelah for loop selesai , memberi output skor yang diraih
                print('\nScore kamu:',skor)
                print()
        # Jika jenis kuis 3 ,ganti mode maka berhenti dari inner loop 1 dan kembali ke outer loop
        elif jenis_kuis==3:
            print()
            break
        # Jika jenis kuis 4 , memberi output dan program berhenti 
        elif jenis_kuis==4:
            print('\nTerima kasih telah bermain kuis ini. Sampai jumpa lagi!')
            exit()
            



