# GUI Part Manager from YouTube Tutorial 
# Red Alert Technologies, LLC

from tkinter import *



#App define / Title 
app = Tk()
app.title("Part Manager")
app.geometry("700x350")

# Part
part_text = StringVar()
part_label = Label(app, text="Part Name", font=('bold', 14), pady=20)
part_label.grid(row=0, column=0, sticky=W)
part_entry = Entry(app, textevariable = part_text)
part_entry.grid(row=0, column=1)


# Main Loop to Start Program 
app.mainloop()