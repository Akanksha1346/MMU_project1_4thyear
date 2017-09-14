from select_friend import select_friend
from steganography.steganography import Steganography
from datetime import datetime
#to read secret messages
def read_message():
  sender = select_friend()

  #to decode secret messages
  output_path = raw_input("What is the name of the file?")
  secret_text = Steganography.decode()
  new_chat = {
      "message": secret_text,
      "time": datetime.now(),
      "sent_by_me": False
  }

  select_friend[sender]['chats'].append(new_chat)
  print "Your secret message has been saved!"