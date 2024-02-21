import time
from tkinter import *
import mysql.connector
from tkinter import ttk,messagebox
from PIL import Image, ImageTk
import os
import tempfile



class BillClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Management System | Developed by: Naman Vikram")
        self.root.config(bg="white")
    
        self.cart_list=[]
        self.chk_print=0
        #******Title*****


        original_image = Image.open("images/image1.png")


        max_width = 100  
        max_height = 70 
        original_image=original_image.resize((max_width, max_height),Image.BOX)


        self.icon_title = ImageTk.PhotoImage(original_image)

        title = Label(self.root, text="Inventory Management System", image=self.icon_title, compound=LEFT,font=("times new roman", 40, "bold"), bg="#010c48", fg="white", anchor="w", padx=20).place(x=0, y=0, relwidth=1, height=70)
   
        btn_logout=Button(self.root,text="Logout",command=self.logout,font=("times new roman",15,"bold"),bg="yellow",cursor="hand2").place(x=1100,y=10,height=50,width=150)

        #******Clock*****
        self.lbl_clock=Label(self.root,text="Welcome to Inventory Management System\t\t Date:DD/MM/YYYY\t\t\t    Time:HH/MM/SS ",font=("times new roman",15),bg="#4d636d",fg="white")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)
        
        #======Product_Frame=====
        ProductFrame=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        ProductFrame.place(x=6,y=110,width=410,height=550)

        pTitle=Label(ProductFrame,text="All Products",font=("times new roman",20,"bold"),bg="#0f4d7d",fg="white").pack(side=TOP,fill=X)
        
        
        #===== PRODUCTSEARCH FRAME===
        self.var_search=StringVar()

        ProductFrame2=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        ProductFrame2.place(x=12,y=155,width=398,height=90)
        
        lbl_search=Label(ProductFrame2,text="Search Product | By Name",font=("times new roman",15,"bold"),bg="white",fg="green").place(x=2,y=5)

        
        lbl_search=Label(ProductFrame2,text="Product Name",font=("times new roman",15,"bold"),bg="white").place(x=5,y=45)

        txt_search=Entry(ProductFrame2,textvariable=self.var_search,font=("times new roman",15),bg="lightyellow").place(x=135,y=47,width=150,height=25)

        btn_search=Button(ProductFrame2,text="Search",command=self.search,font=("times new roman",15),bg="#2196f3",fg="white",cursor="hand2").place(x=290,y=45,width=100,height=30)
        btn_show_all=Button(ProductFrame2,text="Show All",command=self.show,font=("times new roman",15),bg="#083531",fg="white",cursor="hand2").place(x=290,y=10,width=100,height=30)
        
        #**********Distributor Details ****
        cart_Frame=Frame(ProductFrame,bd=3,relief=RIDGE)
        cart_Frame.place(x=2,y=140,width=400,height=385)
        
        scrolly=Scrollbar(cart_Frame,orient=VERTICAL)
        scrollx=Scrollbar(cart_Frame,orient=HORIZONTAL)

        self.product = ttk.Treeview(cart_Frame, columns=("pid", "name", "price", "qty","status"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.product.xview)
        scrolly.config(command=self.product.yview)

            # Add data to the Treeview
        self.product.heading("pid", text="PID")
        self.product.heading("name", text="Name")
        self.product.heading("price", text="Price")
        self.product.heading("qty", text="QTY")
        self.product.heading("status", text="Status")
        
        self.product["show"] = "headings"

          
        self.product.column("pid", width=60)
        self.product.column("name", width=100)
        self.product.column("price", width=100)
        self.product.column("qty", width=60)
        self.product.column("status", width=80)
        
        self.product.pack(fill=BOTH, expand=1)
        self.product.bind("<ButtonRelease-1>",self.get_data)
        # self.show()
        lbl_Note=Label(ProductFrame,text="Note: Enter 0 Quantity to remove from the cart",font=("times new roman",12,"bold"),anchor ='w',bg="white",fg="red").pack(side=BOTTOM,fill=X)



        #======CustomerFrame======
        self.var_cname=StringVar()
        self.var_contact=StringVar()
        CustomerFrame=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        CustomerFrame.place(x=420,y=110,width=510,height=80) 

        cTitle=Label(CustomerFrame,text="Customer Details",font=("times new roman",20,"bold"),bg="gray",fg="white").pack(side=TOP,fill=X)
        lbl_name=Label(CustomerFrame,text="Name",font=("times new roman",15,"bold"),bg="white").place(x=5,y=40)
        txt_name=Entry(CustomerFrame,textvariable=self.var_cname,font=("times new roman",13),bg="lightyellow").place(x=65,y=42,width=180)

        lbl_contact=Label(CustomerFrame,text="Contact No.",font=("times new roman",15,"bold"),bg="white").place(x=250,y=40)
        txt_contact=Entry(CustomerFrame,textvariable=self.var_contact,font=("times new roman",13),bg="lightyellow").place(x=380,y=42,width=120)

        #=====CAL CART FRAME===

        Cal_Cart_Frame=Frame(self.root,bd=3,relief=RIDGE,bg="white")
        Cal_Cart_Frame.place(x=420,y=200,width=510,height=360) 

        #=====Calculator FRAME======
        self.var_cal_input=StringVar()
        Cal_Frame=Frame(Cal_Cart_Frame,bd=3,relief=RIDGE,bg="white")
        Cal_Frame.place(x=5,y=10,width=270,height=340) 

        self.text_cal_input=Entry(Cal_Frame,textvariable=self.var_cal_input,font=("arial",15,"bold"),width=22,bg="lightyellow",bd=10,justify="right")
        self.text_cal_input.grid(row=0,columnspan=4)

        btn_7=Button(Cal_Frame,text="7",font=("arial",15,"bold"),command=lambda: self.get_input(7),bd=4,width=5,pady=14,cursor="hand2",bg="lightgray")
        btn_7.grid(row=1,column=0)
        btn_8=Button(Cal_Frame,text="8",font=("arial",15,"bold"),command=lambda: self.get_input(8),bd=4,width=5,pady=14,cursor="hand2",bg="lightgray")
        btn_8.grid(row=1,column=1)
        btn_9=Button(Cal_Frame,text="9",font=("arial",15,"bold"),command=lambda: self.get_input(9),bd=4,width=5,pady=14,cursor="hand2",bg="lightgray")
        btn_9.grid(row=1,column=2)
        
        btn_sum=Button(Cal_Frame,text="+",font=("arial",19,"bold"),command=lambda: self.get_input("+")).grid(row=1,column=3)
        
        btn_4=Button(Cal_Frame,text="4",font=("arial",15,"bold"),command=lambda: self.get_input(4),bd=4,width=5,pady=15,cursor="hand2",bg="lightgray")
        btn_4.grid(row=2,column=0)
        btn_5=Button(Cal_Frame,text="5",font=("arial",15,"bold"),command=lambda: self.get_input(5),bd=4,width=5,pady=15,cursor="hand2",bg="lightgray")
        btn_5.grid(row=2,column=1)
        btn_6=Button(Cal_Frame,text="6",font=("arial",15,"bold"),command=lambda: self.get_input(6),bd=4,width=5,pady=15,cursor="hand2",bg="lightgray")
        btn_6.grid(row=2,column=2)
        
        btn_sub=Button(Cal_Frame,text="-",font=("arial",22,"bold"),command=lambda: self.get_input("-")).grid(row=2,column=3)
        
        btn_1=Button(Cal_Frame,text="1",font=("arial",15,"bold"),command=lambda: self.get_input(1),bd=4,width=5,pady=15,cursor="hand2",bg="lightgray")
        btn_1.grid(row=3,column=0)
        btn_2=Button(Cal_Frame,text="2",font=("arial",15,"bold"),command=lambda: self.get_input(2),bd=4,width=5,pady=15,cursor="hand2",bg="lightgray")
        btn_2.grid(row=3,column=1)
        btn_3=Button(Cal_Frame,text="3",font=("arial",15,"bold"),command=lambda: self.get_input(3),bd=4,width=5,pady=15,cursor="hand2",bg="lightgray")
        btn_3.grid(row=3,column=2)

        btn_mul=Button(Cal_Frame,text="*",font=("arial",22,"bold"),command=lambda: self.get_input("*")).grid(row=3,column=3)
        
        btn_0=Button(Cal_Frame,text="0",font=("arial",15,"bold"),command=lambda: self.get_input(0),bd=4,width=5,pady=14,cursor="hand2",bg="lightgray")
        btn_0.grid(row=4,column=0)
        btn_clear=Button(Cal_Frame,text="C",font=("arial",15,"bold"),command=self.clear_cal,bd=5,width=5,pady=14,cursor="hand2",bg="lightgray")
        btn_clear.grid(row=4,column=1)
        btn_equal=Button(Cal_Frame,text="=",font=("arial",15,"bold"),command=self.perform_cal,bd=5,width=5,pady=14,cursor="hand2",bg="lightgray")
        btn_equal.grid(row=4,column=2)
        
        btn_div=Button(Cal_Frame,text="/",font=("arial",22,"bold"),command=lambda: self.get_input("/")).grid(row=4,column=3)



        #=====CART FRAME===
        cart_Frame=Frame(Cal_Cart_Frame,bd=3,relief=RIDGE)
        cart_Frame.place(x=280,y=8,width=220,height=342)
        self.cartTitle=Label(cart_Frame,text="Cart \t Total Product : [0]",font=("times new roman",12),bg="gray",fg="white")
        self.cartTitle.pack(side=TOP,fill=X)
       
        
        scrolly=Scrollbar(cart_Frame,orient=VERTICAL)
        scrollx=Scrollbar(cart_Frame,orient=HORIZONTAL)

        self.Cart = ttk.Treeview(cart_Frame, columns=("pid", "name", "price", "qty"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.Cart.xview)
        scrolly.config(command=self.Cart.yview)

            # Add data to the Treeview
        self.Cart.heading("pid", text="PID")
        self.Cart.heading("name", text="Name")
        self.Cart.heading("price", text="Price")
        self.Cart.heading("qty", text="QTY")
        # self.Cart.heading("status", text="Status")
        
        self.Cart["show"] = "headings"

          
        self.Cart.column("pid", width=40)
        self.Cart.column("name", width=100)
        self.Cart.column("price", width=100)
        self.Cart.column("qty", width=70)
        # self.Cart.column("status", width=90)
        
        self.Cart.pack(fill=BOTH, expand=1)
        self.Cart.bind("<ButtonRelease-1>",self.get_data_cart)
        # self.show()
        # lbl_Note=Label(CartFrame,text="Note: Enter 0 Quantity to remove from the cart",font=("times new roman",12,"bold"),anchor ='w',bg="white",fg="red").pack(side=BOTTOM,fill=X)

        #=====ADD CART Widgets FRAME====
        self.var_pid=StringVar()
        self.var_pname=StringVar()
        self.var_price=StringVar()
        self.var_qty=StringVar()
        self.var_stock=StringVar()

        
        ADD_CartWidgetsFrame=Frame(self.root,bd=3,relief=RIDGE,bg="white")
        ADD_CartWidgetsFrame.place(x=420,y=560,width=510,height=110) 

        p_name=Label(ADD_CartWidgetsFrame,text="Product Name",font=("times new roman",15,"bold"),bg="white").place(x=5,y=5)
        self.txt_p_name=Entry(ADD_CartWidgetsFrame,textvariable= self.var_pname,font=("times new roman",15),bg="lightyellow",state="readonly")
        self.txt_p_name.place(x=5,y=35,width=170,height=22)

        p_price=Label(ADD_CartWidgetsFrame,text="Price Per Qty",font=("times new roman",15,"bold"),bg="white").place(x=200,y=5)
        self.txt_p_price=Entry(ADD_CartWidgetsFrame,textvariable=self.var_price,font=("times new roman",15),bg="lightyellow",state="readonly")
        self.txt_p_price.place(x=200,y=35,width=130,height=22)

        self.lbl_inStock=Label(ADD_CartWidgetsFrame,text="In Stock",font=("times new roman",15,"bold"),bg="white")
        self.lbl_inStock.place(x=5,y=70)

        p_qty=Label(ADD_CartWidgetsFrame,text="Quantity",font=("times new roman",15,"bold"),bg="white").place(x=350,y=5)
        self.txt_p_qty=Entry(ADD_CartWidgetsFrame,textvariable=self.var_qty,font=("times new roman",15),bg="lightyellow")
        self.txt_p_qty.place(x=350,y=35,width=130,height=22)

        btn_clear_cart=Button(ADD_CartWidgetsFrame,text="Clear",command=self.clear_cart,font=("times in  new roman",15,"bold"),bg="gray",cursor="hand2").place(x=150,y=70,width=150,height=30)
        btn_add_cart=Button(ADD_CartWidgetsFrame,text="ADD | Update Cart ",command=self.add_update_cart,font=("times in  new roman",15,"bold"),bg="#FFD700",cursor="hand2").place(x=320,y=70,width=180,height=30)
        # btn_clear_cart=Button(ADD_CartWidgetsFrame,text="Cear",font=("times in  new roman",15,"bold"),bg="gray",cursor="hand2").place(x=180,y=70,width=150,height=30)
        
        #============Billing Area======

        BillFrame=Frame(self.root,bd=3,relief=RIDGE)
        BillFrame.place(x=932,y=110,width=375,height=410)

        bill_title=Label(BillFrame,text="Bill Area",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scrolly=Scrollbar(BillFrame,orient=VERTICAL)
        self.txt_bill_area=Text(BillFrame,yscrollcommand=scrolly.set)
        scrolly.pack(side=RIGHT,fill=Y)
        scrolly.config(command=self.txt_bill_area.yview)
        self.txt_bill_area.pack(fill=BOTH,expand=1)

        #=======Button Frame======
        self.var_amnt=StringVar()
        self.var_discount=StringVar()
        self.var_net_pay=StringVar()    
        

        btn_Frame=Frame(self.root,bd=3,relief=RIDGE)
        btn_Frame.place(x=932,y=520,width=348,height=150)
        
        self.lbl_amnt=Label(btn_Frame,text="Bill Amount\n[0]",font=("times new roman",15,"bold"),bg="lightblue")
        self.lbl_amnt.place(x=2,y=10,width=130,height=90)

        self.lbl_discount=Label(btn_Frame,text="Discount\n[5%]",font=("times new roman",15,"bold"),bg="lightgreen")
        self.lbl_discount.place(x=133,y=10,width=100,height=90)

        self.lbl_net_pay=Label(btn_Frame,text="Net Pay \n[0]",font=("times new roman",15,"bold"),bg="#8B7D6B")
        self.lbl_net_pay.place(x=235,y=10,width=118,height=90)

        # self.txt_amnt=Entry(btn_Frame,textvariable=self.var_amnt,font="arial 15",bg="lightyellow",state="readonly")
        # self.txt_amnt.place(x=150,y=5,width=150,height=22)

        # self.txt_discount=Entry(btn_Frame,textvariable=self.var_discount,font="arial 15",bg="lightyellow",state="readonly")
        # self.txt_discount.place(x=150,y=35,width=150,height=22)

        # self.txt_net_pay=Entry(btn_Frame,textvariable=self.var_net_pay,font="arial 15",bg="lightyellow",state="readonly")
        # self.txt_net_pay.place(x=150,y=75,width=150,height=22)

        btn_gbill=Button(btn_Frame,text="Generate Bill",command=self.generate_bill,font=("times new roman",15,"bold"),bg="orange",cursor="hand2").place(x=2,y=110,width=150,height=30)
        btn_pbill=Button(btn_Frame,text="Print",command=self.print_bill,font=("times new roman",15,"bold"),bg="red",cursor="hand2").place(x=154,y=110,width=100,height=30)
        btn_clear_all=Button(btn_Frame,text="Clear All",command=self.clear_all,font=("times new roman",15,"bold"),bg="pink",cursor="hand2").place(x=255,y=110,width=95,height=30)
        self.show()
        
        self.update_date_time()

        

        



    def get_input(self,num):
        self.var_cal_input.set(self.var_cal_input.get()+str(num))

    def clear_cal(self):
        self.var_cal_input.set("")

    def perform_cal(self):
        result=self.var_cal_input.get()
        self.var_cal_input.set(eval(result))

    def get_data(self,ev):
        f=self.product.focus()
        content=(self.product.item(f))
        row=content["values"]
        self.var_pid.set(row[0])
        self.var_pname.set(row[1])
        self.var_price.set(row[2])
        self.lbl_inStock.config(text=f"In Stock[{str(row[3])}]")
        self.var_stock.set(row[3])
        self.var_qty.set("1")
    
    def get_data_cart(self,ev):
        f=self.Cart.focus()
        content=(self.Cart.item(f))
        row=content["values"]
        self.var_pid.set(row[0])
        self.var_pname.set(row[1])
        self.var_price.set(row[2])
        self.var_qty.set(row[3])
        self.lbl_inStock.config(text=f"In Stock[{str(row[4])}]")
        self.var_stock.set(row[4])
        

    def show(self):
        con=mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="Root",
            database="ims"
        )
        cur=con.cursor()
        
        try:
            cur.execute("select pid, name, price, qty,status from product where status='Active'")
            rows=cur.fetchall()
            
            self.product.delete(*self.product.get_children())
            for row in rows:
                self.product.insert('',END,values=row)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)
        finally:
            con.close()
    
    def search(self):
        con=mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="Root",
            database="ims"
        )
        cur=con.cursor()
        try:
            
            if self.var_search.get() == "":
                messagebox.showerror("Error", "Enter search text", parent=self.root)
            else:
                cur.execute("SELECT pid, name, price, qty,status FROM product where name LIKE %s", '("%" + self.var_search.get() + "%" and status="Active")') 
                rows = cur.fetchall()
                if len(rows) != 0:
                    self.product.delete(*self.product.get_children())
                    for row in rows:
                        self.product.insert('', END, values=row)
                else:                    messagebox.showerror("Error", "No data found !!!")

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)
        finally:
            con.close()
    
    def add_update_cart(self):
        if self.var_qty.get() == "Select" or self.var_pid.get() == "":
            messagebox.showerror("Error", "Please select product from list", parent=self.root)
        elif self.var_qty.get() == "":
            messagebox.showerror("Error", "Quantity is required", parent=self.root)
        elif int(self.var_qty.get())>int(self.var_stock.get()):
            messagebox.showerror("Error", "Invalid Quantity", parent=self.root)
        # elif self.var_qty.get() == "0":
        #     messagebox.showerror("Error", "Quantity is required", parent=self.root)
        else:
            price_cal = self.var_price.get()
            
            # price_cal=int(self.var_qty.get())*float(self.var_price.get())
            # price_cal=float(price_cal)
            # price_cal=self.var_price.get()
            cart_data=[self.var_pid.get(),self.var_pname.get(),price_cal,self.var_qty.get(),self.var_stock.get()]
                
            #======CHECKING TO UPDATE CART========

            present="no"
            index_=0
            for row in self.cart_list:
                if self.var_pid.get() == row[0]:
                    present="yes"
                    break
                index_+=1
            if present=="yes":
                op=messagebox.askyesno("Confirm","Product already present\nDo you want to update|remove from cart?",parent=self.root)
                if op==True:
                    if self.var_qty.get()=="0":
                        self.cart_list.pop(index_)
                    else:
                        # self.cart_list[index_][2]=price_cal
                        self.cart_list[index_][3]=self.var_qty.get()
            else:
                self.cart_list.append(cart_data)
                
            self.show_cart()
            self.bill_update()
    
    def bill_update(self):
        self.bill_amount=0
        self.net_pay=0
        self.discount=0
        for row in self.cart_list:
            self.bill_amount=self.bill_amount + (float(row[2])*int(row[3]))
        self.discount=(self.bill_amount*5) / 100    
        self.net_pay=self.bill_amount -self.discount
        
        self.lbl_amnt.config(text=f"Bill Amount\n{str(self.bill_amount)}")
        self.lbl_net_pay.config(text=f"Net Pay\n{str(self.net_pay)}")
        self.cartTitle.config(text=f"Cart\t Total Product : [{str(len(self.cart_list))}]")
        


    
    def show_cart(self):
        try:
           self.Cart.delete(*self.Cart.get_children())
           for row in self.cart_list:
                self.Cart.insert('',END,values=row)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)

    def generate_bill(self):
        if self.var_cname.get()=="" or self.var_contact.get()=="":
            messagebox.showerror("Error","Customer Details are required",parent=self.root)
        elif len(self.cart_list)==0:
            messagebox.showerror("Error","Please Add product to the cart",parent=self.root)
        else:
            self.bill_top()
            self.bill_middle()
            self.bill_bottom()
            fp=open(f"bill/{str(self.invoice)}.txt","w")
            fp.write(self.txt_bill_area.get("1.0",END))
            fp.close()
            messagebox.showinfo("Saved","Bill has been generated/Save in Backend",parent=self.root)
            self.chk_print=1
            # self.clear_all()
    
    def bill_top(self):
        self.invoice=int(time.strftime("%H%M%S"))+int(time.strftime("%d%m%Y"))
        bill_top_temp=f'''
\t\tXYZ Store
\t Phone No.9999XXXXXX
{str("="*43)}
Customer Name:{self.var_cname.get()}
Contact No.:{self.var_contact.get()}
Bill No.:{str(self.invoice)}\t\t\tDate:{str(time.strftime("%d-%m-%Y"))}
{str("="*43)}
Product\t\tQTY\tPrice
{str("="*43)}
        '''
        self.txt_bill_area.delete("1.0",END)
        self.txt_bill_area.insert("1.0",bill_top_temp)
    
    def bill_bottom(self):
        bill_bottom_temp=f'''
{str("="*43)}
Bill Amount\t\t\tRs.{self.bill_amount}
Discount\t\t\tRs.{self.discount}
Net Pay\t\t\tRs.{self.net_pay}
{str("="*43)}
        '''
        self.txt_bill_area.insert(END,bill_bottom_temp)
    
    def bill_middle(self):
        con=mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="Root",
            database="ims"
        )
        cur=con.cursor()
        try:
            for row in self.cart_list:
                pid=row[0]
                pname=row[1]
                
                qty=int(row[4])-int(row[3])

                if int(row[3])==int(row[4]):
                    status="Inactive"
                if int(row[3])!=int(row[4]):
                    status="Active"
                price=float(row[2])*int(row[3])
                price=str(price)
                self.txt_bill_area.insert(END,"\n "+pname+"\t\t"+row[3]+"\tRs."+str(price))
                
                cur.execute("UPDATE product SET qty=%s, status=%s WHERE pid=%s",(
                    qty,
                    status,
                    pid
                ))
                con.commit()
                
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)
        con.close()
        
         

    def print_bill(self):
        if self.chk_print==1:
            messagebox.showinfo("Print","Please wait while printing",parent=self.root)
            new_file=tempfile.mktemp(".txt")
            open(new_file,"w").write(self.txt_bill_area.get("1.0",END))
            os.startfile(new_file,"print")
        else:
            messagebox.showerror("Error","Please generate bill",parent=self.root)
    
    
        

    def clear_cart(self):
        self.var_pid.set("")
        self.var_pname.set("")
        self.var_price.set("")
        self.var_qty.set("")
        self.var_stock.set("")
        self.lbl_inStock.config(text=f"In Stock[0]")
    
    def update_date_time(self):
        time_=time.strftime("%I:%M:%S")
        date_=time.strftime("%d-%m-%Y")
        self.lbl_clock.config(text=f"Welcome to Inventory Management System\t\t Date: {str(date_)}\t\t Time: {str(time_)}")
        self.lbl_clock.after(200,self.update_date_time)
                

    
    def clear_all(self):
        
        del self.cart_list[:]
      
        self.var_cname.set("")
        self.var_contact.set("")
        self.txt_bill_area.delete("1.0",END)
        self.cartTitle.config(text=f"Cart\t Total Product : [0]")
        self.var_search.set("")
        self.show()
        self.clear_cart()
        self.show()
        self.show_cart()
        
    def logout(self):
        self.root.destroy()
        os.system("python login.py")
        
            



if __name__=="__main__":
    root = Tk()
    obj = BillClass(root)
    root.mainloop()