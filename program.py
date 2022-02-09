from ctypes import alignment
import json
from fpdf import FPDF

#creating pdf file
pdf = FPDF ('P', 'cm', 'A4')
pdf.add_page()
