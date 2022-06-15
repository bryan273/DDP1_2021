# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

# Load file ndsi dan return dictionary berisi kata kata dan nilai ndsi-nya
def load_ndsi(ndsi_filename):
    ndsi = open(ndsi_filename,'r')  
    word_ndsi = {}
    for char in ndsi:
        word,val = char.split()
        word_ndsi[word] = val
        
    ndsi.close()
    return word_ndsi

# Menghitung nilai berorientasi positif dan negatif pada setiap baris di filename
def compute_score(filename, word_ndsi):

    unknown_label = open(filename,'r',encoding="utf-16-le")
    pos_neg_scores = []

    # Loop setiap baris
    for sentence in unknown_label:
        pos = 0.
        neg = 0.

        # Mengecek score kata kata positif dan negatif pada tiap baris
        for word in sentence.split():

            value = float(word_ndsi.get(word,0))
            if value >= 0:
                pos += value
            else:
                neg += abs(value)

        pos_neg_scores.append((pos,neg))

    unknown_label.close()
    return pos_neg_scores

# Fungsi untuk menampilkan scatter plot
def show_scatter_plot(pos_neg_scores):

    plt.clf()

    predicted_as_pos = [(pos_score, neg_score) for (pos_score, neg_score) \
                        in pos_neg_scores if pos_score > neg_score]
    predicted_as_neg = [(pos_score, neg_score) for (pos_score, neg_score) \
                        in pos_neg_scores if pos_score < neg_score]

    x_pos_1 = [pos_score for (pos_score, _) in predicted_as_pos]
    y_pos_1 = [neg_score for (_, neg_score) in predicted_as_pos]
    x_pos_2 = [pos_score for (pos_score, _) in predicted_as_neg]
    y_pos_2 = [neg_score for (_, neg_score) in predicted_as_neg]

    plt.scatter(x_pos_1, y_pos_1, color = 'blue', s = 5)
    plt.scatter(x_pos_2, y_pos_2, color = 'hotpink', s = 5)

    plt.xlabel("Positive Score")
    plt.ylabel("Negative Score")
    plt.xlim(-0.1, 8)
    plt.ylim(-0.1, 8)
    plt.savefig("senti-plot.pdf")



if __name__ == "__main__":

    # memuat dictionary berisi kata dan nilai NDSI-nya
    word_ndsi = load_ndsi("ndsi.txt")

    # Menghitung nilai
    pos_neg_scores = compute_score("sent-unknown-label-utf-16-le.txt", word_ndsi)

    # Menampilkan scatter plot
    # dokumen yang netral tidak diiukutsertakan.
    show_scatter_plot(pos_neg_scores)

    # untuk setiap kalimat (setiap baris di sent-unknown-label.txt),
    # jika nilai positif > nilai negatif --> predicted label: positif
    # jika nilai positif < nilai negatif --> predicted label: negatif
    # else --> predicted label: netral (hampir tidak ada sepertinya)
    for i, (pos_score, neg_score) in enumerate(pos_neg_scores):
        predicted_label = "neutral"
        if pos_score > neg_score:
            predicted_label = "pos"
        elif neg_score > pos_score:
            predicted_label = "neg"
        
        print(f"sentence {i+1} -- pos:{pos_score:6.3f}  neg:{neg_score:6.3f}  prediction:{predicted_label}")
