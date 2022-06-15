import re
from typing import Pattern

# Main class yang atribut akan diturunkan ke seller dan buyer
class User() :
    def __init__(self, user_name, tipe):
        self.__user_name = user_name
        self.__tipe = tipe

# Class Seller untuk orang yang ingin berjualan
class Seller(User) : 

    # Atribut seller yaitu username, tipe, pemasukan , list barang jual
    def __init__(self, tipe ,  user_name):
        super().__init__(user_name, tipe)
        self.__pemasukan = 0
        self.__list_barang_jual = []

    # Mendapatkan jumlah pemasukan
    def get_pemasukan(self) : 
        return self.__pemasukan

    # Menambah nilai pemasukan sebesar value
    def add_pemasukan(self, value) : 
        self.__pemasukan += value
    
    # Mengurangi stok setiap ada pembelian
    def subs_stok(self,nama):
        Product.all_product[nama][2] -= 1
        
    # Menambah produk ke class product dan list barang jualan seller bila belum pernah terdaftar
    def tambah_product(self, nama, harga, stock, penjual) :
        if nama in Product.all_product:
            print("Produk sudah pernah terdaftar")
        else:
            self.__list_barang_jual.append(nama)
            Product(nama,int(harga),int(stock),penjual)

    # Melihat produk jualan seller yang sudah di sorted
    def lihat_daftar_produk_saya(self) : 
        print("\nBerikut merupakan barang jualan saya")
        print("-------------------------------------")
        print("  Nama Produk  |   Harga   | Stock ")
        print("-------------------------------------")
        sorted_product = sorted(self.__list_barang_jual)
        for product in sorted_product :
            data_produk = Product.all_product[product] 
            print(f'{data_produk[0]:<16}| {data_produk[1]:<11}| {data_produk[2]:<7}')
        print("-------------------------------------\n")

    # Menampilkan menu yang akan dipilih oleh seller
    def menu(self,perintah,penjual) : 
        if perintah == '1':
            nama, harga, stock = input('Masukkan data produk : ').split()
            self.tambah_product(nama, harga, stock, penjual)
        elif perintah == '2':
            self.lihat_daftar_produk_saya()
        elif perintah == '3':
            print(f'Anda telah keluar dari akun {penjual}')
            return True

# Class Buyer untuk orang yang ingin membeli            
class Buyer(User) : 

    # Atribut buyer yaitu tipe , nama , saldo , riwayat pembelian 
    def __init__(self, tipe, user_name, saldo):
        super().__init__(user_name, tipe)
        self.__saldo = int(saldo)
        self.__riwayat = []
    
    # Mendapatkan nilai saldo
    def get_saldo(self):
        return self.__saldo
    
    # Melihat semua nilai produk yang dijual (sorted)
    def lihat_semua_produk(self) : 
        print("\nBerikut merupakan daftar produk di Dekdepedia")
        print("---------------------------------------------------")
        print("  Nama Produk   |   Harga    | Stock  |  Penjual ")
        print("---------------------------------------------------")
        sorted_product = sorted(Product.all_product.values(),key= lambda x : x[0])
        for produk in sorted_product:
                print(f'{produk[0]:<16}| {produk[1]:<11}| {produk[2]:<7}| {produk[3]:<6}')
        print("---------------------------------------------------\n")

    # Membeli produk dari Dekdekpedia
    def beli_produk(self,barang):

        # Mendapatkan data produk
        produk = Product.all_product.get(barang,None)
        if produk == None:
            print(f'Barang dengan nama {barang} tidak ditemukan dalam Dekdepedia.')
        else: 
            nama , harga , stok , penjual = produk
            data_penjual = user_object[penjual]

            # Menangani kasus jika saldo tidak cukup dan stok 0
            if stok == 0:
                print('Maaf, stok produk telah habis.')
            elif self.__saldo < harga: 
                print(f'Maaf, saldo Anda tidak cukup untuk membeli {nama}.') 
            else:
                # Menambahkan riwayat pembelian buyer , mengurangi saldo buyer 
                # Menambahkan pemasukan seller , mengurangi stok seller ketika pembelian berhasil
                print(f'Berhasil membeli {nama} dari {penjual}.')
                self.__riwayat.append(produk)
                self.__saldo -= harga
                data_penjual.add_pemasukan(harga)
                data_penjual.subs_stok(nama)

    # Menampilkan riwayat pembelian buyer (sorted)
    def riwayat_pembelian_saya(self):
        print('Berikut merupakan barang yang saya beli')
        print('----------------------------------------')
        print(' Nama Produk   |   Harga   | Penjual')
        print('----------------------------------------')
        sorted_product = sorted(self.__riwayat,key= lambda x : x[0])
        for produk in sorted_product:
                print(f'{produk[0]:<16}| {produk[1]:<11}| {produk[3]:<6}')
        print('----------------------------------------')
    
    # Menampilkan menu yang akan dipilih buyer
    def menu(self,perintah,pembeli) : 
        if perintah == '1':
            self.lihat_semua_produk()
        elif perintah == '2':
            barang = input('Masukkan barang yang ingin dibeli : ')
            self.beli_produk(barang)
        elif perintah == '3':
            self.riwayat_pembelian_saya()
        elif perintah == '4':
            print(f'Anda telah keluar dari akun {pembeli}')
            return True

# Class produk yang berisi data produk ( 'nama_produk' : ['nama_produk','harga','stock','penjual'] )
class Product : 
    all_product = {}
    def __init__(self, nama, harga, stock, penjual):
        Product.all_product[nama] = [nama, harga, stock, penjual]

# Fungsi mengambil data user dari nama user
def get_user(name, user_data):
    return user_data.get(name,None)

# User data menampung ( nama_user : [tipe_user , nama_user , *saldo] )
# User_object menampung ( nama_user : object_class_user )
user_data = {}
user_object = {}

def main():
    print("\nSelamat datang di Dekdepedia!")
    print("Silakan memilih salah satu menu di bawah:")
    print("1. Sign Up")
    print("2. Log In")
    print("3. Exit\n")

    pilih = input("Pilihan Anda: ")

    # Sign Up untuk user
    if (pilih == "1") : 

        banyak_user = int(input("Jumlah akun yang ingin didaftarkan : "))
        print("Data akun: ")

        # Menampung user yang sign up ke user_data dan menangani beberapa case yang tidak valid
        for i in range (banyak_user) : 
            data = input(str(i+1)+". ").split()

            try:
                tipe , nama , *saldo = data
                pattern = re.compile('[A-Za-z0-9_-]+')

                # Mengecek karakter nama valid dengan menggunakan regular expression
                # Mengecek apakah saldo int dan > 0 , mengecek tipe seller dan buyer
                if ((tipe == "SELLER" and len(data)==2) or (tipe=='BUYER' and len(data)==3)) and \
                    (saldo==[] or int(saldo[0]) > 0)  and (pattern.fullmatch(nama)):
                    if nama in user_data:
                        print('Username sudah terdaftar')
                    else:
                        user_data[nama] = data
                else:
                    print('Akun tidak valid.')
            except:
                print('Akun tidak valid.')

    # Log in untuk user
    elif (pilih == "2") : 

        user_name_login = input("user_name : ")
        user_logged_in = get_user(user_name_login,user_data)

        if user_logged_in == None:
            print(f'Akun dengan user_name {user_name_login} tidak ditemukan')

        # Ketika user sebagai seller
        elif user_logged_in[0] == 'SELLER':
            tipe , nama = user_logged_in
            print(f'Anda telah masuk dalam akun {nama} sebagai {tipe}')
            print(f'\nSelamat datang {nama},')
            print('berikut menu yang bisa Anda lakukan:')
            print('1. TAMBAHKAN_PRODUK')
            print('2. LIHAT_DAFTAR_PRODUK_SAYA')
            print('3. LOG_OUT\n')

            # Membuat object seller dan menge-loop menu seller sampai seller ingin keluar
            if nama not in user_object:
                orang = Seller(*user_logged_in)
                user_object[nama] = orang
            else:
                orang = user_object[nama]
            while True:
                print(f'Pemasukan anda {orang.get_pemasukan()},')
                inp = input('Apa yang ingin Anda lakukan? ')
                keluar = orang.menu(inp, nama)
                if keluar : break
                print()

        # Ketika user adalah buyer
        elif user_logged_in[0] == 'BUYER':
            tipe , nama , saldo = user_logged_in
            print(f'Anda telah masuk dalam akun {nama} sebagai {tipe}')
            print(f'\nSelamat datang {nama},')
            print('berikut menu yang bisa Anda lakukan:')
            print('1. LIHAT_SEMUA_PRODUK')
            print('2. BELI_PRODUK')
            print('3. RIWAYAT_PEMBELIAN_SAYA')
            print('4. LOG_OUT\n')

            # Membuat object buyer dan menge-loop menu buyer sampai buyer ingin keluar
            if nama not in user_object:
                orang = Buyer(*user_logged_in)
                user_object[nama] = orang
            else:
                orang = user_object[nama]
            while True:
                print(f'Saldo anda {orang.get_saldo()},')
                inp = input('Apa yang ingin Anda lakukan? ')
                keluar = orang.menu(inp, nama)
                if keluar : break
                print()
                
    elif (pilih == "3") : 
        print("Terima kasih telah menggunakan Dekdepedia!")
        exit()
    print()

if __name__ == "__main__":
    while True:
        main()