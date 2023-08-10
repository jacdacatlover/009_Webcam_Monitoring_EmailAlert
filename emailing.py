import smtplib
from email.message import EmailMessage
from PIL import Image


SENDER = "jac4code@gmail.com"
PASSWORD = "xqlqefuuaouwgvau"
RECEIVER = "jac4code@gmail.com"
def get_image_type(image_path):
    with Image.open(image_path) as img:
        return img.format

def send_email(image_path):
    print("send email started")
    email_message = EmailMessage()
    email_message["Subject"] = "New customer showed up!"
    email_message.set_content("Hey, we just saw a new customer")

    with open(image_path, "rb") as file:
        content = file.read()
    email_message.add_attachment(content, maintype="image", subtype=get_image_type(image_path))

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER,PASSWORD)
    gmail.sendmail(SENDER, RECEIVER, email_message.as_string())
    gmail.quit()
    print("send email ended")

if __name__== "__main__":
    send_email(image_path="images/ 17.png")