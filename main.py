import pandas as pd
from fpdf import FPDF


pdf = FPDF(orientation="P",
           unit="mm",
           format="A4")
pdf.set_auto_page_break(auto=False, margin=0)
df = pd.read_csv("topics.csv", sep=",")
# print(df.head())
for index, row in df.iterrows():
    pages = int(row['Pages'])
    topic = row['Topic']

    pdf.add_page()

    # Set the header
    pdf.set_font(family="Arial", style="B", size=24)
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0, h=12, txt=topic,
             align="L", ln=1)
    pdf.line(10,21,200,21)

    # Set the footer
    pdf.ln(265)
    pdf.set_font(family="Arial", style="I", size=8)
    pdf.set_text_color(180,180,180)
    pdf.cell(w=0, h=8, txt=topic, align="R")

    for page in range(pages-1):
        pdf.add_page()

        # Set the footer
        pdf.ln(277)
        pdf.set_font(family="Arial", style="I", size=8)
        pdf.set_text_color(180,180,180)
        pdf.cell(w=0, h=8, txt=topic, align="R")


pdf.output("output.pdf")