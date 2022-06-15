from itertools import combinations

MENIT_DALAM_JAM = 60
MENIT_DALAM_HARI = 60 * 24

HARI = [i * MENIT_DALAM_HARI for i in range(7)]
JAM = [i * MENIT_DALAM_JAM for i in range(24)]

MATKUL_TERSEDIA = [
["ddp 1 a",     HARI[0] + JAM[8] + 0,    HARI[0] +  JAM[9] + 40],
["ddp 1 a",     HARI[2] + JAM[8] + 0,    HARI[2] +  JAM[9] + 40],
["ddp 1 b",     HARI[1] + JAM[8] + 0,    HARI[1] +  JAM[9] + 40],
["manbis",      HARI[0] + JAM[9] + 0,    HARI[0] + JAM[10] + 40],
["matdis 1 a",  HARI[2] + JAM[9] + 0,    HARI[2] + JAM[10] + 40],
["matdis 1 b",  HARI[0] + JAM[9] + 0,    HARI[0] + JAM[10] + 40]
]



hari_huruf = ['Senin','Selasa','Rabu','Kamis','Jumat','Sabtu','Minggu']
matkul_user = []

# Membuat loop untuk melakukan penyusunan jadwal 
while True:
  print('''=========== SUSUN JADWAL ===========
  1  Add matkul
  2  Drop matkul
  3  Cek ringkasan
  4  Lihat daftar matkul 
  5  Selesai 
  ====================================
  ''')

  pilihan = input('Masukkan pilihan: ').strip()
  # Melakukan tambahan matkul bila matkul ada di dalam matkul tersedia
  if pilihan == '1':
    matkul = input('Masukkan nama matkul: ').strip().lower()
    matkul_dipilih = [daftar for daftar in MATKUL_TERSEDIA if matkul in daftar ]
    print('Matkul tidak ditemukan') if matkul_dipilih == [] else matkul_user.extend(matkul_dipilih)
    print()

  # Melakukan drop matkul bila matkul ada di dalam matkul user
  elif pilihan == '2':
    matkul = input('Masukkan nama matkul: ').strip().lower()
    matkul_didrop = [daftar for daftar in matkul_user if matkul in daftar ]
    if matkul_didrop == []:
            print('Matkul tidak ditemukan') 
    else:
        for drop in matkul_didrop:
                matkul_user.remove(drop)
    print()

  #  Mengecek apakah ada jadwal yang bentrok
  elif pilihan == '3':
      bentrok = 0
      # Mengurutkan jadwal matkul
      matkul_sort = sorted(matkul_user, key = lambda x : (x[1],x[0]))
      # Bila ada kombinasi 2 matkul yang jam start matkul kedua <= jam end matkul pertama , maka bentrok
      for i,j in combinations(matkul_sort,2):
          if j[1]<=i[2]:
              bentrok +=1
              print('\t'+i[0]+' bentrok dengan '+j[0]) 
      if bentrok == 0:
          print('Tidak ada mata kuliah yang bermasalah')
      print()
    
  elif pilihan == '4' :
      # Kondisi dimana tidak ada matkul yang terdaftar
      if matkul_user == []:
          print("Tidak ada matkul yang diambil")
      else:
          # Mengurutkan mata kuliah dan memberi output sesuai urutan start (hari dan jam),
          # Kemudian jika start sama diurutkan berdsarkan nama alphabet
          matkul_sort = sorted(matkul_user, key = lambda x : (x[1],x[0]))
          print('daftar matkul:')
          for matkul in matkul_sort:
              hari_start = str(hari_huruf[matkul[1]//(24*60)]) + ','
              hari_end = str(hari_huruf[matkul[2]//(24*60)]) + ','
              print(f'\t{matkul[0].upper():<16s} ',
                  f'{hari_start:<9}',
                  f'{matkul[1]%(24*60)//60:0>2d}.{matkul[1]%(24*60)%60:0>2d}   s/d ',
                  f'{hari_end:<9}',
                  f'{matkul[2]%(24*60)//60:0>2d}.{matkul[2]%(24*60)%60:0>2d}')
      print()

  # Program berakhir jika pilihan user meminta selesai
  elif pilihan == '5':
    print('Terima kasih!\n')
    exit()
  # Kondisi dimana pilihan user tidak sesuai
  else:
    print('Maaf, pilihan tidak tersedia\n')

