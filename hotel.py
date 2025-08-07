from tkinter import*

import PIL.Image
from PIL import Image,ImageTk
from cust import cust_win
from room import room_win
from details import details_win
class HotelManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("InnSync")
        self.root.geometry("1550x800+0+0")
        #============img1=================
        img1=Image.open("pg1.jpg")
        img1=img1.resize((1550,170),PIL.Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        Lbimage=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        Lbimage.place(x=0,y=0,width=1550,height=170)

        #============logo=========================

        img2 = Image.open("photo_2024-07-18_01-28-47.jpg")
        img2 = img2.resize((230, 170), PIL.Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        Lbimage = Label(self.root, image=self.photoimg2, bd=1, relief=GROOVE)
        Lbimage.place(x=0, y=0, width=230, height=170)
        #=============title================
        lbl_title=Label(self.root,text="InnSync",font=("times new roman",40,"bold"),bg="black",fg="orange",bd=1,relief=RIDGE)
        lbl_title.place(x=0,y=170,width=1550,height=50)

        #==========main frame=========

        main_frame=Frame(self.root,bd=1,relief=RIDGE)
        main_frame.place(x=0,y=220,width=1550,height=620)

        #========menu===========

        lbl_title = Label(main_frame, text="MENU", font=("times new roman", 20, "bold"), bg="black",
                          fg="orange", bd=1, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=230)
        #========btn============
        btn_frame = Frame(main_frame, bd=1, relief=RIDGE)
        btn_frame.place(x=0, y=35, width=230, height=190)
        cust_btn=Button(btn_frame,text="CUSTOMER",command=self.cust_details,width=22,font=("times new roman", 14, "bold"), bg="black",
                          fg="orange", bd=1,cursor="hand2" )
        cust_btn.grid(row=0,column=0,pady=1)

        room_btn = Button(btn_frame, text="ROOM", width=22,command=self.room_details, font=("times new roman", 14, "bold"), bg="black",
                          fg="orange", bd=1, cursor="hand2")
        room_btn.grid(row=1, column=0, pady=1)

        details_btn = Button(btn_frame, text="DETAILS", width=22, command=self.detailnew,font=("times new roman", 14, "bold"), bg="black",
                          fg="orange", bd=1, cursor="hand2")
        details_btn.grid(row=2, column=0, pady=1)

        report_btn = Button(btn_frame, text="REPORT", width=22, font=("times new roman", 14, "bold"), bg="black",
                          fg="orange", bd=1, cursor="hand2")
        report_btn.grid(row=3, column=0, pady=1)

        log_out_btn = Button(btn_frame, text="LOG OUT", width=22, command=self.logoutf,font=("times new roman", 14, "bold"), bg="black",
                          fg="orange", bd=1, cursor="hand2")
        log_out_btn.grid(row=4, column=0, pady=1)
        #=========right side image=========
        img3 = Image.open("png3.jpg")
        img3 = img3.resize((1310, 590), PIL.Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        Lbimage = Label(main_frame, image=self.photoimg3, bd=4, relief=RIDGE)
        Lbimage.place(x=225, y=0, width=1310, height=590)

        # ==========#======image 4===============
        img4 = Image.open("png4.jpg")
        img4 = img4.resize((227, 170), PIL.Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        Lbimage = Label(self.root, image=self.photoimg4, bd=1, relief=RIDGE)
        Lbimage.place(x=0, y=447, width=227, height=170)
        # ==========#======image 5===============
        img5 = Image.open("png5.jpg")
        img5 = img5.resize((227, 170), PIL.Image.Resampling.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        Lbimage = Label(self.root, image=self.photoimg5, bd=1, relief=RIDGE)
        Lbimage.place(x=0, y=618, width=227, height=170)




    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=cust_win(self.new_window)
    def room_details(self):
        self.new_window=Toplevel(self.root)
        self.app=room_win(self.new_window)
    def detailnew(self):
        self.new_window=Toplevel(self.root)
        self.app=details_win(self.new_window)
    def logoutf(self):
        self.root.destroy()

if __name__ == '__main__':
    root=Tk()
    obj=HotelManagementSystem(root)
    root.mainloop()