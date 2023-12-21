from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from gsheet_func import *

from dateutil.parser import parse


app = Flask(__name__)
count=0


@app.route("/sms", methods=['POST'])
def reply():
    
    incoming_msg = request.form.get('Body').lower()
    response = MessagingResponse()
    print(incoming_msg)
    message=response.message()
    responded = False
    words = incoming_msg.split('@')
    if "hello" in incoming_msg:
        reply = "Welcome to BMTC ticket bot"
        reply = "Hello! I am your ticket-bot and I will assist you in purchasing bus tickets, bus passes and tracking live location of busses. Type your queries or choose one of the options below for me to assist you"
        message.body(reply)
        responded = True
        
        
    if len(words) == 2 and "Bus tickets" in incoming_msg:
        reminder_string = "Would you like to enter your bus stop or bus number"
        message.body(reminder_string)
        responded = True

        if len(words)==2 and "Bus stop" in incoming_msg:
            reminder_string = "Please enter the source stop name choose one of the following options or type your query"
            message.body(reminder_string)
            responded = True
            
            if len(words)==3 and "Type stop name" in incoming_msg:
                reminder_string = "Please type your stop name"
                message.body(reminder_string)
                responded = True


        elif len(words)==2 and "Bus Number" in incoming_msg:
            reminder_string="Please enter your bus number"
            message.body(reminder_string)
            responded= True 



    if len(words) == 1 and "no" in incoming_msg:
        reply="Ok. Have a nice day!"
        message.body(reply)
        responded = True
    
    elif len(words) != 1:
        input_type = words[0].strip().lower()
        input_string = words[1].strip()
        if input_type == "date":
            reply="Please enter the reminder message in the following format only.\n\n"\
            "*Reminder @* _type the message_"
            set_reminder_date(input_string)
            message.body(reply)
            responded = True
        if input_type == "reminder":
            print("yuhu")
            reply="Your reminder is set!"
            set_reminder_body(input_string)
            message.body(reply)
            responded = True
        
    if not responded:
        print("why", input_type)
        message.body('Incorrect request format. Please enter in the correct format')
    
    return str(response)
    
def set_reminder_date(msg):
    p= parse(msg)
    date=p.strftime('%d/%m/%Y')
    save_reminder_date(date)
    return 0
    
def set_reminder_body(msg):
    save_reminder_body(msg)
    return 0
    
     
    return reminder_message


if __name__ == "__main__":
    app.run(debug=True)