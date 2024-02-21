from tkinter import *
import mysql.connector
from tkinter import ttk,messagebox
from PIL import Image, ImageTk
from tkinter import ttk

class DistributorClass:
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
        ###### ALL Variables #######
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()

        self.var_dis_Id=StringVar()
        self.var_contact=StringVar()
        self.var_name=StringVar()
       

        ####SEARCH FRAME#######
       

        #=====Search OPTIONS=====
        lbl_search=Label(self.root,text="Search by Id",bg="white",font=("Comic Sans MS",15,"bold"))
        lbl_search.place(x=630,y=70)
        

        txt_search=Entry(self.root,textvariable=self.var_searchtxt,font=("Comic Sans MS",15),bg="lightyellow").place(x=800,y=70)
        btn_search=Button(self.root,text="Search",command=self.search,font=("Comic Sans MS",15),bg="#4caf50",cursor="hand2").place(x=1050,y=70,width=150,height=30)
       ########################### TITLE ########
        title=Label(self.root,text="Distributor Details",font=("goudy old style",20,"bold"),bg="#0f4d7d",fg="white").pack(fill=X) 


        ##### DETAILS #######

        # ********************** ROW 1 **********
        lbl_distributor_Id=Label(self.root,text="Id No.",font=("goudy old style",15),bg="white").place(x=50,y=80)
        
        txt_distributor_Id=Entry(self.root,textvariable=self.var_dis_Id,font=("goudy old style",15),bg="lightyellow").place(x=180,y=80,width=180)
        # txt_gender=Entry(self.root,textvariable=self.var_gender,font=("goudy old style",15),bg="white").place(x=550,y=150,width=180)
        
         
        # ********************** ROW 2 **********
        lbl_name=Label(self.root,text="Name",font=("goudy old style",15),bg="white").place(x=50,y=130)
        text_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",15),bg="lightyellow").place(x=180,y=130,width=180)
        
        # ************ ROW 3 ********
        lbl_contact=Label(self.root,text="Contact",font=("goudy old style",15),bg="white").place(x=50,y=180)
        
        text_email=Entry(self.root,textvariable=self.var_contact,font=("goudy old style",15),bg="lightyellow").place(x=180,y=180,width=180)
        

        #******************ROW 4 ****************
        lbl_desc=Label(self.root,text="Description",font=("goudy old style",15),bg="white").place(x=50,y=230)
       
        self.text_desc=Text(self.root,font=("goudy old style",15),bg="lightyellow")
        self.text_desc.place(x=180,y=230,width=400,height=90)
        
        #*********************************Buttons***********************
        # txt_search=Entry(self.root,textvariable=self.var_searchtxt,font=("Comic Sans MS",15),bg="lightyellow").place(x=620,y=330)
        btn_save=Button(self.root,text="Save",font=("Comic Sans MS",15),command=self.add,bg="Violet",cursor="hand2").place(x=180,y=340,width=110,height=30)
        btn_update=Button(self.root,text="Update",command=self.update,font=("Comic Sans MS",15),bg="lightGreen",cursor="hand2").place(x=330,y=340,width=110,height=30)
        btn_delete=Button(self.root,text="Delete",command=self.delete,font=("Comic Sans MS",15),bg="Red",cursor="hand2").place(x=480,y=340,width=110,height=30)
        btn_Clear=Button(self.root,text="Clear",command=self.clear,font=("Comic Sans MS",15),bg="Pink",cursor="hand2").place(x=630,y=340,width=110,height=30)

        #**********Distributor Details ****
        emp_frame=Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=800,y=130,width=400,height=400)
        
        scrolly=Scrollbar(emp_frame,orient=VERTICAL)
        scrollx=Scrollbar(emp_frame,orient=HORIZONTAL)

        self.Distributor = ttk.Treeview(emp_frame, columns=("Id", "name", "contact", "desc"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.Distributor.xview)
        scrolly.config(command=self.Distributor.yview)

            # Add data to the Treeview
        self.Distributor.heading("Id", text="Id no.")
        self.Distributor.heading("name", text="Name")
        self.Distributor.heading("contact", text="Contact")
        self.Distributor.heading("desc", text="Description")
        
        self.Distributor["show"] = "headings"

          
        self.Distributor.column("Id", width=100)
        self.Distributor.column("name", width=150)
        self.Distributor.column("contact", width=200)
        self.Distributor.column("desc", width=100)
        
        self.Distributor.pack(fill=BOTH, expand=1)
        self.Distributor.bind("<ButtonRelease-1>",self.get_data)
        self.show()

    # **************************
    def add(self):
        con=mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="Root",
            database="ims"
        )
        cur=con.cursor()

        try:
            if not self.var_dis_Id.get():
                    messagebox.showerror("Error", "Id is required", parent=self.root)

            else:
                cur.execute("Select * from distributor WHERE Id=%s",(self.var_dis_Id.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Id no. already assigned,try different",parent=self.root)
                else:
                    cur.execute("INSERT INTO distributor(Id, name, contact, description) VALUES(%s, %s, %s, %s)",(
                                self.var_dis_Id.get(),
                                self.var_name.get(),
                                self.var_contact.get(),
                                self.text_desc.get('1.0','end-1c'),
                                

                    ))
                    con.commit()
                    messagebox.showinfo("Success","Distributor Added Successfully",parent=self.root)
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
            cur.execute("select * from distributor")
            rows=cur.fetchall()
            self.Distributor.delete(*self.Distributor.get_children())
            for row in rows:
                self.Distributor.insert('',END,values=row)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)
        finally:
            con.close()
    
    def get_data(self,ev):
        f=self.Distributor.focus()
        content=(self.Distributor.item(f))
        row=content['values']
        # print(row)
        self.var_dis_Id.set(row[0]),
        self.var_name.set(row[1]),
        self.var_contact.set(row[2]),
        self.text_desc.delete('1.0','end-1c'),
        self.text_desc.insert('end-1c',row[3]),
        self.var_salary.set(row[10])

    def update(self):
        con=mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="Root",
            database="ims"
        )
        cur=con.cursor()

        try:
            if not self.var_dis_Id.get():
                    messagebox.showerror("Error", "Id no. is required", parent=self.root)

            else:
                cur.execute("Select * from distributor WHERE Id=%s",(self.var_dis_Id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Id no.",parent=self.root)
                else:
                    cur.execute("UPDATE distributor SET name=%s, contact=%s, description=%s WHERE Id=%s", (
                    self.var_name.get(),
                    self.var_contact.get(),
                    self.text_desc.get('1.0','end-1c'),
                    self.var_dis_Id.get()
                ))

                    con.commit()
                    messagebox.showinfo("Success","Distributor Updated Successfully",parent=self.root)
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
            if not self.var_dis_Id.get():
                    messagebox.showerror("Error", "Id no. is required", parent=self.root)

            else:
                
                cur.execute("Select * from distributor WHERE Id=%s",(self.var_dis_Id.get(),))
                
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Id no.",parent=self.root)
                else:
                    op=messagebox.askyesno ("Confirm","Do you want to delete ?",parent=self.root)
                    
                    if op==True:

                        cur.execute("Delete from distributor WHERE Id=%s",(self.var_dis_Id.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Distributor Deleted Successfully",parent=self.root)
                        self.clear()
                    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)
        finally:
            con.close()
    def clear(self):
        self.var_dis_Id.set(""),
        self.var_name.set(""),
        self.var_contact.set(""),
        self.text_desc.delete('1.0','end-1c'),
        self.var_searchtxt.set(""),
        
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
           if self.var_searchtxt.get() == "":
                messagebox.showerror("Error", "Enter search text", parent=self.root)
           else:
                cur.execute("SELECT * FROM distributor where Id = %s ", (self.var_searchtxt.get(),))
                row = cur.fetchone()
                if row is not None:
                    self.Distributor.delete(*self.Distributor.get_children())
                    self.Distributor.insert('', END, values=row)
                else:
                    messagebox.showerror("Error", "No data found !!!")
              

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)
        finally:
            con.close()



if __name__=="__main__":
    root = Tk()
    obj = DistributorClass(root)
    root.mainloop()
       

   