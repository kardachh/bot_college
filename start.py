import openpyxl
from helper import output_lesson, check_not_none,get_cell
i = 24
while i<99:
    if check_not_none(get_cell(i)) == True:
        print(output_lesson(i))
    i=i+1
    