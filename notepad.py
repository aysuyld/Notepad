from tkinter import *
from tkinter.filedialog import asksaveasfilename #kaydetme seçeneği yapmak için modülü içe aktardık

def save():
    #nereye kaydedileceğini, uzantının ne olacağını karar vermemizi sağlar.
    filepath = asksaveasfilename(defaultextension="txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not filepath:
        return 
    with open(filepath,"w") as output_file: 
        text = notepad.get(1.0, END)
        output_file.write(text)
    root.title(f"Notepad - {filepath}")

root = Tk()
root.geometry("600x600")
root.title("Notepad")
root.configure(bg='thistle2')
p1 = PhotoImage(file='note.png')
root.iconphoto(False, p1)

heading = Label(root, text="Notepad", font=('bold',20), bg='thistle2') # Bu, başlık için bir etiket oluşturacaktır. 
heading.pack()

notepad = Text(root, width=400, height=450)
scroller = Scrollbar(root,command=notepad.yview)
scroller.pack(side=RIGHT, fill=Y)
notepad.config(yscrollcommand=scroller.set)
notepad.pack(fill=BOTH)

button = Button(root, text='Save', font=('normal',10), command=save, bg='thistle2')
button.place(x=270, y=520)

root.mainloop()