# Write a class Train which has methods to book a ticket, get Status (no. of seats) and get fare information of train running under Indian Railways.


from random import randint

class Train:
    def __init__(self, TrainNo): 
        self.TrainNo = TrainNo
    
    def Welcome(self):
        print("Welcome to Indian Railways :) ")
        
    def book(self, fro, to): # "fro" means from 
        print(f"Ticket is book in Train No: {self.TrainNo} from {fro} to {to}")

    def getStatus(self):
        print(f"Train No: {self.TrainNo} is running successfully on time")


    def getFare(self, fro, to):
        print(f"Ticket fare  in Train No: {self.TrainNo} from {fro} to {to} is {randint(1, 999)}")

t = Train(12399)
t.Welcome()

t.book( "Jaipur", "Kota")

t.getStatus()

t.getFare("Jaipur", "Kota")
