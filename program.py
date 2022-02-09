from ctypes import alignment
import json
from fpdf import FPDF

#creating pdf file
pdf = FPDF ('P', 'cm', 'A4')
pdf.add_page()

#reading json file
resume_details = open('details.json', 'r')
details = resume_details.read()
information = json.loads(details)

#for looping informations
for i in information:
    pdf.set_font('times','B',18)
    pdf.cell(10, 1, f"{i['name']}", align="C", ln= 1),