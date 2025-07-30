  # Self ki jagah slf use kra hai bss.... Par usse koi farak ni padta hai 
from random import randint

class Train:
    def __init__(slf, TrainNo): 
        slf.TrainNo = TrainNo
    
    def Welcome(slf):
        print("Welcome to Indian Railways :) ")
        
    def book(slf, fro, to): # "fro" means from 
        print(f"Ticket is book in Train No: {slf.TrainNo} from {fro} to {to}")

    def getStatus(slf):
        print(f"Train No: {slf.TrainNo} is running successfully on time")


    def getFare(slf, fro, to):
        print(f"Ticket fare  in Train No: {slf.TrainNo} from {fro} to {to} is {randint(1, 999)}")

t = Train(12399)
t.Welcome()

t.book( "Jaipur", "Kota")

t.getStatus()

t.getFare("Jaipur", "Kota")