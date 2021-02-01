import openpyxl
from groups import mass_of_group
# читаем excel-файл
wb = openpyxl.load_workbook("rasp.xlsx")
# получаем активный лист
sheet = wb.active

def name_of_group(i):
    sn=mass_of_group[i].name_of_group+str(22)
    name_ = str(sheet[sn].value)
    name_ = name_.replace('\n','\n\t')
    return name_

def output_groups():
    i = 0
    while i<len(mass_of_group):
        print(str(i+1) + '.\t'+name_of_group(i))
        i=i+1

def choose_group():
    output_groups()
    numberj=0
    while numberj==0:
        numberj = int(input('Выберите свою группу: '))
        if numberj > 0 and numberj <= len(mass_of_group):
            return numberj-1
        else:
            numberj=0

number_of_group = choose_group()

def name_of_group_():
    sn=mass_of_group[number_of_group].name_of_group+str(22)
    name_ = str(sheet[sn].value)
    name_ = name_.replace('\n','\n\t')
    return name_

def get_day_of_week(i):
    sd='AW'+str(i)
    day = str(sheet[sd].value)
    return day

def get_time(i):
    st='AX'+str(i)
    time = str(sheet[st].value)
    time = time.replace(' ','')
    return time

def get_type(i):
    sty=mass_of_group[number_of_group].type_+str(i)
    type_ = str(sheet[sty].value)
    if type_ == 'None':
        return ''
    return type_

def get_name(i):
     s=mass_of_group[number_of_group].name+str(i)
     name = str(sheet[s].value)
     name = name.replace('\n',' ')
     return name

def get_cabinet(i):
    sc=mass_of_group[number_of_group].cabinet+str(i)
    cabinet = str(sheet[sc].value)
    cabinet = cabinet.replace('\n','\n\t\t\t\t')
    if cabinet == 'None':
        return 'Teams'
    else: return cabinet

def get_prepod(i):
    sp=mass_of_group[number_of_group].prepod+str(i)
    prepod = str(sheet[sp].value)
    prepod = prepod.replace('\n','\n\t\t')
    if prepod == 'None':
        return ''
    else: return prepod

def check_not_none(get_cell):
    if get_cell != "None":
        return True
    else:
        return False

def output_lesson(i):
    if get_name(i) == 'день самостоятельной подготовки':
        print('день самостоятельной подготовки')
    elif check_not_none(get_name(i)) == True:
        all = get_time(i)+':\t'+get_prepod(i)+'\t'+get_cabinet(i)+'\t'+get_type(i)+'\t'+get_name(i)
        print(all)
    
def output_week(i):
    if i == 24:
        print('\n\t'+get_day_of_week(i))
        j=i
        while j<40:
            output_lesson(j)
            j=j+1
    elif i == 40:
        print('\n\t'+get_day_of_week(i))
        j=i
        while j<53:
            output_lesson(j)
            j=j+1
    elif i == 53:
        print('\n\t'+get_day_of_week(i))
        j=i
        while j<67:
            output_lesson(j)
            j=j+1
    elif i == 67:
        print('\n\t'+get_day_of_week(i))
        j=i
        while j<79:
            output_lesson(j)
            j=j+1
    elif i == 79:
        print('\n\t'+get_day_of_week(i))
        j=i
        while j<93:
            output_lesson(j)
            j=j+1
    elif i == 93:
        print('\n\t'+get_day_of_week(i))
        j=i
        while j<99:
            output_lesson(j)
            j=j+1

def output_week_all():
    print('\n')
    name = name_of_group_().replace('\n','\n\t\t')
    print('\t\t\t'+name)
    i = 24
    while i<99:
        output_week(i)
        i=i+1
    print('\n')