from tkinter import *
import PIL.Image
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
from time import strftime
from datetime import datetime

class room_win:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1300x550+228+250")
        # =============title=========
        lbl_title = Label(self.root, text="ROOM BOOKING", font=("times new roman", 20, "bold"), bg="black",
                          fg="orange", bd=1, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1300, height=50)
        #================variable============
        self.var_contact=StringVar()
        self.var_ckin = StringVar()
        self.var_ck_out = StringVar()
        self.var_no_of_date = StringVar()
        self.var_Room_type = StringVar()
        self.var_meal = StringVar()
        self.var_meal.set("breakfast")
        self.var_Total_cost = StringVar()
        self.var_Paid_tax = StringVar()
        self.var_sub_total = StringVar()
        self.var_room_avelable = StringVar()
        self.ver_search = StringVar()
        self.text_search = StringVar()

        # =========logo==========
        img2 = Image.open("photo_2024-07-18_01-28-47.jpg")
        img2 = img2.resize((100, 50), PIL.Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        Lbimage = Label(self.root, image=self.photoimg2, bd=2, relief=RIDGE)
        Lbimage.place(x=0, y=0, width=100, height=50)

        # =================label frame==========
        label_framelef = LabelFrame(self.root, bd=4, relief=RIDGE, text="ROOM BOOKING DETAILS",
                                     font=("times new roman", 10, "bold"), bg="#A97882",
                                     fg="black")
        label_framelef.place(x=5, y=50, width=425, height=490)


        # =========right side image=========



        #img4 = Image.open(r"C:\Users\asus\OneDrive\Pictures\photo_2024-08-23_13-54-45.jpg")
        #img4 = img4.resize((295, 377), PIL.Image.Resampling.LANCZOS)
        #self.photoimg4 = ImageTk.PhotoImage(img4)
        #Lbimage = Label(label_framelef, image=self.photoimg4, bd=4, relief=RIDGE)
        #Lbimage.place(x=125, y=0, width=295, height=377)




        # ===========lebel entry1========
        lb1_customer_contact = Label(label_framelef, text="Customer Contact",font=("times new roman", 12, "bold"),
                                     padx=2, pady=6,bg="#A97882")
        lb1_customer_contact.grid(row=0, column=0, sticky=W)
        entrycustomer_contact = ttk.Entry(label_framelef, width=20,textvariable=self.var_contact,
                                          font=("times new roman", 12, "bold"))
        entrycustomer_contact.grid(row=0, column=1, sticky=W)
        btn_fetch = Button(label_framelef, text="Fetch", command=self.fetch_contact,font=("arial", 9, "bold"), bg="black",
                           fg="orange", width=9, padx=2,
                           pady=-2)
        btn_fetch.place(x=300, y=4)
        # ===========lebel entry2========
        lb1_date = Label(label_framelef, text="Check_in Date", font=("times new roman", 12, "bold"), padx=2,
                              pady=6,bg="#A97882")
        lb1_date.grid(row=1, column=0, sticky=W)
        entry_date = ttk.Entry(label_framelef, width=29,textvariable=self.var_ckin,
                               font=("times new roman", 12, "bold"))
        entry_date.grid(row=1, column=1, sticky=W)
        # ===========lebel entry3========
        lb1_out_date = Label(label_framelef, text="Check_out Date",font=("times new roman", 12, "bold"), padx=2,
                                pady=6,bg="#A97882")
        lb1_out_date.grid(row=2, column=0, sticky=W)
        entry_out_date = ttk.Entry(label_framelef, width=29,textvariable=self.var_ck_out,
                                 font=("times new roman", 12, "bold"))
        entry_out_date.grid(row=2, column=1, sticky=W)

        # ===========lebel entry4========

        lb1_room_type = Label(label_framelef, text="Room Type", font=("times new roman", 12, "bold"), padx=2, pady=6,bg="#A97882")
        lb1_room_type.grid(row=3, column=0, sticky=W)
        conn = mysql.connector.connect(host="localhost", user="root", password="34632", database="hozayfa1",
                                       auth_plugin="mysql_native_password")
        my_cursor = conn.cursor(buffered=True)
        my_cursor.execute("select RoomType from h3")
        type = my_cursor.fetchall()
        combo_room_type = ttk.Combobox(label_framelef, font=("times new roman", 11, "bold"),textvariable=self.var_Room_type,
                                 width=27, state="readonly")
        combo_room_type["value"] = type
        combo_room_type.current(0)
        combo_room_type.grid(row=3,column=1,sticky=W)

        # ===========lebel entry5========
        lb1_meal = Label(label_framelef, text="Meal ",font=("times new roman", 12, "bold"), padx=2, pady=6,bg="#A97882")
        lb1_meal.grid(row=4, column=0, sticky=W)
        entry_meal = ttk.Entry(label_framelef, width=29, textvariable=self.var_meal,
                               font=("times new roman", 12, "bold"))
        entry_meal.grid(row=4, column=1, sticky=W)
        # ===========lebel entry6========
        avl_room = Label(label_framelef, text="Available Room",font=("times new roman", 12, "bold"), padx=2, pady=6,bg="#A97882")
        avl_room.grid(row=5, column=0, sticky=W)
        #entry_avl_room = ttk.Entry(label_framelef, width=29, textvariable=self.var_room_avelable,
                             #font=("times new roman", 12, "bold"))
        #entry_avl_room.grid(row=5, column=1, sticky=W)
        conn = mysql.connector.connect(host="localhost", user="root", password="34632", database="hozayfa1",
                                       auth_plugin="mysql_native_password")
        my_cursor = conn.cursor(buffered=True)
        my_cursor.execute("select RoomNo from h3")
        rows = my_cursor.fetchall()
        combo_avl_room = ttk.Combobox(label_framelef, font=("times new roman", 11, "bold"),
                                       textvariable=self.var_room_avelable,
                                       width=27, state="readonly")
        combo_avl_room["value"] = rows
        combo_avl_room.current(0)
        combo_avl_room.grid(row=5, column=1, sticky=W)

        # ===========lebel entry7========
        No_of_Days = Label(label_framelef, text="No of Days",font=("times new roman", 12, "bold"), padx=2, pady=6,bg="#A97882")
        No_of_Days.grid(row=6, column=0, sticky=W)
        entry_No_of_Days  = ttk.Entry(label_framelef, width=29, textvariable=self.var_no_of_date,
                               font=("times new roman", 12, "bold"))
        entry_No_of_Days .grid(row=6, column=1, sticky=W)
        # ===========lebel entry10========
        paid_Tax = Label(label_framelef, text="Paid Tax", font=("times new roman", 12, "bold"), padx=2, pady=6,bg="#A97882")
        paid_Tax.grid(row=7, column=0, sticky=W)
        entry_paid_Tax = ttk.Entry(label_framelef, width=29,textvariable=self.var_Paid_tax,
                              font=("times new roman", 12, "bold"))
        entry_paid_Tax.grid(row=7, column=1, sticky=W)
        # ===========lebel entry11========
        sub_total = Label(label_framelef, text="Sub Total", font=("times new roman", 12, "bold"), padx=2, pady=6,bg="#A97882")
        sub_total.grid(row=8, column=0, sticky=W)
        entry_sub_total = ttk.Entry(label_framelef, width=29,textvariable=self.var_sub_total,
                                   font=("times new roman", 12, "bold"))
        entry_sub_total.grid(row=8, column=1, sticky=W)
        # ===========lebel entry12========
        total_cost= Label(label_framelef, text="Total Cost", font=("times new roman", 12, "bold"), padx=2, pady=6,bg="#A97882")
        total_cost.grid(row=9, column=0, sticky=W)
        entry_total_cost = ttk.Entry(label_framelef, width=29,textvariable=self.var_Total_cost,
                                   font=("times new roman", 12, "bold"))
        entry_total_cost.grid(row=9, column=1, sticky=W)
        # ===============btn============down==
        btn_frame = Frame(label_framelef, bd=1, relief=RIDGE)
        btn_frame.place(x=0, y=400, width=412)
        btn_add = Button(btn_frame, text="Add",command=self.add_data, font=("arial", 12, "bold"), bg="black",
                         fg="orange", width=9)
        btn_add.grid(row=0, column=0, padx=1)

        btn_update = Button(btn_frame, text="Update",command=self.update, font=("arial", 12, "bold"), bg="black",
                            fg="orange", width=9)
        btn_update.grid(row=0, column=1, padx=1)

        btn_delete = Button(btn_frame, text="Delete",command=self.deletef,font=("arial", 12, "bold"), bg="black",
                            fg="orange", width=9)
        btn_delete.grid(row=0, column=2, padx=1)

        btn_reset = Button(btn_frame, text="Reset",command=self.reset,font=("arial", 12, "bold"), bg="black",
                           fg="orange", width=10)
        btn_reset.grid(row=0, column=3, padx=1)
        #==========bill button==========
        total_bill_button =Button(label_framelef, text="Bill",command=self.total ,font=("times new roman", 10, "bold"), bg="black",
                           fg="orange", width=10)
        total_bill_button.grid(row=10, column=0, sticky=W)

        # ================== right side image============
        img3 = Image.open("midpic.jpg")
        img3 = img3.resize((536, 240), PIL.Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        Lbimage = Label(self.root, image=self.photoimg3, bd=2, relief=RIDGE)
        Lbimage.place(x=760, y=50, width=536, height=240)
        # ============table frame search system=========
        label_frameright = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details And Search System ",
                                      font=("times new roman", 15, "bold"), bg="white",
                                      fg="black")
        label_frameright.place(x=435, y=280, width=860, height=260)
        lbl_sarchby = Label(label_frameright, font=("arial", 12, "bold"), text="Search By", bg="blue", fg="black")
        lbl_sarchby.grid(row=0, column=0, sticky=W)
        combo_sarch = ttk.Combobox(label_frameright,textvariable=self.ver_search, font=("times new roman", 11, "bold"),
                                   width=24,
                                   state="readonly")
        combo_sarch["value"] = ("contract", "avlroom")
        combo_sarch.current(0)
        combo_sarch.grid(row=0, column=1, padx=1)
        entry_src = ttk.Entry(label_frameright, width=24, textvariable=self.text_search,
                              font=("times new roman", 11, "bold"))
        entry_src.grid(row=0, column=2, padx=1)

        # ============btn sarch========
        btn_sarch = Button(label_frameright, text="Search", command=self.searchf,font=("arial", 11, "bold"), bg="black",
                           fg="orange",
                           width=9)
        btn_sarch.grid(row=0, column=3, padx=1)

        btn_showall = Button(label_frameright, text="Show all", command=self.fetch_data,font=("arial", 11, "bold"),
                             bg="black", fg="orange",
                             width=9)
        btn_showall.grid(row=0, column=6, padx=1)

        # ---------------show table----------#
        tableframeshow = Frame(label_frameright, bd=1, relief=RIDGE)
        tableframeshow.place(x=0, y=50, width=850, height=170)
        scroll_x = ttk.Scrollbar(tableframeshow, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(tableframeshow, orient=VERTICAL)
        self.Details_Table = ttk.Treeview(tableframeshow, columns=(
            "Contact", "Check_in Date", "Check_out Date", "Room Type","Meal","Available Room", "No of Date", "Paid Tax", "Sub Total", "Total cost"))
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Details_Table.xview)
        scroll_y.config(command=self.Details_Table.yview)
        self.Details_Table.heading("Contact", text="Contact")
        self.Details_Table.heading("Check_in Date", text="Check_in Date")
        self.Details_Table.heading("Check_out Date", text="Check_out Date")
        self.Details_Table.heading("Room Type", text="Room Type")
        self.Details_Table.heading("Meal", text="Meal")
        self.Details_Table.heading("Available Room", text="Available Room")
        self.Details_Table.heading("No of Date", text="No of Date")

        self.Details_Table["show"] = "headings"
        self.Details_Table.column("Contact", width=115)
        self.Details_Table.column("Check_in Date", width=115)
        self.Details_Table.column("Check_out Date", width=115)
        self.Details_Table.column("Room Type", width=115)
        self.Details_Table.column("Available Room", width=115)
        self.Details_Table.column("Meal", width=115)
        self.Details_Table.column("No of Date", width=115)

        self.Details_Table.pack(fill=BOTH, expand=1)
        self.Details_Table.bind("<ButtonRelease-1>", self.get_vale)
        self.fetch_data()
    def fetch_contact(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please Enter Customer Contact Number",parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="34632", database="hozayfa1",
                                           auth_plugin="mysql_native_password")
            my_cursor = conn.cursor(buffered=True)

            my_cursor.execute(f"select name from h1 where  mobile like '%{self.var_contact.get()}'")
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","This Number Not Found",parent=self.root)
            else:
                conn.commit()
                conn.close()
                showdataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                showdataframe.place(x=442,y=55,width=300,height=180)
                lblname1=Label(showdataframe,text="Name:",font=("arial",12,"bold"))
                lblname1.grid(row=0, column=0, sticky=W)
                lblname1 = Label(showdataframe, text=row, font=("arial", 12, "bold"))
                lblname1.grid(row=0, column=1, sticky=W)
                # =======gender==========
                conn = mysql.connector.connect(host="localhost", user="root", password="34632", database="hozayfa1",
                                               auth_plugin="mysql_native_password")
                my_cursor = conn.cursor(buffered=True)

                my_cursor.execute(f"select gender from h1 where  mobile like '%{self.var_contact.get()}'")
                row = my_cursor.fetchone()
                lblgender = Label(showdataframe, text="Gender:", font=("arial", 12, "bold"))
                lblgender.grid(row=1, column=0, sticky=W)
                lblgender = Label(showdataframe, text=row, font=("arial", 12, "bold"))
                lblgender.grid(row=1, column=1, sticky=W)
                # =======father==========
                conn = mysql.connector.connect(host="localhost", user="root", password="34632", database="hozayfa1",
                                               auth_plugin="mysql_native_password")
                my_cursor = conn.cursor(buffered=True)
                my_cursor.execute(f"select father from h1 where  mobile like '%{self.var_contact.get()}'")
                row = my_cursor.fetchone()
                lblgender = Label(showdataframe, text="Father:", font=("arial", 12, "bold"))
                lblgender.grid(row=2, column=0, sticky=W)
                lblgender = Label(showdataframe, text=row, font=("arial", 12, "bold"))
                lblgender.grid(row=2, column=1, sticky=W)
                # =======email==========
                conn = mysql.connector.connect(host="localhost", user="root", password="34632", database="hozayfa1",
                                               auth_plugin="mysql_native_password")
                my_cursor = conn.cursor(buffered=True)

                my_cursor.execute(f"select email from h1 where  mobile like '%{self.var_contact.get()}'")
                row = my_cursor.fetchone()
                lblgender = Label(showdataframe, text="Email:", font=("arial", 12, "bold"))
                lblgender.grid(row=3, column=0, sticky=W)
                lblgender = Label(showdataframe, text=row, font=("arial", 12, "bold"))
                lblgender.grid(row=3, column=1, sticky=W)
                # =======nationality==========
                conn = mysql.connector.connect(host="localhost", user="root", password="34632", database="hozayfa1",
                                               auth_plugin="mysql_native_password")
                my_cursor = conn.cursor(buffered=True)

                my_cursor.execute(f"select nationnality from h1 where  mobile like '%{self.var_contact.get()}'")
                row = my_cursor.fetchone()
                lblgender = Label(showdataframe, text="Nationality:", font=("arial", 12, "bold"))
                lblgender.grid(row=4, column=0, sticky=W)
                lblgender = Label(showdataframe, text=row, font=("arial", 12, "bold"))
                lblgender.grid(row=4, column=1, sticky=W)
                # =======address==========
                conn = mysql.connector.connect(host="localhost", user="root", password="34632", database="hozayfa1",
                                               auth_plugin="mysql_native_password")
                my_cursor = conn.cursor(buffered=True)
                my_cursor.execute(f"select address from h1 where  mobile like '%{self.var_contact.get()}'")
                row = my_cursor.fetchone()
                lblgender = Label(showdataframe, text="Address:", font=("arial", 12, "bold"))
                lblgender.grid(row=5, column=0, sticky=W)
                lblgender = Label(showdataframe, text=row, font=("arial", 12, "bold"))
                lblgender.grid(row=5, column=1, sticky=W)

    def add_data(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Hotel Management System", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost",user="root",password="34632", database="hozayfa1",auth_plugin="mysql_native_password")
                my_cursor = conn.cursor(buffered=True)
                my_cursor.execute("insert into h2 values(%s,%s,%s,%s,%s,%s,%s)", (
                self.var_contact.get(),
                self.var_ckin.get(),
                self.var_ck_out.get(),
                self.var_Room_type.get(),
                self.var_meal.get(),
                self.var_room_avelable.get(),
                self.var_no_of_date.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                w=self.var_room_avelable.get()
                conn = mysql.connector.connect(host="localhost", user="root", password="34632", database="hozayfa1",
                                               auth_plugin="mysql_native_password")
                my_cursor = conn.cursor(buffered=True)
                my_cursor.execute(f"delete from h3 where RoomNo={w}")
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Hotel Management System", "Room details has been added", parent=self.root)
            except Exception as es:
                messagebox.showwarning("warning", f"some thing went wrong :{str(es)}", parent=self.root)
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="34632", database="hozayfa1",
                                       auth_plugin="mysql_native_password")
        my_cursor = conn.cursor(buffered=True)
        my_cursor.execute("select * from h2")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Details_Table.delete(*self.Details_Table.get_children())
            for i in rows:
                self.Details_Table.insert("",END,values=i)
        conn.commit()
        conn.close()
    def get_vale(self,event=""):
        curser_row=self.Details_Table.focus()
        content=self.Details_Table.item(curser_row)
        row=content["values"]
        self.var_contact.set("0"+str(row[0])),
        self.var_ckin.set(row[1]),
        self.var_ck_out.set(row[2]),
        self.var_Room_type.set(row[3]),
        self.var_meal.set(row[4]),
        self.var_room_avelable.set(row[5]),
        self.var_no_of_date.set(row[6])
    def update(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Hotel Management System","please enter mobile number",parents=self.root)
        else:

             conn = mysql.connector.connect(host="localhost", user="root", password="34632", database="hozayfa1",
                                           auth_plugin="mysql_native_password")
             my_cursor = conn.cursor(buffered=True)
             my_cursor.execute("update h2 set  check_in=%s, check_out=%s, roomtype=%s, meal=%s, avlroom=%s, noofdate=%s where contract=%s",(


                 self.var_ckin.get(),
                 self.var_ck_out.get(),
                 self.var_no_of_date.get(),
                 self.var_Room_type.get(),
                 self.var_meal.get(),
                 self.var_room_avelable.get(),
                 self.var_contact.get()

                 ))
             conn.commit()
             self.fetch_data()
             conn.close()
             messagebox.showinfo("Hotel Management System","Room details has been updated successfully",parent=self.root)
    def deletef(self):
        deletecheck = messagebox.askyesno("Hotel Management System", "Do you delete this room details", parent=self.root)
        if deletecheck:
            r=self.var_room_avelable.get()
            f=r[0]
            rt=self.var_Room_type.get()
            conn = mysql.connector.connect(host="localhost", user="root", password="34632", database="hozayfa1",
                                           auth_plugin="mysql_native_password")
            my_cursor = conn.cursor(buffered=True)
            my_cursor.execute("delete from h2 where contract=%s", (
                self.var_contact.get(),
            ))
        else:
            return
        conn.commit()
        self.fetch_data()
        conn.close()
        conn = mysql.connector.connect(host="localhost", user="root", password="34632", database="hozayfa1",
                                       auth_plugin="mysql_native_password")
        my_cursor = conn.cursor(buffered=True)
        my_cursor.execute("insert into h3 values(%s,%s,%s)", (
            f,
            r,
            rt

        ))
        conn.commit()
        self.fetch_data()
        conn.close()


    def reset(self):

            conn = mysql.connector.connect(host="localhost", user="root", password="34632", database="hozayfa1",
                                           auth_plugin="mysql_native_password")
            my_cursor = conn.cursor(buffered=True)
            self.var_contact.set(""),
            self.var_ckin.set(""),
            self.var_ck_out.set(""),
            self.var_Room_type.set("Single"),
            self.var_meal.set("breakfast"),
            self.var_room_avelable.set(""),
            self.var_no_of_date.set(""),
            self.var_Paid_tax.set(""),
            self.var_sub_total.set(""),
            self.var_Total_cost.set("")
            conn.commit()
            self.fetch_data()
            conn.close()
    def total(self):
        indate=self.var_ckin.get()
        outdate=self.var_ck_out.get()
        indate=datetime.strptime(indate,"%d/%m/%Y")
        outdate = datetime.strptime(outdate, "%d/%m/%Y")
        self.var_no_of_date.set(abs(outdate-indate).days)
        if self.var_Room_type.get()=="Double":
            q1=int(3000)
            q2=int(200)
            q3=(q1+q2)*int(self.var_no_of_date.get())
            tax=float("%0.2f"%(q3*0.15))
            total=q3+tax
            self.var_Paid_tax.set(str(tax)+"TK")
            self.var_sub_total.set(str(q3)+"TK")
            self.var_Total_cost.set(str(total)+"Tk")
        if self.var_Room_type.get()=="Single":
            q1=int(2000)
            q2=int(200)
            q3=(q1+q2)*int(self.var_no_of_date.get())
            tax=float("%0.2f"%(q3*0.15))
            total=q3+tax
            self.var_Paid_tax.set(str(tax)+"TK")
            self.var_sub_total.set(str(q3)+"TK")
            self.var_Total_cost.set(str(total)+"Tk")
    def searchf(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="34632", database="hozayfa1",
                                       auth_plugin="mysql_native_password")
        my_cursor = conn.cursor(buffered=True)
        x=self.text_search.get()
        y=self.ver_search.get()
        my_cursor.execute(f"select * from h2 where {y}={x}")
        rows=my_cursor.fetchall()
        if len(rows)!=0:

            self.Details_Table.delete(*self.Details_Table.get_children())
            for i in rows:
                self.Details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()




if __name__ == '__main__':
    root = Tk()
    obj = room_win(root)
    root.mainloop()
