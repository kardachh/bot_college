import openpyxl
# читаем excel-файл
wb = openpyxl.load_workbook("rasp.xlsx")
# получаем активный лист
sheet = wb.active

days_of_week = ['Понедельник','Вторник','Среда','Четверг','Пятница','Суббота']

def get_time(i):
    st='AX'+str(i)
    time = str(sheet[st].value)
    return time

def get_cell(i):
     s='AS'+str(i)
     cell = str(sheet[s].value)
     return cell

def check_not_none(get_cell):
    if get_cell != "None":
        return True
    else:
        return False

def output_lesson(i):
    if check_not_none(get_cell(i)) == True:
        all = get_time(i)+':\t'+get_cell(i)
        print(all)

def output_day(i):
    if i == 24:
        print('\n\t'+days_of_week[0])
        j=i
        while j<40:
            output_lesson(j)
            j=j+1
    elif i == 40:
        print('\n\t'+days_of_week[1])
        j=i
        while j<53:
            output_lesson(j)
            j=j+1
    elif i == 53:
        print('\n\t'+days_of_week[2])
        j=i
        while j<67:
            output_lesson(j)
            j=j+1
    elif i == 67:
        print('\n\t'+days_of_week[3])
        j=i
        while j<79:
            output_lesson(j)
            j=j+1
    elif i == 79:
        print('\n\t'+days_of_week[4])
        j=i
        while j<93:
            output_lesson(j)
            j=j+1
    elif i == 93:
        print('\n\t'+days_of_week[5])
        j=i
        while j<99:
            output_lesson(j)
            j=j+1