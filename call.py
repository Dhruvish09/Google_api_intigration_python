from twilio.rest import Client

client = Client()
call = client.calls.create(
    from_='+916353573222',
    to='+918488861415',
    url='https://handler.twilio.com/twiml/EH467a05eab28d29e910389f7ea291a585'
)
