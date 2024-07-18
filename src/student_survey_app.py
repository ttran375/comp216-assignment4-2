import tkinter as tk
from tkinter import ttk, messagebox


class StudentSurveyApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Centennial College")
        self.configure(bg="green")

        # Frame for the form
        self.frame = tk.Frame(
            self, bg="green", padx=10, pady=10, relief=tk.SUNKEN, bd=2
        )
        self.frame.grid(sticky="nsew")

        # Grid configuration
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(1, weight=1)

        # Labels and Widgets
        tk.Label(
            self.frame, text="ICET Student Survey", font=("Helvetica", 16), bg="green"
        ).grid(row=0, column=0, columnspan=2, pady=10)

        tk.Label(self.frame, text="Full name:", bg="green").grid(
            row=1, column=0, sticky="e"
        )
        self.fullname_entry = tk.Entry(self.frame)
        self.fullname_entry.grid(row=1, column=1, sticky="ew")

        tk.Label(self.frame, text="Residency:", bg="green").grid(
            row=2, column=0, sticky="e"
        )
        self.residency_var = tk.StringVar(value="dom")
        tk.Radiobutton(
            self.frame,
            text="Domestic",
            variable=self.residency_var,
            value="dom",
            bg="green",
        ).grid(row=2, column=1, sticky="w")
        tk.Radiobutton(
            self.frame,
            text="International",
            variable=self.residency_var,
            value="intl",
            bg="green",
        ).grid(row=3, column=1, sticky="w")

        tk.Label(self.frame, text="Program:", bg="green").grid(
            row=4, column=0, sticky="e"
        )
        self.program_combobox = ttk.Combobox(
            self.frame, values=["AI", "Gaming", "Health", "Software"], state="readonly"
        )
        self.program_combobox.grid(row=4, column=1, sticky="ew")

        tk.Label(self.frame, text="Courses:", bg="green").grid(
            row=5, column=0, sticky="e"
        )
        self.programming_var = tk.StringVar(value="COMP100")
        self.web_design_var = tk.StringVar(value="")
        self.software_eng_var = tk.StringVar(value="")
        tk.Checkbutton(
            self.frame,
            text="Programming I",
            variable=self.programming_var,
            onvalue="COMP100",
            offvalue="",
            bg="green",
        ).grid(row=5, column=1, sticky="w")
        tk.Checkbutton(
            self.frame,
            text="Web Page Design",
            variable=self.web_design_var,
            onvalue="COMP213",
            offvalue="",
            bg="green",
        ).grid(row=6, column=1, sticky="w")
        tk.Checkbutton(
            self.frame,
            text="Software Engineering",
            variable=self.software_eng_var,
            onvalue="COMP120",
            offvalue="",
            bg="green",
        ).grid(row=7, column=1, sticky="w")

        # Buttons
        tk.Button(self.frame, text="Reset", command=self.reset_form).grid(
            row=8, column=0, pady=10
        )
        tk.Button(self.frame, text="Ok", command=self.display_info).grid(
            row=8, column=1, pady=10
        )
        tk.Button(self.frame, text="Exit", command=self.quit).grid(
            row=8, column=2, pady=10
        )

        # Initialize form
        self.reset_form()

        # Make the application responsive
        self.frame.grid_rowconfigure(7, weight=1)
        self.frame.grid_columnconfigure(1, weight=1)

    def reset_form(self):
        self.fullname_entry.delete(0, tk.END)
        self.fullname_entry.insert(0, "Narendra Pershad")
        self.residency_var.set("dom")
        self.program_combobox.set("Health")
        self.programming_var.set("COMP100")
        self.web_design_var.set("")
        self.software_eng_var.set("")

    def display_info(self):
        info = f"{self.fullname_entry.get()}\n{self.program_combobox.get()}\n{self.residency_var.get()}\n({self.programming_var.get()} {self.web_design_var.get()} {self.software_eng_var.get()})"
        messagebox.showinfo("Information", info)


if __name__ == "__main__":
    app = StudentSurveyApp()
    app.mainloop()
