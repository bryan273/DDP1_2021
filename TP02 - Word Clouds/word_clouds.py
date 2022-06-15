# Mengimport fungsi punctuation , dan fungsi dari html_functions.py 
from string import punctuation
from html_functions import make_HTML_box , make_HTML_word , print_HTML_file

# Mengeprint sesuai kriteria dan memberi input nama file 
print('''Program untuk membuat word cloud dari text file
---------------------------------------------
hasilnya disimpan sebagai file html,
yang bisa ditampilkan di browser.
''')

input_file=input('Silakan masukan nama file: ')

print(f'''
{input_file} : 
56 kata diurutkan berdasarkan jumlah kemunculan dalam pasangan (jumlah:kata)
''')

# Membuka dan membaca file input dan stop words
open_file=open(input_file,'r')
read_file=open_file.read()
stop_word=open('stopwords.txt','r')
read_stop_word=stop_word.read()

# Menghilangkan setiap punctuation dari paling depan atau belakang setiap kata
# Jika setelah punctuation dihilangkan , isi kata-nya kosong ,maka IndexError ketika indexing dan masuk ke except
word_without_punctuation = []
for char in read_file.split():
    try:
        while True:
            if char[0] in list(punctuation):
                char=char.replace(char[0],'')
                continue
            elif char[-1] in list(punctuation):
                char=char.replace(char[-1],'')
                continue
            else:
                word_without_punctuation.append(char)
                break
    except IndexError:
        pass

# Menghilangkan stop words menggunakan list comprehension
clear_word= [ var for var in [word.lower() for word in word_without_punctuation] if var not in read_stop_word.split()]

# Menghitung jumlah setiap kata yang sudah tidak ada stop word
dictionary={}
for i in clear_word:
    if i not in dictionary:
        dictionary[i]=1
    else:
        dictionary[i]+=1

# Mengurutkan berdasar jumlah kata muncul dan alphabet dengan urutan terbalik dan mengambil tiap key , value
dictionary=dict(sorted(dictionary.items() , key = lambda x : (x[1],x[0]) , reverse=True ))
item=list(dictionary.items())

# Memberi output nama kata dan jumlah kata muncul 56 pertama dengan 4 kolom dan 14 baris
for n in range(0,14):
    print(f'{item[4*n][1]:<2d}:{item[4*n][0]:<18s}{item[4*n+1][1]:<2d}:{item[4*n+1][0]:<18s}',end='')
    print(f'{item[4*n+2][1]:<2d}:{item[4*n+2][0]:<18s}{item[4*n+3][1]:<2d}:{item[4*n+3][0]:<18s}\n')

# Mengecek input enter dari user
while True:
    enter=input('Tekan Enter untuk keluar …')
    if enter=='':
        break

# Mengambil 56 kata yang diurutkan kemudian mengurutkannya berdasar alphabet , dan juga
# Menghitung jumlah kata yang muncul terbanyak dan terdikit
item=item[0:56]
high_count = item[0][1]
low_count = item[-1][1]
item=sorted(item)

# Membuat file output html dengan kriteria yang telah ditentukan
body = ''
for word, cnt in item:
    body = body + " " + make_HTML_word(word, cnt, high_count, low_count)
box = make_HTML_box(body)
print_HTML_file(box, input_file)

# Menutup file
open_file.close()
stop_word.close()