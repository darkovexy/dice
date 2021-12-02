#Write a class Train which has methods to book a ticket, get status(no of seats),
# and get fare information of trains running under Indian Railways.

class Train():
    
    def __init__(self,name,seats,fare):
        self.name = name
        self.seats = seats
        self.fare = fare
        # self.totalSeats = []
        # for i in range(1, seats+1):
        #     self.totalSeats.insert(i, i)
        
    def bookTicket(self):
        if  self.seats >0:
            print(f"Congratulation your seat no {self.seats} has been booked")
            self.seats -= 1
        else:
            print("Train is full")
            
    def getStatus(self):
        print("Available seats : ",self.seats)
        print("Train name is : ",self.name)
        
    def getFare(self):
        print(f"Train ticket price is : Rs{self.fare} ")
        
    def cancelTicket(self,seatno):
        pass

chinmay = Train("Chennai Express",2,90)
chinmay.getStatus()
chinmay.getFare()
chinmay.bookTicket()
chinmay.bookTicket()
chinmay.bookTicket()
chinmay.getStatus()
        
        
    
