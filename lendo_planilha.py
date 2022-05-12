import openpyxl

#carregando arquivo
book = openpyxl.load_workbook('Frutas.xlsx')

#selecionando uma página
frutas_page = book['Frutas']

#imprimindo os dados de cadas linha
for rows in frutas_page.iter_rows(min_row=2, max_row=5):
    print(rows[0].value, rows[1].value,rows[2].value)