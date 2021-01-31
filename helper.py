import openpyxl
import groups
# читаем excel-файл
wb = openpyxl.load_workbook("rasp.xlsx")
# получаем активный лист
sheet = wb.active

def get_day_of_week(i):
    sd='AW'+str(i)
    day = str(sheet[sd].value)
    return day

def get_time(i):
    st='AX'+str(i)
    time = str(sheet[st].value)
    time = time.replace(' ','')
    return time

def get_name(i):
     s='AS'+str(i)
     name = str(sheet[s].value)
     name = name.replace('\n',' ')
     return name

def get_cabinet(i):
    sc='AV'+str(i)
    cabinet = str(sheet[sc].value)
    if cabinet == 'None':
        return ''
    else: return cabinet

def get_prepod(i):
    sp='AU'+str(i)
    prepod = str(sheet[sp].value)
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
        all = get_time(i)+':\t'+get_prepod(i)+'\t'+get_name(i)+'\t'+get_cabinet(i)
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
    i = 24
    while i<99:
        output_week(i)
        i=i+1

