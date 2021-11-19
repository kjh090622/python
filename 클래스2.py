class game:
  def __init__(self,name,level,server):
    self.name = name
    self.level = level
    self.server = server

name = input("name:")
level = int(input("level:"))
server = input("server:")

print("당신의 닉네임은 '%s'입니다"%name)
print("당신의 레벨은 %dlv입니다"%level)
print("당신이 있는 서버는 '%s'입니다"%server)
