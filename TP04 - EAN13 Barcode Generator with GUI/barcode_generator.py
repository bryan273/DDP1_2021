from tkinter import *
from tkinter.messagebox import showerror

# Membuat kelas untuk Barcode Logic (perhitungan barcode)
class BarcodeLogic:

    # Menginisiasi dictionary untuk encoding first digit , encoding L , G , R
    def __init__(self):
        self.first_digit = {0:'LLLLLL', 1:'LLGLGG', 2:'LLGGLG', 3:'LLGGGL', 4:'LGLLGG', 
        5:'LGGLLG', 6:'LGGGLL', 7:'LGLGLG', 8:'LGLGGL', 9:'LGGLGL'}
        self.encoding_L = {0:'0001101', 1:'0011001', 2:'0010011', 3:'0111101', 4:'0100011',
        5:'0110001', 6:'0101111', 7:'0111011', 8:'0110111', 9:'0001011'}
        self.encoding_R = self.calculate_R()
        self.encoding_G = self.calculate_G()
    
    # Membuat encoding R , yang berupa komplemen dari encoding L
    def calculate_R(self):
        value = list(self.encoding_L.values())
        encoding_R = {}
        for i in range(10):
            encoding_R[i] = ''.join(list(map(lambda x : '0' if int(x) else '1',value[i])))
        return encoding_R
    
    # Membuat encoding G , yang berupa invers dari encoding R
    def calculate_G(self):
        encoding_G = {}
        for key,item in self.encoding_R.items():
            encoding_G[key] = item[::-1]
        return encoding_G

    # Mendapat nilai encoding first digit dari value
    def get_first(self,value):
        return self.first_digit[int(value)]
    
    # Mendapat nilai encoding L dari value
    def get_L(self,value):
        return self.encoding_L[int(value)]
    
    # Mendapat nilai encoding R dari value
    def get_R(self,value):
        return self.encoding_R[int(value)]
    
    # Mendapat nilai encoding G dari value
    def get_G(self,value):
        return self.encoding_G[int(value)]
    
    # Menghitung nilai checkdigit 
    def checkdigit(digit):
        sum_1 = sum(map(int,digit[0::2]))
        sum_2 = sum(map(int,digit[1::2]))*3
        chck_dgt = (sum_1 + sum_2)%10
        return str(10 - chck_dgt) if chck_dgt!=0 else str(chck_dgt)  

# Class untuk membuat GUI Barcode
class BarcodeWindow(Frame):

    # Meng-inherit master dari Frame
    def __init__(self, cv_size ,master=None):
        super().__init__(master)
        self.pack()
        self.master.title("EAN-13")
        self.cv_size = cv_size
        self.create_widgets()
    
    # Membuat widget
    def create_widgets(self):

        # Membuat Label dan Entry untuk nama_file.eps
        self.lbl_save = Label(self,text='Save Barcode to PS file [eg: EAN13.eps]:',font=('Arial 12 bold'))
        self.lbl_save.pack()

        self.name = StringVar()
        self.ent_save = Entry(self,textvariable= self.name,font=('Arial 12'))
        self.ent_save.bind('<Return>',self.validation) # Ketika klik enter , dilakukan validasi dahulu
        self.ent_save.pack()

        # Membuat Label dan Entry untuk angka code
        self.lbl_code = Label(self,text='Enter code (first 12 decimal digits):',font=('Arial 12 bold'))
        self.lbl_code.pack()

        self.code = StringVar()
        self.ent_code = Entry(self,textvariable=self.code,font=('Arial 12'))
        self.ent_code.bind('<Return>',self.validation) # Ketika klik enter , dilakukan validasi dahulu
        self.ent_code.pack(pady=(0,5))

        # Membuat canvas kosong
        self.cv = Canvas(self, width=self.cv_size, height=self.cv_size, bg='white')
        self.cv.pack(pady=(5,10),padx=10)

    # Mendapatkan checkdigit yang dihitung di class BarcodeLogic
    def get_checkdigit(self):
        digit = self.code.get()
        return BarcodeLogic.checkdigit(digit)

    # Memvalidasi input user 
    def validation(self,_):
        save = self.name.get()
        code = self.code.get()

        # Kondisi tidak valid
        if not code.isdigit() or len(code)!=12 or not save.endswith('.eps') :
            showerror('Wrong input!','Please enter correct input code')
        else:
            # Jika valid barulah membuat Barcode
            self.create_barcode()

    # Untuk menge-save file ean-13
    def save_eps(self):
        self.cv.postscript(file = f"{self.name.get()}")
        # Jika setelah membuat barcode , textfield di Entry ingin kosong , uncomment di bawah ini
        # self.code.set('') , self.name.set('')

    # Membuat barcode
    def create_barcode(self):
        # Clear all barcode sebelumnya jika ada (jadi ketika membuat barcode baru tidak stacked)
        self.cv.delete('all')

        # Membuat text canvas di tengah atas
        txt_x = self.cv_size/2
        txt_y = self.cv_size/6
        self.cv.create_text(txt_x, txt_y, text="EAN-13 Barcode:", font=('Arial 16 bold'))
        self.cv.pack()
        
        # Mengatur panjang bar (yang vertikal) , dari titik y1 sampai y2 , serta panjang bar start middle end
        y1 = 2*self.cv_size/8
        y2 = 6*self.cv_size/8
        y2_SME = y2 + 8

        # Mengatur lebar bar (yang horizontal) / sb x , dengan lebar tiap bar = 2 px (total 95 bar)
        brcode_width = 2*95

        # Mengatur start posisi x bar supaya barcode berada di tengah
        x_left = self.cv_size/2 - brcode_width/2
        
        # Mendapatkan code barcode + check digit
        barcode = self.code.get()+ self.get_checkdigit()

        # Melokasikan angka pertama di sisi kiri , dan text check digit di tengah bawah
        self.cv.create_text(x_left-7, y2+14, text=barcode[0], font=('Arial 12 bold'))
        self.cv.create_text(self.cv_size/2, y2+40, text=f'Check Digit: {barcode[-1]}', 
                            font=('Arial 15 bold'),fill='orange')

        x1 = x_left   # Membuat shallow copy variabel x1
        init = BarcodeLogic()

        # Mengeloop 15 barcode section , Start middle end + 12 code
        for i in range(15):
            # Membuat bar untuk start middle end
            if i in [0,7,14]:
                # Line untuk Middle
                if i==7:
                    for j in range(5):
                        self.cv.create_line([x1,y1 ,x1, y2_SME ],width=2, fill= ('blue' if j%2 else ''))
                        x1 +=2   # x1 bertambah 2 , supaya bar tidak menumpuk (jadi menyamping)  

                # Line untuk start end
                else: 
                    for j in range(3):
                        self.cv.create_line([x1,y1 ,x1, y2_SME ],width=2, fill= ('' if j%2 else 'blue'))
                        x1 +=2
            else:
                # Kondisi untuk 6 code pertama encoding L or G
                if i in range(1,7):
                    barcode_first = barcode[0] # example : 3 068320 05500 then (3)
                    struct = init.get_first(barcode_first) # example : 3 -> LLGGGL
                    encode = init.get_L if struct[i-1] == 'L' else init.get_G # get_L if index(i-1)='L' else get_G
                    self.cv.create_text(x1+7, y2+14, text=barcode[i], 
                                       font=('Arial 12 bold')) # Membuat angka code ke-1 s/d ke-6 di posisi tengah

                    # loop setiap bit di encode ke G / L dari kode ke-i 
                    # ex : encode = get_L , barcode[i] = 1  -> get_L(1) = '0011001'
                    for var in encode(barcode[i]): 
                        self.cv.create_line([x1,y1 ,x1, y2 ],width=2, fill= ('green' if int(var) else ''))
                        x1 +=2

                # Kondisi untuk 6 code belakang dengan encoding R
                elif i in range(8,14):
                    encode = init.get_R(barcode[i-1])
                    self.cv.create_text(x1+7, y2+14, text=barcode[i-1], font=('Arial 12 bold'))
                    # Mengeloop isi bit setelah angka di-encoded
                    for var in encode:
                        self.cv.create_line([x1,y1 ,x1, y2 ],width=2, fill= ('green' if int(var) else ''))
                        x1 +=2
        # Save file
        self.save_eps()

def main():
    cv_size = 300 
    my_gui = BarcodeWindow(cv_size)
    my_gui.mainloop()

if __name__ == '__main__':  
    main()