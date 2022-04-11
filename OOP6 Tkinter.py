import tkinter

window = tkinter.Tk()

label = tkinter.Label(window, text='label1')
label2 = tkinter.Label(window, text="label2")

tombol = tkinter.Button(window, text='tombol1')
tombol2 = tkinter.Button(window, text='tombol2')

# methode positioning
label.pack()
label2.pack()

tombol.pack()
tombol2.pack()

# methode menampilkan GUI
window.mainloop()