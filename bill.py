from tkinter import*
import math,random,os
from tkinter import messagebox
import pymysql

class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1250x800+0+0")
        self.root.title("Billing Software")
        
        bg_color="#2C041D"
        self.root.configure(bg = bg_color)
        title=Label(self.root,text="Billing Software",bd=12,relief=GROOVE,bg=bg_color,fg="white", font=("times new roman",30,"bold"), pady=2).pack(fill=X)
        ##########variable
        ##########cosmetics
        self.soap=IntVar()
        self.face_cream=IntVar()
        self.face_wash= IntVar()
        self.hair_spray=IntVar()
        self.hair_gel=IntVar()
        self.lotion=IntVar()
        #######grocery vaiable
        self.rice=IntVar()
        self.food_oil=IntVar()
        self.daal=IntVar()
        self.wheat=IntVar()
        self.sugar=IntVar()
        self.tea=IntVar()
        ########cold drinks variable
        self.mazza=IntVar()
        self.coke=IntVar()
        self.frooti=IntVar()
        self.thumbs_up=IntVar()
        self.limca=IntVar()
        self.sprite=IntVar()
        ########total product price and tax variable
        self.total_cosmetic_price=StringVar()
        self.total_grocery_price=StringVar()
        self.total_cold_drink_price=StringVar()
        self.total_cosmetic_tax=StringVar()
        self.total_grocery_tax=StringVar()
        self.total_cold_drink_tax=StringVar()
        ############customer detail variable
        self.c_name=StringVar()
        self.p_no= StringVar()
        self.b_no=StringVar()
        x=random.randint(1000,9999)
        self.b_no.set(str(x))
        self.search_bill=StringVar()
        ##########
        self.end_bill=StringVar()
        ##customer detail frame
        F1=LabelFrame(self.root,text="Customer Details",bd=12,relief=GROOVE,font=("times new roman",15 ,"bold"),fg="pink",bg=bg_color)
        F1.place(x=0,y=80,relwidth=1)
        #########customer name
        cname_lbl=Label(F1,text="Customer Name",fg="white",bg=bg_color,font=("times new roman",18,"bold")).grid(row=0,column=0,padx=40,pady=10)
        cname_txt=Entry(F1,textvariable=self.c_name,width=15,bd=7,relief=SUNKEN,font="arial 15").grid(row=0,column=1,padx=5,pady=10)
        #########phone no
        cphone_lbl=Label(F1,text="Phone No.",fg="white",bg=bg_color,font=("times new roman",18,"bold")).grid(row=0,column=2,padx=20,pady=10)
        cphone_txt=Entry(F1,textvariable=self.p_no,width=15,bd=7,relief=SUNKEN,font="arial 15").grid(row=0,column=3,padx=5,pady=10)

        #########bill no
        cbill_lbl=Label(F1,text="Bill No.",fg="white",bg=bg_color,font=("times new roman",18,"bold")).grid(row=0,column=4,padx=20,pady=10)
        cbill_txt=Entry(F1,textvariable=self.b_no,width=15,bd=7,relief=SUNKEN,font="arial 15").grid(row=0,column=5,padx=5,pady=10)
        #########seach button
        btn=Button(F1,text="Search",width=10,command=self.find_bill,bd=7,font="arial 12 bold").grid(row=0,column=6,padx=70,pady=10)
        ############cosmetic frame
        F2=LabelFrame(self.root,text="Cosmetics",bd=12,relief=GROOVE,font=("times new roman",15 ,"bold"),fg="pink",bg=bg_color)
        F2.place(x=5,y=180,width=315,height=380)
        ##########soap label
        bsoap_lbl=Label(F2, text="Bath Soap", font=("times new roman",18,"bold"),fg="white",bg=bg_color).grid(row=0,column=0,padx=10,pady=5,sticky="w")
        bsoap_txt=Entry(F2,textvariable=self.soap,font="arial 15 bold",bd=7,relief=SUNKEN,width=10).grid(row=0,column=1,padx=10,pady=5)
        ######Face cream
        fcream_lbl=Label(F2, text="Face Cream", font=("times new roman",18,"bold"),fg="white",bg=bg_color).grid(row=1,column=0,padx=10,pady=5,sticky="w")
        fcream_txt=Entry(F2,textvariable=self.face_cream,font="arial 15 bold",bd=7,relief=SUNKEN,width=10).grid(row=1,column=1,padx=10,pady=5)
        #######Face Wash
        fwash_lbl=Label(F2, text="Face Wash", font=("times new roman",18,"bold"),fg="white",bg=bg_color).grid(row=2,column=0,padx=10,pady=5,sticky="w")
        fwash_txt=Entry(F2,textvariable=self.face_wash,font="arial 15 bold",bd=7,relief=SUNKEN,width=10).grid(row=2,column=1,padx=10,pady=5)
        #######Hair Spray
        hairsp_lbl=Label(F2, text="Hair Spray", font=("times new roman",18,"bold"),fg="white",bg=bg_color).grid(row=3,column=0,padx=10,pady=5,sticky="w")
        hairsp_txt=Entry(F2,textvariable=self.hair_spray,font="arial 15 bold",bd=7,relief=SUNKEN,width=10).grid(row=3,column=1,padx=10,pady=5)
        ######Hair gel
        gelhair_lbl=Label(F2, text="Hair Gel", font=("times new roman",18,"bold"),fg="white",bg=bg_color).grid(row=4,column=0,padx=10,pady=5,sticky="w")
        gelhair_txt=Entry(F2,textvariable=self.hair_gel,font="arial 15 bold",bd=7,relief=SUNKEN,width=10).grid(row=4,column=1,padx=10,pady=5)
        ######Body Lotion
        blotion_lbl=Label(F2, text="Body Lotion", font=("times new roman",18,"bold"),fg="white",bg=bg_color).grid(row=5,column=0,padx=10,pady=5,sticky="w")
        blotion_txt=Entry(F2,textvariable=self.lotion,font="arial 15 bold",bd=7,relief=SUNKEN,width=10).grid(row=5,column=1,padx=10,pady=5)
        ############GROCERY
        F3=LabelFrame(self.root,text="Grocery",bd=12,relief=GROOVE,font=("times new roman",15 ,"bold"),fg="pink",bg=bg_color)
        F3.place(x=320,y=180,width=315,height=380)
        ##########rice
        rice_lbl=Label(F3, text="Rice", font=("times new roman",18,"bold"),fg="white",bg=bg_color).grid(row=0,column=0,padx=10,pady=5,sticky="w")
        rice_txt=Entry(F3,textvariable=self.rice,font="arial 15 bold",bd=7,relief=SUNKEN,width=10).grid(row=0,column=1,padx=10,pady=5)
        ######food oil
        foil_lbl=Label(F3, text="Food Oil", font=("times new roman",18,"bold"),fg="white",bg=bg_color).grid(row=1,column=0,padx=10,pady=5,sticky="w")
        foil_txt=Entry(F3,textvariable=self.food_oil,font="arial 15 bold",bd=7,relief=SUNKEN,width=10).grid(row=1,column=1,padx=10,pady=5)
        #######dal
        daal_lbl=Label(F3, text="Dal", font=("times new roman",18,"bold"),fg="white",bg=bg_color).grid(row=2,column=0,padx=10,pady=5,sticky="w")
        daal_txt=Entry(F3,textvariable=self.daal,font="arial 15 bold",bd=7,relief=SUNKEN,width=10).grid(row=2,column=1,padx=10,pady=5)
        #######wheat
        wheat_lbl=Label(F3, text="Wheat flour", font=("times new roman",18,"bold"),fg="white",bg=bg_color).grid(row=3,column=0,padx=10,pady=5,sticky="w")
        wheat_txt=Entry(F3,textvariable=self.wheat,font="arial 15 bold",bd=7,relief=SUNKEN,width=10).grid(row=3,column=1,padx=10,pady=5)
        ######sugar
        sugar_lbl=Label(F3, text="Sugar", font=("times new roman",18,"bold"),fg="white",bg=bg_color).grid(row=4,column=0,padx=10,pady=5,sticky="w")
        sugar_txt=Entry(F3,textvariable=self.sugar,font="arial 15 bold",bd=7,relief=SUNKEN,width=10).grid(row=4,column=1,padx=10,pady=5)
        ######tea
        tea_lbl=Label(F3, text="Tea", font=("times new roman",18,"bold"),fg="white",bg=bg_color).grid(row=5,column=0,padx=10,pady=5,sticky="w")
        tea_txt=Entry(F3,textvariable=self.tea,font="arial 15 bold",bd=7,relief=SUNKEN,width=10).grid(row=5,column=1,padx=10,pady=5)
        ############cold drinks
        F4=LabelFrame(self.root,text="Cold Drinks",bd=12,relief=GROOVE,font=("times new roman",15 ,"bold"),fg="pink",bg=bg_color)
        F4.place(x=635,y=180,width=315,height=380)
        ##########maza
        mazza_lbl=Label(F4, text="Mazza", font=("times new roman",18,"bold"),fg="white",bg=bg_color).grid(row=0,column=0,padx=10,pady=5,sticky="w")
        mazza_txt=Entry(F4,textvariable=self.mazza,font="arial 15 bold",bd=7,relief=SUNKEN,width=10).grid(row=0,column=1,padx=10,pady=5)
        ######cock
        coke_lbl=Label(F4, text="Coca Cola", font=("times new roman",18,"bold"),fg="white",bg=bg_color).grid(row=1,column=0,padx=10,pady=5,sticky="w")
        coke_txt=Entry(F4,textvariable=self.coke,font="arial 15 bold",bd=7,relief=SUNKEN,width=10).grid(row=1,column=1,padx=10,pady=5)
        #######frooti
        frooti_lbl=Label(F4, text="Frooti", font=("times new roman",18,"bold"),fg="white",bg=bg_color).grid(row=2,column=0,padx=10,pady=5,sticky="w")
        frooti_txt=Entry(F4,textvariable=self.frooti,font="arial 15 bold",bd=7,relief=SUNKEN,width=10).grid(row=2,column=1,padx=10,pady=5)
        #######thumbs up
        thumbsup_lbl=Label(F4, text="Thumbs Up", font=("times new roman",18,"bold"),fg="white",bg=bg_color).grid(row=3,column=0,padx=10,pady=5,sticky="w")
        thumbsup_txt=Entry(F4,textvariable=self.thumbs_up,font="arial 15 bold",bd=7,relief=SUNKEN,width=10).grid(row=3,column=1,padx=10,pady=5)
        ######limca
        limca_lbl=Label(F4, text="Limca", font=("times new roman",18,"bold"),fg="white",bg=bg_color).grid(row=4,column=0,padx=10,pady=5,sticky="w")
        limca_txt=Entry(F4,textvariable=self.limca,font="arial 15 bold",bd=7,relief=SUNKEN,width=10).grid(row=4,column=1,padx=10,pady=5)
        ######sprite
        sprite_lbl=Label(F4, text="Sprite", font=("times new roman",18,"bold"),fg="white",bg=bg_color).grid(row=5,column=0,padx=10,pady=5,sticky="w")
        sprite_txt=Entry(F4,textvariable=self.sprite,font="arial 15 bold",bd=7,relief=SUNKEN,width=10).grid(row=5,column=1,padx=10,pady=5)
        ######Bill Area
        F5=LabelFrame(self.root,bd=10,relief=GROOVE)
        F5.place(x=960,y=185,width=400,height=380)
        bill_title=Label(F5,text="Bill Area", font="arial 15 bold",bd=7,relief=GROOVE,fg="navy blue").pack(fill=X)
        scrol_y=Scrollbar(F5,orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)
        ###########button frame
        F6=LabelFrame(self.root,text="Bill Menu",bd=12,relief=GROOVE,font=("times new roman",15 ,"bold"),fg="pink",bg=bg_color)
        F6.place(x=5,y=560,relwidth=1,height=140)
        #########Total prices
        #########total cosmetics price
        m1=Label(F6,text="Total Cosmetic Price",font=("times new roman",14, "bold"),bg=bg_color,fg="white").grid(row=0,column=0,padx=20,pady=1,sticky="w")
        m1_txt=Entry(F6,text="arial 10 bold",width=18,textvariable=self.total_cosmetic_price, bd=7,relief=SUNKEN).grid(row=0, column=1, padx=10, pady=1)
        #########total grocery price
        m2=Label(F6,text="Total Grocery Price",font=("times new roman",14, "bold"),bg=bg_color,fg="white").grid(row=1,column=0,padx=20,pady=1,sticky="w")
        m2_txt=Entry(F6,text="arial 10 bold",width=18,textvariable=self.total_grocery_price, bd=7,relief=SUNKEN).grid(row=1, column=1, padx=10, pady=1)
        #########total cold drinks price
        m3=Label(F6,text="Total Cold Drinks Price",font=("times new roman",14, "bold"),bg=bg_color,fg="white").grid(row=2,column=0,padx=20,pady=1,sticky="w")
        m3_txt=Entry(F6,text="arial 10 bold",width=18,textvariable=self.total_cold_drink_price, bd=7,relief=SUNKEN).grid(row=2, column=1, padx=10, pady=1)
        #######total tax prices
        #######total cosmetics tax
        t1=Label(F6,text="Total Cosmetic IGST",font=("times new roman",14, "bold"),bg=bg_color,fg="white").grid(row=0,column=2,padx=20,pady=1,sticky="w")
        t1_txt=Entry(F6,text="arial 10 bold",width=18,textvariable=self.total_cosmetic_tax, bd=7,relief=SUNKEN).grid(row=0, column=3, padx=10, pady=1)
        #########total grocery tax
        t2=Label(F6,text="Total Grocery IGST",font=("times new roman",14, "bold"),bg=bg_color,fg="white").grid(row=1,column=2,padx=20,pady=1,sticky="w")
        t2_txt=Entry(F6,text="arial 10 bold",width=18,textvariable=self.total_grocery_tax, bd=7,relief=SUNKEN).grid(row=1, column=3, padx=10, pady=1)
        #########total cold drinks tax
        t3=Label(F6,text="Total Cold Drinks IGST",font=("times new roman",14, "bold"),bg=bg_color,fg="white").grid(row=2,column=2,padx=20,pady=1,sticky="w")
        t3_txt=Entry(F6,text="arial 10 bold",width=18,textvariable=self.total_cold_drink_tax, bd=7,relief=SUNKEN).grid(row=2, column=3, padx=10, pady=1)
        ####frame for button
        btn_F=LabelFrame(F6,bd=7,relief=GROOVE)
        btn_F.place(x=800,width=500, height=100)
        total_btn=Button(btn_F,text="Total",bd=1,bg="#3E3D53",fg="white",width=10,font="arial 12 bold",pady=15,command=self.total).grid(row=0,column=0,padx=5,pady=15)
        Genrate_btn=Button(btn_F,text="Generate Bill",bd=1,bg="#3E3D53",fg="white",width=10,font="arial 12 bold",command=self.bill_area,pady=15).grid(row=0,column=1,padx=5,pady=15)
        Clear_btn=Button(btn_F,text="Clear",bd=1,bg="#3E3D53",fg="white",width=10,font="arial 12 bold",command=self.clear_win,pady=15).grid(row=0,column=2,padx=5,pady=15)
        Exit_btn=Button(btn_F,text="Exit",bd=1,bg="#3E3D53",fg="white",width=10,font="arial 12 bold",command=self.Exit_app,pady=15).grid(row=0,column=3,padx=5,pady=15)
        self.welcome_bill()
    def total(self):
        ######cosmetics price evaluate
        self.c_s_p=self.soap.get()*30
        self.c_fc_p=self.face_cream.get()*40
        self.c_fw_p=self.face_wash.get()*50
        self.c_hs_p=self.hair_spray.get()*60
        self.c_hg_p=self.hair_gel.get()*70
        self.c_l_p=self.lotion.get()*80
        self.co=float(self.c_s_p+self.c_fc_p+self.c_fw_p+self.c_hs_p+self.c_hg_p+self.c_l_p)
        self.total_cosmetic_price.set("Rs. "+str(self.co))
        #########cosmetic tax
        self.t_c_t=self.co*0.09
        self.total_cosmetic_tax.set("Rs. "+str(self.t_c_t))
        ######grocery price evaluate
        self.g_r_p=self.rice.get()*35
        self.g_fo_p=self.food_oil.get()*90
        self.g_d_p=self.daal.get()*40
        self.g_w_p=self.wheat.get()*50
        self.g_s_p=self.sugar.get()*40
        self.g_t_p=self.tea.get()*60
        self.gr=float(self.g_r_p+self.g_fo_p+self.g_d_p+self.g_w_p+self.g_s_p+self.g_t_p)
        self.total_grocery_price.set("Rs. "+str(self.gr))
        #########grocery tax
        self.t_g_t=self.gr*0.025
        self.total_grocery_tax.set("Rs. "+str(self.t_g_t))
        ######cold drinks price evaluate
        self.cd_m_p=self.mazza.get()*90
        self.cd_c_p=self.coke.get()*50
        self.cd_f_p=self.frooti.get()*70
        self.cd_tu_p=self.thumbs_up.get()*60
        self.cd_l_p=self.limca.get()*40
        self.cd_s_p=self.sprite.get()*30
        self.cd=float(self.cd_m_p+self.cd_c_p+self.cd_f_p+self.cd_tu_p+self.cd_l_p+self.cd_s_p)
        self.total_cold_drink_price.set("Rs. "+str(self.cd))
        #########cold drinks tax
        self.t_cd_t=self.cd*0.06
        self.total_cold_drink_tax.set("Rs. "+str(self.t_cd_t))
        
        self.end_bill=float(self.co+self.gr+self.cd+self.t_c_t+self.t_g_t+self.t_cd_t)

        ##########Datatbase
        def addData():
            sqlCon = pymysql.connect(host="localhost", user="root", password="me", database="billingdb") 
            cur = sqlCon.cursor()
            cur.execute  
      
    def welcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\t   Welcome Webcode Retail")
        self.txtarea.insert(END,f"\n Bill Number:{self.b_no.get()}")
        self.txtarea.insert(END,f"\n Customer name:{self.c_name.get()}")
        self.txtarea.insert(END,f"\n Phone number:{self.p_no.get()}")
        self.txtarea.insert(END,f"\n============================================")
        self.txtarea.insert(END,f"\nProduct   Quantity   Price(pu)  Price(total)")
        self.txtarea.insert(END,f"\n============================================")
    def bill_area(self):
        if self.c_name.get()=="" or self.p_no.get()=="" :
            messagebox.showerror("Error","customer details are must")
        elif len(self.p_no.get()) > 10 :
            messagebox.showerror("Error","Enter a valid number")
        elif self.total_cosmetic_price.get()=="Rs. 0.0" and self.total_grocery_price.get()=="Rs. 0.0" and self.total_cold_drink_price.get()=="Rs. 0.0":
            messagebox.showerror("Error","No product purchased")
        else:
            self.welcome_bill()
            ##########cosmetic
            if self.soap.get()!=0:
                self.txtarea.insert(END,f"\n Bath Soap\t\t{self.soap.get()}\t {self.c_s_p}")
            if self.face_cream.get()!=0:
                self.txtarea.insert(END,f"\n Face Cream\t\t{self.face_cream.get()}\t {self.c_fc_p}")
            if self.face_wash.get()!=0:
                self.txtarea.insert(END,f"\n Face Wash\t\t{self.face_wash.get()}\t {self.c_fw_p}")
            if self.hair_spray.get()!=0:
                self.txtarea.insert(END,f"\n Hair Spray\t\t{self.hair_spray.get()}\t {self.c_hs_p}")
            if self.hair_gel.get()!=0:
                self.txtarea.insert(END,f"\n Hair Gel\t\t{self.hair_gel.get()}\t {self.c_hg_p}")
            if self.lotion.get()!=0:
                self.txtarea.insert(END,f"\n Body Lotion\t\t{self.lotion.get()}\t {self.c_l_p}")
            ##########grocery
            if self.rice.get()!=0:
                self.txtarea.insert(END,f"\n Rice\t\t{self.rice.get()}\t {self.g_r_p}")
            if self.food_oil.get()!=0:
                self.txtarea.insert(END,f"\n Food Oil\t\t{self.food_oil.get()}\t {self.g_fo_p}")
            if self.daal.get()!=0:
                self.txtarea.insert(END,f"\n Daal\t\t{self.daal.get()}\t {self.g_d_p}")
            if self.wheat.get()!=0:
                self.txtarea.insert(END,f"\n Wheat\t\t{self.wheat.get()}\t {self.g_w_p}")
            if self.sugar.get()!=0:
                self.txtarea.insert(END,f"\n Sugar\t\t{self.sugar.get()}\t {self.g_s_p}")
            if self.tea.get()!=0:
                self.txtarea.insert(END,f"\n Tea\t\t{self.tea.get()}\t {self.g_t_p}")
            ##########cold drinks
            if self.mazza.get()!=0:
                self.txtarea.insert(END,f"\n Mazza\t\t{self.mazza.get()}\t 70 \t {self.cd_m_p}")
            if self.coke.get()!=0:
                self.txtarea.insert(END,f"\n Coke\t\t{self.coke.get()}\t {self.cd_c_p}")
            if self.frooti.get()!=0:
                self.txtarea.insert(END,f"\n Frooti\t\t{self.frooti.get()}\t {self.cd_f_p}")
            if self.thumbs_up.get()!=0:
                self.txtarea.insert(END,f"\n Thumbs Up\t\t{self.thumbs_up.get()}\t {self.cd_tu_p}")
            if self.limca.get()!=0:
                self.txtarea.insert(END,f"\n Limca\t\t{self.limca.get()}\t {self.cd_l_p}")
            if self.sprite.get()!=0:
                self.txtarea.insert(END,f"\n Sprite\t\t{self.sprite.get()}\t {self.cd_s_p}")
            ########tax on text window
            self.txtarea.insert(END,f"\n--------------------------------------------")
            if self.total_cosmetic_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END,f"\nCosmatics IGST\t\t\t{self.total_cosmetic_tax.get()}")
            if self.total_grocery_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END,f"\nGrocery IGST\t\t\t{self.total_grocery_tax.get()}")
            if self.total_cold_drink_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END,f"\nCold Drinks IGST\t\t\t{self.total_cold_drink_tax.get()}")
            self.txtarea.insert(END,f"\n--------------------------------------------")
            #############end bill
            self.txtarea.insert(END,f"\nTotal money\t\t Rs. {str(self.end_bill)}")
            self.save_bill()
    def save_bill(self):
        op=messagebox.askyesno("Save Bill", "Do you want to save Bill?")
        if op>0:
            self.bill_data=self.txtarea.get('1.0',END)
            f1=open("bills/"+str(self.b_no.get())+".text","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved",f"Bill no. :{self.b_no.get()} saved Sucessfully")
        else:
            return
    
    def find_bill(self):
        present="no"
        for i in os.listdir("bills/"):
            if i.split('.')[0]==self.b_no.get():
                f1=open(f"bills/{i}","r")
                self.txtarea.delete('1.0',END)
                for d in f1:
                    self.txtarea.insert(END,d)
                f1.close()
                present="yes"
        if present=="no":
            messagebox.showerror("Error","Invalid Bill No.")
    def clear_win(self):
        op=messagebox.askyesno("Clear","Do you Really want to Clear data")
        if op>0:
            self.soap.set(0)
            self.face_cream.set(0)
            self.face_wash.set(0)
            self.hair_spray.set(0)
            self.hair_gel.set(0)
            self.lotion.set(0)
            #######grocery vaiable
            self.rice.set(0)
            self.food_oil.set(0)
            self.daal.set(0)
            self.wheat.set(0)
            self.sugar.set(0)
            self.tea.set(0)
            ########cold drinks variable
            self.mazza.set(0)
            self.coke.set(0)
            self.frooti.set(0)
            self.thumbs_up.set(0)
            self.limca.set(0)
            self.sprite.set(0)
            ########total product price and tax variable
            self.total_cosmetic_price.set(0)
            self.total_grocery_price.set(0)
            self.total_cold_drink_price.set(0)
            self.total_cosmetic_tax.set(0)
            self.total_grocery_tax.set(0)
            self.total_cold_drink_tax.set(0)
            ############customer detail variable
            self.c_name.set("")
            self.p_no.set("")
            self.b_no.set("")
            x=random.randint(1000,9999)
            self.b_no.set(str(x))
            self.search_bill.set("")
            self.welcome_bill()
    def Exit_app(self):
        op=messagebox.askyesno("Do you Really want to exit")
        if op>0:
            self.root.destroy()

root=Tk()
obj=Bill_App(root)
root.mainloop()
