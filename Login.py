import Tkinter as tk
window = tk.Tk()
users = {'bob': 'bob', }

def ch():
    for key in users.keys():
          if users[usr.get()] == pas.get():
            return True


def checkusr():
    if users.has_key(usr.get()) == True and ch() == True:
        confirm.config(text='You have successfully logged on!' )
        usr.delete(0, tk.END)
        pas.delete(0, tk.END)
        uol = tk.Label(window, text='User Options')
        uol.grid(row=8, column=1, columnspan=3)
    else:
        confirm.config(text='Your username and/or password is incorrect.' )
        usr.delete(0, tk.END)
        pas.delete(0, tk.END)

def cleart():
    usr.delete(0, tk.END)
    pas.delete(0, tk.END)
    confirm.config(text=' ' )

def ee():
    quit()

def newuser():
    
        
    newusrl = tk.Label(window, text='Create a username:')
    newusrl.grid(row=8, column=1)
    newusr = tk.Entry(window)
    newusr.grid(row=9, column=1, columnspan=3)
    newpasl = tk.Label(window, text='Create a password:')
    newpasl.grid(row=10, column=1)
    newpas = tk.Entry(window, show='*')
    newpas.grid(row=11, column=1, columnspan=3)
    newconl = tk.Label(window, text='Confirm password:')
    newconl.grid(row=12, column=1)
    newcon = tk.Entry(window, show='*')
    newcon.grid(row=13, column=1, columnspan=3)
    def reg():
        if users.has_key(newusr.get()) == False and newpas.get() == newcon.get():
            users[newusr.get()] = newpas.get()
            confirm.config(text='You have successfully registered!')
            newusrl.grid_forget()
            newusr.grid_forget()
            newpasl.grid_forget()
            newpas.grid_forget()
            newconl.grid_forget()
            newcon.grid_forget()
            register.grid_forget()
        else:
            confirm.config(text='Please retry.')
    register = tk.Button(window, text="Register!", command=reg)
    register.grid(row=14, column=1)
          
usr = tk.Entry(window)
pas = tk.Entry(window, show='*')
usrl = tk.Label(window, text='Username:')
pasl = tk.Label(window, text='Password:')
login = tk.Button(window, text='Login', command=checkusr)
newusr = tk.Button(window, text = 'Register', command=newuser)
clear = tk.Button(window, text = 'Clear', command=cleart)
confirm = tk.Label(window)
ex = tk.Button(window, text = 'Exit', command= ee)
tk.Label(window, text="LOGON GUI").grid(row=1,column=1, columnspan=4)
usrl.grid(row=2,column=1)
usr.grid(row=3,column=1, columnspan=4)
pasl.grid(row=4,column=1)
pas.grid(row=5,column=1, columnspan=4)
login.grid(row=6, column=1)
newusr.grid(row=6, column=2)
clear.grid(row=6, column=3)
confirm.grid(row=7, column=1, columnspan=4)
ex.grid(row=6, column=4)

window.mainloop()
