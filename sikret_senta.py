import random 
import smtplib
from email.mime.multipart import MIMEMultipart as MIMEMultipart
from email.mime.text import MIMEText 
from email.mime.image import MIMEImage 
from tqdm import tqdm, trange

sender = "<user name>"
sender_pass = "<user app password>"        #Application Password may be necessary

#Feel free to message these guys xDD
receivers = {
    "Jijju" : 'rohanjijju@gmail.com', 
    "K-man" : 'kaustubhpsonawane@gmail.com', 
    "Allwin" : 'aldsouza4@gmail.com', 
    "Sam" : 'samsabu2000@gmail.com',
    "Bachu" : 'bachuharish577@gmail.com', 
    "Warke" : 'shrvu36@gmail.com'
}

def send_email(receiver, beneficiary):
    message = MIMEMultipart("alternative") 
    message["From"] = sender 
    message["To"] = receivers[receiver] 
    message["subject"] = "Your Secret Santa name is..."

    body = f"""
        <h1 style="font-size:40px">Ah shit, here we go again.</h1>
        <p style="font-size:18px"> 
            Felicitations fellow fucker! <br>  
            Your Secret Santa name is: {beneficiary} <br>
            Email ID : {receivers[beneficiary]}
            <br><br>
            Disclose your name and risk fatality. John Wick style. <br>
            Moye Moye <br>
            <br> 
            'tis the season to be silly<br>
            Fa la la la la<br>
            la la la laaaa
            <br><br> 
            Regards, <br>
            Bhupendra Jogi. 
        </p>
        
    """     
    html_body = MIMEText(body, "html")
    message.attach(html_body) 

    s = smtplib.SMTP('smtp.gmail.com', 587) 
    s.starttls()
    s.login(sender, sender_pass) 

    s.sendmail(sender, receivers[receiver], message.as_string())
    s.quit()

def main():

    santas = list(receivers.keys())
    while True:
        flag = 0
        print("Shuffling...") 
        santees = santas.copy()
        random.shuffle(santees) 
        for idx in range(len(santas)):
            if santas[idx] == santees[idx]: 
                flag = 1 
        if flag == 0:
            break 
    print("Shuffled!")

    # send_email("Harish", "Harish") 
    for idx in trange(len(santas), desc="Sending Emails", ncols=100):
        santa = santas[idx]
        santee = santees[idx] 
        send_email(santa, santee)

if __name__ == "__main__":
    main()