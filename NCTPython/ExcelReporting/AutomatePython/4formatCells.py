from openpyxl import load_workbook
from openpyxl.styles import Font

wb = load_workbook('3.apply-formulas-report.xlsx')
sheet = wb['Report']

# Add format
sheet['A1'] = 'Sales Report'
sheet['A2'] = 'January'
sheet['A1'].font = Font('Arial', bold=True, size=20)
sheet['A2'].font = Font('Arial', bold=True, size=10)

wb.save('4.report_january.xlsx')
