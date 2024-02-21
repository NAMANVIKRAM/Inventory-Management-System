from tkinter import *
import mysql.connector
from tkinter import ttk,messagebox
from PIL import Image, ImageTk
from tkinter import ttk

class categoryClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x500+220+130")#width and height and Xaxis and top
        self.root.title("Inventory Management System | Developed by: Naman Vikram")
        self.root.config(bg="white")
        self.root.focus_force()


        # Initialize the database connection
        self.conn = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="Root",
            database="inventory_management_system"  
        )
        self.cursor = self.conn.cursor()

        #***********VARIABLES***********
        self.var_cat_id=StringVar()
        self.var_name=StringVar()

        #**********Title********
        lbl_title=Label(self.root,text="Manage Product",font=("times new roman",18,"bold"),bg="#010c48",fg="white",bd=4,relief=RIDGE).pack(side=TOP,fill=X,padx=10,pady=15)
        
        lbl_name=Label(self.root,text="Enter Category Name ",font=("times new roman",30,"bold"),bg="white").place(x=50,y=80)
        txt_name=Entry(self.root,textvariable=self.var_name,font=("times new roman",18),bg="lightyellow").place(x=50,y=170,width=300)

        btn_add=Button(self.root,text="ADD",command=self.add,font=("times new roman",15),bg="#2196f3",fg="white",cursor="hand2").place(x=360,y=170,width=150,height=30)
        btn_delete=Button(self.root,text="Delete",command=self.delete,font=("times new roman",15),bg="green",fg="white",cursor="hand2").place(x=520,y=170,width=150,height=30)


        # ******Category Details ***********
        cat_frame=Frame(self.root,bd=3,relief=RIDGE)
        cat_frame.place(x=700,y=80,width=400,height=100)
        
        scrolly=Scrollbar(cat_frame,orient=VERTICAL)
        scrollx=Scrollbar(cat_frame,orient=HORIZONTAL)

        self.category = ttk.Treeview(cat_frame, columns=("cid", "name"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.category.xview)
        scrolly.config(command=self.category.yview)

            # Add data to the Treeview
        self.category.heading("cid", text="Category ID")
        self.category.heading("name", text="Name")
        
        
        self.category["show"] = "headings"

          
        self.category.column(0, width=100)
        self.category.column(1, width=150)
    
        
        self.category.pack(fill=BOTH, expand=1)
        
        

        #***IMAGES ****
        self.im1=Image.open(r"images\cat.jpg")
        # self.im1=self.im1.resize((500,250),Image.ANTIALIAS)
        self.im1=self.im1.resize((500, 250),Image.BOX)
        self.im1=ImageTk.PhotoImage(self.im1)

        self.lbl_im1=Label(self.root,image=self.im1,bd=2,relief=RAISED)
        self.lbl_im1.place(x=50,y=220)

        self.im2=Image.open(r"images\cat2.jpg")
        # self.im2=self.im2.resize((500,250),Image.ANTIALIAS)
        self.im2=self.im2.resize((500, 250),Image.BOX)
        self.im2=ImageTk.PhotoImage(self.im2)

        self.lbl_im2=Label(self.root,image=self.im2,bd=2,relief=RAISED)
        self.lbl_im2.place(x=580,y=220)
        self.category.bind("<ButtonRelease-1>",self.get_data)
        self.show()


###*********FUNCTIONS**********
    def add(self):
        con=mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="Root",
            database="ims"
        )
        cur=con.cursor()

        try:
            if not self.var_name.get():
                    messagebox.showerror("Error", "Category name  is required", parent=self.root)

            else:
                cur.execute("Select * from category WHERE name=%s",(self.var_name.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Category already there,try different",parent=self.root)
                else:
                    cur.execute("INSERT INTO category(name) VALUES(%s)",(
                                self.var_name.get(),
                               
                                

                    ))
                    con.commit()
                    messagebox.showinfo("Success","Category Added Successfully",parent=self.root)
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
            cur.execute("select * from category")
            rows=cur.fetchall()
            self.category.delete(*self.category.get_children())
            for row in rows:
                self.category.insert('',END,values=row)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)
        finally:
            con.close()
    
    def get_data(self,ev):
        f=self.category.focus()
        content=(self.category.item(f))
        row=content['values']
        # print(row)
        self.var_cat_id.set(row[0])
        self.var_name.set(row[1])

    def delete(self):
        con=mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="Root",
            database="ims"
        )
        cur=con.cursor()
        try:
            if not self.var_cat_id.get():
                    messagebox.showerror("Error", "Please select category name", parent=self.root)

            else:
                
                cur.execute("Select * from category WHERE cid=%s",(self.var_cat_id.get(),))
                
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Please Try Again",parent=self.root)
                else:
                    op=messagebox.askyesno ("Confirm","Do you want to delete ?",parent=self.root)
                    
                    if op==True:

                        cur.execute("Delete from category WHERE cid=%s",(self.var_cat_id.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Category Deleted Successfully",parent=self.root)
                        self.show()
                        self.var_cat_id.set("")
                        self.var_name.set("")
                        # self.clear()
                    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)
        finally:
            con.close()


if __name__=="__main__":
    root = Tk()
    obj = categoryClass(root)
    root.mainloop()