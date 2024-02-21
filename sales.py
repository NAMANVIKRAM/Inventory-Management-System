from tkinter import *
import mysql.connector
from tkinter import ttk,messagebox
from PIL import Image, ImageTk
from tkinter import ttk
import os

class salesClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x500+220+130")#width and height and Xaxis and top
        self.root.title("Inventory Management System | Developed by: Naman Vikram")
        self.root.config(bg="white")
        self.root.focus_force()

        self.var_invoice = StringVar()
        self.bill_list=[]

        #*****TITLE*****
        lbl_title=Label(self.root,text="View Customer Bills",font=("times new roman",18,"bold"),bg="#184a45",fg="white",bd=4,relief=RIDGE).pack(side=TOP,fill=X,padx=10,pady=20)
        
        
        lbl_invoice=Label(self.root,text="Invoice no.",font=("times new roman",15,"bold"),bg="white").place(x=50,y=100)
        txt_invoice=Entry(self.root,textvariable=self.var_invoice,font=("times new roman",15),bg="lightyellow").place(x=160,y=100,width=180,height=30)
        
        btn_search=Button(self.root,text="Search",command=self.search,font=("times new roman",15,"bold"),bg="#4caf50",fg="white",cursor="hand2").place(x=360,y=100,width=120,height=30)
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("times new roman",15,"bold"),bg="gray",fg="white",cursor="hand2").place(x=490,y=100,width=120,height=30)
        
        #*******Bill List********
        sales_frame=Frame(self.root,bd=3,relief=RIDGE)
        sales_frame.place(x=50,y=140,width=200,height=380)

        scrolly=Scrollbar(sales_frame,orient=VERTICAL)

        self.Sales_List=Listbox(sales_frame,font=("times new roman" ,15,"bold"),bg="white",bd=2,relief=RIDGE,yscrollcommand=scrolly.set)
        scrolly.pack(side=RIGHT,fill=Y)
        scrolly.config(command=self.Sales_List.yview)
        self.Sales_List.config(yscrollcommand=scrolly.set)
        self.Sales_List.pack(fill=BOTH,expand=1)
        self.Sales_List.bind("<ButtonRelease-1>", self.get_data)

        #********BILL AREA ******
        bill_frame=Frame(self.root,bd=3,relief=RIDGE)
        bill_frame.place(x=280,y=140,width=410,height=380)

        lbl_title2=Label(bill_frame,text=" Customer Bill Area",font=("times new roman",18,"bold"),bg="orange",fg="white").pack(side=TOP,fill=X)
        
        scrolly2=Scrollbar(bill_frame,orient=VERTICAL)

        self.bill_area=Text(bill_frame,bg="lightyellow",bd=2,relief=RIDGE,yscrollcommand=scrolly2.set)
        scrolly2.pack(side=RIGHT,fill=Y)
        scrolly2.config(command=self.bill_area.yview)
        self.bill_area.config(yscrollcommand=scrolly2.set)
        self.bill_area.pack(fill=BOTH,expand=1)

        #====Image======
        self.bill_photo = Image.open("images/billing.jpg")
        self.bill_photo=self.bill_photo.resize((450, 400),Image.BOX)
        self.bill_photo = ImageTk.PhotoImage(self.bill_photo)
        
        lbl_image=Label(self.root,image=self.bill_photo,bd=0)
        lbl_image.place(x=750,y=120)
        
        self.show()
#===================================
    def show(self):
        del self.bill_list[:]
        self.Sales_List.delete(0,END)

        for i in os.listdir('bill'):
            if i.split('.')[-1]=='txt':
                self.Sales_List.insert(END,i)
                self.bill_list.append(i.split('.')[0])
    
    def get_data(self,ev):
        row=self.Sales_List.curselection()
        filename=self.Sales_List.get(row)
        self.bill_area.delete('1.0',END)
        fp=open(f'bill/{filename}','r')
        for i in fp:
            self.bill_area.insert(END,i)
        fp.close()
        return filename

    def search(self):
        if self.var_invoice.get() == "":
         messagebox.showerror("Error", "Invoice no. should be required", parent=self.root)
        else:
            if self.var_invoice.get() in self.bill_list:
                self.bill_area.delete('1.0', END)
                file_path = f'bill/{self.var_invoice.get()}.txt'
                if os.path.exists(file_path):
                    fp = open(file_path, 'r')
                    for i in fp:
                        self.bill_area.insert(END, i)
                    fp.close()
                else:
                    messagebox.showerror("Error", "File not found for the given Invoice no.", parent=self.root)
            else:
                messagebox.showerror("Error", "Invalid Invoice no.", parent=self.root)

    
    def clear(self):
        self.show()
        self.bill_area.delete('1.0',END)




if __name__=="__main__":
    root = Tk()
    obj = salesClass(root)
    root.mainloop()