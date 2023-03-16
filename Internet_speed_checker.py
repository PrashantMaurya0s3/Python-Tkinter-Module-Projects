from tkinter import *

import speedtest


def speedcheck():
    st = speedtest.Speedtest()
    # st.get_server()
    st.get_servers()
    down = str(round(st.download() / (10 ** 6), 3)) + "Mbps"
    up = str(round(st.upload() / (10 ** 6), 3)) + "Mbps"
    lab_down.config(text=down)
    lab_up.config(text=up)


sp = Tk()
sp.title(" Internet Speed Test ")
sp.geometry("500x600")
sp.config(bg="Black")

lab = Label(sp, text="Internet Speed Test", font=("Time New Roman", 30, "bold"), bg="Black", fg="Red")
lab.place(x=60, y=40, height=50, width=380)

lab = Label(sp, text="Download Speed", font=("Time New Roman", 30, "bold"))
lab.place(x=60, y=130, height=50, width=380)

lab_down = Label(sp, text="00", font=("Time New Roman", 30, "bold"))
lab_down.place(x=60, y=200, height=50, width=380)

lab = Label(sp, text="Upload speed", font=("Time New Roman", 30, "bold"))
lab.place(x=60, y=290, height=50, width=380)

lab_up = Label(sp, text="00", font=("Time New Roman", 30, "bold"))
lab_up.place(x=60, y=360, height=50, width=380)

button = Button(sp, text="CHECK SPEED", font=("Time New Roman", 30, "bold"), bg="red", fg="black", relief=RAISED,
                command=speedcheck)
button.place(x=60, y=460, height=50, width=380)

sp.mainloop()
