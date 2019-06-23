import smtplib, ssl


def sendMail(re_add,subject,message):
    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls
    sender_email ="vk3334703@gmail.com"
    password = ""
    message=subject+"    " +message

	# Create a secure SSL context
    context = ssl.create_default_context()

	# Try to log in to server and send email
    try:
        
        server = smtplib.SMTP(smtp_server,port)
        server.ehlo() # Can be omitted 
        server.starttls(context=context)
        server.ehlo() # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, re_add, message)
		# TODO: Send email here
    except Exception as e:
        # Print any error messages to stdout
        print(e)
    finally:
        server.quit()
