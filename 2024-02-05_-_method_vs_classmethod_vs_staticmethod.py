class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None
    def set_user(self, user):
        self.user = user
    def set_password(self, password):
        self.password = password
    @classmethod
    def create_with_auth(cls, user, password):
        conexao = cls()
        conexao.user = user
        conexao.password = password
        return conexao 
    @staticmethod
    def soma(x, y):
        return x + y
c1 = Connection()
c1.set_user(user='Edsuu')
c1.set_password(password='123456')
print(c1.user) #1:
print(c1.password) #2:
print(c1.host) #3:
c2 = Connection.create_with_auth(user='Edsononon', password='987654')
print(c2.user) #4:
print(c2.password) #5:
print(Connection.soma(3, 5)) #6:

# Edson Copque | https://linktr.ee/edsoncopque
