from tkinter import *
from PIL import Image, ImageTk  # pip install pillow
from tkinter import ttk,messagebox
import sqlite3


class resultClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg='white')
        self.root.focus_force()

        # ==== Title ====
        title = Label(self.root, text="Add Student Results",
                      font=("goudy old style", 20, "bold"),
                      bg='orange', fg='#262626').place(x=10, y=15, width=1180, height=50)
        

        #======Widgets=====
        #========Variables========
        self.var_roll=StringVar
        self.var_name=StringVar()
        self.var_course=StringVar()
        self.var_marks=StringVar()
        self.var_full_marks=StringVar()
        self.roll_list=[]
        lb1_select = Label(self.root, text="Select Student", font=("goudy old style", 15, 'bold'), bg='white')
        lb1_select.place(x=50, y=100)

        lb1_name = Label(self.root, text="Name", font=("goudy old style", 15, 'bold'), bg='white')
        lb1_name.place(x=50, y=160)

        lb1_course = Label(self.root, text="Course", font=("goudy old style", 15, 'bold'), bg='white')
        lb1_course.place(x=50, y=220)

        lb1_marks = Label(self.root, text="Marks Obtained", font=("goudy old style", 15, 'bold'), bg='white')
        lb1_marks.place(x=50, y=280)

        lb1_full_marks = Label(self.root, text="Full Marks", font=("goudy old style", 15, 'bold'), bg='white')
        lb1_full_marks.place(x=50, y=340)


        self.txt_student = ttk.Combobox(self.root,textvariable=self.var_roll,values=self.roll_list, font=("goudy old style", 15, 'bold'),state='readonly',justify=CENTER)
        self.txt_student.place(x=280, y=100,width=200)
        self.txt_student.set("Select")
        btn_search=Button(self.root,text='Search',font=("goudy old style",15,"bold"),bg="#03a9f4",fg="white",cursor="hand2").place(x=500,y=100,width=100,height=28)

        txt_name = Entry(self.root,textvariable=self.var_name, font=("goudy old style", 20, 'bold'), bg='lightyellow',state='readonly').place(x=280, y=160,width=320)
        txt_couse = Entry(self.root,textvariable=self.var_course, font=("goudy old style", 20, 'bold'), bg='lightyellow',state='readonly').place(x=280, y=220,width=320)
        txt_marks = Entry(self.root,textvariable=self.var_marks, font=("goudy old style", 20, 'bold'), bg='lightyellow',state='readonly').place(x=280, y=280,width=320)
        txt_full_marks = Entry(self.root,textvariable=self.var_full_marks, font=("goudy old style", 20, 'bold'), bg='lightyellow',state='readonly').place(x=280, y=340,width=320)


        #=======button==============

        btn_add=Button(self.root,text="Submit",font=("times new roman",15),bg='lightgreen',activebackground='lightgreen',cursor="hand2").place(x=300,y=420,width=120,height=35)
        btn_clear=Button(self.root,text="Clear",font=("times new roman",15),bg='lightgray',activebackground='lightgray',cursor="hand2").place(x=430,y=420,width=120,height=35)


        #====Image======
        self.bg_img=Image.open("images/result.jpg")
        self.bg_img = self.bg_img.resize((500, 300), Image.Resampling.LANCZOS)
        self.bg_img=ImageTk.PhotoImage(self.bg_img)

        self.lb1_bg=Label(self.root,image=self.bg_img).place(x=650,y=100)









if __name__ == "__main__":
    root = Tk()
    obj = resultClass(root)
    root.mainloop()