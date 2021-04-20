from twilio.rest import Client
import config

client = Client(config.twilio_account_sid, config.twilio_auth_token)

message = client.messages.create(
    body="bete ..bete mauj kardi ..tum toh bade heavy driver nikle",
    to=config.receiving_number_me,
    from_=config.sending_number
)

print(message)