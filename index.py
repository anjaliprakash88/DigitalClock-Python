from tkinter import *
import time
clk = Tk()
clk.title("clock")
clk.geometry("1350x700+0+0")
clk.config(bg="Grey")

def clock():
    hr = str(time.strftime("%H"))  # %H for hour (00-23)
    mn = str(time.strftime("%M"))  # %M for minute (00-59)
    sc = str(time.strftime("%S"))  # %S for second (00-59)
    # print(hr, mn, sc)
    if int(hr) > 12 and int(mn)>0:
        lb_dm.config(text="PM")
    if int(hr) > 12:
        hr = str(int(int(hr)-12))    
    
    lb_hr.config(text=hr)
    lb_mn.config(text=mn)
    lb_sec.config(text=sc)

    lb_hr.after(200, clock)




lb_hr = Label(clk, text = "12", font=("Times 20 bold", 75, "bold"), bg= "white", fg="black")
lb_hr.place(x=350, y=200, width=150, height=150)

lb_hr_txt = Label(clk, text="HOUR", font=("Times 20 bold", 20, "bold"), bg="black", fg="white")
lb_hr_txt.place(x=350, y=360, width=150, height=50)


lb_mn = Label(clk, text = "12", font=("Times 20 bold", 75, "bold"), bg= "white", fg="black")
lb_mn.place(x=520, y=200, width=150, height=150)

lb_mn_txt = Label(clk, text="MINUTES", font=("Times 20 bold", 20, "bold"), bg="black", fg="white")
lb_mn_txt.place(x=520, y=360, width=150, height=50)


lb_sec = Label(clk, text = "12", font=("Times 20 bold", 75, "bold"), bg= "white", fg="black")
lb_sec.place(x=690, y=200, width=150, height=150)

lb_sec_txt = Label(clk, text="SECONDS", font=("Times 20 bold", 20, "bold"), bg="black", fg="white")
lb_sec_txt.place(x=690, y=360, width=150, height=50)


lb_dm = Label(clk, text = "AM", font=("Times 20 bold", 70, "bold"), bg= "white", fg="black")
lb_dm.place(x=860, y=200, width=150, height=150)

lb_dm_txt = Label(clk, text="NOON", font=("Times 20 bold", 20, "bold"), bg="black", fg="white")
lb_dm_txt.place(x=860, y=360, width=150, height=50)

clock()

clk.mainloop()
