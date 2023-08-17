customer={
    'Name': "saishree",
    "age": 16,
    "is_verified":True
}
customer["Name"]="Mika"
customer["phno."]=9123678450
print(customer.get("Name"))
print(customer["Name"])
print(customer)

#EXERCISE
number=(input("Phone: "))
digits={
    "1":"one",
    "2":"two",
    "3":"three",
    "4":"four"
    }
output=""
for x in number:
    output+=digits.get(x,"!")+" "
    print(output)

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
