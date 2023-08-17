print("What your favourite colour says about you!")
Name=input("What's your name?")
colour=input("What's your favourite colour?")
if(colour.capitalize()=="Black"):
    print(Name+''',  You strive for power and control in life, but are often artistic and intuitive and do not share
     things well with others.You are above average, worldly, conventional, proper, polite, and regal.
     While black may mean depression to the clinical psychologist, to you it means dignity.''')
elif(colour.capitalize()=="White"):
    print(Name+''' , You are organized and very independent, and you rely on logic to solve every problem.''')
elif(colour.capitalize()=="Blue"):
    print(Name+''' , You want to find inner peace and absolute truth, and you always make an effort to 
    think of others and their needs.''')
elif(colour.capitalize()=="Purple"):
    print(Name+''' , You are a perfectionist who requires emotional security in life, and you are a
     good humanitarian who helps others in need.''')
elif(colour.capitalize()=="Red"):
    print(Name+''' , You have drive and determination, and you prefer action and risk-taking behaviors.
     Your biggest need is for physical fulfillment and fitness.''')
elif(colour.capitalize()=="Pink"):
    print(Name+''', All you want in life is unconditional love and to be accepted for who you are by your peers.''')
elif(colour.capitalize()=="Orange") :
    print(Name+''' , You love to be with people and socialize with them, as you want to be accepted and respected
     as a part of a group.''')
elif(colour.capitalize()=="Green") :
    print(Name+''' , You are loyal and very frank with others, and you consider your reputation a very important
     part of your life.''')
elif(colour.capitalize()=="Yellow"):
    print(Name+ ''' , You enjoy learning and sharing knowledge with others, and you feel a need to always 
    express your individuality.''')
else:
    print("Sorry, we don't have information regarding the colour you asked for")
