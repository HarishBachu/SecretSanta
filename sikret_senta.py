import random 
import smtplib
from email.mime.multipart import MIMEMultipart as MIMEMultipart
from email.mime.text import MIMEText 
from email.mime.image import MIMEImage 
from tqdm import tqdm, trange

sender = "<add sender email>"
sender_pass = "<add sender email password>"        #Application Password may be necessary

#Feel free to message these guys xDD
receivers = {
    "Rohan" : 'rohanjijju@gmail.com', 
    "Kaustubh" : 'kaustubhpsonawane@gmail.com', 
    "Manas" : 'manasdtrivedi@gmail.com', 
    "Sam" : 'samsabu2000@gmail.com',
    "Harish" : "bachuharish577@gmail.com"
}

def send_email(receiver, beneficiary):
    message = MIMEMultipart("alternative") 
    message["From"] = sender 
    message["To"] = receivers[receiver] 
    message["subject"] = "Your Secret Santa name is..."

    body = f"""
        <h1 style="font-size:40px">Secret Santa!!!</h1>
        <p style="font-size:18px"> 
            Henlo Fren!!! <br>
            Good Afternoon <br>  
            Your Secret Santa name is: {beneficiary}
            <br><br>
            For maximum hilarious, keep your name mysterious :) 
            <br> 
            Merry jingle sounds or whatever
            <br><br> 
            Regards, <br>
            Your friendly neighborhood spiderman. 
        </p>
        
    """ 
    # <img src="C:\\Users\\bachu\\Downloads\\santa.png" alt="trial"></img>    
    html_body = MIMEText(body, "html")
    message.attach(html_body) 

    # # ###########Error
    fp = open("C:\\Users\\bachu\\Downloads\\office-christmas-giphy1.gif", 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()
    message.attach(msgImage)
    # # ###################
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    s.starttls()
    s.login(sender, sender_pass) 

    s.sendmail(sender, receivers[receiver], message.as_string())
    s.quit()

def main():

    santas = list(receivers.keys())
    while True:
        flag = 0 
        santees = santas.copy()
        random.shuffle(santees) 
        for idx in range(len(santas)):
            if santas[idx] == santees[idx]: 
                flag = 1 
        if flag == 0:
            break 
        
    # send_email("Harish", "Harish") 
    for idx in trange(len(santas), desc="Sending Emails", ncols=100):
        santa = santas[idx]
        santee = santees[idx] 
        send_email(santa, santee)

if __name__ == "__main__":
    main()