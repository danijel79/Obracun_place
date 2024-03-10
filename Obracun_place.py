import tkinter as tk

root = tk.Tk()
root.title('Obracun place')
root.geometry('700x700')
root.configure(bg='DarkSeaGreen1')

label_username = tk.Label(root, text='Prijava', font='Times 20', bg='DarkSeaGreen1')
label_username.pack(ipady=70)

userName_label = tk.Label(root, text='userName', font='Times 14', bg='DarkSeaGreen1')
userName_label.pack()
userName = tk.Entry(root, width=20)
userName.pack(pady=2)


root.mainloop()
