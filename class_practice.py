class JSS:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def testa():
    a = JSS("Luke", "31")
    print(a.name)
    print(a.age)

class JSS2(JSS):
    def __init__(self, name, age, gender):
        super().__init__(name, age)
        self.gender = gender


b = JSS("TH", "23")
print(b.name, b.age)

c = JSS2("Min", "99", "W")

if __name__ == "__main__":
    print("hello")
    testa()
    print(c.gender)