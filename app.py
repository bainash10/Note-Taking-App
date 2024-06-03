import tkinter as tk
from tkinter import messagebox

def save_note():
    note = text.get("1.0", "end-1c")
    if note.strip():
        with open("notes.txt", "a") as file:
            file.write(note + "\n")
        messagebox.showinfo("Note Saved", "Your note has been saved successfully.")
        text.delete("1.0", "end")
    else:
        messagebox.showwarning("Empty Note", "Please write something before saving.")

def view_notes():
    try:
        with open("notes.txt", "r") as file:
            notes = file.readlines()
            if notes:
                notes_window = tk.Toplevel(root)
                notes_window.title("Your Notes")
                notes_text = tk.Text(notes_window)
                notes_text.pack()
                for note in notes:
                    notes_text.insert(tk.END, "- " + note)
            else:
                messagebox.showinfo("No Notes", "You have no notes yet.")
    except FileNotFoundError:
        messagebox.showinfo("No Notes", "You have no notes yet.")

root = tk.Tk()
root.title("Nischal takes Notes!!!!")

label = tk.Label(root, text="Write your note:")
label.pack()

text = tk.Text(root, height=10)
text.pack()

save_button = tk.Button(root, text="Save Note", command=save_note)
save_button.pack()

view_button = tk.Button(root, text="View Notes", command=view_notes)
view_button.pack()

root.mainloop()
