from tkinter import *
import tkinter.messagebox as mb
import sqlite3


class Registr:

    def CreateNewUser(self, username, password, password_again):
        if username == '' or password == '' or password_again == '':
            msg = 'Заполните все поля'
            mb.showerror("Ошибка", msg)
        else:
            con = sqlite3.connect('Users.sqlite')
            cur = con.cursor()
            cur.execute(' create table if not exists Users(Username TEXT,Password TEXT)')
            con.commit()
            cur.execute('SELECT Username FROM Users')
            for i in cur.fetchall():
                if username == i[0]:
                    msg = 'Имя пользователя уже существует'
                    mb.showerror("Ошибка", msg)
            else:
                if password != password_again:
                    msg = 'Пароли не совпадают'
                    mb.showerror("Ошибка", msg)
                else:
                    new_user = (username, password)
                    cur.execute("""INSERT INTO Users(Username, Password) VALUES(?,?);""", new_user)
                    con.commit()
                    msg = "Новый пользователь успешно зарегестрирован"
                    mb.showinfo("Успешно", msg)
                    self.window_Reg.destroy()

    def __init__(self):
        window_Entry.destroy()
        self.window_Reg = Tk()
        self.window_Reg.title('Регистрация')
        self.window_Reg.geometry('300x300')
        self.window_Reg.eval('tk::PlaceWindow . center')
        username_label = Label(self.window_Reg, text='Имя пользователя', )
        username_entry = Entry(self.window_Reg, bg='#fff', fg='#444')
        password_label = Label(self.window_Reg, text='Пароль')
        password_entry = Entry(self.window_Reg, bg='#fff', fg='#444')
        password_label_confirm = Label(self.window_Reg, text='Повторите пароль')
        password_entry_confirm = Entry(self.window_Reg, bg='#fff', fg='#444')
        send_btn = Button(self.window_Reg, text='Зарегистрироваться', command=lambda:
        self.CreateNewUser(username_entry.get(), password_entry.get(), password_entry_confirm.get(), ))

        username_label.pack(padx=10, pady=8)
        username_entry.pack(padx=10, pady=8)
        password_label.pack(padx=10, pady=8)
        password_entry.pack(padx=10, pady=8)
        password_label_confirm.pack(padx=10, pady=8)
        password_entry_confirm.pack(padx=10, pady=8)
        send_btn.pack(padx=10, pady=8)

        self.window_Reg.mainloop()


class Login_in:

    def CheckExist(self, username, password):
        if username == '' or password == '':
            msg = 'Заполните все поля'
            mb.showerror("Ошибка", msg)
        else:
            con = sqlite3.connect('Users.sqlite')
            cur = con.cursor()
            cur.execute(' create table if not exists Users(Username TEXT,Password TEXT)')
            con.commit()
            cur.execute('SELECT * FROM Users')
            for i in cur.fetchall():
                if username == i[0]:
                    print(password == i[1])
                    if password == i[1]:
                        msg = "Вы успешно зашли"
                        mb.showinfo("Успешно", msg)
                        self.window_Login.destroy()
                        return
                    else:
                        msg = 'Пароль не совпадает'
                        mb.showerror("Ошибка", msg)
                        return
            msg = 'Такой пользователь не зарегестрирован'
            mb.showerror("Ошибка", msg)
            return



    def __init__(self):
        window_Entry.destroy()
        self.window_Login = Tk()
        self.window_Login.title('Вход')
        self.window_Login.geometry('300x250')
        self.window_Login.eval('tk::PlaceWindow . center')
        username_label = Label(self.window_Login, text='Имя пользователя', )
        username_entry = Entry(self.window_Login, bg='#fff', fg='#444')
        password_label = Label(self.window_Login, text='Пароль')
        password_entry = Entry(self.window_Login, bg='#fff', fg='#444')
        send_btn = Button(self.window_Login, text='Войти', command=lambda:
        self.CheckExist(username_entry.get(), password_entry.get()))

        username_label.pack(padx=10, pady=8)
        username_entry.pack(padx=10, pady=8)
        password_label.pack(padx=10, pady=8)
        password_entry.pack(padx=10, pady=8)
        send_btn.pack(padx=10, pady=8)

        self.window_Login.mainloop()



window_Entry = Tk()
window_Entry.title('Lab 9')
window_Entry.geometry('250x250')
window_Entry.eval('tk::PlaceWindow . center')
loginin = Button(window_Entry, text='Вход', command=Login_in)
reg = Button(window_Entry, text='Регистрация', command=Registr)
loginin.pack(padx=10, pady=8)
reg.pack(padx=10, pady=8)

window_Entry.mainloop()
