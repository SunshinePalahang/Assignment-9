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
    pdf.set_font('times','B',20)
    pdf.cell(11, 1, f"{i['name']}", align="C", ln = 1),
    pdf.set_font('times', '', 14)
    pdf.cell(8.5, .5, f"{i['phone']}",ln = 1)
    pdf.cell(8.5, .5, f"{i['email']}",ln = 1)
    pdf.set_font('times', 'B', 16)
    pdf.cell(10, 2, "Career Objective", ln = 1 )
    pdf.set_font('times', '', 12)
    pdf.cell(6, 0.5, f"{i['summary']}", ln = 1)
    pdf.cell(6, 0.5, f"{i['summary2']}", ln = 1)
    pdf.cell(6, 0.5, f"{i['summary3']}", ln = 1)
    pdf.set_font('times', 'B', 16)
    pdf.cell(10, 2, "Personal Vitae", ln = 1 )
    pdf.set_font('times', '', 12)
    pdf.cell(6, 0.65, f"Birthday: {i['birthday']}", ln = 1)
    pdf.cell(6, 0.65, f"Father's Name: {i['father']}", ln = 1)
    pdf.cell(6, 0.65, f"Occupation: {i['foccupation']}", ln = 1)
    pdf.cell(6, 0.65, f"Mother's Name: {i['mother']}", ln = 1)
    pdf.cell(6, 0.65, f"Occupation: {i['occupation']}", ln = 1)
    pdf.cell(6, 0.65, f"Religion: {i['religion']}", ln = 1)
    pdf.cell(6, 0.65, f"Height: {i['height']}", ln = 1)
    pdf.cell(6, 0.65, f"Weight: {i['weight']}", ln = 1)
    pdf.set_font('times', 'B', 16)
    pdf.cell(10, 2, "Hard Skills", ln = 1)
    pdf.set_font('times', '', 12)
    pdf.cell(6, 0.5, f"{i['hard'],}", ln = 1)
    pdf.set_font('times', 'B', 16)
    pdf.cell(10, 2, "Soft Skills", ln = 1)
    pdf.set_font('times', '', 12)
    pdf.cell(6, 0.5, f"{i['soft'],}", ln = 1)
    pdf.set_font('times', 'B', 16)
    pdf.cell(10, 2, "Educational Background", ln = 1)
    pdf.set_font('times', '', 12)
    pdf.cell(6, 0.65, f"School: {i['school']}", ln = 1)
    pdf.cell(6, 0.65, f"Year Level: {i['yearlevel']}", ln = 1)
    pdf.cell(6, 0.65, f"Academic Year: {i['acadyear']}", ln = 1)


pdf.output('PALAHANG_SUNSHINE RICHMER.pdf')