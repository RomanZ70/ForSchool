import math


def K_convert():
    K = input('Чему равно K?\n')
    try:
        K_list = K.split('x')
        K_ret = int(K_list[0]) * int(K_list[1])
        return K_ret
    except ValueError:
            K_list = K.split(' ')
            K_ret = int(K_list[0]) * int(K_list[1])
            return K_ret


def I_convert_in(name):
    inp = input(f'Чему равно {name} и какие единицы измерения? Ничего не писать если в битах\n')
    inp_list = inp.split()
    if len(inp_list) == 1:
        return int(inp_list[0])
    if inp_list[1] == 'bit':
        return inp_list[0]
    elif inp_list[1] == 'byte':
        I = int(inp_list[0])*8
        return I
    elif inp_list[1] == 'Kb':
        I = int(inp_list[0])*8192
        return I
    elif inp_list[1] == 'Mb':
        I = int(inp_list[0])*8388604
        return I
    elif inp_list[1] == 'Gb':
        I = int(inp_list[0])*(8388608*1024)
        return I
    else:
        print(f'Неизвестная величина. {name} будет измеряться в битах')
        return int(inp_list[0])


def I_convert_out(name, count):
    inp = input(f'В чём измерять {name}? Enter если в битах\n')
    if inp == 'bit':
        return str(count) + ' bit'
    elif inp == 'byte':
        I = int(count)/8
        return str(I) + ' byte'
    elif inp == 'Kb':
        I = int(count)/8192
        return str(I) + ' Kb'
    elif inp == 'Mb':
        I = int(count)/8388604
        return str(I) + ' Mb'
    elif inp == 'Gb':
        I = int(count)/(8388608*1024)
        return str(I) + ' Gb'
    elif inp == '':
        return str(count) + ' bit'
    else:
        print(f'Неизвестная величина. {name} будет измеряться в битах')
        return str(count) + ' bit'

def inf_encoding():
    print('Что найти?')
    choice = input()
    a = 0
    while a != 1:
        if choice == 'N':
            a = 1
            list = input('Что дано?\n')
            list = list.split(' ')
            for x in list:
                if x == 'i':
                    i = int(input('Чему равно i?\n'))
                    print(f'N = {2**i}')
                    return
            for x in list:
                if x == 'I':
                    for xx in list:
                        if xx == 'K':
                            K = int(input('Чему равно K?\n'))
                            I = int(input('Чему равно I?\n'))
                            i = I/K
                            print(f'N = {2 ** i}')
                            return
                    if 'K' not in list:
                        print('Невозможно решить')
                        return
            print('Невозможно решить - недостаточно данных')


        elif choice == 'i':
            a = 1
            list = input('Что дано?\n')
            list = list.split(' ')
            for x in list:
                if x == 'N':
                    N = int(input('Чему равно N?\n'))
                    print(f'i = {round(math.log(N, 2))} бит')
                    return
            for x in list:
                if x == 'I':
                    for xx in list:
                        if xx == 'K':
                            K = int(input('Чему равно K?\n'))
                            I = int(input('Чему равно I?\n'))
                            print(f'i = {round(I/K)} бит')
                            return
                    if 'K' not in list:
                        print('Невозможно решить')
                        return
            print('Невозможно решить - недостаточно данных')


        elif choice == 'I':
            a = 1
            list = input('Что дано?\n')
            list = list.split(' ')
            for x in list:
                if x == 'i':
                    for xx in list:
                        if xx == 'K':
                            K = int(input('Чему равно K?\n'))
                            i = int(input('Чему равно i?\n'))
                            print(f'I = {round(i*K)} бит')
                            return
                    if 'K' not in list:
                        print('Невозможно решить')
                        return
            for x in list:
                if x == 'N':
                    for xx in list:
                        if xx == 'K':
                            N = int(input('Чему равно N?\n'))
                            K = int(input('Чему равно K?\n'))
                            print(f'I = {round(round(math.log(N, 2))*K)} бит')
                            return
                    if 'K' not in list:
                        print('Невозможно решить')
                        return
            print('Невозможно решить - недостаточно данных')

        elif choice == 'K':
            a = 1
            list = input('Что дано?\n')
            list = list.split(' ')
            for x in list:
                if x == 'I':
                    for xx in list:
                        if xx == 'i':
                            I = int(input('Чему равно I?\n'))
                            i = int(input('Чему равно i?\n'))
                            print(f'K = {round(I/i)}')
                            return
                    if ('i' not in list) and ('N' not in list):
                        print('Невозможно решить')
                        return
            for x in list:
                if x == 'I':
                    for xx in list:
                        if xx == 'N':
                            N = int(input('Чему равно N?\n'))
                            I = int(input('Чему равно I?\n'))
                            print(f'K = {round(math.log(N, 2)) / I} ')
                            return
                    if 'N' not in list:
                        print('Невозможно решить')
                        return
            print('Невозможно решить - недостаточно данных')
        else:
            print('Что найти?')
            choice = input()


def image():
    print('Что найти?')
    choice = input()
    a = 0
    while a != 1:
        if choice == 'N':
            a = 1
            list = input('Что дано?\n')
            list = list.split(' ')
            for x in list:
                if x == 'i':
                    i = int(input('Чему равно i?\n'))
                    print(f'N = {2 ** i}')
                    return
            for x in list:
                if x == 'I':
                    for xx in list:
                        if xx == 'K':
                            K = K_convert()
                            I = I_convert_in('I')
                            i = I / K
                            print(f'N = {2 ** i}')
                            return
                    if 'K' not in list:
                        print('Невозможно решить')
                        return
            print('Невозможно решить - недостаточно данных')


        elif choice == 'i':
            a = 1
            list = input('Что дано?\n')
            list = list.split(' ')
            for x in list:
                if x == 'N':
                    N = int(input('Чему равно N?\n'))
                    print(f'i = {round(math.log(N, 2))} бит')
                    return
            for x in list:
                if x == 'I':
                    for xx in list:
                        if xx == 'K':
                            K = K_convert()
                            I = I_convert_in('I')
                            print(f'i = {round(I / K)} бит')
                            return
                    if 'K' not in list:
                        print('Невозможно решить')
                        return
            print('Невозможно решить - недостаточно данных')


        elif choice == 'I':
            a = 1
            list = input('Что дано?\n')
            list = list.split(' ')
            for x in list:
                if x == 'i':
                    for xx in list:
                        if xx == 'K':
                            K = K_convert()
                            i = int(input('Чему равно i?\n'))
                            I = i * K
                            print(I_convert_out('I', I))
                            return
                    if 'K' not in list:
                        print('Невозможно решить')
                        return
            for x in list:
                if x == 'N':
                    for xx in list:
                        if xx == 'K':
                            N = int(input('Чему равно N?\n'))
                            K = K_convert()
                            I = (round(math.log(N, 2)) * K)
                            print(I_convert_out('I', I))
                            return
                    if 'K' not in list:
                        print('Невозможно решить')
                        return
            print('Невозможно решить - недостаточно данных')

        elif choice == 'K':
            a = 1
            list = input('Что дано?\n')
            list = list.split(' ')
            for x in list:
                if x == 'I':
                    for xx in list:
                        if xx == 'i':
                            I = I_convert_in('I')
                            i = int(input('Чему равно i?\n'))
                            print(f'K = {round(I / i)}')
                            return
                    if ('i' not in list) and ('N' not in list):
                        print('Невозможно решить')
                        return
            for x in list:
                if x == 'I':
                    for xx in list:
                        if xx == 'N':
                            N = int(input('Чему равно N?\n'))
                            I = I_convert_in('I')
                            print(f'K = {round(math.log(N, 2)) / I} ')
                            return
                    if 'N' not in list:
                        print('Невозможно решить')
                        return
            print('Невозможно решить - недостаточно данных')
        else:
            print('Что найти?')
            choice = input()


def sound():
    print('Что найти?')
    choice = input()
    a = 0
    while a != 1:
        if choice == 'l':
            a = 1
            list = input('Что дано?\n')
            list = list.split(' ')
            for x in list:
                if x == 'i':
                    for xx in list:
                        if xx == 'f':
                            for xxx in list:
                                if xxx == 't':
                                    for xxxx in list:
                                        if xxxx == 'n':
                                            i = int(input('Чему равно i?\n'))
                                            f = int(input('Чему равно f?\n'))
                                            t = int(input('Чему равно t?\n'))
                                            n = int(input('Чему равно n?\n'))
                                            l = i * f * t * n
                                            print(I_convert_out('l', l))
                                            return
                if x == 'N':
                    for xx in list:
                        if xx == 'f':
                            for xxx in list:
                                if xxx == 't':
                                    for xxxx in list:
                                        if xxxx == 'n':
                                            N = int(input('Чему равно N?\n'))
                                            i = round(math.log(N, 2))
                                            f = int(input('Чему равно f?\n'))
                                            t = int(input('Чему равно t?\n'))
                                            n = int(input('Чему равно n?\n'))
                                            l = i*f*t*n
                                            print(I_convert_out('l', l))
                                            return
            print('Невозможно решить - недостаточно данных')

        elif choice == 'n':
            a = 1
            list = input('Что дано?\n')
            list = list.split(' ')
            for x in list:
                if x == 'i':
                    for xx in list:
                        if xx == 'f':
                            for xxx in list:
                                if xxx == 't':
                                    for xxxx in list:
                                        if xxxx == 'l':
                                            i = int(input('Чему равно i?\n'))
                                            f = int(input('Чему равно f?\n'))
                                            t = int(input('Чему равно t?\n'))
                                            l = I_convert_in('l')
                                            print(f'n = {l/(f*t*i)}')
                                            return
                if x == 'N':
                    for xx in list:
                        if xx == 'f':
                            for xxx in list:
                                if xxx == 't':
                                    for xxxx in list:
                                        if xxxx == 'n':
                                            N = int(input('Чему равно N?\n'))
                                            i = round(math.log(N, 2))
                                            f = int(input('Чему равно f?\n'))
                                            t = int(input('Чему равно t?\n'))
                                            l = I_convert_in('l')
                                            print(f'n = {l / (f * t * i)}')
                                            return
            print('Невозможно решить - недостаточно данных')

        elif choice == 't':
            a = 1
            list = input('Что дано?\n')
            list = list.split(' ')
            for x in list:
                if x == 'i':
                    for xx in list:
                        if xx == 'f':
                            for xxx in list:
                                if xxx == 'n':
                                    for xxxx in list:
                                        if xxxx == 'l':
                                            i = int(input('Чему равно i?\n'))
                                            f = int(input('Чему равно f?\n'))
                                            n = int(input('Чему равно n?\n'))
                                            l = I_convert_in('l')
                                            print(f't = {l/(f*n*i)}')
                                            return
                if x == 'N':
                    for xx in list:
                        if xx == 'f':
                            for xxx in list:
                                if xxx == 'n':
                                    for xxxx in list:
                                        if xxxx == 'n':
                                            N = int(input('Чему равно N?\n'))
                                            i = round(math.log(N, 2))
                                            f = int(input('Чему равно f?\n'))
                                            n = int(input('Чему равно n?\n'))
                                            l = I_convert_in('l')
                                            print(f't = {l / (f * n * i)}')
                                            return

        elif choice == 'f':
            a = 1
            list = input('Что дано?\n')
            list = list.split(' ')
            for x in list:
                if x == 'i':
                    for xx in list:
                        if xx == 'f':
                            for xxx in list:
                                if xxx == 'n':
                                    for xxxx in list:
                                        if xxxx == 'l':
                                            i = int(input('Чему равно i?\n'))
                                            t = int(input('Чему равно t?\n'))
                                            n = int(input('Чему равно n?\n'))
                                            l = I_convert_in('l')
                                            print(f'f = {l / (t * n * i)}')
                                            return
                if x == 'N':
                    for xx in list:
                        if xx == 'f':
                            for xxx in list:
                                if xxx == 'n':
                                    for xxxx in list:
                                        if xxxx == 'n':
                                            N = int(input('Чему равно N?\n'))
                                            i = round(math.log(N, 2))
                                            t = int(input('Чему равно t?\n'))
                                            n = int(input('Чему равно n?\n'))
                                            l = I_convert_in('l')
                                            print(f'f = {l / (t * n * i)}')
                                            return

        elif choice == 'i':
            a = 1
            list = input('Что дано?\n')
            list = list.split(' ')
            for x in list:
                if x == 'l':
                    for xx in list:
                        if xx == 'f':
                            for xxx in list:
                                if xxx == 'n':
                                    for xxxx in list:
                                        if xxxx == 'l':
                                            f = int(input('Чему равно f?\n'))
                                            t = int(input('Чему равно t?\n'))
                                            n = int(input('Чему равно n?\n'))
                                            l = I_convert_in('l')
                                            print(f'i = {l / (t * n * f)}')
                                            return
                if x == 'N':
                    N = int(input('Чему равно N?\n'))
                    print(f'i = {round(math.log(N, 2))} бит')
                    return
            print('Невозможно решить - недостаточно данных')


        else:
            print('Что найти?')
            choice = input()

def main():
    print('╔═══╗╔═══╗╔╗╔╗╔╗╔══╗ ╔══╗╔══╗\n'
          '║╔═╗║║╔══╝║║║║║║║╔╗║ ║╔╗║║╔╗║\n'
          '║╚═╝║║╚══╗║║║║║║║╚╝║ ║║║║║╚╝║\n'
          '║╔══╝║╔══╝║║║║║║║╔╗║ ║║║║║╔╗║\n'
          '║║   ║╚══╗║╚╝╚╝║║║║║╔╝║║║║║║║\n'
          '╚╝   ╚═══╝╚════╝╚╝╚╝╚═╝╚╝╚╝╚╝\n')
    print('Вас приветствует РЕШАЛА - Решатель для ЕГЭ и Школы Автоматизированный - Логический Алгоритм')
    print('Какой тип задачи решить: 1) Кодирование информации 2) Размер изображения '
          '3) Размер звукового файла')
    a = 0
    b = input()
    while a != 1:
        if b == '1':
            a += 1
            inf_encoding()
        elif b == '2':
            a += 1
            image()
        elif b == '3':
            a += 1
            sound()
        else:
            print('Невозможный тип задачи')
            b = input()


main()
