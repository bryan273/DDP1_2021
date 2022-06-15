
list_jadwal = []
print('Selamat datang! Silakan masukkan jadwal KA: ')

# Menampung isi jadwal yang dimasukan user
while True:
     jadwal = input().split()
     if jadwal == ["selesai"]: break
     else: list_jadwal.append(jadwal)

print('''
Perintah yang tersedia:
1. INFO_TUJUAN
2. TUJUAN_KELAS <tujuan_akhir> <kelas_kereta>
3. TUJUAN_KELAS_TERMURAH <tujuan_akhir> <kelas_kereta>
4. TUJUAN_JAM <tujuan_akhir> <jam_keberangkatan>
5. TUJUAN_JAM_TERMURAH <tujuan_akhir> <jam_keberangkatan>
6. EXIT
''')

# Membuat dictionary untuk masing masing kelas kereta berdasarkan nomor kereta api
dict_class = {'Eksekutif':[100,199],'Bisnis':[200,299],'Ekonomi':[300,399]}

# Membuat fungsi yang mempunyai argumen berupa lists: merupakan isi jadwal kereta , span : range id kereta ataupun id jam keberangkatan
# val: value berupa index pada lists , tujuan : lokasi tujuan kereta , murah : apakah fungsi untuk mencari harga termurah
# Tujuan fungsi untuk mencetak output sesuai dengan kriteria dari argumen (id / jam berada pada range tertentu dan tujuan sesuai )
# Dan juga mencari tiket dengan harga termurah dengan ketentuan yang telah ada
def info(lists,span,val,tujuan,murah=0):
     jadwal_cls = [jadwal for jadwal in lists if eval(f'{span[0]}<={jadwal[val]}<={span[1]}') and jadwal[1]==tujuan]
     if jadwal_cls == []:
          print('Tidak ada jadwal KA yang sesuai.')
     else:
          if murah:
               jadwal_cls = sorted(jadwal_cls ,key= lambda x : int(x[3]))
               jadwal_cls = [i for i in jadwal_cls if int(i[3])==int(jadwal_cls[0][3])]
               for jadwal in jadwal_cls:
                    print(f'KA {jadwal[0]} berangkat pukul {jadwal[2]} dengan harga tiket {jadwal[3]}')
          else:
               for jadwal in jadwal_cls:
                    print(f'KA {jadwal[0]} berangkat pukul {jadwal[2]} dengan harga tiket {jadwal[3]}')

# Looping untuk memasukkan perintah user
while True:
     # Menangani error ketika perintah tidak dapat diindexing
     try:
          perintah = input('Masukkan perintah: ').split()

          # Mencetak output berdasarkan kondisi kriteria yang telah ditentukan
          if perintah == ['INFO_TUJUAN']:
               # Membuat set karena tujuan yang dicetak harus berbeda
               tujuan_berbeda = {kota[1] for kota in list_jadwal}
               print('KA di stasiun ini memiliki tujuan akhir:')
               for kota in tujuan_berbeda : print(kota)

          elif perintah[0] == 'TUJUAN_KELAS':
               info(list_jadwal,dict_class[perintah[2]],0,perintah[1])
          
          elif perintah[0] == 'TUJUAN_JAM':
               info(list_jadwal,[0,perintah[2]],2,perintah[1])

          elif perintah[0] == 'TUJUAN_KELAS_TERMURAH':
               info(list_jadwal,dict_class[perintah[2]],0,perintah[1],1)
          
          elif perintah[0] == 'TUJUAN_JAM_TERMURAH':
               info(list_jadwal,[0,perintah[2]],2,perintah[1],1)

          elif perintah == ['EXIT']:
               print('Terima kasih sudah menggunakan program ini!')
               break
          else:
               print('Perintah yang dimasukkan tidak valid.') 
          print()
     except :
          print('Perintah yang dimasukkan tidak valid.')     
          print()     

