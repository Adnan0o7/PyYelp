from twilio.rest import Client
import config

client = Client(config.twilio_account_sid, config.twilio_auth_token)

message = client.messages.create(
    body="kha ho bro .. mai US me hu .. tumhara kya chal rha",
    to=config.receiving_number,
    from_=config.sending_number
)

print(message)