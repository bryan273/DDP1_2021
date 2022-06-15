import tkinter as tk
import tkinter.messagebox as tkmsg

# Membuat class product 
class Product(object):
    def __init__(self, nama, harga, stok):
        self.__nama = nama
        self.__harga = harga
        self.__stok = stok

    # Mendapat nama dari produk
    def get_nama(self):
        return self.__nama

    # Mendapat harga dari produk
    def get_harga(self):
        return self.__harga

    # Mendapat jumlah stok dari produk
    def get_stok(self):
        return self.__stok
    
    # Mengurangi stok bila ada pembelian
    def set_stok(self, jumlah):
        self.__stok -= jumlah

# Membuat class Buyer
class Buyer(object):
    def __init__(self):
        self.__daftar_beli = {}

    # Menambahkan daftar pembelian bila ada yang membeli
    def add_daftar_beli(self, produk, jumlah):
        if produk in self.__daftar_beli:
          self.__daftar_beli[produk] += jumlah
        else :
          self.__daftar_beli[produk] = jumlah

    # Mendapatkan isi daftar beli
    def get_daftar_beli(self):
      return self.__daftar_beli

# Class untuk melihat barang yang dijual
class WindowLihatBarang(tk.Toplevel):
    def __init__(self, product_dict, master = None):
        super().__init__(master)
        self.product_dict = product_dict
        self.wm_title("Daftar Barang")
        self.create_widgets()

    # Membuat widget sesuai ketentuan 
    def create_widgets(self):
        self.lbl_judul = tk.Label(self, \
                                  text = 'Daftar Barang Yang Tersedia').grid(row = 0, column = 1)
        self.lbl_nama = tk.Label(self, \
                                 text = 'Nama Produk').grid(row = 1, column = 0)
        self.lbl_harga = tk.Label(self, \
                                  text = 'Harga').grid(row = 1, column = 1)
        self.lbl_stok = tk.Label(self, \
                                 text = 'Stok Produk').grid(row = 1, column = 2)
        
        i = 2
        for nama, barang in sorted(self.product_dict.items()):
            tk.Label(self, \
                     text = f"{nama}").grid(row = i, column= 0)
            tk.Label(self, \
                     text = f"{barang.get_harga()}").grid(row = i, column= 1)
            tk.Label(self, \
                     text = f"{barang.get_stok()}").grid(row = i, column= 2)
            i += 1

        self.btn_exit = tk.Button(self, text = "EXIT", \
                                  command = self.destroy).grid(row = i, column=1)

# Class untuk membeli barang
class WindowBeliBarang(tk.Toplevel):
    def __init__(self, buyer, product_dict, master = None):
        super().__init__(master)
        self.buyer = buyer
        self.product_dict = product_dict
        self.wm_title("Beli Barang")
        self.geometry("280x140")
        self.create_widgets()

    # Membuat widget sesuai ketentuan
    def create_widgets(self):
        self.lbl_judul = tk.Label(self, \
                                  text = 'Form Beli Barang').grid(row = 0, column = 1)
        self.lbl_nama = tk.Label(self, \
                                 text = 'Nama Barang').grid(row = 1, column = 0)
        self.lbl_stok = tk.Label(self, \
                                 text = 'Jumlah').grid(row = 2, column = 0)

        # Membuat setting untuk Entry user
        self.nama = tk.StringVar()
        self.jumlah = tk.StringVar()
        self.ent_nama_barang = tk.Entry(self,textvariable=self.nama).grid(row=1,column=1)
        self.ent_jumlah = tk.Entry(self,textvariable=self.jumlah).grid(row=2,column=1)
        self.btn_beli = tk.Button(self, text = "BELI", \
                                  command = self.beli_barang).grid(row = 3, column=1)
        self.btn_exit = tk.Button(self, text = "EXIT", \
                                  command = self.destroy).grid(row = 4, column=1)
        self.nama.set('')
        self.jumlah.set('')
        

    def beli_barang(self):
        nama_barang = self.nama.get()
        jumlah = self.jumlah.get()

        # Menampilkan kondisi yang mungkin terjadi
        if nama_barang == "":
            # Bila nama kosong muncul warning
            close = tkmsg.askretrycancel(title='Barang Not Found',message='Nama barang tidak boleh kosong.')
            # Ketika click cancel mengeclose window
            if not close : self.destroy()                

        elif nama_barang not in self.product_dict:
            # Bila nama barang tidak terdaftar
            close = tkmsg.askretrycancel('BarangNotFound',
                    message=f'Barang dengan nama {nama_barang} tidak ditemukan dalam BakungLapak.')
            if not close : self.destroy()

        elif self.product_dict[nama_barang].get_stok() - int(jumlah) < 0:
            # Warning bila stok habis
            tkmsg.showwarning(title='StokEmpty',message='Maaf, stok produk telah habis.')
        else :
            # Melakukan penambahan daftar beli , pengurangan stok
            barang = self.product_dict[nama_barang]
            buyer.add_daftar_beli(barang, int(jumlah))
            barang.set_stok(int(jumlah))
            tkmsg.showinfo("Berhasil!", f"Berhasil membeli {nama_barang} sejumlah {jumlah}")

            # Membuat entry menjadi kosong kembali
            self.nama.set('')
            self.jumlah.set('')

# Membuat class untuk checkout
class WindowCheckOut(tk.Toplevel):
    def __init__(self, buyer, master = None):
        super().__init__(master)
        self.wm_title("Daftar Barang")
        self.daftar_dibeli = buyer.get_daftar_beli()
        self.create_widgets()
        
    # Membuat widget sesuai dengan ketentuan
    def create_widgets(self):
        self.lbl_judul = tk.Label(self, \
                                  text = 'Keranjangku').grid(row = 0, column = 1)
        self.lbl_nama = tk.Label(self, \
                                 text = 'Nama Produk').grid(row = 1, column = 0)
        self.lbl_nama = tk.Label(self, \
                                 text = 'Harga Barang').grid(row = 1, column = 1)
        self.lbl_stok = tk.Label(self, \
                                 text = 'Jumlah').grid(row = 1, column = 2)
        i = 2
       
        if len(self.daftar_dibeli.items()) == 0:
            self.lbl_kosong = tk.Label(self, \
                                 text = 'Belum ada barang yang dibeli :(').grid(row = 2, column = 1)
        else:
            for object,jumlah in self.daftar_dibeli.items():
                self.lbl_nama = tk.Label(self, \
                                    text = f'{object.get_nama()}').grid(row = i, column = 0)
                self.lbl_harga = tk.Label(self, \
                                        text = f'{object.get_harga()}').grid(row = i, column = 1)
                self.lbl_stok = tk.Label(self, \
                                        text = f'{jumlah}').grid(row = i, column = 2)
                i+=1

        self.btn_exit = tk.Button(self, text = "EXIT", \
                                  command = self.destroy).grid(row =i+1, column=1)
        
# Membuat Class Main yang akan memunculkan daftar window utama
class MainWindow(tk.Frame):

    def __init__(self, buyer, product_dict, master = None):
        super().__init__(master)
        self.buyer = buyer
        self.product_dict = product_dict
        self.pack()
        self.create_widgets()

    # Membuat widget sesuai dengan ketentuan
    def create_widgets(self):
        self.label = tk.Label(self, \
                              text = 'Selamat datang di BakungLapak. Silahkan pilih Menu yang tersedia')

        self.btn_lihat_daftar_barang = tk.Button(self, \
                                                 text = "LIHAT DAFTAR BARANG", \
                                                 command = self.popup_lihat_barang )
        self.btn_beli_barang = tk.Button(self, \
                                         text = "BELI BARANG", \
                                         command = self.popup_beli_barang )
        self.btn_check_out = tk.Button(self, \
                                       text = "CHECK OUT", \
                                       command = self.popup_check_out )
        self.btn_exit = tk.Button(self, \
                                  text = "EXIT", \
                                  command = self.master.destroy)

        self.label.pack()
        self.btn_lihat_daftar_barang.pack()
        self.btn_beli_barang.pack()
        self.btn_check_out.pack()
        self.btn_exit.pack()

    # semua barang yand dijual
    def popup_lihat_barang(self):
        WindowLihatBarang(self.product_dict)

    # menu beli barang
    def popup_beli_barang(self):
        WindowBeliBarang(self.buyer, self.product_dict)

    # menu riwayat barang yang dibeli
    def popup_check_out(self):
        WindowCheckOut(self.buyer)

if __name__ == "__main__":

    buyer = Buyer()

    product_dict = {"Kebahagiaan" : Product("Kebahagiaan", 999999, 1),
                    "Kunci TP3 SDA" : Product("Kunci TP3 SDA", 1000000, 660),
                    'a':Product('a',1000,0)}

    m = MainWindow(buyer, product_dict)
    m.master.title("BakungLapak")
    m.master.mainloop()