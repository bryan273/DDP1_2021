# Membuat default skor variabel 
Happiness = 50
Sadness = 50
Anger = 50

input_file=input('Masukkan nama file input: ')

# Mengecek input file yang akan di open kosong , tidak ada atau ada isinya
try:
    open_file= open(input_file,'r')
    read_file=open_file.read()
    if read_file=='':
        print('File input ada tapi kosong :(')
        exit()
except IOError:
    print('File input tidak ada :(')
    exit()

# Membuat fungsi untuk mengubah skor kalau menemukkan emote smile
def smile():
    global Happiness,Sadness
    Happiness+=9
    Sadness-=6

# Membuat fungsi untuk mengubah skor kalau menemukkan emote sad
def sad():
    global Anger,Sadness
    Sadness+=10
    Anger-=8

# Membuat fungsi untuk mengubah skor kalau menemukkan emote angry
def angry():
    global Anger,Happiness
    Anger+=13
    Happiness-=5

# Membuat fungsi untuk menemukan emote dan mengevaluasi setiap skor emote di chat Pak Chanek
def final_score():
    open_file.seek(0)
    for line in open_file:
        if line.startswith('Pak Chanek'):
            for word in line.split():
                if word=='(smile)':
                    smile()
                    evaluate()
                elif word=='(sad)':
                    sad()
                    evaluate()
                elif word=='(angry)':
                    angry()
                    evaluate()    

# Membuat fungsi untuk mereplace huruf menjadi emote
def emoji_file():
    global read_file
    read_file=read_file.replace('(smile)','\U0001f603')
    read_file=read_file.replace('(sad)','\U0001f622')
    read_file=read_file.replace('(angry)','\U0001f621')
    return read_file

# Membuat fungsi untuk membuat limit skor emote dari 0 sampai 100   
def evaluate():
    global Anger,Happiness,Sadness
    Anger,Happiness,Sadness=[0 if i<0 else i for i in [Anger,Happiness,Sadness] ]  
    Anger,Happiness,Sadness=[100 if i>100 else i for i in [Anger,Happiness,Sadness] ]

# Membuat fungsi untuk mengecek kesimpulan ekspresi Pak Chanek
def expression():
    if Happiness>Sadness and Happiness>Anger:
        return 'Pak Chanek sedang bahagia'
    elif Sadness>Anger and  Sadness>Happiness :
        return 'Pak Chanek sedang sedih'
    elif Anger>Happiness and Anger>Sadness:
        return 'Pak Chanek sedang marah'
    elif Happiness==Sadness and Happiness>Anger:
        return 'Pak Chanek sedang bahagia atau sedih'
    elif Sadness==Anger and  Sadness>Happiness :
        return 'Pak Chanek sedang sedih atau marah'
    elif Anger==Happiness and Anger>Sadness:
        return 'Pak Chanek sedang bahagia atau marah'
    elif Happiness==Anger==Sadness:
        return 'Kesimpulan tidak ditemukan'

# Memanggil fungsi untuk menentukkan skor akhir happiness , sadness ,dan anger
final_score()

# Mengeprint Output dengan format yang ditentukan, seperti skor anger happiness sadness
# Mengeprint isi text file yang sudah diconvert dari kata kata menjadi emoji dan menge-print kesimpulan ekspresi
print(f'''
{emoji_file()}

Mengukur suasana hati....

##### Hasil Pengukuran #####
Happiness = {Happiness} | Sadness = {Sadness} | Anger = {Anger}

##### Kesimpulan #####
{expression()}.''')

# Menge-close file
open_file.close()