import openpyxl
# читаем excel-файл
wb = openpyxl.load_workbook("D://code//bot_college//rasp.xlsx")
# получаем активный лист
sheet = wb.active
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
        all = '\t'+get_time(i)+'\n'+get_cell(i)+'\n\n'
        return all