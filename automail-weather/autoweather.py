import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, message, to_email, smtp_server, smtp_port, smtp_username, smtp_password):
    msg = MIMEMultipart()
    msg['From'] = smtp_username
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    smtp = smtplib.SMTP(smtp_server, smtp_port)
    smtp.starttls()
    smtp.login(smtp_username, smtp_password)
    smtp.sendmail(smtp_username, to_email, msg.as_string())
    smtp.quit()

city = input("\nEnter the city name: ")
url = "https://wttr.in/{}?format=%C+%t".format(city)  # Get weather forecast in Celsius and temperature

try: 
    res = requests.get(url)
    weather_forecast = res.text.strip()
    print("Weather Forecast:", weather_forecast)
except Exception as e:
    error_message = "An error occurred: {}".format(e)
    print(error_message)
    
    # Send email notification
    smtp_server = 'smtp.example.com'  # Replace with your SMTP server address
    smtp_port = 587  # Replace with the appropriate SMTP port
    smtp_username = 'your_email@example.com'
    smtp_password = 'your_email_password'
    to_email = 'yskomartin@gmail.com'
    
    subject = 'Weather Forecast Error'
    message = f"An error occurred while fetching the weather forecast for city {city}.\nError: {error_message}"
    
    send_email(subject, message, to_email, smtp_server, smtp_port, smtp_username, smtp_password)
else:
    # Send weather forecast email
    smtp_server = 'smtp.example.com'  # Replace with your SMTP server address
    smtp_port = 587  # Replace with the appropriate SMTP port
    smtp_username = 'your_email@example.com'
    smtp_password = 'your_email_password'
    to_email = 'yskomartin@gmail.com'
    
    subject = f'Weather Forecast for {city}'
    message = f"The weather forecast for {city}:\n{weather_forecast}"
    
    send_email(subject, message, to_email, smtp_server, smtp_port, smtp_username, smtp_password)
