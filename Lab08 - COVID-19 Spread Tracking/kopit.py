# Membuat fungsi rekursif untuk menampilkan setiap nama yang ditularkan oleh penular 
def RANTAI_PENYEBARAN(nama,rantai):
    print('-',nama)
    nama_next = rantai.get(nama,None)
    if nama_next == None:
        return
    else:
        # Jika yang ditularkan penular banyak , maka looping untuk setiap orang yang tertular sebagai next penular
        for char in nama_next :
            RANTAI_PENYEBARAN(char,rantai)

# Mengecek apakah penular menularkan orang yang tertular dengan rekursif
def CEK_PENULARAN(rantai,tertular,penular):
    # Membuat global value sebagai flag
    global value
    if tertular == penular : value = True

    nama_next = rantai.get(penular,None)
    # Base case ketika value = True dan nama penular brikutnya kosongg
    if nama_next == None or value == True:
        return
    # Membuat flag True bila penular menularkan tertular
    elif nama_next == tertular or tertular in nama_next:
        value = True
    else:
        for char in nama_next :
            CEK_PENULARAN(rantai,tertular,char)


print('Masukkan rantai penyebaran:')
rantai ,nama_unik = {} , set()

# Mengeloop untuk mendapat penular dan tertular
while True:
    penular , *tertular = input().split()

    if penular == 'selesai' :
        break
    # Jika input hanya penular , maka dictionary beruapa key : None
    elif tertular == []:
        rantai[penular] = None
    elif penular not in rantai:
        rantai[penular] = tertular
    else:
        rantai[penular].extend(tertular)
    
    # Membuat nama_unik untuk set orang yang berada di rantai
    nama_unik.update(set([penular]) | set(tertular) ) 

print('''
List perintah:
1. RANTAI_PENYEBARAN 
2. CEK_PENULARAN 
3. EXIT
''')

# Mengecek kondisi input valid atau tidak
try:
    while True:
        perintah = input('Masukkan perintah: ').split()

        # Kondisi untuk perintah rantai penyebaran
        if perintah[0] == 'RANTAI_PENYEBARAN':
            if perintah[1] in nama_unik:
                print(f'Rantai penyebaran {perintah[1]}:')
                RANTAI_PENYEBARAN(perintah[1],rantai)
            else:
                print(f'Maaf, nama {perintah[1]} tidak ada dalam rantai penyebaran.')

        # Kondisi untuk perintah cek penularan
        elif perintah[0] == 'CEK_PENULARAN':
            # Set Flag
            value = False

            # Kondisi untuk mengecek apakah nama penular atau tertular valid
            if perintah[1] in nama_unik and perintah[2] in nama_unik:
                CEK_PENULARAN(rantai,perintah[1],perintah[2])
                print('YA') if value else print('TIDAK') 
            elif (perintah[1] not in nama_unik and perintah[2] in nama_unik) or (perintah[1] == perintah[2]):
                print(f'Maaf, nama {perintah[1]} tidak ada dalam rantai penyebaran.')
            elif perintah[2] not in nama_unik and perintah[1] in nama_unik:
                print(f'Maaf, nama {perintah[2]} tidak ada dalam rantai penyebaran.')
            else:
                print(f'Maaf, nama {perintah[1]} dan {perintah[2]} tidak ada dalam rantai penyebaran.')

        elif perintah[0] == 'EXIT':
            print('Goodbye~ Semoga virus KOPIT cepat berakhir.')
            break
        else:
            print('Maaf perintah tidak dikenali. Masukkan perintah yang valid.')
        print()
except:
    print('Maaf perintah tidak dikenali. Masukkan perintah yang valid.')