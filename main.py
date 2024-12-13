import pandas as pd
from fpdf import FPDF


pdf = FPDF(orientation="P",
           unit="mm",
           format="A4")

df = pd.read_csv("topics.csv", sep=",")
# print(df.head())
for index, row in df.iterrows():
    pages = int(row['Pages'])
    topic = row['Topic']
    for page in range(pages):
        pdf.add_page()
        pdf.set_font(family="Arial", style="B", size=24)
        pdf.set_text_color(100,100,100)
        pdf.cell(w=0, h=12, txt=topic,
                 align="L", ln=1)
        pdf.line(10,21,200,21)


pdf.output("output.pdf")