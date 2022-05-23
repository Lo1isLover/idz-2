print("Эта программа проверяет правильность скобочной записи с тремя видами скобок: '[]', '{}', '()'\n"
      "с условием, что на каждом уровне вложенности не может быть более двух пар подряд идущих скобок.\n"
      "Нужно ввести подобную запись, используя только 6 перечисленных символов, т.е. '(', ')', '[', ']', '{', '}',\n"
      "а также в конце записи добавить 0: \n"
      "Пример правильной записи: {(()())}({()}[()()])0\n"
      "Пример неправильной записи: [{}()()]([][]){}0\n"
      "Введите: ")


instr = input()
i = 0
ch = 'a'


class FWBError(Exception):
    def __init__(self):
        print('Попробуйте снова. Введите синтаксически верную запись! ')


def read():
    global ch, i
    i += 1
    ch = instr[i]


def error():
    raise FWBError()


def formula():
    if ch == '0':
        print('true')
    else:
        print('false')


class MainClass:
    def corexp(self):
        if ch == '(' or ch == '[' or ch == '{':
            self.brackets()
            if ch == '(' or ch == '[' or ch == '{':
                self.brackets()

    def brackets(self):
        try:
            if ch == '(':
                if ch == '(':
                    read()
                else:
                    error()
                self.corexp()
                if ch == ')':
                    read()
                else:
                    error()
            elif ch == '[':
                if ch == '[':
                    read()
                else:
                    error()
                self.corexp()
                if ch == ']':
                    read()
                else:
                    error()
            elif ch == '{':
                if ch == '{':
                    read()
                else:
                    error()
                self.corexp()
                if ch == '}':
                    read()
                else:
                    error()
            else:
                error()
        except FWBError:
            return


def main():
    global ch
    global instr
    global i
    ch = instr[0]
    m = MainClass()
    m.corexp()
    formula()
    chk = input("Хотите ввести еще одну запись? Да - 'y', нет - 'n':\n")
    if chk == 'n':
        return
    elif chk == 'y':
        print('Введите: ')
        instr = input()
        i = 0
        main()


main()
