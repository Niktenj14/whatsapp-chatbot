from twilio.rest import Client
 
account_sid = 'AC74ac5abb0a0513024716ffaa3fc36a49'
auth_token = 'ce0c8a3e32468bfd444fa0c7d3ad13a0'
client = Client(account_sid, auth_token)
def send_rem(date,rem):
    message = client.messages.create(
                                  from_='whatsapp:+14155238886',
                                  body='*REMINDER* '+date+'\n'+rem,
                                  to='whatsapp:+918496922977'
                              )
     
    print(message.sid)
