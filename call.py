from twilio.twiml.voice_response import VoiceResponse
from twilio.rest import Client
def call():
    # Your Account SID from twilio.com/console
    account_sid = "AC24e0e818487a27f3810370b39088f5ef"
    # Your Auth Token from twilio.com/console
    auth_token  = "1e293d8201b42626f69eb1f93debd857"
    message = "Hey Your Friend is getting trouble please call him or alert to the police by messaging his number"
    client = Client(account_sid, auth_token)
    response = VoiceResponse()
    response.say(message, voice='woman')
    call = client.calls.create(
        to="+917306264750", # recipient phone number
        from_="+15074163963", # your Twilio phone number
        twiml=str(response))

    print(call.status)