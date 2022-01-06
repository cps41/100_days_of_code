import tkinter

window = tkinter.Tk()
window.title("Window Title")
window.minsize(width=500, height=300)

#Label
my_label = tkinter.Label(text="A label", font=("Arial", 24, "bold"))
my_label.pack()

# must be at end to keep window open
window.mainloop()