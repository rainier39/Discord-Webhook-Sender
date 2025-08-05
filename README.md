# Discord-Webhook-Sender
Configurable Python script that sends a configurable amount of messages to every discord webhook specified in its hooks file (hooks.txt by default). This script is intended to be configured through its config file rather than directly editing the script. The different config options are explained via comments in the config file. The script only supports full line comments, and the comment character is the hash symbol (#).

In case you are unfamiliar with Discord or its Webhooks, Discord is a chatting site and Webhooks are API endpoints that one can create within their own Discord channels that allow anybody with the Webhook URL to send messages to that channel via POST requests. This script takes advantage of a few features of Webhooks, including being able to set a username, avatar, and sending text-to-speech messages.

Developed and tested with Python 3.11.2 on Debian 12.
