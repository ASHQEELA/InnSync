import random
from tkinter import *
import PIL.Image
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

class cust_win:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1300x550+228+250")
        # ============variable=========
        self.ver_ref = StringVar()
        x = random.randint(1000, 9999)
        self.ver_ref.set(str(x))

        self.ver_name = StringVar()
        self.ver_father = StringVar()
        self.ver_gender = StringVar()
        self.ver_post = StringVar()
        self.ver_mobile = StringVar()
        self.ver_email = StringVar()
        self.ver_nationality = StringVar()
        self.ver_idproof = StringVar()
        self.ver_idnumber = StringVar()
        self.ver_address = StringVar()
        self.ver_search = StringVar()
        self. text_search = StringVar()

        # =============title=========
        lbl_title = Label(self.root, text="CUSTOMER DETAILS", font=("times new roman", 10, "bold"), bg="black",
                          fg="orange", bd=1, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1300, height=50)

        # =========log==========
        img2 = Image.open("photo_2024-07-18_01-28-47.jpg")
        img2 = img2.resize((100, 50), PIL.Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        Lbimage = Label(self.root, image=self.photoimg2, bd=2, relief=RIDGE)
        Lbimage.place(x=0, y=0, width=100, height=50)

        # =================label frame==========
        label_frameleft = LabelFrame(self.root, bd=4, relief=RIDGE, text="CUSTOMER DETAILS",
                                     font=("times new roman", 15, "bold"), bg="#A97882",
                                     fg="black")
        label_frameleft.place(x=5, y=50, width=425, height=490)
        #================pic=======


        #img9 = Image.open(r"C:\Users\asus\OneDrive\Pictures\photo_2024-08-23_13-54-45.jpg")
        #img9 = img9.resize((300, 380), PIL.Image.Resampling.LANCZOS)
        #self.photoimg9 = ImageTk.PhotoImage(img9)
        #Lbimage = Label(label_frameleft, image=self.photoimg9, bd=4, relief=RIDGE)
        #Lbimage.place(x=115, y=0, width=300, height=380)
        # ===========lebel entry1========
        lb1_cust_ref = Label(label_frameleft, text="Customer Ref", font=("times new roman", 12, "bold"), padx=2, pady=6,bg="#A97882")
        lb1_cust_ref.grid(row=0, column=0, sticky=W)
        entry_ref = ttk.Entry(label_frameleft, width=31, textvariable=self.ver_ref,
                              font=("times new roman", 12, "bold"), state="readonly")
        entry_ref.grid(row=0, column=1, sticky=W)
        # ===========lebel entry2========
        lb1_cust_name = Label(label_frameleft, text="Customer Name", font=("times new roman", 12, "bold"), padx=2,
                              pady=6,bg="#A97882")
        lb1_cust_name.grid(row=2, column=0, sticky=W)
        entry_name = ttk.Entry(label_frameleft, width=31, textvariable=self.ver_name,
                               font=("times new roman", 12, "bold"))
        entry_name.grid(row=2, column=1, sticky=W)
        # ===========lebel entry3========
        lb1_cust_father = Label(label_frameleft, text="Father name", font=("times new roman", 12, "bold"), padx=2,
                                pady=6,bg="#A97882")
        lb1_cust_father.grid(row=3, column=0, sticky=W)
        entry_father = ttk.Entry(label_frameleft, width=31, textvariable=self.ver_father,
                                 font=("times new roman", 12, "bold"))
        entry_father.grid(row=3, column=1, sticky=W)

        # ===========lebel entry4========

        lb1_cust_gnd = Label(label_frameleft, text="Gender", font=("times new roman", 12, "bold"), padx=2, pady=6,bg="#A97882")
        lb1_cust_gnd.grid(row=4, column=0, sticky=W)
        combo_gnd = ttk.Combobox(label_frameleft, textvariable=self.ver_gender, font=("times new roman", 11, "bold"),
                                 width=29, state="readonly")
        combo_gnd["value"] = ("male", "Female", "other")
        combo_gnd.current(0)
        combo_gnd.grid(row=4, column=1, sticky=W)

        # ===========lebel entry5========
        lb1_cust_post = Label(label_frameleft, text="Post Code", font=("times new roman", 12, "bold"), padx=2, pady=6,bg="#A97882")
        lb1_cust_post.grid(row=5, column=0, sticky=W)
        entry_code = ttk.Entry(label_frameleft, width=31, textvariable=self.ver_post,
                               font=("times new roman", 12, "bold"))
        entry_code.grid(row=5, column=1, sticky=W)
        # ===========lebel entry6========
        mobile = Label(label_frameleft, text="Mobile", font=("times new roman", 12, "bold"), padx=2, pady=6,bg="#A97882")
        mobile.grid(row=6, column=0, sticky=W)
        entry_mb = ttk.Entry(label_frameleft, width=31, textvariable=self.ver_mobile,
                             font=("times new roman", 12, "bold"))
        entry_mb.grid(row=6, column=1, sticky=W)
        # ===========lebel entry7========
        email = Label(label_frameleft, text="Email", font=("times new roman", 12, "bold"), padx=2, pady=6,bg="#A97882")
        email.grid(row=7, column=0, sticky=W)
        entry_mail = ttk.Entry(label_frameleft, width=31, textvariable=self.ver_email,
                               font=("times new roman", 12, "bold"))
        entry_mail.grid(row=7, column=1, sticky=W)
        # ===========lebel entry8========
        id_proof_Type = Label(label_frameleft, text="Id Proof Type", font=("times new roman", 12, "bold"), padx=2,
                              pady=6,bg="#A97882")
        id_proof_Type.grid(row=8, column=0, sticky=W)
        combo_id_proof = ttk.Combobox(label_frameleft, textvariable=self.ver_idproof,
                                      font=("times new roman", 11, "bold"), width=29,
                                      state="readonly")
        combo_id_proof["value"] = ("NID", "Student id", "Driving licence", "Passport")
        combo_id_proof.current(0)
        combo_id_proof.grid(row=8, column=1, sticky=W)

        # ===========lebel entry9========
        nationality = Label(label_frameleft, text="Nationality", font=("times new roman", 12, "bold"), padx=2, pady=6,bg="#A97882")
        nationality.grid(row=9, column=0, sticky=W)
        combo_nationality = ttk.Combobox(label_frameleft, textvariable=self.ver_nationality,
                                         font=("times new roman", 11, "bold"), width=29, state="readonly")
        combo_nationality["value"] = ("Bangladeshi", "Indian", "American", "British")
        combo_nationality.current(0)
        combo_nationality.grid(row=9, column=1, sticky=W)

        # ===========lebel entry10========
        address = Label(label_frameleft, text="Address", font=("times new roman", 12, "bold"), padx=2, pady=6,bg="#A97882")
        address.grid(row=11, column=0, sticky=W)
        entry_ref = ttk.Entry(label_frameleft, width=31, textvariable=self.ver_address,
                              font=("times new roman", 12, "bold"))
        entry_ref.grid(row=11, column=1, sticky=W)

        # ===========lebel entry11========

        id_number = Label(label_frameleft, text="Id Number", font=("times new roman", 12, "bold"), padx=2, pady=6,bg="#A97882")
        id_number.grid(row=10, column=0, sticky=W)
        entry_id = ttk.Entry(label_frameleft, width=31, textvariable=self.ver_idnumber,
                             font=("times new roman", 12, "bold"))
        entry_id.grid(row=10, column=1, sticky=W)
        # ===============btn============down==
        btn_frame = Frame(label_frameleft, bd=1, relief=RIDGE)
        btn_frame.place(x=0, y=400, width=412)
        btn_add = Button(btn_frame, text="Add", command=self.add_data, font=("arial", 12, "bold"), bg="black",
                         fg="orange", width=9)
        btn_add.grid(row=0, column=0, padx=1)

        btn_update = Button(btn_frame, text="Update",command=self.update, font=("arial", 12, "bold"), bg="black", fg="orange", width=9)
        btn_update.grid(row=0, column=1, padx=1)

        btn_delete = Button(btn_frame, text="Delete",command=self.deletef, font=("arial", 12, "bold"), bg="black", fg="orange", width=9)
        btn_delete.grid(row=0, column=2, padx=1)

        btn_reset = Button(btn_frame, text="Reset",command=self.reset ,font=("arial", 12, "bold"), bg="black", fg="orange", width=10)
        btn_reset.grid(row=0, column=3, padx=1)

        # ============label frame r8=========
        label_frameright = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details And Search System ",
                                      font=("times new roman", 15, "bold"), bg="white",
                                      fg="black")
        label_frameright.place(x=435, y=50, width=860, height=490)
        lbl_sarchby = Label(label_frameright, font=("arial", 12, "bold"), text="Search By", bg="blue", fg="black")
        lbl_sarchby.grid(row=0, column=0, sticky=W)
        combo_sarch = ttk.Combobox(label_frameright,textvariable=self.ver_search, font=("times new roman", 11, "bold"), width=24,
                                   state="readonly")
        combo_sarch["value"] = ("Ref", "name")
        combo_sarch.current(0)
        combo_sarch.grid(row=0, column=1, padx=1)
        entry_src = ttk.Entry(label_frameright, width=24, textvariable=self.text_search,font=("times new roman", 11, "bold"))
        entry_src.grid(row=0, column=2, padx=1)

        # ============btn sarch========
        btn_sarch = Button(label_frameright,text="Search",command=self.search, font=("arial", 11, "bold"), bg="black", fg="orange",
                           width=9)
        btn_sarch.grid(row=0, column=3, padx=1)

        btn_showall = Button(label_frameright, text="Show all",command=self.fetch_data, font=("arial", 11, "bold"), bg="black", fg="orange",
                             width=9)
        btn_showall.grid(row=0, column=6, padx=1)

        # ---------------show table----------#
        tableframeshow = Frame(label_frameright, bd=1, relief=RIDGE)
        tableframeshow.place(x=0, y=50, width=850, height=370)
        scroll_x = ttk.Scrollbar(tableframeshow, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(tableframeshow, orient=VERTICAL)
        self.cust_Details_Table = ttk.Treeview(tableframeshow, columns=(
        "ref", "name", "gender", "father", "post", "mobile", "email", "nationality", "idproof", "idnumber", "address"))
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.cust_Details_Table.xview)
        scroll_y.config(command=self.cust_Details_Table.yview)

        self.cust_Details_Table.heading("ref", text="ReferNo")
        self.cust_Details_Table.heading("name", text="Name")
        self.cust_Details_Table.heading("gender", text="Gender")
        self.cust_Details_Table.heading("father", text="FatherName")
        self.cust_Details_Table.heading("post", text="PostCode")
        self.cust_Details_Table.heading("mobile", text="MobileNumber")
        self.cust_Details_Table.heading("email", text="Email")
        self.cust_Details_Table.heading("nationality", text="Nationality")
        self.cust_Details_Table.heading("idproof", text="IdProof")
        self.cust_Details_Table.heading("idnumber", text="IdNumber")
        self.cust_Details_Table.heading("address", text="Address")

        self.cust_Details_Table["show"] = "headings"

        self.cust_Details_Table.column("ref", width=100)
        self.cust_Details_Table.column("name", width=100)
        self.cust_Details_Table.column("gender", width=100)
        self.cust_Details_Table.column("father", width=100)
        self.cust_Details_Table.column("post", width=100)
        self.cust_Details_Table.column("mobile", width=100)
        self.cust_Details_Table.column("email", width=100)
        self.cust_Details_Table.column("nationality", width=100)
        self.cust_Details_Table.column("idproof", width=100)
        self.cust_Details_Table.column("idnumber", width=100)
        self.cust_Details_Table.column("address", width=100)
        self.cust_Details_Table.pack(fill=BOTH, expand=1)
        self.cust_Details_Table.bind("<ButtonRelease-1>",self.get_vale)
        self.fetch_data()

    def add_data(self):
        if self.ver_mobile.get() == "" or self.ver_idnumber.get() == "":
            messagebox.showerror("Hotel Management System", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost",user="root",password="34632", database="hozayfa1",auth_plugin="mysql_native_password")
                my_cursor = conn.cursor(buffered=True)
                my_cursor.execute("insert into h1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                    self.ver_ref.get(),
                    self.ver_name.get(),
                    self.ver_gender.get(),
                    self.ver_father.get(),
                    self.ver_post.get(),
                    self.ver_mobile.get(),
                    self.ver_email.get(),
                    self.ver_nationality.get(),
                    self.ver_idproof.get(),
                    self.ver_idnumber.get(),
                    self.ver_address.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Hotel Management System", "customer details has been added", parent=self.root)
            except Exception as es:
                messagebox.showwarning("warning", f"some thing went wrong :{str(es)}", parent=self.root)
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="34632", database="hozayfa1",
                                       auth_plugin="mysql_native_password")
        my_cursor = conn.cursor(buffered=True)
        my_cursor.execute("select * from h1")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.cust_Details_Table.delete(*self.cust_Details_Table.get_children())
            for i in rows:
                self.cust_Details_Table.insert("",END,values=i)
        conn.commit()
        conn.close()
    def get_vale(self,event=""):
        curser_row=self.cust_Details_Table.focus()
        content=self.cust_Details_Table.item(curser_row)
        row=content["values"]
        self.ver_ref.set(row[0]),
        self.ver_name.set(row[1]),
        self.ver_gender.set(row[2]),
        self.ver_father.set(row[3]),
        self.ver_post.set(row[4]),
        self.ver_mobile.set("0"+str(row[5])),
        self.ver_email.set(row[6]),
        self.ver_nationality.set(row[7]),
        self.ver_idproof.set(row[8]),
        self.ver_idnumber.set(row[9]),
        self.ver_address.set(row[10])
    def update(self):
        if self.ver_mobile.get()=="":
            messagebox.showerror("Hotel Management System","please enter mobile number",parents=self.root)
        else:

             conn = mysql.connector.connect(host="localhost", user="root", password="34632", database="hozayfa1",
                                           auth_plugin="mysql_native_password")
             my_cursor = conn.cursor(buffered=True)
             my_cursor.execute("update h1 set name=%s, gender=%s, father=%s, post=%s, mobile=%s, email=%s, nationnality=%s, idproof=%s, idnumber=%s, address=%s where ref=%s",(

                 self.ver_name.get(),
                 self.ver_gender.get(),
                 self.ver_father.get(),
                 self.ver_post.get(),
                 self.ver_mobile.get(),
                 self.ver_email.get(),
                 self.ver_nationality.get(),
                 self.ver_idproof.get(),
                 self.ver_idnumber.get(),
                 self.ver_address.get(),
                 self.ver_ref.get()

                 ))
             conn.commit()
             self.fetch_data()
             conn.close()
             messagebox.showinfo("Hotel Management System","customer has been updated successfully",parent=self.root)
    def deletef(self):
        deletecheck=messagebox.askyesno("Hotel Management System","Do you delete this customer",parent=self.root)
        if deletecheck:
            conn = mysql.connector.connect(host="localhost", user="root", password="34632", database="hozayfa1",
                                           auth_plugin="mysql_native_password")
            my_cursor = conn.cursor(buffered=True)
            my_cursor.execute("delete from h1 where ref=%s",(
                self.ver_ref.get(),
            ))
        else:
            return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):

            conn = mysql.connector.connect(host="localhost", user="root", password="34632", database="hozayfa1",
                                           auth_plugin="mysql_native_password")
            my_cursor = conn.cursor(buffered=True)
            x = random.randint(1000, 9999)
            self.ver_ref.set(str(x)),
            self.ver_name.set(""),
            self.ver_father.set(""),
            self.ver_post.set(""),
            self.ver_mobile.set(""),
            self.ver_email.set(""),
            self.ver_idnumber.set(""),
            self.ver_address.set("")
            conn.commit()
            self.fetch_data()
            conn.close()
    def search(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="34632", database="hozayfa1",
                                       auth_plugin="mysql_native_password")
        my_cursor = conn.cursor(buffered=True)
        x = self.text_search.get()
        y = str(self.ver_search.get())
        my_cursor.execute(f"select * from h1 where {y}='{x}'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.cust_Details_Table.delete(*self.cust_Details_Table.get_children())
            for i in rows:
                self.cust_Details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()

if __name__ == '__main__':
    root = Tk()
    obj = cust_win(root)
    root.mainloop()
