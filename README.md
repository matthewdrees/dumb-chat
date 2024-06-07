# dumb-chat
Have dumb text conversations with this chat client.

# twilio notes

* <https://www.twilio.com/>
* [Getting Started Twilio Webhooks](https://www.twilio.com/docs/usage/webhooks/getting-started-twilio-webhooks)
* [Receive and Reply to Incoming Messages - Python](https://www.twilio.com/docs/messaging/tutorials/how-to-receive-and-reply/python)
  * Only have 15 seconds for primary webhook URL to respond.
* Text responses from webhook not working, saying it needs money. I put $20 on it. (Note to self: buy twilio stock. :) )
* Text responses from webhook not working, message says because "Toll-free verification required for US messaging". I submitted that. It looks like it could be [3-5 business days to verify](https://help.twilio.com/articles/5377174717595-Toll-Free-Message-Verification-for-US-Canada#h_01GTCNPTVZFNCK8FFNYRDD2TZR)
* HOOOO! Toll-free verification was validated in ~48 hours. Responses to text messages are working! Very cool!
* [Account Insights - Billing Usage Insights](https://console.twilio.com/us1/monitor/insights/billing). So far I've spent $3.05. Each text message costs $0.0079, and I've had 17 text messages so far, for a total of $0.1343. Unsure what the other $3 was for?
* [Secure your Flask App by Validating Incoming Twilio Requests](https://www.twilio.com/docs/usage/tutorials/how-to-secure-your-flask-app-by-validating-incoming-twilio-requests). Worked by copying TWILIO_ATUH_TOKEN from the console to the RequestValidator call, didn't have to do anything with the X-TWILIO-SIGNATURE in the code. Verified by changing the auth token slightly, then didn't get any responses in text chat. It was hard to find that reflected in the twilio error logs but that seems like a [known issue](https://help.twilio.com/articles/21923437804315-Upcoming-Improvements-on-Programmable-Messaging-Error-Visibility).
* Next steps:
  * Put TWILIO_AUTH_TOKEN in environment variable.
  * What's up with regional routing? How to make it work in other countries?
  * Make the client slightly less dumb:
    * Put an actual small natural language model in it?
    * Have a database for statefulness, remember the metadata (e.g. phone number, time, etc)?

# pythonanywhere notes

* <https://www.pythonanywhere.com/>
* Twilio libraries seem to be pre-loaded and ran just fine out of the box. Very cool.
