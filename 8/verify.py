import pdfkit

# configuring pdfkit to point to our installation of wkhtmltopdf
config = pdfkit.configuration(wkhtmltopdf=r"C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")

# converting url to pdf file
pdfkit.from_url('https://www.javatpoint.com/tic-tac-toe-in-python', 'output2.pdf', configuration=config)