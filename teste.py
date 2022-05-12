import openpyxl

book = openpyxl.Workbook()

book.create_sheet('Frutas')

frutas_page = book['Frutas']

frutas_page.append(['Banana', '5', 'R$ 10,00'])
frutas_page.append(['Maçã', '7', 'R$ 16,00'])
frutas_page.append(['Abacate', '5', 'R$ 10,00'])
frutas_page.append(['Tangerina', '3', 'R$ 20,00'])

book.save('Frutas.xlsx')