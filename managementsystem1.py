from tkinter import *
from tkinter import ttk
import auth as auth
import pyodbc
from tkinter import messagebox
from PIL import Image, ImageTk

global b
b = 0

auth.main_screen()

if auth.a == 1:

    class Tours:
        def __init__(self, root):
            self.root = root
            self.root.title("Tour&Travel Management System")
            self.root.geometry("1350x700+0+0")
            title = Label(self.root, text="Tour&Travel Management System", bd=10, relief=GROOVE,
                          font=("Times new roman", 40, "bold"), bg="RosyBrown", fg="dark green")
            title.pack(side=TOP, fill=X)

            # ========================================================AllVariables======================================================================#

            self.date = StringVar()
            self.vehno = StringVar()
            self.vehtype = StringVar()
            self.LO = StringVar()
            self.optime = StringVar()
            self.clotime = StringVar()
            self.ttime = StringVar()
            self.opkm = StringVar()
            self.clokm = StringVar()
            self.totalkm = StringVar()
            self.nt = StringVar()
            self.fuel = StringVar()
            self.amt = StringVar()
            self.search_by = StringVar()
            self.search_txt = StringVar()
            self.Bill_no = StringVar()


            # =======================================================DetailFrame(RHS)========================================================================================#
            Detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="RosyBrown")
            Detail_Frame.place(x=540, y=90, width=780, height=640)

            lb1_search = Label(Detail_Frame, text="Search", bg="RosyBrown", fg="Dark Green",
                               font=("Times new roman", 20, "bold"))
            lb1_search.grid(row=0, column=0, pady=10, padx=20, sticky="w")

            combo_srh = ttk.Combobox(Detail_Frame, textvariable=self.search_by, width=10,
                                     font=("Times new roman", 10, "bold"), state='readonly')
            combo_srh['values'] = ("Veh_No", "Veh_type", "LO")
            combo_srh.grid(row=0, column=5, padx=10, pady=5)

            txt_search = Entry(Detail_Frame, textvariable=self.search_txt, font=("Times new roman", 15, "bold"), bd=5,
                               relief=GROOVE)
            txt_search.grid(row=0, column=1, pady=10, padx=5, sticky="w")

            searchbtn = Button(Detail_Frame, text="Search", width=10, command=self.search)
            searchbtn.grid(row=0, column=2, padx=10, pady=10)
            showbtn = Button(Detail_Frame, text="Showall", width=10, command=self.fetch)
            showbtn.grid(row=0, column=3, padx=10, pady=10)


            # =====================================================ManageFrame(LHS)=====================================================================================#
            Manage_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="RosyBrown")
            Manage_Frame.place(x=20, y=100, width=490, height=600)

            m_title = Label(Manage_Frame, text="Manage Car Bookings", bg="RosyBrown", fg="Dark Green",
                            font=("Times new roman", 20, "bold"))
            m_title.grid(row=0, columnspan=2, pady=10)

            lb1_date = Label(Manage_Frame, text="Date", bg="RosyBrown", fg="Dark Green",
                             font=("Times new roman", 15, "bold"))
            lb1_date.grid(row=1, column=0, pady=5, padx=10, sticky="w")

            txt_date = Entry(Manage_Frame, textvariable=self.date, font=("Times new roman", 15, "bold"), bd=5,
                             relief=GROOVE)
            txt_date.grid(row=1, column=1, pady=0, padx=0, sticky="w")

            lb1_vehno = Label(Manage_Frame, text="Vehicle No", bg="RosyBrown", fg="Dark Green",
                              font=("Times new roman", 15, "bold"))
            lb1_vehno.grid(row=2, column=0, pady=5, padx=10, sticky="w")

            txt_vehno = Entry(Manage_Frame, textvariable=self.vehno, font=("Times new roman", 15, "bold"), bd=5,
                              relief=GROOVE)
            txt_vehno.grid(row=2, column=1, pady=0, padx=0, sticky="w")

            lb1_vehtype = Label(Manage_Frame, text="Vehicle Model", bg="RosyBrown", fg="Dark Green",
                                font=("Times new roman", 10, "bold"))
            lb1_vehtype.grid(row=3, column=0, pady=5, padx=10, sticky="w")

            txt_vehtype = Entry(Manage_Frame, textvariable=self.vehtype, font=("Times new roman", 15, "bold"), bd=5,
                                relief=GROOVE)
            txt_vehtype.grid(row=3, column=1, pady=0, padx=0, sticky="w")

            lb1_LO = Label(Manage_Frame, text="Local/Out", bg="RosyBrown", fg="Dark Green",
                           font=("Times new roman", 15, "bold"))
            lb1_LO.grid(row=4, column=0, pady=5, padx=10, sticky="w")

            txt_LO = Entry(Manage_Frame, textvariable=self.LO, font=("Times new roman", 15, "bold"), bd=5,
                           relief=GROOVE)
            txt_LO.grid(row=4, column=1, pady=0, padx=0, sticky="w")

            lb1_opTime = Label(Manage_Frame, text="Opening Time", bg="RosyBrown", fg="Dark Green",
                               font=("Times new roman", 15, "bold"))
            lb1_opTime.grid(row=5, column=0, pady=5, padx=10, sticky="w")

            txt_opTime = Entry(Manage_Frame, textvariable=self.optime, font=("Times new roman", 15, "bold"), bd=5,
                               relief=GROOVE)
            txt_opTime.grid(row=5, column=1, pady=0, padx=0, sticky="w")

            lb1_cloTime = Label(Manage_Frame, text="Closing Time", bg="RosyBrown", fg="Dark Green",
                                font=("Times new roman", 15, "bold"))
            lb1_cloTime.grid(row=6, column=0, pady=5, padx=10, sticky="w")

            txt_cloTime = Entry(Manage_Frame, textvariable=self.clotime, font=("Times new roman", 15, "bold"), bd=5,
                                relief=GROOVE)
            txt_cloTime.grid(row=6, column=1, pady=0, padx=0, sticky="w")

            lb1_Time = Label(Manage_Frame, text="Total Time", bg="RosyBrown", fg="Dark Green",
                             font=("Times new roman", 15, "bold"))
            lb1_Time.grid(row=7, column=0, pady=5, padx=10, sticky="w")

            txt_Time = Entry(Manage_Frame, textvariable=self.ttime, font=("Times new roman", 15, "bold"), bd=5,
                             relief=GROOVE)
            txt_Time.grid(row=7, column=1, pady=0, padx=0, sticky="w")

            lb1_opkm = Label(Manage_Frame, text="opening km", bg="RosyBrown", fg="Dark Green",
                             font=("Times new roman", 15, "bold"))
            lb1_opkm.grid(row=8, column=0, pady=5, padx=10, sticky="w")

            txt_opkm = Entry(Manage_Frame, textvariable=self.opkm, font=("Times new roman", 15, "bold"), bd=5,
                             relief=GROOVE)
            txt_opkm.grid(row=8, column=1, pady=0, padx=0, sticky="w")

            lb1_clokm = Label(Manage_Frame, text="Closing km", bg="RosyBrown", fg="Dark Green",
                              font=("Times new roman", 15, "bold"))
            lb1_clokm.grid(row=9, column=0, pady=5, padx=10, sticky="w")

            txt_clokm = Entry(Manage_Frame, textvariable=self.clokm, font=("Times new roman", 15, "bold"), bd=5,
                              relief=GROOVE)
            txt_clokm.grid(row=9, column=1, pady=0, padx=0, sticky="w")

            lb1_km = Label(Manage_Frame, text="Total(distance) km", bg="RosyBrown", fg="Dark Green",
                           font=("Times new roman", 15, "bold"))
            lb1_km.grid(row=10, column=0, pady=5, padx=10, sticky="w")

            txt_km = Entry(Manage_Frame, textvariable=self.totalkm, font=("Times new roman", 15, "bold"), bd=5,
                           relief=GROOVE)
            txt_km.grid(row=10, column=1, pady=0, padx=0, sticky="w")

            lb1_night = Label(Manage_Frame, text="NT", bg="RosyBrown", fg="Dark Green",
                              font=("Times new roman", 15, "bold"))
            lb1_night.grid(row=11, column=0, pady=5, padx=10, sticky="w")

            txt_night = Entry(Manage_Frame, textvariable=self.nt, font=("Times new roman", 15, "bold"), bd=5,
                              relief=GROOVE)
            txt_night.grid(row=11, column=1, pady=0, padx=0, sticky="w")

            lb1_fuel = Label(Manage_Frame, text="Fuel advance", bg="RosyBrown", fg="Dark Green",
                             font=("Times new roman", 15, "bold"))
            lb1_fuel.grid(row=12, column=0, pady=5, padx=10, sticky="w")

            txt_fuel = Entry(Manage_Frame, textvariable=self.fuel, font=("Times new roman", 15, "bold"), bd=5,
                             relief=GROOVE)
            txt_fuel.grid(row=12, column=1, pady=0, padx=0, sticky="w")

            lb1_amt = Label(Manage_Frame, text="Total Amount", bg="RosyBrown", fg="Dark Green",
                            font=("Times new roman", 15, "bold"))
            lb1_amt.grid(row=13, column=0, pady=5, padx=10, sticky="w")

            txt_amt = Entry(Manage_Frame, textvariable=self.amt, font=("Times new roman", 15, "bold"), bd=5,
                            relief=GROOVE)
            txt_amt.grid(row=13, column=1, pady=0, padx=0, sticky="w")

            # ============================================================ButtonFrame========================================================================================#

            btn_Frame = Frame(Manage_Frame, bd=3, relief=RIDGE, bg="RosyBrown")
            btn_Frame.place(x=280, y=550, width=200)

            Addbtn = Button(btn_Frame, text="Add", width=10, command=self.add_cab)
            Addbtn.grid(row=0, column=0, padx=5, pady=5)


            import main3 as main

            def tom():
                main.main()

            Advbtn = Button(Detail_Frame, text="Advance", width=10, command=tom)
            Advbtn.grid(row=0, column=4, padx=10, pady=10)

            lb1_bill = Label(Detail_Frame, text="Bill Number", bg="RosyBrown", fg="Red",
                             font=("Times new roman", 15, "bold"))
            lb1_bill.grid(row=2, column=2, padx=10, pady=500)

            txt_bill = Entry(Detail_Frame, textvariable=self.Bill_no, font=("Times new roman", 15, "bold"), bd=5,
                             relief=GROOVE)
            txt_bill.grid(row=2, column=1, pady=500, padx=5, sticky="w")

            Resbtn = Button(Detail_Frame, text="Reset", command=self.reset)
            Resbtn.grid(row=2, column=4, pady=500, padx=5)

            Delbtn = Button(Detail_Frame, text="Delete", width=10, command=self.del_cab)
            Delbtn.grid(row=2, column=3, padx=5, pady=500)

            # =============================================TableFrame====================================================================#

            Table_Frame = Frame(Detail_Frame, bd=4, relief=RIDGE, bg="RosyBrown")
            Table_Frame.place(x=10, y=70, width=750, height=470)

            scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
            scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)
            self.Tours_table = ttk.Treeview(Table_Frame, columns=(
                "Date", "Veh_No", "Veh_type", "LO", "Op_time", "clo_time", "Total_time", "op_km", "clo_km", "Total_km",
                "NT", "Fuel_Adv", "Total_amt","Bill_no")
                                            , xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
            scroll_x.pack(side=BOTTOM, fill=X)
            scroll_y.pack(side=RIGHT, fill=Y)
            scroll_x.config(command=self.Tours_table.xview)
            scroll_y.config(command=self.Tours_table.yview)
            self.Tours_table.heading("Date", text="Date")
            self.Tours_table.heading("Veh_No", text="Veh_no")
            self.Tours_table.heading("Veh_type", text="Veh_type")
            self.Tours_table.heading("LO", text="Local/Out")
            self.Tours_table.heading("Op_time", text="Op_time")
            self.Tours_table.heading("clo_time", text="clo_time")
            self.Tours_table.heading("Total_time", text="Total_time")
            self.Tours_table.heading("op_km", text="op_km")
            self.Tours_table.heading("clo_km", text="clo_km")
            self.Tours_table.heading("Total_km", text="Total_km")
            self.Tours_table.heading("NT", text="NT")
            self.Tours_table.heading("Fuel_Adv", text="Fuel_advance")
            self.Tours_table.heading("Total_amt", text="Total_amount")
            self.Tours_table.heading("Bill_no", text="Bill_Number")

            self.Tours_table['show'] = 'headings'
            self.Tours_table.column("Date", width=100)
            self.Tours_table.column("Veh_No", width=100)
            self.Tours_table.column("Veh_type", width=100)
            self.Tours_table.column("LO", width=100)
            self.Tours_table.column("Op_time", width=100)
            self.Tours_table.column("clo_time", width=100)
            self.Tours_table.column("Total_time", width=100)
            self.Tours_table.column("op_km", width=100)
            self.Tours_table.column("clo_km", width=100)
            self.Tours_table.column("Total_km", width=100)
            self.Tours_table.column("NT", width=100)
            self.Tours_table.column("Fuel_Adv", width=100)
            self.Tours_table.column("Total_amt", width=100)
            self.Tours_table.column("Bill_no", width=100)
            self.Tours_table.pack(fill=BOTH, expand=1)
            self.Tours_table.bind("<ButtonRelease-1>", self.get_cursor)

        def add_cab(self):
            cn = pyodbc.connect('Driver={SQL Server};'
                                'Server=CHIKU;'
                                'Database=tours;'
                                'Trusted_Connection=yes;')
            cursor = cn.cursor()
            cursor.execute("INSERT INTO projdset1 (Date,Veh_No,Veh_type,LO,Op_time,clo_time,Total_time,"
                           "op_km,clo_km,Total_km,NT,Fuel_Adv,Total_amt,Bill_no)"
                           "values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(
                            self.date.get(), self.vehno.get(), self.vehtype.get(), self.LO.get(),
                            self.optime.get(), self.clotime.get(),
                            self.ttime.get(), self.opkm.get(), self.clokm.get(), self.totalkm.get(),
                            self.nt.get(), self.fuel.get(), self.amt.get(), self.Bill_no.get()))
            cn.commit()
            self.fetch()
            cn.close()
            self.clear()

        def fetch(self):
            cn = pyodbc.connect('Driver={SQL Server};'
                                'Server=CHIKU;'
                                'Database=tours;'
                                'Trusted_Connection=yes;')
            cursor = cn.cursor()
            self.reset()
            cursor.execute("select * from projdset1")
            rows = cursor.fetchall()
            if len(rows) != 0:
                for row in rows:
                    self.Tours_table.insert('', END, values=row)
                cn.commit()
            cn.close()

        def del_cab(self):
            cn = pyodbc.connect('Driver={SQL Server};'
                                'Server=CHIKU;'
                                'Database=tours;'
                                'Trusted_Connection=yes;')
            cursor = cn.cursor()
            if not self.Tours_table.selection():
                print("ERROR")
            else:
                result = messagebox.askquestion('InvY', 'Are you sure you want to delete this record?',icon="warning")
                if result == 'yes':
                    curItem = self.Tours_table.focus()
                    contents = (self.Tours_table.item(curItem))
                    selecteditem = contents['values']
                    self.Tours_table.delete(curItem)
                    cursor.execute("delete from data1 where Bill_no='" + self.Bill_no.get() + "'")
                    cursor.close()
            cn.commit()
            cn.close()
            messagebox.showinfo("Data entry from", "Record succesfully Deleted ")

        def get_cursor(self, s):
            cur_row = self.Tours_table.focus()
            content = self.Tours_table.item(cur_row)
            row = content['values']
            self.date.set(row[0])
            self.vehno.set(row[1])
            self.vehtype.set(row[2])
            self.LO.set(row[3])
            self.optime.set(row[4])
            self.clotime.set(row[5])
            self.ttime.set(row[6])
            self.opkm.set(row[7])
            self.clokm.set(row[8])
            self.totalkm.set(row[9])
            self.nt.set(row[10])
            self.fuel.set(row[11])
            self.amt.set(row[12])
            self.Bill_no.set(row[13])

        def search(self):
            cn = pyodbc.connect('Driver={SQL Server};'
                                'Server=CHIKU;'
                                'Database=tours;'
                                'Trusted_Connection=yes;')
            cursor = cn.cursor()
            self.reset()
            cursor.execute(
                "select * from projdset1 where {} = '{}';".format(str(self.search_by.get()), str(self.search_txt.get())))
            rows = cursor.fetchall()
            if len(rows) != 0:
                for row in rows:
                    self.Tours_table.insert('', END, values=row)
                cn.commit()
            cn.close()
            if rows is None:
                messagebox.showinfo("Data entry from", "No Such Record found")

        def clear(self):
            self.date.set('')
            self.vehno.set('')
            self.vehtype.set('')
            self.LO.set('')
            self.optime.set('')
            self.clotime.set('')
            self.ttime.set('')
            self.opkm.set('')
            self.clokm.set('')
            self.totalkm.set('')
            self.nt.set('')
            self.fuel.set('')
            self.amt.set('')
            self.Bill_no.set('')

        def reset(self):
            self.Tours_table.delete(*self.Tours_table.get_children())
            self.clear()


    root = Tk()
    ob = Tours(root)
    root.mainloop()
