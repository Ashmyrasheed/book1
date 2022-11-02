import mysql.connector

mydb = mysql.connector.connect(host = 'localhost' , user = 'root' , password = '' , database = 'librarydb')
mycursor = mydb.cursor()
while True:

    print("select an option from the menu")

    print("1 add book")

    print("2 view all book")  

    print("3 search a book")

    print("4 update the book")    

    print("5 delete a book")

    print("6 exit")
    
    choice = int(input('enter an option:'))

    

    if(choice==1):

        print('book enter selected')
        
        
        

        title = input('enter the title')

        author = input('enter the author')

        category = input('enter the category ')

        chargeperday = input('enter the chargeperday')
        
        
        
        sql = 'INSERT INTO `books`( `title`, `author`, `category`, `charge per day`) VALUES (%s,%s,%s,%s)'

        

        data = (title,author,category,chargeperday)

        mycursor.execute(sql , data)

        mydb.commit()
    elif(choice==2):

        print('view book')

    elif(choice==3):

        print('search book')

    elif(choice==4):

        print('update book')

    elif(choice==5):

        print('delete book')

    elif(choice==6):

        break