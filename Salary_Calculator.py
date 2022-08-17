weeks=int(input("How many weeks do you work? ")) #Asking the user the amount of the weeks they are going to work.

if weeks<=0:
    print("Invalid week input!") #The amount of the weeks must be positive.
     
else:
    weekday_earnings=int(input("Enter weekday earnings [$]: ")) #Asking the user how much does s/he earn in weekdays.
    
    if weekday_earnings<=0:
        print("Weekday earnings should be higher than zero!") # Weekday earnings must be higher than zero.
        
    
    if weekday_earnings>0:
        weekend_earnings= int(input("Enter weekend earnings [$]: ")) #Asking the user how much does s/he earn in weekends.

        if weekend_earnings<=0 and weekend_earnings<=weekday_earnings:
            print("Weekend earnings should be positive and higher than weekday earnings!") #If the user types a negative value or 0 it will display "Weekend earnings should be positive and higher than weekday earnings!"
        
        if weekend_earnings<=weekday_earnings and weekend_earnings >0:  
            print("Weekend earnings should be higher than the weekday earnings!") #If the user types a positive value that is lower than weekday earnings, it says "Weekend earnings should be higher than the weekday earnings!"
        
        
        if weekday_earnings>0 and weekend_earnings>weekday_earnings:   
            groceries=int(input("Enter the cost of groceries [$]: ")) #Asking the user the cost of the groceries.
                    
            if groceries<=0:
                print("Grocery expenditure should be positive!") #Grocery expenditure should be positive.
                        
            else:
                rent=int(input("Enter the rent [$]: ")) #Asking the user the rent.
                        
                if rent<=0:
                    print("Rent should be positive!") #Rent must be positive.
                    
                       
                else: #If every input is valid, the amount of the earnings,spendings and remaining amount of money will be calculated.
                    
                    remaining=500
                    for a in range(1,weeks+1,1): #It will calculate all the values that is mentioned above until the end of the user's working range.
                     
                        for b in range(1,8,1): #The changing amount of money will be calculated by days.
                            
                           if a%2==1 and b==1:
                               remaining+=weekday_earnings
                               print("Week",a,"day",1,"earnings:",weekday_earnings,"spendings: 0","remaining:" ,remaining)
                           
                           if a%2==1 and b==2:
                               print("Week",a,"day",2,"earnings: 0","spendings: 0","remaining:" ,remaining)
                               
                           if a%2==1 and b==3:
                               remaining+=weekday_earnings
                               print("Week",a,"day",3,"earnings:",weekday_earnings,"spendings:",groceries,"remaining:" ,remaining-groceries) 
                           
                           if a%2==1 and b==4:
                               print("Week",a,"day",4,"earnings: 0","spendings:  0","remaining:" ,remaining)
                            
                           if a%2==1 and b==5:
                              remaining=remaining-groceries+weekday_earnings
                              print("Week",a,"day",5,"earnings:",weekday_earnings,"spendings: 0","remaining:" ,remaining) 
                           
                           if a%2==1 and b==6:
                              print("Week",a,"day",6,"earnings: 0","spendings:  0","remaining:" ,remaining)
                           
                           if a%2==1 and b==7:
                              remaining+=weekend_earnings
                              print("Week",a,"day",7,"earnings:",weekend_earnings,"spendings: 0","remaining:" ,remaining) 
                              
                              
                           if a%2==0 and b==1:
                               print("Week",a,"day",1,"earnings: 0","spendings:  0","remaining:" ,remaining)
                            
                           if a%2==0 and b==2:
                               remaining+=weekday_earnings
                               print("Week",a,"day",2,"earnings:",weekday_earnings,"spendings: 0","remaining:" ,remaining) 
                               
                           if a%2==0 and b==3:
                               remaining-=groceries
                               print("Week",a,"day",3,"earnings: 0","spendings:",groceries,"remaining:" ,remaining) 
                           
                           if a%2==0 and b==4:
                               remaining+=weekday_earnings
                               print("Week",a,"day",4,"earnings:",weekday_earnings,"spendings: 0","remaining:" ,remaining)  
                           
                           if a%2==0 and b==5:
                               print("Week",a,"day",5,"earnings: 0","spendings:  0","remaining:" ,remaining) 
                               
                           if a%2==0 and a%4!=0 and b==6 :
                               remaining+=weekend_earnings
                               print("Week",a,"day",6,"earnings:",weekend_earnings,"spendings: 0","remaining:" ,remaining)  
                                
                           if a%2==0 and b==7:
                               print("Week",a,"day",7,"earnings: 0","spendings: 0","remaining:" ,remaining)    
                        
                           
                           if a%4==0 and b==6:
                               remaining=remaining+weekend_earnings-rent #The rent will be subtracted from the remaining amount of money.
 
                               print("Week",a,"day",6,"earnings:",weekend_earnings,"spendings:",rent,"remaining:" ,remaining) 
                            
                            
                            
