import re
import smtplib
import ssl
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import date


def get_response(user_intput: str) -> str:
    lowered: str = user_intput.lower()
    data = {1: "asamyukthan@gmail.com", 2: "asamyukthan2@gmail.com",
            3: "asamyukthan3@gmail.com", 4: "asamyukthan2gmail.com"}
    if user_intput.startswith('absent'):
        roll = user_intput[7:-2]
        hou = user_intput[-1]
        res = re.split(',', roll)
        res = (list(map(int, res)))
        i = 0
        lt = ""
        while i < len(res):
            i = i+1
            for i in res:
                lt = lt+","+data[i]
        rec = lt[1:]
        listToStr = ' '.join(map(str, rec))
        listToStr = listToStr.replace(" ", "")
        print(listToStr)
        body = f"""
Good day,
                        
I trust this email finds you in good health.

I am writing to inform you that your ward was absent for the class on date of {date.today()} for {hou} hours. It is essential to bring this to your attention, as regular attendance plays a crucial role in ensuring academic success.

If there is a specific reason for your ward's absence, please feel free to share it with me. Staying informed about any challenges students may be facing is vital for us to provide the necessary support.

In the meantime, I would appreciate it if you could ensure your ward catches up on any missed assignments or class material. Additionally, if there were any announcements or important information shared during the class, please make sure [he/she] is aware of it.

If there are ongoing concerns or if additional support is required, please don't hesitate to reach out. We are here to work together to ensure the academic success of the students.

Thank you for your understanding and cooperation.
                        
Best regards,"""
        msg = MIMEMultipart()
        msg['From'] = "spam67182@gmail.com"
        msg['To'] = listToStr
        msg['Subject'] = "Important Notice: Absence of Your Ward from Class"
        msg.attach(MIMEText(body, 'plain'))
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login("spam67182@gmail.com", "hyid xkcp ngtn yfvp")
        server.send_message(msg)
        server.quit()

        return f"Email Sent To :{listToStr} "
