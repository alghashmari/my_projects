import smtplib

my_email = "alghashmari@yahoo.com"
password = "Amg@10231012"

connection = smtplib.SMTP("smtp.mail.yahoo.com")
connection.starttls()
connection.login(user=my_email,password=password)
connection.sendmail(from_addr=my_email,to_addrs="alghashmari02@gmail.com",msg="Hello")
connection.close()