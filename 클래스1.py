class Student:
    def __init__(self, name,age,contry):
        self.name = name
        self.age = age
        self.contry = contry


name = input("이름:")
age = int(input("나이:"))
contry = input("출신:")

st = Student(name, age,contry)

print("당신의 이름은 %s입니다"%st.name)
print("당신의 나이는 %d입니다"%st.age)
print("당신은 '%s'출신입니다 "%st.contry)
