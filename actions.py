import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)

# initializes sheet like a sheet in google
sheet = client.open("vurdering").sheet1

'''adds student at bottom of list
    param : string name
'''

def new_stud(name):
    #get all data
    data = sheet.get_all_records()
    #get length of list
    num_rows = len(data) + 1
    #print(num_rows)
    name_list = []
    name_list.append(name.upper())
    #print(name_list)
    sheet.insert_row(name_list, num_rows +1)


'''
    Inserts name and sorts the list
    so that the sheet is still alphabetical
    param : string name
'''
def insert_stud_alphabetical(name):
    name_list = sheet.col_values(1)
    name_list.append(name.upper())
    name_list = name_list[1:]
    new_stud(name)
    stud_data = make_dict(name_list)
    name_list = sorted(name_list)

    for n in range(len(name_list)):
        name = name_list[n]
        print(f'Found name :  {name}')
        sheet.delete_row(n+2)
        sheet.update_cell(n +2, 1, name)
        cell = sheet.find(name)
        for i in range(len(stud_data[name])):
            sheet.update_cell(cell.row, i +2, stud_data[name][i])

def get_review_from(stud, review):
     pass


'''
    makes a dictionary of the studentlist, student name as key
    param : list of string names
'''
def make_dict(name_list):
    dict = {}
    for name in name_list:
        cell = sheet.find(name)
        stud_data = sheet.row_values(cell.row)
        dict[name] = stud_data[1:]
    return dict

'''
    Find student in register
    param : string student name
'''
def get_stud(name):
    try:
        cell = sheet.find(name.upper())
        print(f"Fant {name} i rad {cell.row} og kol {cell.col}")
        value_col = sheet.row_values(cell.row)


    except gspread.exceptions.CellNotFound:
        print('--------------------------\n fant ikke navn\n')


'''
    Find review in register
    param : find
'''
def get_tests_grades_review(tgr):
    try:
        cell = sheet.find(tgr.upper())
        print(f"Fant {tgr} i rad {cell.row} og kol {cell.col}")
        students = sheet.col_values(1)
        tgr_col = sheet.col_values(cell.col)
        view = []
        for stud in students:
            print(stud)
            #TODO print student, review side ny side
            #for t in tgr_col[1:]:
            #    print(t)


    except gspread.exceptions.CellNotFound:
        print('--------------------------\n fant ikke navn\n')


if __name__=="__main__":
    #new_stud('Max')
    #get_stud_records('Doffen')
    get_tests_grades_review("review 1")
