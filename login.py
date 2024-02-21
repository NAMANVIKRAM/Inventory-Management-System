from tkinter import *
from tkinter import ttk,messagebox
import mysql.connector
from PIL import ImageTk,Image
import os
import email_pass
import smtplib
import time

class Login_system:
    def __init__(self,root):
        self.root=root
        self.root.title("Login System | Developed by: Naman Vikram")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        
        self.otp=''

        self.employee_id=StringVar()
        self.var_password=StringVar()
        #======IMages======

        self.image=ImageTk.PhotoImage(file="images/phone.png")
        
        self.lbl_image=Label(self.root,image=self.image,bd=0).place(x=120,y=30)

        #======Login Frame======
        frame_login=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        frame_login.place(x=600,y=60,width=400,height=500)
        title=Label(frame_login,text="Login System",font=("Comic Sans MS" ,30 ,"bold"),bg="white",fg="black").place(x=0,y=30,relwidth=1)
        lbl_user=Label(frame_login,text="Employee/Admin ID",font=("Comic Sans MS",15,"bold"),bg="white",fg="black").place(x=50,y=120)
        self.txt_user=Entry(frame_login,textvariable=self.employee_id,font=("Comic Sans MS",15),bg="#ECECEC").place(x=50,y=150,width=300)
        
        lbl_password=Label(frame_login,text="Password",font=("Comic Sans MS",15,"bold"),bg="white",fg="black").place(x=50,y=200)
        self.txt_password=Entry(frame_login,textvariable=self.var_password,show='*',font=("Comic Sans MS",15),bg="#ECECEC").place(x=50,y=230,width=300)

        btn_login=Button(frame_login,text="Log In",command=self.login,font=("Comic Sans MS",15,"bold"),bg="#007FFF",activebackground="#007FFF",fg="white",activeforeground="white",cursor="hand2").place(x=50,y=300,width=300,height=35)
        btn_register=Button(frame_login,text="Register",font=("Comic Sans MS",15,"bold"),bg="#007FFF",activebackground="#007FFF",fg="white",activeforeground="white",cursor="hand2").place(x=50,y=350,width=300,height=35)

        hr=Label(frame_login,bg="black").place(x=50,y=427,width=300,height=2)
        or_=Label(frame_login,text="OR",font=("Comic Sans MS",15,"bold"),bg="white",fg="black").place(x=180,y=410)

        btn_forget=Button(frame_login,text="Forget Password?",command=self.forget_window,font=("Times new roman",15,"bold"),bg="white",activebackground="white",fg="#00759E", activeforeground="#00759E",cursor="hand2",bd=0).place(x=120,y=450)
       
    #    #========FRAME 2 +++++++++++
    #     frame_register=Frame(self.root,bd=2,relief=RIDGE,bg="white")
    #     frame_register.place(x=600,y=570,width=400,height=60)

    #     lbl_reg=Label(frame_register,text="Don't have an account?",font=("Comic Sans MS" ,13 ,"bold"),bg="white",fg="black").place(x=20,y=15)
    #     # btn_reg=Button(frame_register,text="Sign Up",font=("Comic Sans MS" ,13 ,"bold"),bg="white",fg="#00759E",activebackground="white",cursor="hand2",bd=0).place(x=220,y=11)
        
        #======ANIMATION IMAGE =============
        self.im1=ImageTk.PhotoImage(file="images/im1.png")
        self.im2=ImageTk.PhotoImage(file="images/im2.png")
        self.im3=ImageTk.PhotoImage(file="images/im3.png")

        self.lbl_change_image=Label(self.root,bg="white")
        self.lbl_change_image.place(x=287,y=133,width=240,height=428)
    
        self.animate()
        
        


    def animate(self):
        self.im=self.im1
        self.im1=self.im2
        self.im2=self.im3
        self.im3=self.im
        self.lbl_change_image.config(image=self.im)
        self.lbl_change_image.after(2000,self.animate)


        

    def login(self):
        con=mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="Root",
            database="ims"
        )
        cur=con.cursor()
        try:
            if(self.employee_id.get()=="" or self.var_password.get()==""):
                messagebox.showerror("Error","All fields are required",parent=self.root)
            else:
                cur.execute("select usertype from employee where eid=%s and password=%s",(self.employee_id.get(),self.var_password.get()))
                user=cur.fetchone()
                if user==None:
                    messagebox.showerror("Error","Invalid Employee ID/Password",parent=self.root)
                else:
                    if user[0]=="Admin":
                        messagebox.showinfo("Success","Welcome Admin",parent=self.root)
                        self.root.destroy()
                        os.system("python dashboard.py")
                    else:
                        messagebox.showinfo("Success","Welcome ",parent=self.root)
                        self.root.destroy()
                        os.system("python billing.py")
                    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)

    def forget_window(self):
        con=mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="Root",
            database="ims"
        )
        cur=con.cursor()
        try:
            if self.employee_id.get()=="" :
                messagebox.showerror("Error","Employee ID required",parent=self.root)
            else:
                cur.execute("select email from employee where eid=%s ",(self.employee_id.get(),))
                email=cur.fetchone()
                if email==None:
                    messagebox.showerror("Error","Invalid Employee ID",parent=self.root)
                else:
                    #======Forget_window=======
                    self.var_otp=StringVar()
                    self.var_new_password=StringVar()
                    self.var_confirm_password=StringVar()
                #    call send_email_function
                    chk=self.send_email(email[0])
                    if(chk!='s'):
                        messagebox.showerror("Error","Connection Error ,Try Again",parent=self.root)
                    else:

                        self.forget_win=Toplevel(self.root)
                        self.forget_win.title('Reset Password')
                        self.forget_win.geometry('400x350+500+200')
                        self.forget_win.config(bg='white')
                        self.forget_win.focus_force()

                        title=Label(self.forget_win,text='Reset Password',font=('times new roman',20,'bold'),bg='white',fg='#0f4d7d').pack(side=TOP,fill=X)

                        lbl_reset=Label(self.forget_win,text='Enter  OTP sent on Registered Email',font=('times new roman',15,'bold'),bg='white',fg='#0f4d7d').place(x=20,y=60)
                        self.txt_reset=Entry(self.forget_win,textvariable=self.var_otp,font=('times new roman',15),bg='lightyellow')
                        self.txt_reset.place(x=50,y=130,width=250)

                        lbl_new_password=Label(self.forget_win,text='New Password',font=('times new roman',15,'bold'),bg='white',fg='#0f4d7d').place(x=20,y=180)
                        self.txt_new_password=Entry(self.forget_win,textvariable=self.var_new_password,font=('times new roman',15),bg='lightyellow')
                        self.txt_new_password.place(x=50,y=230,width=250)

                        lbl_confirm_password=Label(self.forget_win,text='Confirm Password',font=('times new roman',15,'bold'),bg='white',fg='#0f4d7d').place(x=20,y=280)
                        self.txt_confirm_password=Entry(self.forget_win,textvariable=self.var_confirm_password,font=('times new roman',15),bg='lightyellow')
                        self.txt_confirm_password.place(x=50,y=330,width=250)


                        self.btn=Button(self.forget_win,text='Submit',command=self.validate_otp,font=('times new roman',15,'bold'),bg='#0f4d7d',fg='white',cursor='hand2')
                        self.btn.place(x=320,y=125,width=250,height=30)
                        
                        self.update=Button(self.forget_win,text='Update',command=self.update_password,state=DISABLED,font=('times new roman',15,'bold'),bg='#0f4d7d',fg='white',cursor='hand2')
                        self.update.place(x=50,y=410,width=250,height=30)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)
    
    def send_email(self,to_):
        s=smtplib.SMTP('smtp.gmail.com',587)
        s.starttls()
        email_=email_pass.email_
        pass_=email_pass.pass_
        s.login(email_,pass_)
        self.otp=int(time.strftime("%H%M%S"))+int(time.strftime("%S"))
        # self.var_otp.set(str(self.otp))
        subject="Password Reset"
        message=f'Dear sir, your OTP is {str(self.otp)}.\n\nWith Regards ,\nIMS Team'
        message="Subject:{}\n\n{}".format(subject,message)
        s.sendmail(email_,to_,message)
        chk=s.ehlo()
        if(chk[0]==250):
                return 's';
        else:
            return 'f';
        s.quit()
    def update_password(self):
        if(self.var_new_password.get()=="" or self.var_confirm_password.get()==""):
            messagebox.showerror("Error","Password is required",parent=self.forget_win)
        elif(self.var_new_password.get()!=self.var_confirm_password.get()):
            messagebox.showerror("Error","Password and confirm password must be same",parent=self.forget_win)
        else:
            try:
                con=mysql.connector.connect(
                    host="127.0.0.1",
                    user="root",
                    password="Root",
                    database="ims"
                )
                cur=con.cursor()
                cur.execute("select password from employee where eid=%s",(self.employee_id.get(),))
                password=cur.fetchone()
                if password==None:
                    messagebox.showerror("Error","Invalid Employee ID",parent=self.forget_win)
                else:
                    cur.execute("update employee set password=%s where eid=%s",(self.var_new_password.get(),self.employee_id.get()))
                    con.commit()
                    messagebox.showinfo("Success","Password Updated Successfully",parent=self.forget_win)
                    self.forget_win.destroy()
                    con.close()
            except Exception as ex:
                messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.forget_win)
    def validate_otp(self):
        if(self.var_otp.get()==str(self.otp)):
            self.txt_new_password.config(state=NORMAL)
            self.txt_confirm_password.config(state=NORMAL)
            self.update.config(state=NORMAL)
            self.btn.config(state=DISABLED)
        else:
            messagebox.showerror("Error","Invalid OTP",parent=self.forget_win)
        
root=Tk()
obj=Login_system(root)
root.mainloop()