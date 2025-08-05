# https://github.com/rainier39/Discord-Webhook-Sender
import requests

# Name of the config file.
configfile = "config.cfg"
# Header that must be sent, tells Discord what kind of data we are sending.
headers = {"Content-Type": "application/json"}
# Stores the URL of all webhooks from specified file.
webhooks = []

# -- Default config --
config = {
  "hookfilename": "hooks.txt",
  "message": "Hello world!",
  "username": "",
  "avatarurl": "",
  "tts": False,
  "debug": False,
  "msgcount": 1
}

# Try to read the config file.
try:
  f = open(configfile, "r")
# If we can't, print a message, and we will use the hardcoded defaults.
except:
  print("Couldn't read config file. Using default config.")
# If we can, overwrite the config with whatever is in the config file.
else:
  for line in f:
    # Ignore comments.
    if (line[0] == "#"):
      continue
    left = line[:line.find("=")].strip()
    right = line[line.find("=")+1:].strip()
    
    # Make sure tts and debug are valid booleans.
    if ((left == "tts") or (left == "debug")):
      if not ((right == "True") or (right == "False")):
        print("Value for " + left + " was invalid. Must be 'True' or 'False'.")
        continue
      else:
        if (right == "True"):
          right = True
        else:
          right = False
    # Make sure msgcount is a valid number.
    if (left == "msgcount"):
      if not right.isdecimal() or "." in right or "-" in right:
        print("Value for msgcount was invalid. Must be a non-negative integer.")
        continue
      else:
        right = int(right)
    
    config[left] = right
  f.close()

# Make sure the message isn't empty.
if (len(config["message"]) < 1):
  print("Error: message cannot be empty.")
  exit()
# Make sure the message isn't too long.
if (len(config["message"]) > 2000):
  print("Warning: message was too long. Truncating to 2000 characters.")
  config["message"] = config["message"][:2000]
# Make sure the username isn't too long.
if (len(config["username"]) > 80):
  print("Warning: username was too long. Truncating to 80 characters.")
  config["username"] = config["username"][:80]

# Try to read the webhook file.
try:
  f2 = open(config["hookfilename"], "r")
# Stop if we can't.
except:
  print("Couldn't open webhook file.")
  exit()
# Otherwise read the file, making sure each line looks like a valid webhook URL.
else:
  for line in f2:
    if line.startswith("https://discord.com/api/webhooks/"):
      webhooks.append(line.strip())
    else:
      print("Ignoring invalid hookfile line " + line.strip())
  f2.close()

# Send the specified number of messages to each webhook.
print("Sending to the webhook(s)...")
for i in range(0, config["msgcount"]):
  for webhook in webhooks:
    resp = requests.post(webhook, headers=headers, data='{"content":"' + config["message"] + '"' + ((',"username":"' + config["username"] + '"') if (len(config["username"]) > 0) else "") + ((',"avatar_url":"' + config["avatarurl"] + '"') if (len(config["avatarurl"]) > 0) else "") + ((',"tts":"true"') if config["tts"] else "") + '}')
    if ("Invalid Webhook Token" in resp.text):
      print("Webhook " + webhook + " doesn't exist.")
    if config["debug"]:
      print(resp.text)

print("Done!")
