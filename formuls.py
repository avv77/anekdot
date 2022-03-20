
def list_faile(path):
    jokes_vovochka = []
    line_complit = ''

    f = open(path, 'r', encoding='cp1251')
    lines = f.readlines()
    f.close()
    for line in lines:
        if line != '\n':
            line_complit = line_complit + ' ' + line
        else:
            jokes_vovochka.append(line_complit)
            line_complit = ''
    return jokes_vovochka


def list_faile_2():
    jokes_medezina = []

    f = open('file_base/anekdoty/medezina.txt', 'r', encoding='utf8')
    lines = f.readlines()
    f.close()
    for line in lines:
        jokes_medezina.append(line)
    return jokes_medezina


def list_faile_3():
    jokes_ohota = []
    line_complit = ''

    f = open('file_base/anekdoty/ohota_otdih.txt', 'r', encoding='utf8')
    lines = f.readlines()
    f.close()
    for line in lines:
        if line[0] != '*':
            line_complit = line_complit + ' ' + line
        else:
            jokes_ohota.append(line_complit)
            line_complit = ''
    return jokes_ohota


def list_faile_4(path):
    jokes_rjevskiy = []
    line_complit = ''

    f = open(path, 'r', encoding='utf8')
    lines = f.readlines()
    f.close()
    for line in lines:
        if line[0] != '\n':
            line_complit = line_complit + ' ' + line
        else:
            jokes_rjevskiy.append(line_complit)
            line_complit = ''
    return jokes_rjevskiy
