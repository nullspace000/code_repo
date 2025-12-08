import tkinter as tk
#main window
root = tk.Tk()
root.geometry("1920x1080")
root.title("Gestor de Entretenimiento")
#modules
label = tk.Label(root, text="hello world")
label.pack()


myentry = tk.Entry(root, font=('Arial',18))
myentry.pack()


btn1 = tk.Button(root, text="1", font=('Arial', 18))
btn1.place(x=200, y=200, height=100, width=100)

#myentry = tk.Entry(root)
#myentry.pack()

#button = tk.Button(root, text="click me", font=('Arial',18))
#button.pack()

#textbox = tk.Text(root, height = 3, font=('Arial',16))
#textbox.pack(padx=10)

#mainloop
root.mainloop()
