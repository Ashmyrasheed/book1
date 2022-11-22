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
    print("6total amount of book")
    print("7 displays Total number of books for each category")
    print("8 Displays the character which you needed ")
    print("8 indidual book  ")

    print("9 exit")
    
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
        
        sql = 'SELECT * FROM `books`'
        mycursor.execute(sql)
        result = mycursor.fetchall()
        for i in result:
            print(i)

        print('view book')

    elif(choice==3):

        print('search book')
        
        title = input('enter the title')
        

        sql = "SELECT * FROM `books` WHERE `title` = '"+title+"'"

        mycursor.execute(sql)

        result = mycursor.fetchall()

        print(result)


    elif(choice==4):

        print('update book')
        
        
        
        
       

        chargeperday = input('Enter the price for each day to be get updated : ')

        title = input('Enter the book name : ')

        category = input('Enter the category of the book : ')

       

        author = input('Enter the author name : ')

       

        sql = "UPDATE `books` SET `title`='"+title+"',`category`='"+category+"',`charge per day`='"+chargeperday+"',`author`='"+author+"' WHERE `charge per day`="+chargeperday

        mycursor.execute(sql)

        mydb.commit()

        print('Updated sucessfully !!!')

    elif(choice==5):

        print('delete book')
        
        title = input('enter the title')
        sql = "DELETE FROM `books` WHERE `title` = '"+title+"'"
        mycursor.execute(sql)
        mydb.commit()
        print("data deleted succesfully")

    elif(choice==6):
        
        print('total amount of book')
        
        
        sql = 'SELECT i.`userid`, i.`bookid`, i.`issuedate`, i.`returndate`,DATEDIFF(i.`returndate`,i.issuedate) AS datediff,DATEDIFF(i.`returndate`,i.issuedate)*b.`charge per day` AS amount FROM `issuebook` i JOIN books b ON i.bookid=b.id'
        mycursor.execute(sql)

        result = mycursor.fetchall()

        for i in result:

            print(i)
            
    elif(choice == 7):

        print('displays Total number of books for each category')

        
        
        sql = 'SELECT COUNT(*) AS total_book_per_category,`category` FROM `books` GROUP BY `category`'

        mycursor.execute(sql)

        result = mycursor.fetchall()

        for i in result:

            print(i)
            
    elif(choice == 8):

        print('Displays the character which you needed ')

        st = input('Enter the starting character of book you need to display : ')

        sql = "SELECT `id`, `title`, `category`, `charge per day`, `author` FROM `books` WHERE `title` LIKE '%"+st+"%'"

        mycursor.execute(sql)

        result = mycursor.fetchall()

        print(result)
    elif(choice == 9):
        break
    