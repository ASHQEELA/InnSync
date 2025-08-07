from tkinter import *
import PIL.Image
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
from time import strftime
from datetime import datetime
class details_win:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1300x550+228+250")
        #==========variable======
        self.var_floor=StringVar()
        self.var_room=StringVar()
        self.var_room_Type=StringVar()
        # =============title=========
        lbl_title = Label(self.root, text="ROOMBOOKING DETAILS", font=("times new roman", 18, "bold"), bg="black",
                          fg="orange", bd=1, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1300, height=50)

        # =========log==========
        img2 = Image.open("photo_2024-07-18_01-28-47.jpg")
        img2 = img2.resize((100, 50), PIL.Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        Lbimage = Label(self.root, image=self.photoimg2, bd=2, relief=RIDGE)
        Lbimage.place(x=0, y=0, width=100, height=50)

        # =================label frame==========
        label_frameleft = LabelFrame(self.root, bd=4, relief=RIDGE, text="New Room Add",
                                     font=("times new roman", 15, "bold"), bg="white",
                                     fg="black")
        label_frameleft.place(x=5, y=50, width=540, height=350)

        #===========floor================

        lb1_floor = Label(label_frameleft, text="Floor No", font=("times new roman", 12, "bold"), padx=2, pady=4)
        lb1_floor.grid(row=0, column=0, sticky=W)
        entry_floor = ttk.Entry(label_frameleft, width=29, textvariable=self.var_floor,
                              font=("times new roman", 12, "bold"))
        entry_floor.grid(row=0, column=1, sticky=W)

        #======room no=============

        lb1_Room = Label(label_frameleft, text="Room No", font=("times new roman", 12, "bold"), padx=2, pady=4)
        lb1_Room.grid(row=1, column=0, sticky=W)
        entry_room = ttk.Entry(label_frameleft, width=29, textvariable=self.var_room,
                                font=("times new roman", 12, "bold"))
        entry_room.grid(row=1, column=1, sticky=W)

        #=======Rooom Type=========

        lb1_room_type = Label(label_frameleft, text="Room Type", font=("times new roman", 12, "bold"), padx=2, pady=4)
        lb1_room_type.grid(row=2, column=0, sticky=W)
        entry_room_typ = ttk.Entry(label_frameleft, width=29, textvariable=self.var_room_Type,
                                font=("times new roman", 12, "bold"))
        entry_room_typ.grid(row=2, column=1, sticky=W)

        # ===============btn============down==

        btn_frame = Frame(label_frameleft, bd=1, relief=RIDGE)
        btn_frame.place(x=0, y=200, width=412)
        btn_add = Button(btn_frame, text="Add", command=self.add_data,font=("arial", 12, "bold"), bg="black",
                         fg="orange", width=9)
        btn_add.grid(row=0, column=0, padx=1)

        btn_update = Button(btn_frame, text="Update",command=self.update,font=("arial", 12, "bold"), bg="black",
                            fg="orange", width=9)
        btn_update.grid(row=0, column=1, padx=1)

        btn_delete = Button(btn_frame, text="Delete",command=self.deletef, font=("arial", 12, "bold"), bg="black",
                            fg="orange", width=9)
        btn_delete.grid(row=0, column=2, padx=1)

        btn_reset = Button(btn_frame, text="Reset", command=self.reset,font=("arial", 12, "bold"), bg="black",
                           fg="orange", width=10)
        btn_reset.grid(row=0, column=3, padx=1)
        #=========rigt frame==========
        label_frameright = LabelFrame(self.root, bd=2, relief=RIDGE, text="Show Room Details ",
                                      font=("times new roman", 15, "bold"), bg="white",
                                      fg="black")
        label_frameright.place(x=600, y=55, width=600, height=350)
        # ---------------show table----------#
        scroll_x = ttk.Scrollbar(label_frameright, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(label_frameright, orient=VERTICAL)
        self.cust_Details_Table = ttk.Treeview(label_frameright, columns=(
            "Floor", "RoomNo", "RoomType"))
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.cust_Details_Table.xview)
        scroll_y.config(command=self.cust_Details_Table.yview)
        self.cust_Details_Table.heading("Floor", text="Floor")
        self.cust_Details_Table.heading("RoomNo", text="RoomNo")
        self.cust_Details_Table.heading("RoomType", text="RoomType")
        self.cust_Details_Table["show"] = "headings"
        self.cust_Details_Table.column("Floor", width=100)
        self.cust_Details_Table.column("RoomNo", width=100)
        self.cust_Details_Table.column("RoomType", width=100)
        self.cust_Details_Table.pack(fill=BOTH, expand=1)
        self.cust_Details_Table.bind("<ButtonRelease-1>",self.get_vale)
        self.fetch_data()
    def add_data(self):
        if self.var_room.get() == "":
            messagebox.showerror("Hotel Management System", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost",user="root",password="34632", database="hozayfa1",auth_plugin="mysql_native_password")
                my_cursor = conn.cursor(buffered=True)
                my_cursor.execute("insert into h3 values(%s,%s,%s)", (
                    self.var_floor.get(),
                    self.var_room.get(),
                    self.var_room_Type.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Hotel Management System", "New Room Added Successfully", parent=self.root)
            except Exception as es:
                messagebox.showwarning("warning", f"some thing went wrong :{str(es)}", parent=self.root)
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="34632", database="hozayfa1",
                                       auth_plugin="mysql_native_password")
        my_cursor = conn.cursor(buffered=True)
        my_cursor.execute("select * from h3")
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
        self.var_floor.set(row[0]),
        self.var_room.set(row[1]),
        self.var_room_Type.set(row[2])
    def update(self):
        if self.var_room.get()=="":
            messagebox.showerror("Hotel Management System","please enter mobile number",parents=self.root)
        else:

             conn = mysql.connector.connect(host="localhost", user="root", password="34632", database="hozayfa1",
                                           auth_plugin="mysql_native_password")
             my_cursor = conn.cursor(buffered=True)
             my_cursor.execute("update h3 set Floor=%s, RoomType=%s where RoomNo=%s",(

                 self.var_floor.get(),
                 self.var_room_Type.get(),
                 self.var_room.get()


                 ))
             conn.commit()
             self.fetch_data()
             conn.close()
             messagebox.showinfo("Hotel Management System","Room Details has been updated successfully",parent=self.root)
    def deletef(self):
        deletecheck=messagebox.askyesno("Hotel Management System","Do you delete this room",parent=self.root)
        if deletecheck:
            conn = mysql.connector.connect(host="localhost", user="root", password="34632", database="hozayfa1",
                                           auth_plugin="mysql_native_password")
            my_cursor = conn.cursor(buffered=True)
            my_cursor.execute("delete from h3 where RoomNo=%s",(
                self.var_room.get(),
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

            self.var_floor.set(""),
            self.var_room.set(""),
            self.var_room_Type.set(""),

            conn.commit()
            self.fetch_data()
            conn.close()



if __name__ == '__main__':
    root = Tk()
    obj = details_win(root)
    root.mainloop()