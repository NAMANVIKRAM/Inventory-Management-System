from tkinter import *
import mysql.connector
from tkinter import ttk,messagebox
from PIL import Image, ImageTk
from tkinter import ttk

class productClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x500+220+130")#width and height and Xaxis and top
        self.root.title("Inventory Management System | Developed by: Naman Vikram")
        self.root.config(bg="white")
        self.root.focus_force()

        #================
        #VARIABLES
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()

        self.var_cat=StringVar()
        self.var_sup=StringVar()
        self.var_pid=StringVar()
        self.cat_list=[]
        self.sup_list=[]
        self.fetch_cat_sup()
        self.var_name=StringVar()
        self.var_price=StringVar()
        self.var_qty=StringVar()
        self.var_status=StringVar()


        product_frame=Frame(self.root,bd=2,relief=RIDGE)
        product_frame.place(x=10,y=10,width=450,height=480)

        title=Label(product_frame,text=" Product Details",font=("times new roman",18,"bold"),bg="#010c48",fg="white").pack(side=TOP,fill=X)
        
         #=====Column 1

        lbl_category=Label(product_frame,text="Category ",font=("times new roman",18,"bold"),bg="white").place(x=30,y=60)
        lbl_supplier=Label(product_frame,text="Distributor ",font=("times new roman",18,"bold"),bg="white").place(x=30,y=110)
        lbl_product_name=Label(product_frame,text="Product Name ",font=("times new roman",18,"bold"),bg="white").place(x=30,y=160)
        lbl_price=Label(product_frame,text="Price ",font=("times new roman",18,"bold"),bg="white").place(x=30,y=210)
        lbl_qty=Label(product_frame,text="Quantity ",font=("times new roman",18,"bold"),bg="white").place(x=30,y=260)
        lbl_status=Label(product_frame,text="Status ",font=("times new roman",18,"bold"),bg="white").place(x=30,y=310)

        # txt_category=Label(product_frame,text="Category ",font=("times new roman",18,"bold"),bg="white").place(x=30,y=60)
      
       #=====Column 2

        cmb_cat=ttk.Combobox(product_frame,textvariable=self.var_cat,values=self.cat_list,state='readonly',justify=CENTER,font=("Comic Sans MS",15,"bold"))
        cmb_cat.place(x=200,y=60,width=200)
        cmb_cat.current(0)
        
        cmb_sup=ttk.Combobox(product_frame,textvariable=self.var_sup,values=self.sup_list,state='readonly',justify=CENTER,font=("Comic Sans MS",15,"bold"))
        cmb_sup.place(x=200,y=110,width=200)
        cmb_sup.current(0)

        lbl_name=Entry(product_frame,textvariable=self.var_name,font=("times new roman",18,"bold"),bg="lightyellow").place(x=200,y=160,width=200)
        lbl_price=Entry(product_frame,textvariable=self.var_price,font=("times new roman",18,"bold"),bg="lightyellow").place(x=200,y=210,width=200)
        lbl_qty=Entry(product_frame,textvariable=self.var_qty,font=("times new roman",18,"bold"),bg="lightyellow").place(x=200,y=260,width=200)
        
        cmb_status=ttk.Combobox(product_frame,textvariable=self.var_status,values=("Active","Inactive"),state='readonly',justify=CENTER,font=("Comic Sans MS",15,"bold"))
        cmb_status.place(x=200,y=310,width=200)
        cmb_status.current(0)

        #=====BUTTONS=======
        btn_add=Button(product_frame,text="Save",font=("Comic Sans MS",15),command=self.add,bg="Violet",cursor="hand2").place(x=10,y=400,width=80,height=30)
        btn_update=Button(product_frame,text="Update",command=self.update,font=("Comic Sans MS",15),bg="lightGreen",cursor="hand2").place(x=120,y=400,width=80,height=30)
        btn_delete=Button(product_frame,text="Delete",command=self.delete,font=("Comic Sans MS",15),bg="Red",cursor="hand2").place(x=230,y=400,width=80,height=30)
        btn_Clear=Button(product_frame,text="Clear",command=self.clear,font=("Comic Sans MS",15),bg="Pink",cursor="hand2").place(x=340,y=400,width=80,height=30)

        ############SEARCH FRAMES
        SearchFrame=LabelFrame(self.root,text="Search",font=("Comic Sans MS",12,"bold"),bd=2,relief=RIDGE,bg="white")
        SearchFrame.place(x=480,y=10,width=600,height=80)

        cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby,values=("Select","Category","Distributor","Name"),state='readonly',justify=CENTER,font=("Comic Sans MS",15,"bold"))
        cmb_search.place(x=10,y=8,width=180)
        cmb_search.current(0)

        txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=("Comic Sans MS",15),bg="lightyellow").place(x=200,y=10)
        btn_search=Button(SearchFrame,text="Search",command=self.search,font=("Comic Sans MS",15),bg="#4caf50",cursor="hand2").place(x=445,y=10,width=150,height=30)
      

################# PRODUCT DETAILS ######3
        p_frame=Frame(self.root,bd=3,relief=RIDGE)
        p_frame.place(x=480,y=100,width=600,height=400)
        
        scrolly=Scrollbar(p_frame,orient=VERTICAL)
        scrollx=Scrollbar(p_frame,orient=HORIZONTAL)

        self.ProductTable = ttk.Treeview(p_frame, columns=("pid", "distributor", "category", "name", "price", "qty", "status"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.ProductTable.xview)
        scrolly.config(command=self.ProductTable.yview)

            # Add data to the Treeview
        self.ProductTable.heading("pid", text="Product ID")
        self.ProductTable.heading("category", text="Category")
        self.ProductTable.heading("distributor", text="Distributor")
        self.ProductTable.heading("name", text="Name")
        self.ProductTable.heading("price", text="Price")
        self.ProductTable.heading("qty", text="Qty")
        self.ProductTable.heading("status", text="Status")
        
        
        self.ProductTable["show"] = "headings"

          
        self.ProductTable.column("pid", width=100)
        self.ProductTable.column("category", width=150)
        self.ProductTable.column("distributor", width=200)
        self.ProductTable.column("name", width=100)
        self.ProductTable.column("price", width=100)
        self.ProductTable.column("qty", width=100)
        self.ProductTable.column("status", width=100)
       

        self.ProductTable.pack(fill=BOTH, expand=1)
        self.ProductTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
        

        ### FUNCTIONS ######
    
    def fetch_cat_sup(self):
        con=mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="Root",
            database="ims"
        )
        cur=con.cursor()
        try:
            cur.execute("select name from category")
            cat=cur.fetchall()
            self.cat_list.append("Empty")
            
            if len(cat)>0:
                del self.cat_list[:]
                self.cat_list.append("Select")
                for row in cat:
                    self.cat_list.append(row[0])

            cur.execute("select name from distributor")
            sup=cur.fetchall()
            # self.sup_list.append("Empty")
            if len(sup)>0:
                del self.sup_list[:]
                self.sup_list.append("Select")
                for row in sup:
                    self.sup_list.append(row[0])
            
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)


    def add(self):
        con=mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="Root",
            database="ims"
        )
        cur=con.cursor()

        try:
            if not self.var_cat.get()=="Select" and self.var_cat.get()=="Empty" and self.var_sup.get()=="Select" and self.var_name.get()!="":
                    messagebox.showerror("Error", "All field is required", parent=self.root)

            else:
                cur.execute("Select * from product WHERE name=%s",(self.var_name.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Product already present,try different",parent=self.root)
                else:
                    cur.execute("INSERT INTO product(category, distributor, name, price, qty, status) VALUES(%s, %s, %s, %s, %s, %s)",(
                                
                                self.var_cat.get(),
                                self.var_sup.get(),
                                self.var_name.get(),
                                self.var_price.get(),
                                self.var_qty.get(),
                                self.var_status.get(),
                                
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Product  Added Successfully",parent=self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)
        finally:
            con.close()
    
    def show(self):
        con=mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="Root",
            database="ims"
        )
        cur=con.cursor()
        
        try:
            cur.execute("select * from product")
            rows=cur.fetchall()
            self.ProductTable.delete(*self.ProductTable.get_children())
            for row in rows:
                self.ProductTable.insert('',END,values=row)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)
        finally:
            con.close()
    
    def get_data(self,ev):
        f=self.ProductTable.focus()
        content=(self.ProductTable.item(f))
        row=content['values']
        self.var_pid.set(row[0]),
        self.var_cat.set(row[2]),
        self.var_sup.set(row[1]),
        self.var_name.set(row[3]),
        self.var_price.set(row[4]),
        self.var_qty.set(row[5]),
        self.var_status.set(row[6]),
       
    def update(self):
        con=mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="Root",
            database="ims"
        )
        cur=con.cursor()

        try:
            if not self.var_pid.get():
                    messagebox.showerror("Error", "Please select product from list ", parent=self.root)

            else:
                cur.execute("Select * from product WHERE pid=%s",(self.var_pid.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Product ",parent=self.root)
                else:
                    cur.execute("UPDATE product SET category=%s, distributor=%s, name=%s ,price=%s, qty=%s, status=%s  WHERE pid=%s", (
                                self.var_cat.get(),
                                self.var_sup.get(),
                                self.var_name.get(),
                                self.var_price.get(),
                                self.var_qty.get(),
                                self.var_status.get(),
                                self.var_pid.get()
                ))

                    con.commit()
                    messagebox.showinfo("Success","Poduct Updated Successfully",parent=self.root)
                    self.show()
                    con.close()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)
        finally:
            con.close()
    
    def delete(self):
        con=mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="Root",
            database="ims"
        )
        cur=con.cursor()
        try:
            if not self.var_pid.get():
                    messagebox.showerror("Error", "Select Product from list", parent=self.root)

            else:
                
                cur.execute("Select * from product WHERE pid=%s",(self.var_pid.get(),))
                
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Product",parent=self.root)
                else:
                    op=messagebox.askyesno ("Confirm","Do you want to delete ?",parent=self.root)
                    
                    if op==True:

                        cur.execute("Delete from product WHERE pid=%s",(self.var_pid.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Product Deleted Successfully",parent=self.root)
                        self.clear()
                    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)
        finally:
            con.close()
    def clear(self):
        self.var_cat.set("Select"),
        self.var_sup.set("Select"),
        self.var_name.set(""),
        self.var_price.set(""),
        self.var_qty.set(""),
        self.var_status.set("Active"),
        self.var_pid.set("")
        self.var_searchtxt.set("")
        self.var_searchby.set("Select")
        self.show()

    def search(self):
        con=mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="Root",
            database="ims"
        )
        cur=con.cursor()
        try:
            if self.var_searchby.get() == "Select":
                messagebox.showerror("Error", "Select Search by option", parent=self.root)
            elif self.var_searchtxt.get() == "":
                messagebox.showerror("Error", "Enter search text", parent=self.root)
            else:
                cur.execute("SELECT * FROM product where " + self.var_searchby.get() + " LIKE %s", ("%" + self.var_searchtxt.get() + "%",))
                rows = cur.fetchall()
                if len(rows) != 0:
                    self.ProductTable.delete(*self.ProductTable.get_children())
                    for row in rows:
                        self.ProductTable.insert('', END, values=row)
                else:                    messagebox.showerror("Error", "No data found !!!")

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)
        finally:
            con.close()


if __name__=="__main__":
    root = Tk()
    obj = productClass(root)
    root.mainloop()