from tkinter import *
class Resume:
    def __init__(self, master, func, text):
        self.title = Label(master, text=text, font=("Times New Roman", 10, "bold"))
        self.ent = Entry(master, width=50)
        self.but = Button(master, text="Растау")
        self.lab = Label(master, width=50, bg='pink', fg='black')
        self.but['command'] = getattr(self, func)
        self.title.pack()
        self.ent.pack()
        self.but.pack()
        self.lab.pack()
    def name(self):
        name = self.ent.get()
        if name.isalpha():
            self.lab['text'] = f'Есіміңіз: {name}'
        else:
            self.lab['text'] = 'Цифр жазбаңыз'
    def age(self):
        age = self.ent.get()
        if age.isdigit():
            self.lab['text'] = f'Жасыңыз: {age}'
        else:
            self.lab['text'] = 'Мәтін жазбаңыз'
    def kurs(self):
        kurs = self.ent.get()
        if kurs.isdigit():
            self.lab['text'] = f'Сіз {kurs}-нші курста оқисыз'
        else:
            self.lab['text'] = 'Мәтін жазбаңыз'
    def mamandyk(self):
        mamandyk = self.ent.get()
        if mamandyk.isalnum():
            self.lab['text'] = f'Мамандық: {mamandyk}'
        else:
            self.lab['text'] = 'Цифр жазбаңыз'
    def number(self):
        number = self.ent.get()
        if number.isdigit():
            self.lab['text'] = f'Байланыс нөміріңіз: {number}'
        else:
            self.lab['text'] = 'Мәтін жазбаңыз'
root = Tk()
root.title("Резюме")
first_block = Resume(root, 'name', "Атыңызды енгізіңіз:")
second_block = Resume(root, 'age', "Жасыңызды енгізіңіз:")
third_block = Resume(root, 'kurs', "Курсыңызды енгізіңіз:")
fourth_block = Resume(root, 'mamandyk', "Мамандығыңызды енгізіңіз:")
fifth_block = Resume(root, "number", "Байланыс нөміріңізді енгізіңіз:")
root.mainloop()
