
#Emoji converter
statement=input("> ")
words=statement.split(" ")
emojis={
    ":)": "😊",
    ':(':"😔"
}
output=" "
for word in words:
    output+=emojis.get(word,word)+" "
print(output)

def emoji_converter(message):
  words=message.split(" ")
  emojis={
        ":)": "😊",
        ':(': "😔"
    }
  output=" "
  for word in words:
     output+=emojis.get(word,word) +" "


emoji_converter("hi sunshine :) ")
