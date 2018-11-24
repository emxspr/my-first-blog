print('Hello, Django girls!')
if 3 > 2:
    print('It works!')
if 5 > 2:
    print('5 est effectivement plus grand que 2')
else:
    print("5 n'est pas plus grand que 2")
name = 'Emma'
if name == 'Soupart':
    print('Hey Soupart')
elif name == 'Emma':
    print('Hey Emma')
else:
    print('Hey anonymous!')
volume = 57
if volume < 20:
    print("C'est plutôt calme.")
elif 20 <= volume < 40:
    print("Une jolie musique de fond.")
elif 40 <= volume < 80:
    print("Parfait, je peux entendre tous les détails du morceau")
elif 60 <= volume < 80:
    print("Parfait pour faire la fête !")
elif 80 <= volume < 100:
    print("Un peu trop fort !")
else:
    print("Au secours ! mes oreilles! :(")
def hi():
    print('Hi there!')
    print('How are you?')
hi()
def hi(name):
    if name == 'emma':
        print('Hi emma')
    elif name == 'Soupart':
        print('Hi Soupart')
    else:
        print('Hi anonymous!')
hi("julie")
hi("emma")
def hi(name):
    print('Hi ' + name +'!')

hi("Rachel")
girls = ['Rachel', 'Monica', 'Phoebe', 'ola', 'you']
for name in girls:
    hi(name)
    print('Next girl')
for i in range(1, 6):
    print(i)
for i in range(1, 36):
    print(i)
