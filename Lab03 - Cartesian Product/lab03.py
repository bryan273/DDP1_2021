# Memberi input isi nilai himpunan A dan B
A=input("Masukkan input himpunan A: ")
B=input("Masukkan input himpunan B: ")

print("A x B = {",end='')

# Membuat variabel ini yang menyatakan variabel untuk letak index koma sebelum isi nya
# Misal 1,2,3 maka index_sebelum_A adalah 1 dan setelah A adalah 3
index_sebelum_A=0

# Membuat outer loop sebanyak koma yang ada pada A
for i in range(A.count(',')):
    # Membuat variabel index sesudah A dengan mencari nilai ',' yang dimulai setelah index sebelum A + 1
    # Supaya mendapatkan index ',' berikutnya 
    # Melakukan hal yang sama untuk B
    index_sesudah_A=A.find(',',index_sebelum_A+1)
    index_sebelum_B=0

    # Membuat inner loop sebanyak koma di B supaya masing masing pemetaan A bisa ke semua B
    for j in range(B.count(',')):
        # Melakukan pembuatan variabel dengan konsep yang sama seperti index A
        index_sesudah_B=B.find(',',index_sebelum_B+1)
        
        # Jika index koma A dan B adalah 0 , maka langsung di output character pertamanya sampai
        # batas ke koma berikutnya
        # Jika index koma A = 0 dan B tidak 0 , maka output nilai characer pertama index A sampai ke batas
        # koma berikutnya dan output nilai character index B dari index koma sebelum + 1 sampai index koma berikutnya
        if index_sebelum_A==0:
            if index_sebelum_B==0:
                print(f'({A[0:index_sesudah_A]},{B[0:index_sesudah_B]})',end=', ')
            else:
                print(f'({A[0:index_sesudah_A]},{B[index_sebelum_B+1:index_sesudah_B]})',end=', ')

        # Jika index B yang 0 , maka kebalikan seperti yang jika A = 0 seperti di atas
        elif index_sebelum_B==0:
            print(f'({A[index_sebelum_A+1:index_sesudah_A]},{B[0:index_sesudah_B]})',end=', ')

        # Jika index koma A dan B tidak 0 , maka output character yang berada di antara 2 koma A dan B
        else:
            print(f'({A[index_sebelum_A+1:index_sesudah_A]},{B[index_sebelum_B+1:index_sesudah_B]})',end=', ')
        
        # Mengganti index B yang sebelum menjadi yang berikutnya , supaya nanti yang index B yang berikutnya lagi
        # bisa terganti dengan index B yang setelahnya lagi
        index_sebelum_B=index_sesudah_B

    # Setelah selesai loop , untuk character terakhir supaya ke print , masuk ke else    
    else:
        # Jika index sebelum A = 0 , maka print characterr dari index pertama sampai sebelum koma pertama
        # Lainnya , print nilai yang berada di antara 2 koma
        if index_sebelum_A==0:
            print(f'({A[0:index_sesudah_A]},{B[index_sesudah_B+1:]})',end=', ')
        else:
            print(f'({A[index_sebelum_A+1:index_sesudah_A]},{B[index_sesudah_B+1:]})',end=', ')

    # Mengganti nilai index sebelum A menjadi setelahnya supaya index_sesudah_A bisa terganti
    # oleh index yang setelahnya lagi
    index_sebelum_A=index_sesudah_A

# Ketika selesai loop A untuk mendapat nilai character terakhir masuk ke else
else:
    # Menggunakan kondisi yang hampir sama seperti loop di atas , tetapi dipisahkan dengan loop di atas
    # karena character trakhir tidak diapit 2 koma , jadi kita harus membuat else lagi
    index_sebelum_B=0
    for j in range(B.count(',')):
        index_sesudah_B=B.find(',',index_sebelum_B+1)
        if index_sebelum_B==0:
            print(f'({A[index_sesudah_A+1:]},{B[0:index_sesudah_B]})',end=', ')
        else:
            print(f'({A[index_sesudah_A+1:]},{B[index_sebelum_B+1:index_sesudah_B]})',end=', ')
        index_sebelum_B=index_sesudah_B
    else:
        print(f'({A[index_sesudah_A+1:]},{B[index_sesudah_B+1:]})',end='}')

# Note : Pada setiap print ada 'end' supaya output tidak mereturn newline