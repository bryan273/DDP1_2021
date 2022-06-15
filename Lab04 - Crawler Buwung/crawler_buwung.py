# Menerima input user
file_input=input('Masukkan nama file input: ')
file_output=input('Masukkan nama file output: ')

# Memberi variabel untuk menghitung jumlah @/#/www.
mention,hashtag,url=0,0,0

# Mendefine function menggunakan loop untuk mengecek apakah user mengakhiri program dengan 'enter'
def keluar():
    while True:
        print('Program selesai. Tekan enter untuk keluar...',end='')
        enter=input()
        if enter=='':
            break
    
# Membuka input file untuk dibaca dan bila tidak error membuat output file untuk ditulis
# Bila error mengeprint output dan program selesai
try:
    old_file=open(f'{file_input}','r')
except IOError:
    print('File input tidak ada :(')
    keluar()
    exit()
else:
    # Memasukkan isi dari input file ke variabel agar isinya dapat dipakai berulang kali
    read_file=old_file.readlines()
    # Mengecek apakah file inputnya kosong
    if read_file==[]:
        print('File input ada tapi kosong :(')
        keluar()
        exit()
    else:
        new_file=open(f'{file_output}','w')

# Menggunakan iterasi untuk mendapat setiap baris dari isi input file
for line in read_file:
    # Mengesplit spasi dan mengubah jadi list
    # Mengganti isi index terakhir dari list dengan mengambil index [:-1] saja , supaya \n tidak ikut
    line_split=list(line.split(' '))
    line_split[-1]=line_split[-1][:-1]

    # Mengiterasi setiap kata di setiap baris
    for char in line_split:
        # Mengganti kata kata di output file bila dimulai dengan @/#/www.
        # Bila tidak memberi kata kata yang sama di output file
        if char.startswith('@'):
            print('(M)',end=' ',file=new_file)
            mention+=1
        elif char.startswith('#'):
            print('(H)',end=' ',file=new_file)
            hashtag+=1
        elif char.startswith('www.'):
            print('(U)',end=' ',file=new_file)
            url+=1
        else:
            print(char,end=' ',file=new_file)
    # Ketika sudah selesai mengiterasi kata di 1 baris , memberikan newline
    print('',file=new_file)
else:
    # Setelah iterasi tiap baris selesai mengeprint jumlah @/#/www.
    print('',file=new_file)
    print('#'*15,file=new_file)
    print(f'Mention : {mention:>5d}',file=new_file)
    print(f'Hashtag : {hashtag:>5d}',file=new_file)
    print(f'Url     : {url:>5d}',file=new_file)
    print(f'Output berhasil ditulis pada {file_output}')

# Setelah selesai , menggunakan loop untuk mengecek apakah user mengakhiri program dengan 'enter'
keluar()

# Mengeclose file yang telah dibuka :D
old_file.close()
new_file.close()
