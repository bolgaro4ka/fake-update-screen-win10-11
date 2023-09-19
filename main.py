from tkinter import *
import config
from PIL import Image
root = Tk()  # create CTk window like you do with the Tk window
root.title("LOL")  # Modes: system (default), light, dark  # Themes: blue (default), dark-blue, green

root.geometry()
root.attributes('-fullscreen', True)
root.resizable(False, False)

root["bg"] = config.color
percente=0
frames = [PhotoImage(file='img/loader.gif', format='gif -index %i' % (i)) for i in range(75)]

WIDTH_MONITOR = root.winfo_screenwidth()
HEIGHT_MONITOR = root.winfo_screenheight()

death = Image.open("img/death.png")
death = death.resize((WIDTH_MONITOR, HEIGHT_MONITOR)) ## The (250, 250) is (height, width)
death.save('img/yoursize.png')
death = PhotoImage(file="img/yoursize.png")
def update(ind):
    try:
        frame = frames[ind]
        ind += 1
    except:
        ind=0
        frame = frames[ind]
    label.configure(image=frame)
    root.after(75, update, ind)


def plus_persente(*args):
    global percente
    percente += 1
    work_comp["text"] = f"Завершено: {percente}%"

def plus_death(*args):

    death_label["image"]=death

label = Label(root, bg=config.color)
label.place(x=WIDTH_MONITOR//2-50, y=HEIGHT_MONITOR//2-100)

work=Label(text="Работа с обновлениями", bg=config.color, fg="white", font=("Segoe UI", 18))
work.place(x=WIDTH_MONITOR//2-150, y=HEIGHT_MONITOR//2)
work_comp=Label(text="Завершено: 0%", bg=config.color, fg="white", font=("Segoe UI", 18))
work_comp.place(x=WIDTH_MONITOR//2-110, y=HEIGHT_MONITOR//2+35)
work_turn=Label(text="Не выключайте компьютер", bg=config.color, fg="white", font=("Segoe UI", 18))
work_turn.place(x=WIDTH_MONITOR//2-175, y=HEIGHT_MONITOR//2+70)
death_label = Label(bg=config.color)
death_label.place(x=0, y=0)

root.after(0, update, 0)

work_comp.bind("<ButtonPress-1>", plus_persente)
work_turn.bind("<ButtonPress-1>", plus_death)
root.mainloop()