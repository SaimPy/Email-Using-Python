import smtplib
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    loginemail = input("[+] Enter Your From Email Address: ")
    loginpass = input("[+] Enter Your Password: ")
    server.login(loginemail, loginpass)
    server.sendmail(loginemail, to, content)
    server.close()
to = input("[*] Enter To Email Address: ")  
content = input("[*] Enter The Content: ")  
sendEmail(to, content)