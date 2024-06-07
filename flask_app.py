# A very simple Flask Hello World app for you to get started with...

from flask import abort, Flask, request  # , redirect
from functools import wraps
from twilio.twiml.messaging_response import MessagingResponse
from twilio.request_validator import RequestValidator

import os

app = Flask(__name__)


def validate_twilio_request(f):
    """Validates that incoming requests genuinely originated from Twilio"""

    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Create an instance of the RequestValidator class
        # validator = RequestValidator(os.environ.get('TWILIO_AUTH_TOKEN'))
        validator = RequestValidator(
            "TWILIO_AUTH_TOKEN here"
        )  # TODO: hard coding is bad practice.

        # Validate the request using its URL, POST data,
        # and X-TWILIO-SIGNATURE header
        request_valid = validator.validate(
            request.url, request.form, request.headers.get("X-TWILIO-SIGNATURE", "")
        )

        # Continue processing the request if it's valid, return a 403 error if
        # it's not
        if request_valid:
            return f(*args, **kwargs)
        else:
            return abort(403)

    return decorated_function


@app.route("/")
def hello_world():
    return "Hello again from Flask!"


@app.route("/sms", methods=["POST"])
@validate_twilio_request
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
