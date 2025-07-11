from mydb import Database
from tkinter import *
from tkinter import messagebox

class NLPApp:
    
    def __init__(self):
        #Database  object
        self.dbo = Database()

        self.BG ="#34495E"
        self.root = Tk()
        self.root.title("NLP Application")
        self.root.geometry("450x600")
        self.root.configure(bg=self.BG)   

        icon_path = "GUI/resources/favicon.ico"
        self.root.iconbitmap(icon_path)
        
        self.login_gui()
        self.root.mainloop()

    def login_gui(self):
        self.clear()
        self.root.title("Login")
        Label(self.root, text="NLP Application", bg=self.BG, fg="red", font=("Arial", 26, 'bold')).pack(pady=20)

        Label(self.root, text="Enter Email", font=("Arial", 16), bg=self.BG).pack(pady=10)
        self.email_entry = Entry(self.root, font=("Arial", 20), width=25)
        self.email_entry.pack(pady=10)

        Label(self.root, text="Enter Password", font=("Arial", 16), bg=self.BG).pack(pady=10)
        self.password_entry = Entry(self.root, font=("Arial", 20), width=25, show="*")
        self.password_entry.pack(pady=10)

        Button(self.root, text="Login", height=1, width=23, font=("Arial", 20),command=self.login).pack(pady=10)

        Label(self.root, text="Not a member ?", font=("Arial", 8), bg=self.BG).pack(pady=10)
        Button(self.root, text="Register", height=1, width=23, font=("Arial", 20), command=self.register_gui).pack(pady=10)
    
    def register_gui(self):
        self.clear()
        self.root.title("Register")
        
        Label(self.root, text="NLP Application", bg=self.BG, fg="red", font=("Arial", 16, 'bold')).pack(pady=10)
        
        Label(self.root, text="Enter Username", bg=self.BG, font=("Arial", 16)).pack(pady=10)
        self.username_entry = Entry(self.root, font=("Arial", 20), width=25)
        self.username_entry.pack(pady=10)

        Label(self.root, text="Enter Email", bg=self.BG, font=("Arial", 16)).pack(pady=10)
        self.email_entry = Entry(self.root, font=("Arial", 20), width=25)
        self.email_entry.pack(pady=10)

        Label(self.root, text="Enter Password", font=("Arial", 16), bg=self.BG).pack(pady=10)
        self.password_entry = Entry(self.root, font=("Arial", 20), width=25, show="*")
        self.password_entry.pack(pady=10)

        
        Button(self.root, text="Register", height=1, width=25, font=("Arial", 20), command=self.signup).pack(pady=10)

        Label(self.root, text="Already Registration", font=("Arial", 8), bg=self.BG).pack(pady=10)
        Button(self.root, text="Login", height=1, width=23, font=("Arial", 20), command=self.login_gui).pack(pady=10)

    def login(self):
        self.email = self.email_entry.get()
        self.password = self.password_entry.get()

        if not self.check(self.email,self.password):
            return
        
        if self.dbo.search(self.email, self.password):
            messagebox.showinfo("Success", "Login successful!")
            self.home_gui(self.email, self.dbo.get_name(self.email))
        else:
            messagebox.showerror("Error", "Invalid Email or Password.")

    def signup(self):
        username = self.username_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()
        
        if not username :
            messagebox.showerror("Error", "Username cannot be empty.")
            return
        
        if not self.check(email,password):
            return
        
        self.dbo.add_data(username,email,password)
        self.login_gui()
    
    def check(self, email, password):
        if not email or not password:
            messagebox.showerror("Error", "Email and Password cannot be empty.")
            return False

        if "@" not in email or "." not in email:
            messagebox.showerror("Invalid Email", "Please enter a valid email.")
            return False

        return True

    def clear(self):
        for i in self.root.slaves():
            i.destroy()

    def home_gui(self, email, name):
        self.clear()
        self.root.title("Home")
        

        Label(self.root, text=f"Welcome {name.title()} \n to NLP Application", bg=self.BG, fg="white", font=("Arial", 20, 'bold')).pack(pady=20)
        Label(self.root, text=f"Logged in as: {email}", bg=self.BG, font=("Arial", 12)).pack(pady=10)
        Button(self.root, text="NER", height=1, width=23, font=("Arial", 20), command=self.NER).pack(pady=10)
        Button(self.root, text="Sentiment", height=1, width=23, font=("Arial", 20), command=self.Sentiment).pack(pady=10)
        Button(self.root, text="Summarization", height=1, width=23, font=("Arial", 20), command=self.Summarization).pack(pady=10)
        Button(self.root, text="Logout", height=1, width=15, font=("Arial", 20), command=self.login_gui).pack(pady=40)

    def NER(self):
        self.home_panel()
        self.root.title("NER Functionality")
        Label(self.root, text="Named Entity Recognition", bg=self.BG, fg="white", font=("Arial", 20)).pack(pady=20)
        
    def Sentiment(self):
        self.home_panel()
        self.root.title("Sentiment Functionality")
        Label(self.root, text="Sentiment Functionality", bg=self.BG, fg="white", font=("Arial", 20)).pack(pady=20)

    def Summarization(self):
        self.home_panel()
        self.root.title("Summarization Functionality")
        Label(self.root, text="Summarization Functionality", bg=self.BG, fg="white", font=("Arial", 20)).pack(pady=20)


    def home_panel(self):
        self.clear()
        self.root.title("Summarization Functionality")
        Button(self.root, text="← Back", bg=self.BG, fg="white", font=("Arial", 14, 'bold'), command=self.back_to_home).pack(anchor='nw', padx=10, pady=10)
        Label(self.root, text="NLP Application", bg=self.BG, fg="red", font=("Arial", 26, 'bold')).pack(pady=20)
        return

    def back_to_home(self):
        self.home_gui(self.email, self.dbo.get_name(self.email))


nlp = NLPApp()
