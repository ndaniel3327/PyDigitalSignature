from reportlab.pdfgen import canvas

def generate_pdf(input_text, output_file):
    c = canvas.Canvas(output_file)
    c.drawString(50, 750, input_text)
    c.save()

input_text = "Ma numbesc Danutz!"
output_file = "ThreeSigTest.pdf"
generate_pdf(input_text, output_file)
print("PDF generated successfully:", output_file)