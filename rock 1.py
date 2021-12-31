import random
import pymysql

# connecting MySQL with python using pymysql module.

mydb=pymysql.connect(
    host='localhost',
    user='root',
    passwd='isha',
    database='projectrps')
mycursor = mydb.cursor()





#creating the program for playing rock paper scissor
print (' ********* ROCK PAPER SCISSOR ********** ')
print('Hello!! \n Play with computer and try to win the game :)\n')
print ("###############################")
name=input('Enter your name=')
print('\nWelcome',name )




#rules for the game
print ('\nRules for the game are as follows:\n'
       +'1.If rock vs paper then paper wins. \n'
       +'2.If rock vs scissor then  rock wins. \n'
       +'3.If paper vs scissor then scissor wins. \n'
       +'4.The one who wins gets 1 point and 0 for loose.\n'
       +'\nThank you',name
       +'  for reading the rules carefully :)\n')




#initiating codes for the game  ;)
#defining a function.
def menu():
    print ('Choose  any of the following options:'
           + '\n 1.rock'
           +'\n2.paper'
           +'\n 3.scissor'
           +'\n4.EXIT')
    # taking input from the user.
    choice_user=int(input('Write your choice='))

    while choice_user > 4 or choice_user< 1:
                    print('INVALID input')
                    menu()
                    choice_user=int(input('Write your choice='))
                


    #the game beings here.
     #choiceu_name is the name assigned to the integer inpunt of user.
    while choice_user in range(1,5):
         if choice_user == 1:
             choiceu_name = 'rock'
             break
         elif choice_user  == 2:
             choiceu_name ='paper'
             break
         elif choice_user==3:
             choiceu_name ='scissor'
             break
         elif choice_user==4:
             choiceu_name='EXIT'
             break
    print('\nNice choice\n' +'your choice is\n ' + choiceu_name)
        
    #the role of random library comes to play at this moment.
               
    print('\nNow its computer  turn ..............  :)\n ')

    choice_comp = random.randint(1,3)



    #the choicec_name is the name assigned to the integer value choosed by the computer.
    while  choice_comp in range (1,4):
                    if choice_comp==1:
                            choicec_name='rock'
                            break
                    elif choice_comp==2:
                                choicec_name='paper'
                                break
                    else:
                                choicec_name='scissor'
                                break
                                        
    # the result of the game begins now.
    if choice_user == choice_comp:
                            print ('\n','The computer choose =', choicec_name
                                   +'\n the game  is TIE')
                            sql='insert into scores(You,Computer)VALUES(%s,%s)'
                            val=(1,1)
                            mycursor.execute(sql,val)
                            
                            print(mycursor.rowcount,'record inserted','\n')
                            menu()
                            
                            
                                           
    elif choice_user==1:
        if choice_comp==2:
                        print('\n','The computer choose=',choicec_name
                                         +'\n the ' , choicec_name, 'covers', choiceu_name
                                         + '\n the ', name ,'LOOSES  :(')
                        sql='insert into scores(You,Computer)VALUES(%s,%s)'
                        val=(0,1)
                        mycursor.execute(sql,val)
                        
                        
                        print(mycursor.rowcount,'record inserted','\n')
                        
                        menu()

               # cases of wining and losing .         
        else :
            print ('\nThe computer choose=',choicec_name
               +'\n the ' , choiceu_name, 'smashes', choicec_name
               + '\n the ', name ,'WINS  :)')
            sql='insert into scores(You,Computer)VALUES(%s,%s)'
            val=(1,0)
            mycursor.execute(sql,val)
           
            
            print(mycursor.rowcount,'record inserted','\n')
            
            menu()
            
    elif choice_user==2:
                    if choice_comp==3:
                        print('\nThe computer choose=',choicec_name
                                     +'\n The ' , choicec_name, 'cuts', choiceu_name
                                        + '\n the ', name ,'LOOSES  :(')
                        sql='insert into scores(You,Computer)VALUES(%s,%s)'
                        val=(0,1)
                        mycursor.execute(sql,val)
                        
                        print(mycursor.rowcount,'record inserted','\n')
                       
                        menu()
                    else :
                            print ('\nThe computer choose=',choicec_name
                                            +'\n The',choiceu_name,'covers',choicec_name
                                     + '\n the ', name ,'WINS  :)')
                            sql='insert into scores(You,Computer)VALUES(%s,%s)'
                            val=(1,0)
                            mycursor.execute(sql,val)
                           
                            print(mycursor.rowcount,'record inserted','\n')
                            
                            menu()                                         
    elif choice_user==3:
                    if choice_comp==1:
                       print('\nThe computer choose=',choicec_name
                                    +'\n The ' , choicec_name, 'smashes', choiceu_name
                                     + '\n the ', name ,'LOOSES :(')
                       sql='insert into scores(You,Computer)VALUES(%s,%s)'
                       
                       val=(0,1)
                       mycursor.execute(sql,val)
                       
                       print(mycursor.rowcount,'record inserted','\n')
                       
                       menu()                                      
                    else :
                             print ('\nThe computer choose=',choicec_name
                                        +'\n The ' , choiceu_name, 'cuts', choicec_name
                                     + '\n the ', name ,'WINS :)')
                             
                             sql='insert into scores(You,Computer)VALUES(%s,%s)'
                             val=(1,0)
                             mycursor.execute(sql,val)
                             
                             print(mycursor.rowcount,'record inserted','\n')
                                                          
                             menu()           
    else:
        print('Computer choose to say  good bye :) ....  :) ')
        
menu()

#executing the queries of MySQL
mycursor.execute('select * from scores')


#Fetching all the records from the table created in the MySQL.


myresult=mycursor.fetchall()
print('The points are:(',name,'points, computer points)')

for everyselect in myresult:
    print('The points are :',everyselect)


mydb.close()

#Now connection is closed form MySQL.

print('Thank you have a great day :)')









    
