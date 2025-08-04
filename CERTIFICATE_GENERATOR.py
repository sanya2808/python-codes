# import pandas as pd # type: ignore
# from PyPDF2 import PdfReader, PdfWriter # type: ignore
# from reportlab.pdfgen import canvas # type: ignore
# from reportlab.lib.pagesizes import letter # type: ignore
# import smtplib
# import os
# from email.message import EmailMessage

# from reportlab.pdfbase import pdfmetrics
# from reportlab.pdfbase.ttfonts import TTFont

# # Register your custom font
# # pdfmetrics.registerFont(
# #     TTFont("Baskerville Old Face", "fonts/Baskerville Old Face.ttf")
# # )


# # Use it in your canvas
# #c.setFont("MonsieurLaDoulaise", 30)



# # === CONFIGURATION ===
# BLANK_CERTIFICATE = "certificate.pdf"
# EXCEL_FILE = "CG.xlsx"
# OUTPUT_FOLDER = "certificates"
# SENDER_EMAIL = "singhsanya2808@gmail.com"
# SENDER_PASSWORD = "jvbz innu prog xxtd"  # Use an App Password if using Gmail
# SUBJECT = "Your Certificate"
# BODY = "Dear {name},\n\nPlease find your certificate attached.\n\nRegards,\nTeam Sanya!;)"

# # === STEP 1: Load Data ===
# df = pd.read_excel(EXCEL_FILE)
# print(df.columns.tolist())

# # Create output folder
# os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# # === STEP 2: Create Personalized Certificate ===
# def create_certificate(name):
#     # Temp canvas to draw name
#     # c = canvas.Canvas("temp.pdf", pagesize=letter)
#     # c.setFont("Baskerville Old Face", 30)
#     # c.drawCentredString(320, 180, name)  # Adjust coordinates as needed
#     # c.save()

#    from reportlab.lib.pagesizes import A4  # Make sure this is present

# def create_certificate(name):
#     c = canvas.Canvas("temp.pdf", pagesize=A4)

#     # You can use built-in font or register a custom one
#     try:
#         pdfmetrics.registerFont(TTFont("Baskerville Old Face", "fonts/Baskerville Old Face.ttf"))
#         c.setFont("Baskerville Old Face", 30)
#     except:
#         c.setFont("Helvetica-Bold", 30)

#     # Centered horizontally (A4 = 595pt wide), about 490pt from the bottom
#     c.drawCentredString(297.5, 490, name)
#     c.save()

#     cert_reader = PdfReader(BLANK_CERTIFICATE)
#     overlay_reader = PdfReader("temp.pdf")
    
#     writer = PdfWriter()
#     page = cert_reader.pages[0]
#     page.merge_page(overlay_reader.pages[0])
#     writer.add_page(page)
    
#     output_path = f"{OUTPUT_FOLDER}/{name.replace(' ', '_')}_certificate.pdf"
#     with open(output_path, "wb") as f_out:
#         writer.write(f_out)
    
#     os.remove("temp.pdf")
#     return output_path


# # === STEP 3: Send Email ===
# def send_email(name, email, file_path):
#     msg = EmailMessage()
#     msg["Subject"] = SUBJECT
#     msg["From"] = SENDER_EMAIL
#     msg["To"] = email
#     msg.set_content(BODY.format(name=name))
    
#     # Attach PDF
#     with open(file_path, "rb") as f:
#         file_data = f.read()
#         file_name = os.path.basename(file_path)
#     msg.add_attachment(file_data, maintype="application", subtype="pdf", filename=file_name)
    
#     # Send via SMTP
#     with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
#         smtp.login(SENDER_EMAIL, SENDER_PASSWORD)
#         smtp.send_message(msg)

# # === STEP 4: Process All ===
# for _, row in df.iterrows():
#     name = row["Name"]
#     email = row["Email"]
#     print(f"Processing {name}...")
    
#     cert_path = create_certificate(name)
#     send_email(name, email, cert_path)

# print("All certificates created and emailed successfully.")






import pandas as pd  # type: ignore
from PyPDF2 import PdfReader, PdfWriter  # type: ignore
from reportlab.pdfgen import canvas  # type: ignore
from reportlab.lib.pagesizes import A4  # <-- A4 added here
import smtplib
import os
from email.message import EmailMessage

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# === CONFIGURATION ===
BLANK_CERTIFICATE = "certificate.pdf"
EXCEL_FILE = "CG.xlsx"
OUTPUT_FOLDER = "certificates"
SENDER_EMAIL = "singhsanya2808@gmail.com"
SENDER_PASSWORD = "jvbz innu prog xxtd"  # Use an App Password if using Gmail
SUBJECT = "Your Certificate"
BODY = "Dear {name},\n\nPlease find your certificate attached.\n\nRegards,\nTeam Sanya! ;)"

# === STEP 1: Load Data ===
df = pd.read_excel(EXCEL_FILE)
print(df.columns.tolist())

# Create output folder
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# === STEP 2: Create Personalized Certificate ===
def create_certificate(name):
    c = canvas.Canvas("temp.pdf", pagesize=A4)

    # Try to register custom font, fallback if missing
    try:
        pdfmetrics.registerFont(TTFont("Baskerville Old Face", "fonts/Baskerville Old Face.ttf"))
        c.setFont("Baskerville Old Face", 30)
    except:
        c.setFont("Helvetica-Bold", 30)

    # Draw the name centered on the certificate (approx coordinates)
    c.drawCentredString(158, 162, name)
 # A4 width = 595pt
    c.save()

    # Merge the overlay with the original certificate
    cert_reader = PdfReader(BLANK_CERTIFICATE)
    overlay_reader = PdfReader("temp.pdf")
    
    writer = PdfWriter()
    page = cert_reader.pages[0]
    page.merge_page(overlay_reader.pages[0])
    writer.add_page(page)
    
    output_path = f"{OUTPUT_FOLDER}/{name.replace(' ', '_')}_certificate.pdf"
    with open(output_path, "wb") as f_out:
        writer.write(f_out)
    
    os.remove("temp.pdf")
    return output_path

# === STEP 3: Send Email ===
def send_email(name, email, file_path):
    msg = EmailMessage()
    msg["Subject"] = SUBJECT
    msg["From"] = SENDER_EMAIL
    msg["To"] = email
    msg.set_content(BODY.format(name=name))
    
    # Attach PDF
    with open(file_path, "rb") as f:
        file_data = f.read()
        file_name = os.path.basename(file_path)
    msg.add_attachment(file_data, maintype="application", subtype="pdf", filename=file_name)
    
    # Send via SMTP
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(SENDER_EMAIL, SENDER_PASSWORD)
        smtp.send_message(msg)

# === STEP 4: Process All ===
for _, row in df.iterrows():
    name = row["Name"]
    email = row["Email"]
    print(f"Processing {name}...")
    
    cert_path = create_certificate(name)
    send_email(name, email, cert_path)

print("All certificates created and emailed successfully.")
