from tkinter import *
import mysql.connector
from tkinter import ttk,messagebox
from PIL import Image, ImageTk
from tkinter import ttk

class employeeClass:
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

        self.var_emp_id=StringVar()
        self.var_gender=StringVar()
        self.var_contact=StringVar()
        self.var_name=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_email=StringVar()
        self.var_password=StringVar()
        self.var_utype=StringVar()
        self.var_salary=StringVar()

        ####SEARCH FRAME#######
        SearchFrame=LabelFrame(self.root,text="Search Employee",font=("Comic Sans MS",12,"bold"),bd=2,relief=RIDGE,bg="white")
        SearchFrame.place(x=250,y=20,width=600,height=70)

        #=====Search OPTIONS=====
        cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby,values=("Select","Email","Name","Contact"),state='readonly',justify=CENTER,font=("Comic Sans MS",15,"bold"))
        cmb_search.place(x=10,y=8,width=180)
        cmb_search.current(0)

        txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=("Comic Sans MS",15),bg="lightyellow").place(x=200,y=10)
        btn_search=Button(SearchFrame,text="Search",command=self.search,font=("Comic Sans MS",15),bg="#4caf50",cursor="hand2").place(x=445,y=10,width=150,height=30)
       ########################### TITLE ########
        title=Label(self.root,text="Employee Details",font=("goudy old style",15),bg="#0f4d7d",fg="white").place(x=50,y=100,width=1000) 


        ##### DETAILS #######

        # ********************** ROW 1 **********
        lbl_empid=Label(self.root,text="Employee ID",font=("goudy old style",15),bg="white").place(x=50,y=150)
        lbl_gender=Label(self.root,text="Gender",font=("goudy old style",15),bg="white").place(x=450,y=150)
        lbl_contact=Label(self.root,text="Contact",font=("goudy old style",15),bg="white").place(x=750,y=150)

        txt_empid=Entry(self.root,textvariable=self.var_emp_id,font=("goudy old style",15),bg="lightyellow").place(x=180,y=150,width=180)
        # txt_gender=Entry(self.root,textvariable=self.var_gender,font=("goudy old style",15),bg="white").place(x=550,y=150,width=180)
        cmb_gender=ttk.Combobox(self.root,textvariable=self.var_gender,values=("Select","Male","Female","Other"),state='readonly',justify=CENTER,font=("goudy old style",15,"bold"))
        cmb_gender.place(x=550,y=150,width=180)
        cmb_gender.current(0)

        txt_contact=Entry(self.root,textvariable=self.var_contact,font=("goudy old style",15),bg="lightyellow").place(x=850,y=150,width=180)
         
        # ********************** ROW 2 **********
        lbl_name=Label(self.root,text="Name",font=("goudy old style",15),bg="white").place(x=50,y=200)
        lbl_dob=Label(self.root,text="D.O.B",font=("goudy old style",15),bg="white").place(x=450,y=200)
        lbl_doj=Label(self.root,text="D.O.J",font=("goudy old style",15),bg="white").place(x=750,y=200)

        text_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",15),bg="lightyellow").place(x=180,y=200,width=180)
        text_dob=Entry(self.root,textvariable=self.var_dob,font=("goudy old style",15),bg="lightyellow").place(x=550,y=200,width=180)
        text_doj=Entry(self.root,textvariable=self.var_doj,font=("goudy old style",15),bg="lightyellow").place(x=850,y=200,width=180)

        # ************ ROW 3 ********
        lbl_email=Label(self.root,text="Email",font=("goudy old style",15),bg="white").place(x=50,y=250)
        lbl_passw=Label(self.root,text="Password",font=("goudy old style",15),bg="white").place(x=450,y=250)
        lbl_user=Label(self.root,text="User Type",font=("goudy old style",15),bg="white").place(x=750,y=250)

        text_email=Entry(self.root,textvariable=self.var_email,font=("goudy old style",15),bg="lightyellow").place(x=180,y=250,width=180)
        text_passw=Entry(self.root,textvariable=self.var_password,font=("goudy old style",15),bg="lightyellow").place(x=550,y=250,width=180)
        # text_user=Entry(self.root,textvariable=self.var_doj,font=("goudy old style",15),bg="lightyellow").place(x=850,y=200,width=180)
        cmb_user=ttk.Combobox(self.root,textvariable=self.var_utype,values=("Select","Admin","Employee"),state='readonly',justify=CENTER,font=("goudy old style",15,"bold"))
        cmb_user.place(x=850,y=250,width=180)
        cmb_user.current(0)


        #******************ROW 4 ****************
        lbl_addr=Label(self.root,text="Address",font=("goudy old style",15),bg="white").place(x=50,y=300)
        lbl_salary=Label(self.root,text="Salary",font=("goudy old style",15),bg="white").place(x=550,y=300)
        
        self.text_addr=Text(self.root,font=("goudy old style",15),bg="lightyellow")
        self.text_addr.place(x=180,y=300,width=300,height=60)
        text_salary=Entry(self.root,textvariable=self.var_salary,font=("goudy old style",15),bg="lightyellow").place(x=620,y=300,width=180)
        
        #*********************************Buttons***********************
        # txt_search=Entry(self.root,textvariable=self.var_searchtxt,font=("Comic Sans MS",15),bg="lightyellow").place(x=620,y=330)
        btn_save=Button(self.root,text="Save",font=("Comic Sans MS",15),command=self.add,bg="Violet",cursor="hand2").place(x=550,y=340,width=80,height=30)
        btn_update=Button(self.root,text="Update",command=self.update,font=("Comic Sans MS",15),bg="lightGreen",cursor="hand2").place(x=650,y=340,width=80,height=30)
        btn_delete=Button(self.root,text="Delete",command=self.delete,font=("Comic Sans MS",15),bg="Red",cursor="hand2").place(x=750,y=340,width=80,height=30)
        btn_Clear=Button(self.root,text="Clear",command=self.clear,font=("Comic Sans MS",15),bg="Pink",cursor="hand2").place(x=850,y=340,width=80,height=30)

        #**********Employee Details ****
        emp_frame=Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=0,y=400,relwidth=1,height=200)
        
        scrolly=Scrollbar(emp_frame,orient=VERTICAL)
        scrollx=Scrollbar(emp_frame,orient=HORIZONTAL)

        self.EmployeeTable = ttk.Treeview(emp_frame, columns=("eid", "name", "email", "gender", "contact", "dob", "doj", "password", "usertype", "address", "salary"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.EmployeeTable.xview)
        scrolly.config(command=self.EmployeeTable.yview)

            # Add data to the Treeview
        self.EmployeeTable.heading("eid", text="Emp ID")
        self.EmployeeTable.heading("name", text="Name")
        self.EmployeeTable.heading("email", text="Email")
        self.EmployeeTable.heading("gender", text="Gender")
        self.EmployeeTable.heading("contact", text="Contact")
        self.EmployeeTable.heading("dob", text="D.O.B")
        self.EmployeeTable.heading("doj", text="D.O.J")
        self.EmployeeTable.heading("password", text="Password")
        self.EmployeeTable.heading("usertype", text="User Type")
        self.EmployeeTable.heading("address", text="Address")
        self.EmployeeTable.heading("salary", text="Salary")
        
        self.EmployeeTable["show"] = "headings"

          
        self.EmployeeTable.column("eid", width=100)
        self.EmployeeTable.column("name", width=150)
        self.EmployeeTable.column("email", width=200)
        self.EmployeeTable.column("gender", width=100)
        self.EmployeeTable.column("contact", width=100)
        self.EmployeeTable.column("dob", width=100)
        self.EmployeeTable.column("doj", width=100)
        self.EmployeeTable.column("password", width=100)
        self.EmployeeTable.column("usertype", width=100)
        self.EmployeeTable.column("address", width=100)
        self.EmployeeTable.column("salary", width=150)

        self.EmployeeTable.pack(fill=BOTH, expand=1)
        self.EmployeeTable.bind("<ButtonRelease-1>",self.get_data)
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
            if not self.var_emp_id.get():
                    messagebox.showerror("Error", "Employee ID is required", parent=self.root)

            else:
                cur.execute("Select * from employee WHERE eid=%s",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","This Employee ID already assigned,try different",parent=self.root)
                else:
                    cur.execute("INSERT INTO employee(eid, name, email, gender, contact, dob, doj, password, usertype, address, salary) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",(
                                self.var_emp_id.get(),
                                self.var_name.get(),
                                self.var_email.get(),
                                self.var_gender.get(),
                                self.var_contact.get(),
                                self.var_dob.get(),
                                self.var_doj.get(),
                                self.var_password.get(),
                                self.var_utype.get(),
                                self.text_addr.get('1.0','end-1c'),
                                self.var_salary.get()

                    ))
                    con.commit()
                    messagebox.showinfo("Success","Employee Added Successfully",parent=self.root)
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
            cur.execute("select * from employee")
            rows=cur.fetchall()
            self.EmployeeTable.delete(*self.EmployeeTable.get_children())
            for row in rows:
                self.EmployeeTable.insert('',END,values=row)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)
        finally:
            con.close()
    
    def get_data(self,ev):
        f=self.EmployeeTable.focus()
        content=(self.EmployeeTable.item(f))
        row=content['values']
        # print(row)
        self.var_emp_id.set(row[0]),
        self.var_name.set(row[1]),
        self.var_email.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_contact.set(row[4]),
        self.var_dob.set(row[5]),
        self.var_doj.set(row[6]),
        self.var_password.set(row[7]),
        self.var_utype.set(row[8]),
        self.text_addr.delete('1.0','end-1c'),
        self.text_addr.insert('end-1c',row[9]),
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
            if not self.var_emp_id.get():
                    messagebox.showerror("Error", "Employee ID is required", parent=self.root)

            else:
                cur.execute("Select * from employee WHERE eid=%s",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid ID",parent=self.root)
                else:
                    cur.execute("UPDATE employee SET name=%s, email=%s, gender=%s, contact=%s, dob=%s, doj=%s, password=%s, usertype=%s, address=%s, salary=%s WHERE eid=%s", (
                    self.var_name.get(),
                    self.var_email.get(),
                    self.var_gender.get(),
                    self.var_contact.get(),
                    self.var_dob.get(),
                    self.var_doj.get(),
                    self.var_password.get(),
                    self.var_utype.get(),
                    self.text_addr.get('1.0','end-1c'),
                    self.var_salary.get(),
                    self.var_emp_id.get()
                ))

                    con.commit()
                    messagebox.showinfo("Success","Employee Updated Successfully",parent=self.root)
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
            if not self.var_emp_id.get():
                    messagebox.showerror("Error", "Employee ID is required", parent=self.root)

            else:
                
                cur.execute("Select * from employee WHERE eid=%s",(self.var_emp_id.get(),))
                
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid ID",parent=self.root)
                else:
                    op=messagebox.askyesno ("Confirm","Do you want to delete ?",parent=self.root)
                    
                    if op==True:

                        cur.execute("Delete from Employee WHERE eid=%s",(self.var_emp_id.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Employee Deleted Successfully",parent=self.root)
                        self.clear()
                    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)
        finally:
            con.close()
    def clear(self):
        self.var_emp_id.set(""),
        self.var_name.set(""),
        self.var_email.set(""),
        self.var_gender.set("Select"),
        self.var_contact.set(""),
        self.var_dob.set(""),
        self.var_doj.set(""),
        self.var_password.set(""),
        self.var_utype.set(""),
        self.text_addr.delete('1.0','end-1c'),
        self.var_salary.set("")
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
                cur.execute("SELECT * FROM employee where " + self.var_searchby.get() + " LIKE %s", ("%" + self.var_searchtxt.get() + "%",))
                rows = cur.fetchall()
                if len(rows) != 0:
                    self.EmployeeTable.delete(*self.EmployeeTable.get_children())
                    for row in rows:
                        self.EmployeeTable.insert('', END, values=row)
                else:                    messagebox.showerror("Error", "No data found !!!")

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)
        finally:
            con.close()



if __name__=="__main__":
    root = Tk()
    obj = employeeClass(root)
    root.mainloop()
       

   