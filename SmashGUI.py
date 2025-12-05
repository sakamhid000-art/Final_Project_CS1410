import tkinter as tk
from tkinter import messagebox
from FinalProject_stageTwo import (
    CHARACTER_LIST, CharacterFactory
)

class SmashGUI:
    def __init__(self, root):
        self.root = root
        root.title("Smash Ultimate Stage Finder")
        root.geometry("400x300")

        title = tk.Label(root, text="Smash Ultimate Stage Finder", font=("Arial", 16))
        title.pack(pady=20)

        btn1 = tk.Button(root, text="1 - See List of Characters", width=30, command=self.show_characters)
        btn1.pack(pady=5)

        btn2 = tk.Button(root, text="2 - Search Best Stage", width=30, command=self.search_stage)
        btn2.pack(pady=5)

        btn3 = tk.Button(root, text="3 - Exit", width=30, command=root.quit)
        btn3.pack(pady=5)

    def show_characters(self):
        char_window = tk.Toplevel(self.root)
        char_window.title("Available Characters")
        char_window.geometry("300x400")

        label = tk.Label(char_window, text="Characters:", font=("Arial", 14))
        label.pack(pady=10)

        for c in CHARACTER_LIST:
            tk.Label(char_window, text=c, font=("Arial", 12)).pack(anchor="w", padx=20)

    def search_stage(self):
        search_window = tk.Toplevel(self.root)
        search_window.title("Search Best Stage")
        search_window.geometry("350x200")

        label = tk.Label(search_window, text="Enter Character Name:", font=("Arial", 12))
        label.pack(pady=10)

        entry = tk.Entry(search_window, width=30)
        entry.pack(pady=5)

        def run_search():
            name = entry.get().strip()
            try:
                fighter = CharacterFactory.find_character(name)
                result = f"Best Stage: {fighter.get_best_stage()}\n\nReason:\n{fighter.get_reason()}"
                messagebox.showinfo(f"{fighter.character_name}", result)
            except ValueError:
                messagebox.showerror("Error", "Invalid character name.\nCheck spelling and try again.")

        search_btn = tk.Button(search_window, text="Search", command=run_search)
        search_btn.pack(pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    gui = SmashGUI(root)
    root.mainloop()
