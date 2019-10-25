
from tkinter import *
import sys
from school import Student

# global instance
# student = Student()

class Credentials(Frame):
    """Create a login frame that opens database upon 
    successful login or prints relevant message if credentials are 
    incorrect """

    def __init__(self, root ,master):
        """ Initiaize frame"""
        super(Credentials, self).__init__(master)
        self.root = root
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """Create login widgets. """
        
        Label(self, text="Username").grid(row=2, column=3, columnspan=1, sticky=W)
        # username input
        self.username = Entry(self)
        self.username.grid(row=5, column=3, columnspan=4, sticky=W)
        Label(self, text="Password").grid(row=6, column=3, columnspan=1, sticky=W)
        self.password = Entry(self, show="*")
        self.password.grid(row=7, column=3, columnspan=4, sticky=W)

        # create cancel button
        self.cancel_button = Button(self, text="Cancel", command=self.cancel)
        self.cancel_button.grid(row=10, column=3)

        # create a login button
        self.login_button = Button(self, text="Login", command=self.login)
        self.login_button.grid(row=10, column=5)
    
    def login(self):
        """ Open database GUI"""
        # if credentials are correct
        try:
            self.main_root = Tk()
            Student(self.main_root,self.username.get(), self.password.get())
            self.root.destroy()
        except:
            main()
        

    def cancel(self):
        """Destroy windows all together. """
        self.root.destroy()
        sys.exit()
        

def main():
    """Interact with class """
    root = Tk()
    root.title("Login to School Database")
    root.geometry("500x205")
    app = Credentials(root,root)
    root.mainloop()
    return

if __name__ == '__main__':
    main()
