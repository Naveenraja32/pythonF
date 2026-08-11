import smtplib,mimetypes,os
from email.message import EmailMessage
email='naveenrajaspt39@gmail.com'
econtainer=EmailMessage()
econtainer['From'] = email
econtainer['To'] = email
econtainer['Subject'] = "Test Email"
econtainer.set_content("こんにちは、これはテストメールです。")  # Japanese for "Hello, this is a test email."

files= r'C:\Users\DELL\OneDrive\Desktop\GH.jpg'  # Path to the file you want to attach
if files:
    with open(files, 'rb') as f:
        d=f.read()
        fname=f.name
        ftype=mimetypes.guess_type(fname)[0]
        if ftype:maintype,subtype=ftype.split('/', 1)
        else:maintype,subtype='application','octet-stream'
        econtainer.add_attachment(d, maintype=maintype, subtype=subtype, filename=os.path.basename(fname))
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    with open(r'C:\Users\DELL\OneDrive\Documents\pwd.txt', 'r') as f:
        app_pwd = f.read().strip()
    smtp.login(email, app_pwd)  # Use an app password instead of your regular password
    smtp.send_message(econtainer)
print("Email sent successfully.")