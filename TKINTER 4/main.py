from tkinter import *
from tkinter import messagebox

def open_file():
    file_name = entry.get()
    with open(file_name, 'r') as file:
        content = file.read()
        text.delete('1.0', END)
        text.insert(END, content)

def save_file():
    file_name = entry.get()
    content = text.get('1.0', END)
    with open(file_name, 'w') as file:
        file.write(content)
    messagebox.showinfo("поздравляю ты сохранил черта", f"Сохранение выполнено '{file_name}'.")


root = Tk()
root.title("Типо блокнот")



top_frame = Frame(root)
top_frame.pack(pady=5)

entry_label = Label(top_frame, text="Имя файла:")
entry_label.pack(side=LEFT)
entry = Entry(top_frame, width=50)
entry.pack(side=LEFT, padx=5)

open_button = Button(top_frame, text="Открыть", command=open_file)
open_button.pack(side=LEFT, padx=5)

save_button = Button(top_frame, text="Сохранить", command=save_file)
save_button.pack(side=LEFT)


text_frame = Frame(root)
text_frame.pack(pady=10)


v_scrollbar = Scrollbar(text_frame, orient=VERTICAL)
v_scrollbar.pack(side=RIGHT, fill=Y)


h_scrollbar = Scrollbar(text_frame, orient=HORIZONTAL)
h_scrollbar.pack(side=BOTTOM, fill=X)


text = Text(text_frame, wrap='none', width=60, height=15,
            yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)
text.pack(side=LEFT)

v_scrollbar.config(command=text.yview)
h_scrollbar.config(command=text.xview)
root.mainloop()
