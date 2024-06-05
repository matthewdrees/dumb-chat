# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request  # , redirect
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello again from Flask!"


@app.route("/sms", methods=["GET", "POST"])
def sms_reply():
    """Respond to incoming calls with a simple text message."""

    # Get the message the user sent our Twilio number
    body = request.values.get("Body", None)

    # Start our TwiML response
    resp = MessagingResponse()

    # Determine the right reply for this message
    if body == "hello":
        resp.message("Hi!")
    elif body == "bye":
        resp.message("Goodbye")
    else:
        resp.message("The Robots are coming! Head for the hills!")

    return str(resp)
