# -*- coding: utf-8 -*-
import string
import matplotlib.pyplot as plt

# fungsi yang mengembalikan set berupa stop word
def load_stop_words(filename):

    open_file = open(filename,'r')
    stop_words = set(open_file.read().split())

    open_file.close()
    return stop_words

# fungsi untuk menghilangkan punctuation , stop word dan menghitung jumlah tiap kata
def count_words(filepath, stop_words):

    open_file = open(filepath ,'r',encoding="utf-8")
    polarity = open_file.read().split()
    punct = string.punctuation

    # Menghilangkan punctuation dan stop word
    no_punct = [word for word in polarity if word not in punct]
    no_stopwords = [word.lower() for word in no_punct if word.lower() not in stop_words]

    # Menghitung jumlah masing masing kata
    word_freq = {}
    for word in no_stopwords:
        if word not in word_freq:
            word_freq[word]=1
        else:
            word_freq[word]+=1

    open_file.close()
    return word_freq       

# Menghitung ndsi masing masing kata dari kata yang negatif dan positif
def compute_ndsi(word_freq_pos, word_freq_neg):

    # Mengambil semua kata kata unique
    all_word = list(set(word_freq_neg) | set(word_freq_pos))

    # Menghitung ndsi masing masing kata
    word_ndsi = {}
    for word in all_word:
        ndsi = (word_freq_pos.get(word,0) - word_freq_neg.get(word,0)) / \
               (word_freq_pos.get(word,0) + word_freq_neg.get(word,0))
        word_ndsi[word] = ndsi

    return word_ndsi

# Fungsi untuk membuat histogram plot
def show_ndsi_histogram(word_ndsi):
    
    ndsi_scores = [score for _, score in word_ndsi.items()]
    plt.hist(ndsi_scores, 100, facecolor = 'g', alpha = 0.75)
    plt.yscale("log")
    plt.xlabel('NDSI score')
    plt.ylabel('Frekuensi')
    plt.savefig("ndsi-hist.pdf")




if __name__ == "__main__":

    # memuat stop words ke sebuah set
    stop_words = load_stop_words("stopwords.txt")

    # menghitung word frequency untuk file berisi kalimat-kalimat sentiment positif
    word_freq_pos = count_words("./sent-polarity-data/rt-polarity.pos", stop_words)

    # menghitung word frequency untuk file berisi kalimat-kalimat sentiment negatif
    word_freq_neg = count_words("./sent-polarity-data/rt-polarity.neg", stop_words)

    # hitung NDSI untuk semua kata-kata pada kedua jenis dictionary berisi word frequency
    word_freq_ndsi = compute_ndsi(word_freq_pos, word_freq_neg)

    # tampilkan histogram dari nilai-nilai NDSI yang dihasilkan
    show_ndsi_histogram(word_freq_ndsi)

    # Mengurutkan kata sesuai ndsi
    word_freq_ndsi = sorted(word_freq_ndsi.items(),key = lambda x : (x[1],x[0]))

    # Menyimpan hasil di ndsi.txt
    ndsi_filename = "ndsi.txt"
    new_file = open(ndsi_filename,'w')
    for char,val in word_freq_ndsi:
        print(char,val,file=new_file)
    new_file.close()