class Title():
    def __init__(self, title_text, x, y):
        self.title = title_text
        self.x = x
        self.y = y
        self.appearance = True

    def hide(self):
        self.appearance = False
        print(self.title, "-приховано")

    def show(self):
        self.appearance = True
        print(self.title, "-відображається")

    def print_information(self):
        print("Кнопка:", self.title)
        print("Розташування:", "(" + str(self.x) + ',' + str(self.y) + ")" )
        print("Видимість:", self.appearance)

main_text = (" Дізнатися переможця прямо зараз", 150, 50)

rules_text = ("Переможешь може бути тільки один", 150, -100)

main_text.print_information()
rules_text.print_information()
rules_text.hide()