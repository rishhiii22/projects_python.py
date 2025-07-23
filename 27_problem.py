# Spam Filter
p1 = "Make a lots of money"
p2 = "Buy Now"
p3 = "Subscribe Now"
p4 = "Click This"

message = input("Enter your comment: ")

if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("This comment is a Scam")

else:
    print("This comment is not a scam")
