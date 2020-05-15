import smtplib as s

#cretaing Object
object= s.SMTP('smtp.gmail.com', 587)

#connecting server
object.starttls()

#login with email and password

object.login("kumardigamberjha@gmail.com", '**********')

# create message
subject= "This is a testing message"
body= "This is send by Digamber Jha using python's smtblib module."

# message formatting
message= "Subject: {}\n\n{}".format(subject, body)

#number of recipient
emailAddresses= ['kumardigamberjha7@gmail.com', 'digamber1011@gmail.com']

# send mail
object.sendmail('kumardigamberjha@gmail.com', emailAddresses, message)

print("Congrats Sent Successfull!")

object.quit()