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

    def __init__(self):
        window_Reg = Tk()
        window_Reg.title('Регистрация')
        window_Reg.geometry('300x300')
        username_label = Label(window_Reg, text='Имя пользователя', )
        username_entry = Entry(window_Reg, bg='#fff', fg='#444')
        password_label = Label(window_Reg, text='Пароль')
        password_entry = Entry(window_Reg, bg='#fff', fg='#444')
        password_label_confirm = Label(window_Reg, text='Повторите пароль')
        password_entry_confirm = Entry(window_Reg, bg='#fff', fg='#444')
        send_btn = Button(window_Reg, text='Зарегистрироваться', command=lambda:
        self.CreateNewUser(username_entry.get(), password_entry.get(), password_entry_confirm.get(), ))

        username_label.pack(padx=10, pady=8)
        username_entry.pack(padx=10, pady=8)
        password_label.pack(padx=10, pady=8)
        password_entry.pack(padx=10, pady=8)
        password_label_confirm.pack(padx=10, pady=8)
        password_entry_confirm.pack(padx=10, pady=8)
        send_btn.pack(padx=10, pady=8)

        window_Reg.mainloop()


class Login_in:

    def CheckExist(self, username, password):
        if username == '' or password == '':
            msg = 'Заполните все поля'
            mb.showerror("Ошибка", msg)
        else:
            con = sqlite3.connect('Users.sqlite')
            cur = con.cursor()
            cur.execute('SELECT * FROM Users')
            for i in cur.fetchall():
                if username == i[0]:
                    print(password == i[1])
                    if password == i[1]:
                        msg = "Вы успешно зашли"
                        mb.showinfo("Успешно", msg)
                        return
                    else:
                        msg = 'Пароль не совпадает'
                        mb.showerror("Ошибка", msg)
                        return
            msg = 'Такой пользователь не зарегестрирован'
            mb.showerror("Ошибка", msg)
            return



    def __init__(self):
        window_Login = Tk()
        window_Login.title('Вход')
        window_Login.geometry('300x250')
        username_label = Label(window_Login, text='Имя пользователя', )
        username_entry = Entry(window_Login, bg='#fff', fg='#444')
        password_label = Label(window_Login, text='Пароль')
        password_entry = Entry(window_Login, bg='#fff', fg='#444')
        send_btn = Button(window_Login, text='Войти', command=lambda:
        self.CheckExist(username_entry.get(), password_entry.get()))

        username_label.pack(padx=10, pady=8)
        username_entry.pack(padx=10, pady=8)
        password_label.pack(padx=10, pady=8)
        password_entry.pack(padx=10, pady=8)
        send_btn.pack(padx=10, pady=8)

        window_Login.mainloop()


class App:
    window_Entry = Tk()
    window_Entry.title('Lab 9')
    window_Entry.geometry('250x250')
    loginin = Button(window_Entry, text='Вход', command=Login_in)
    reg = Button(window_Entry, text='Регистрация', command=Registr)
    loginin.pack(padx=10, pady=8)
    reg.pack(padx=10, pady=8)

    window_Entry.mainloop()
