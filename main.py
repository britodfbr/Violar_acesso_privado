import toml
import sys


# carregamento de configurações
config = toml.load('config.toml')

class Login:
    """ Exemplo com atributos privados """

    def __init__(self, user, pw):
        self.user = user
        self.__pw = pw


l = Login(config['site']['login'], config['site']['senha'])

try:
    print(l.user, l.__pw)    # tentativa de acesso
except:
    print('Erro ao tentar acesso a atributo privado:\n')
    print(sys.exc_info())

# Violação intencional de acesso
print('\n\nViolação intencional de acesso:\n{}: {}'.format(l.user, l._Login__pw))

# ----------------------
print('-'*50)
class Login1(Login):
    """ Exemplo com atributos protegidos """

    def __init__(self, user, pw):
        super().__init__(user, None)
        self._pw = pw


l = Login1(config['site']['login'], config['site']['senha'])
# acesso a atributos protegidos
print('\n\nAcesso a atributos protegidos:\n{}: {}'.format(l.user, l._pw))


# ----------------------
print('-'*50)
class Login1(Login):
    """ Exemplo com atributos públicos """

    def __init__(self, user, pw):
        super().__init__(user, None)
        self.pw = pw


l = Login1(config['site']['login'], config['site']['senha'])
# Acesso a atributos públicos
print('\n\nAcesso a atributos públicos:\n{}: {}'.format(l.user, l.pw))
