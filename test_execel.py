import gspread

gc = gspread.service_account(filename='conf.json')

table = gc.open_by_url(
    'https://docs.google.com/spreadsheets/d/1XGTMsbrI2T5p_xhmEV3afAFno3u1y9k7kWqUuzuOkrA/edit?gid=0#gid=0')

worksheet = table.worksheet("teachers")

print(worksheet.get_all_values())
