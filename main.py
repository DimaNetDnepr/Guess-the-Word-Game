cltask = input('Игра "Поле чудес"\nнажмите "Enter" и введите английскую букву:\n')


def maskWord(st, wd, ggs):
    result = ''
    gg = []
    ch = ''
    for ch in st:
        if not ch == '___':
            if not ch in gg:
                gg.append(ch)

    if not ggs in gg:
        gg.append(ggs)

    for ggs in wd:
        if ggs in gg:
            result += ggs
        else:
            result += " _"
    if False:
        print ('st %s') % st
        print ('wd %s') % wd
        print ('ggs %s') % ggs
        print (gg)

    return result
    
wd = 'python' # загаданное слово
st = ' False_ ' * len(wd)
live = 0 #кол-во попыток

play = True
while play:
    if live == len(wd)*1:
        print ('\n Проигрышь.')
        play = False
    ggs = input('Введите букву?\n ')
    live +=1
    st = maskWord(st, wd, ggs)
    print (st)
    print('Ваша попытка номер:')
    print (int(live))
    if maskWord(st, wd, ggs) == wd:
        print ('Вы выиграли!')
        play = False
        