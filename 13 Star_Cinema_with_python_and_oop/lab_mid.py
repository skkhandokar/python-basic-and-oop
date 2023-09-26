class Star_Cinema:
 hall_list = []
 def entry_hall(self, obj):
   self.hall_list.append(obj)

class Hall(Star_Cinema):
  def __init__(self, rows, cols, hall_no):
   self.seats = {}
   # list of tuples
   self.show_list = []
   self._rows = rows
   self._cols = cols
   self.hall_no = hall_no
   super().entry_hall(self)

  def entry_show(self,id,movie_name,time):
   self.__id = id
   self._movie_name = movie_name
   self.time = time
   self.entrynew = (self.__id, self._movie_name,self.time)
   self.show_list.append(self.entrynew)
   tmp=[]
   ch=65
   for i in range(self._rows):
    temp = []
    for j in range(self._cols):
     temp.append(f'{chr(ch)}{j}')
    ch+=1
    tmp.append(temp)
   self.seats[self.__id]=(tmp)
  @staticmethod
  def  book_seats():
   name=input("Enter Customer Name: ")
   number=input("Enter Customer Phone Number: ")
   id=input("Enter show ID: ")

   # try:
   if id == "a21":
     show1.finaly(name,number)

   elif id == "a22":
     show2.finaly(name,number)


   elif id !="a21" or "a22":
      print(f'{id} is invalid ID.PLEASE TRY AGAIN')


  def call_by_invalid(self):
     print("You selected booked seat/invalid.please try again valid seat")

  def  succesfuly(self,name,number,tickets,hall):
      print("****************************************************************************")
      print("\n        #####SUCCESFULLY TICKED BOOKED\n")
      print(f'Name: {name}')
      print(f'Phone Number: {number}')
      self.view_show_list()
      print(f'Tickets:',end=" ")
      for i in tickets:
       print(i,end=" ")
      print(f'\nHall no: {hall}')
      print("*****************************************************************************")

  def finaly(self,n,num):
      self.name=n
      self.number=num
      self.seatlist = []
      numbers_ticket = int(input("Enter Numbers of Tickets: "))
      if numbers_ticket > (self._rows * self._cols):
          print("You Selected Over Seat\n")
      else:
          n = 0
          while n < numbers_ticket:
              a = input("ENTER SEAT NO: ")
              f = 0
              for i in self.seats[self.__id]:
                  P = 0
                  for j in i:
                      if j == a:
                          self.seatlist.append(a)
                          i[P] = 'X'
                          f += 1
                      P += 1
              if f == 0:
                  self.call_by_invalid()
                  numbers_ticket += 1
              n += 1
      self.succesfuly(self.name, self.number, self.seatlist, self.hall_no)

  def view_show_list(self):
   print(f'Movie Name: {self.show_list[0][1]}      Show ID: {self.show_list[0][0]}        TIME:{self.show_list[0][2]}')


  def  view_available_seats(self,movie_id):
   try:
    if movie_id == "a22":
      print("**************************************************************************")
      show2.view_show_list()
      print("\nX for already Booked\n")
      for i in self.seats[movie_id]:
       for j in i:
        print(j, end="        ")
       print("\n")
      print("**************************************************************************")
    elif movie_id == "a21":
      print("**************************************************************************")
      show1.view_show_list()
      print("\n'X' for already Booked\n")
      for i in self.seats[movie_id]:
       for j in i:
        print(j, end="         ")
       print("\n")
      print("**************************************************************************")
   except KeyError:
    print("PLEASE TRY AGAIN WITH RIGHT ID")



#test the program

cinema = Star_Cinema()
show1 = Hall(3, 4, 7)
show2 = Hall(3, 4, 7)

show1.entry_show("a21", "Black Adam", "Oct 25 2022 10:00 pm")

show2.entry_show("a22", "Super Man", "Oct 25 2022 8:00 pm")
while True:

    print("1 VIEW ALL SHOWS TODAY: ")
    print("2 VIEW AVAILABLE SEATS: ")
    print("3 BOOK TICKETS: ")
    try:
      A1 = int(input("ENTER OPTION: "))


      if A1 == 1:
        print("**************************************************************************")
        show1.view_show_list()
        show2.view_show_list()
        print("**************************************************************************")
      elif A1 == 2:
        show_id = input("ENTER SHOW ID: ")
        if show_id == "a21":
            show1.view_available_seats("a21")
        elif show_id == "a22":
            show2.view_available_seats("a22")
        else:
           print(f"\nYou Select wrong Show ID '{show_id}'.Please try again currectly\n")
      elif A1 == 3:
        Hall.book_seats()
    except ValueError:
      print("WRONG OPTION SELECT")
    except KeyboardInterrupt:
       print("\nyou left from here\n")
