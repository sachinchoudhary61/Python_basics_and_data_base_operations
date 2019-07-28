import tkinter as t
import time

root=t.Tk()
root.title('Countdown Clock')
root.configure(bg="RoyalBlue3")
root.geometry('500x300')
root.resizable(0, 0)

no_of_sec = t.Label(root, text="NO OF SECOND :", font="Century 15 bold", fg="black",bg="RoyalBlue3")
no_of_sec.grid(row=1, column=0)

no_of_sec_entry = t.Entry(root, width=40, bd=3)
no_of_sec_entry.grid(row=2, column=0, padx=100, pady=1)

#---------------------countdoun fun-----------------------------
def main():
    nsec = int(no_of_sec_entry.get())
    # range from nsec to zero backwards
    for x in range(nsec, -1, -1):
        time.sleep(1)
        print(formatTime(x))

def formatTime(x):
    minutes, seconds_rem = divmod(x, 60)
    # use string formatting with C type % specifiers
    # %02d means integer field of 2 left padded with zero if needed
    return "%02d:%02d" % (minutes, seconds_rem)

#-----------------------end-
#-------------labelconfig fun------------
# -----------and time string----

def fun():
    #time_string = main()
    time_string = time.strftime("%H:%M:%S")
    textprintlabel.config( text=time_string)
    textprintlabel.after(200, fun)

textprintlabel = t.Label(root, font="Century 12 bold", fg="black",text="Count Down start here")
textprintlabel.grid(row=4, column=0,padx=50,pady=50)

start_button = t.Button(root, text=" START ", bg="black", fg="white", bd=2, command=fun, font="Century 10 bold")
start_button.grid(row=3,column=0)

def destroy():
    root.destroy()

destroy_button =  t.Button(root, text=" EXIT ", bg="black", fg="white", bd=2, command=destroy, font="Century 10 bold")
destroy_button.place(x=190,y=270)

root.mainloop()
