from tkinter import *
import mysql.connector
from tkinter import messagebox
from PIL import Image, ImageTk
from employee import employeeClass
from Distributor import DistributorClass
from category import categoryClass
from product import productClass 
from sales import salesClass
import os
import time

class IMS:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Management System | Developed by: Naman Vikram")
        self.root.config(bg="white")
    

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
        
        #LEFT MENU
        Menulogo = Image.open("images/img_left.png")


        width = 200  
        height = 105 
        Menulogo=Menulogo.resize((width, height),Image.BOX)


        self.Menulogo = ImageTk.PhotoImage(Menulogo)
        LeftMenu=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        LeftMenu.place(x=0,y=102,width=200,height=565)
        lbl_menulogo=Label(LeftMenu,image=self.Menulogo)
        lbl_menulogo.pack(side=TOP,fill=X)

        image2 = Image.open("images/image2.png")
        
        widt = 15 
        heigh = 15 
        image2=image2.resize((widt, heigh),Image.BOX)
        self.icon_side = ImageTk.PhotoImage(image2)


        lbl_menu=Label(LeftMenu,text="Menu",font=("times new roman",20),bg="#4d636d").pack(side=TOP,fill=X)
        
        btn_Employee=Button(LeftMenu,text="Employee",command=self.employee,image=self.icon_side,compound=LEFT,anchor="w",padx=5,font=("times new roman",20),bg="lightgreen",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_Distributor=Button(LeftMenu,text="Distributor",command=self.Distributor,image=self.icon_side,compound=LEFT,anchor="w",padx=5,font=("times new roman",20),bg="lightgreen",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_Category=Button(LeftMenu,text="Category",command=self.category,image=self.icon_side,compound=LEFT,anchor="w",padx=5,font=("times new roman",20),bg="lightgreen",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_Product=Button(LeftMenu,text="Product",command=self.product,image=self.icon_side,compound=LEFT,anchor="w",padx=5,font=("times new roman",20),bg="lightgreen",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_Sales=Button(LeftMenu,text="Sales",command=self.sales,image=self.icon_side,compound=LEFT,anchor="w",padx=5,font=("times new roman",20),bg="lightgreen",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_Exit=Button(LeftMenu,text="Exit",image=self.icon_side,compound=LEFT,anchor="w",padx=5,font=("times new roman",20),bg="lightgreen",bd=3,cursor="hand2").pack(side=TOP,fill=X)

        #*******content******

        self.lbl_employee=Label(self.root,text="Total Employee \n [ 0 ]",bd=5,relief=RIDGE,bg="blue",fg="white",font=("Comic Sans MS",20,"bold"))
        self.lbl_employee.place(x=250,y=120,height=150,width=300)

        self.lbl_Distributor=Label(self.root,text="Total Distributor \n [ 0 ]",bd=5,relief=RIDGE,bg="blue",fg="white",font=("Comic Sans MS",20,"bold"))
        self.lbl_Distributor.place(x=600,y=120,height=150,width=300)

        self.lbl_Category=Label(self.root,text="Total Category \n [ 0 ]",bd=5,relief=RIDGE,bg="blue",fg="white",font=("Comic Sans MS",20,"bold"))
        self.lbl_Category.place(x=950,y=120,height=150,width=300)
                
        self.lbl_Product=Label(self.root,text="Total Product \n [ 0 ]",bd=5,relief=RIDGE,bg="blue",fg="white",font=("Comic Sans MS",20,"bold"))
        self.lbl_Product.place(x=250,y=300,height=150,width=300)
                
                
        self.lbl_sales=Label(self.root,text="Total Sales \n [ 0 ]",bd=5,relief=RIDGE,bg="blue",fg="white",font=("Comic Sans MS",20,"bold"))
        self.lbl_sales.place(x=600,y=300,height=150,width=300)


        #Footer
        lbl_footer=Label(self.root,text="Inventory Management System |  Developed by Naman Vikram \n For any issue contact:9899900583\n Email:namanvikram10@gmail.com ",font=("times new roman",15),bg="#4d636d",fg="white").pack(side=BOTTOM,fill=X)
        
        self.update_content()
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def employee(self):
            self.new_win=Toplevel(self.root)
            self.new_obj=employeeClass(self.new_win)
    def Distributor(self):
            self.new_win=Toplevel(self.root)
            self.new_obj=DistributorClass(self.new_win)
    def category(self):
            self.new_win=Toplevel(self.root)
            self.new_obj=categoryClass(self.new_win)
    def product(self):
            self.new_win=Toplevel(self.root)
            self.new_obj=productClass(self.new_win)
    def sales(self):
            self.new_win=Toplevel(self.root)
            self.new_obj=salesClass(self.new_win)
    
    def update_content(self):
        con=mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="Root",
            database="ims"
        )
        cur=con.cursor()
        try:
            cur.execute("select * from employee")
            employee = cur.fetchall()
            self.lbl_employee.config(text=f"Total Employee\n [{str(len(employee))}]")

            cur.execute("select * from distributor")
            distributor = cur.fetchall()
            self.lbl_Distributor.config(text=f"Total Distributor\n [{str(len(distributor))}]")

            cur.execute("select * from category")
            category = cur.fetchall()
            self.lbl_Category.config(text=f"Total Category\n [{str(len(category))}]")

            cur.execute("select * from product")
            product = cur.fetchall()
            self.lbl_Product.config(text=f"Total Product\n [{str(len(product))}]")

            bill=len(os.listdir('bill'))
            self.lbl_sales.config(text=f"Total Sales\n [{str(bill)}]")

            con.commit()
            
               
            time_=time.strftime("%I:%M:%S")
            date_=time.strftime("%d-%m-%Y")
            self.lbl_clock.config(text=f"Welcome to Inventory Management System\t\t Date: {str(date_)}\t\t Time: {str(time_)}")
       
            
            self.lbl_clock.after(200,self.update_content)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)
        finally:
            con.close()
    
    def logout(self):
        self.root.destroy()
        os.system("python login.py")




if __name__=="__main__":
    root = Tk()
    obj = IMS(root)
    root.mainloop()

