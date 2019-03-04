import sqlite3 as sq
import datetime
# import csv
# import argparse


class Library :
    def __init__(self):
        self.table_creation = '''CREATE TABLE if not exists`Book_Details`  (
	                                `ISBN`	INTEGER check(ISBN > 999999999 and ISBN < 10000000000),
                                    `Book_Name`	TEXT NOT NULL,
                                    `Author_Name`	TEXT NOT NULL,
                                    `Count_of_Books`	INTEGER CHECK(Count_of_books > 0),
                                    PRIMARY KEY(`ISBN`)
                                    );'''
        self.sqlEntry(self.table_creation)

    def viewAll(self,table = 'Book_Details'):

        print(f"Do you want to view all the records or limit the records of {table} table : ")
        print(" 1: All Records   2: Limit the Records ")
        choice = int(input('Enter the choice : '))


        if choice == 1:

            sql_query_to_view = f"Select * from {table} ;"
            data_received = self.sqlEntry(sql_query_to_view, receive=True)
            for data in data_received:
                print(data)

        if choice == 2:
            limit_count = int(input('Enter the limit of records : '))
            sql_query_to_view = f"Select * from {table} Limit {limit_count} ;"
            data_received = self.sqlEntry(sql_query_to_view, receive=True)
            for data in data_received:
                print(data)


    def add_entry_into_table(self):

        isbn_code = int(input("Enter the isbn code (must be 10 digit) of the book : "))
        title_book = input("Enter the title of the book : ")
        author_book = input("Enter the author name of the book : ")
        count_book = int(input("Enter the count of books to be added (must be non negative) : "))

        if len(str(isbn_code)) == 10 and len(title_book) > 0 and len(author_book)>0 and count_book > -1 :
            sql_query_to_insert = "Insert into Book_Details values(?,?,?,?);"
            params = (isbn_code,title_book,author_book,count_book)
            self.sqlEntry(sql_query_to_insert,params,receive=False)

        else :
            print("Check The format of each field you entered  ")


    def searchEntry(self):
        print(" \n How Do you want to search in the Book Store table : ")
        print(" \n 1: By ISBN  \n 2: By Title  \n 3: By Author")
        choice = int(input("Enter the choice : "))

        if choice == 1:
            sql_query = "Select * from Book_Details where isbn = ? "
            isbn_code = int(input('Enter the isbn code you want to search  : '))
            params = (isbn_code,)
            data = self.sqlEntry(sql_query,params, receive=True)
            for row in data :
                print(row)

        if choice == 2:
            sql_query = "Select * from Book_Details where title  = ? "
            book_title = input('Enter the book title you want to search  : ')
            params = (book_title,)
            data = self.sqlEntry(sql_query, params, receive=True)
            for row in data:
                print(row)

        if choice == 3:
            sql_query = "Select * from Book_Details where author = ? "
            author_name = input('Enter the author of the book you want to search  : ')
            params = (author_name,)
            data = self.sqlEntry(sql_query, params, receive=True)
            for row in data:
                print(row)


    def del_selected(self):

        print(" \n How Do you want to delete in the Book Store table : ")
        print(" \n 1: By ISBN  \n 2: By Title  \n 3: By Author")

        choice = int(input("Enter the choice : "))

        if choice == 1:
            sql_query = "Delete from Book_Details where isbn = ? "
            isbn_code = int(input('Enter the isbn code you want to delete  : '))
            params = (isbn_code,)
            self.sqlEntry(sql_query, params)


        if choice == 2:
            sql_query = "Delete  from Book_Details where title  = ? "
            book_title = input('Enter the book title you want to delete  : ')
            params = (book_title,)
            self.sqlEntry(sql_query, params)

        if choice == 3:
            sql_query = "Delete from Book_Details where author = ? "
            author_name = input('Enter the author of the book you want to search  : ')
            params = (author_name,)
            self.sqlEntry(sql_query, params)


    def sqlEntry(self, sql_query, data=None, receive=False):
        conn = sq.connect("Book_Details.db")
        cursor = conn.cursor()
        if data:
            cursor.execute(sql_query, data)
        else:
            cursor.execute(sql_query)

        if receive:
            return cursor.fetchall()
        else:
            conn.commit()

        conn.close()



class User :
    def __init__(self):
        self.table_creation = '''CREATE TABLE if not exists`User_Details`  (
    	                                `UserId`	INTEGER,
                                        `User_Name`	TEXT NOT NULL,
                                        'Fine' Integer default 0,
                                        PRIMARY KEY(`UserId`)
                                        );'''
        self.sqlEntry(self.table_creation)

    def viewAll(self,table = "User_Details"):

        print("Do you want to view all the records or limit the records : ")
        print(" 1: All Records   2: Limit the Records ")
        choice = int(input('Enter the choice : '))

        if choice == 1:

            sql_query_to_view = f"Select * from {table} ;"
            data_received = self.sqlEntry(sql_query_to_view, receive=True)
            for data in data_received:
                print(data)

        if choice == 2:
            limit_count = int(input('Enter the limit of records : '))
            sql_query_to_view = f"Select * from {table} Limit {limit_count} ;"
            data_received = self.sqlEntry(sql_query_to_view, receive=True)
            for data in data_received:
                print(data)

    def add_entry_into_table(self):

        user_id = int(input("Enter the User_ID : "))
        user_name = input("Enter the User_Name : ")

        if len(user_name) > 0 :
            sql_query_to_insert = "Insert into User_Details values(?,?);"
            params = (user_id,user_name)
            self.sqlEntry(sql_query_to_insert, params, receive=False)

        else:
            print("Check The format of each field you entered  ")

    def searchEntry(self):
        print(" \n How Do you want to search in the User Details table : ")
        print(" \n 1: By UserId  \n 2: By UserName  ")
        choice = int(input("Enter the choice : "))

        if choice == 1:
            sql_query = "Select * from User_Details where UserId = ? "
            user_id = int(input('Enter the User_Id you want to search  : '))
            params = (user_id,)
            data = self.sqlEntry(sql_query, params, receive=True)
            for row in data:
                print(row)

        if choice == 2:
            sql_query = "Select * from User_Details where User_Name  = ? "
            user_name = input('Enter the book title you want to search  : ')
            params = (user_name,)
            data = self.sqlEntry(sql_query, params, receive=True)
            for row in data:
                print(row)


    def del_selected(self):

        print(" \n How Do you want to delete in the User Details table : ")
        print(" \n 1: By UserId  \n 2: By UserName  ")
        choice = int(input("Enter the choice : "))

        if choice == 1:
            sql_query = "Delete from User_Details where User_Id = ? "
            user_id = int(input('Enter the user_id you want to delete  : '))
            params = (user_id,)
            self.sqlEntry(sql_query, params)

        if choice == 2:
            sql_query = "Delete  from User_Details where User_Name  = ? "
            user_name = input('Enter the User_Name you want to delete  : ')
            params = (user_name,)
            self.sqlEntry(sql_query, params)



    def sqlEntry(self, sql_query, data=None, receive=False):
        conn = sq.connect("Book_Details.db")
        cursor = conn.cursor()
        if data:
            cursor.execute(sql_query, data)
        else:
            cursor.execute(sql_query)

        if receive:
            return cursor.fetchall()
        else:
            conn.commit()

        conn.close()


class Issue_And_Return_Books(Library,User):
    def __init__(self):
        super().__init__()
        self.issue_table_creation = '''CREATE TABLE if not exists`Issue_Status` (
            `Issue_Id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            `Issued_User_Id`	INTEGER NOT NULL,
            `Issued_Book_Name`	TEXT NOT NULL,
            `Issue_Date`	Datetime NOT NULL default current_timestamp,
            `Issued_book_ISBN`	INTEGER NOT NULL,
            FOREIGN KEY(`Issued_User_Id`) REFERENCES User_Details(UserId),
            FOREIGN KEY(`Issued_book_ISBN`) REFERENCES Book_Details(ISBN) );
             '''
        self.sqlEntry(self.issue_table_creation)

        self.return_table_creation = '''CREATE TABLE if not exists`Return_Status` (
            `Return_Id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            `Return_User_Id`	INTEGER NOT NULL,
            `Return_Book_Name`	TEXT NOT NULL,
            `Return_Date`	Datetime NOT NULL default current_timestamp,
            `Returned_book_ISBN`	INTEGER NOT NULL,
            FOREIGN KEY(`Return_User_Id`) REFERENCES Issue_Status(Issued_User_Id),
            FOREIGN KEY(`Returned_book_ISBN`) REFERENCES Book_Details(ISBN) );
             '''
        self.sqlEntry(self.return_table_creation)

    def Issue_Book(self):
        print('This will issue book for you with your preference ')
        user_id = int(input('Enter your user id : '))

        print('Do you remember the book isbn and name if not then input choice as 1 else proceed ')
        choice = int(input('Do you want to view all the books details (Enter 1) :  '))

        if choice == 1:
            Library.viewAll(self)




        book_name = input('Enter the book name : ')
        book_isbn = input('Enter the book Isbn : ')


        sql_query_to_check_the_count = f"Select Count_of_Books from Book_Details where ISBN = {book_isbn}; "
        data_received = self.sqlEntry(sql_query_to_check_the_count,receive= True)

        if data_received[0][0] > 0:
            sql_query_to_decrement = f"Update Book_Details set Count_of_Books = {data_received[0][0] - 1} where ISBN = {book_isbn};"
            self.sqlEntry(sql_query_to_decrement)
            sql_query = "insert into Issue_Status(Issued_User_Id,Issued_Book_Name,Issued_book_ISBN) values (?,?,?) ;"
            params = (user_id,book_name,book_isbn)

            self.sqlEntry(sql_query,params)
        else:
            print('The number of books are insufficient wait for their availablity')
            Library.viewAll(self)


    def return_Book(self):

        print('This will return book for you')
        self.view_Issue()

        user_id = int(input('Enter your user id : '))
        book_name = input('Enter the book name : ')
        book_isbn = input('Enter the book Isbn : ')

        #possible,msg = self.do_validation(user_id,book_name,book_isbn)

        #if possible == True:

        sql_query_to_check_the_count = f"Select Count_of_Books from Book_Details where ISBN = {book_isbn} ;"
        data_received = self.sqlEntry(sql_query_to_check_the_count,receive=True)

        sql_query_to_increment = f"Update Book_Details set Count_of_Books = {data_received[0][0] + 1} where ISBN = {book_isbn};"
        self.sqlEntry(sql_query_to_increment)

        self.fine_calculation(user_id,book_isbn)


        sql_query = "insert into Return_Status(Return_User_Id,Return_Book_Name,Returned_book_ISBN) values (?,?,?) ;"
        params = (user_id, book_name, book_isbn)

        self.sqlEntry(sql_query, params)

        # else :
        #     print(f"It is not possible to return {book_name} by {user_id} due to {msg}")


    def view_Issue(self):
        self.viewAll(table='Issue_Status')


    def view_Return(self):
        self.viewAll(table='Return_Status')

    def del_selected(self):

        print(" \n How Do you want to delete in the Issue Status and Return Status table : ")
        print(" \n 1: Issue Status  \n 2: Return Status  ")
        choice = int(input("Enter the choice : "))

        if choice == 1:
            sql_query = "Delete from Issue_Status where Issue_Id = ? ;"
            issue_id = int(input('Enter the Issue_id you want to delete  : '))
            params = (issue_id,)
            self.sqlEntry(sql_query, params)

        if choice == 2:
            sql_query = "Delete  from Return_Status where Return_Id  = ? ;"
            return_id = input('Enter the Return_Id you want to delete  : ')
            params = (return_id,)
            self.sqlEntry(sql_query, params)


    def fine_calculation(self,userid,book_isbn):
        current_fine = f"Select Fine from User_Details where UserId = {userid}; "
        data_fine = self.sqlEntry(current_fine,receive=True)


        issue_date = f"Select Max(Issue_Date) from Issue_Status where Issued_User_Id = {userid} and Issued_book_ISBN = {book_isbn} ;"
        date_issue_str = self.sqlEntry(issue_date,receive=True)

        return_date = f"Select Max(Return_Date) from Return_Status where Return_User_Id = {userid} and Returned_book_ISBN = {book_isbn} ;"
        date_return_str = self.sqlEntry(return_date,receive=True)

        date_issue_time_format = datetime.datetime.strptime(date_issue_str[0][0], '%Y-%m-%d %H:%M:%S')
        date_return_time_format = datetime.datetime.strptime(date_return_str[0][0], '%Y-%m-%d %H:%M:%S')


        timedifference = date_return_time_format - date_issue_time_format

        if timedifference.days > 15 :
            fine = (timedifference.days - 15 ) * 2
            sql_query_to_update_fine = f"Update User_Details set fine = {fine} where UserId = {userid} ;"
            self.sqlEntry(sql_query_to_update_fine)

        else :
            print(f'You have kept the books for {timedifference.days} days and {timedifference.min} minutes and no fine will be charged for it')



    def do_validation(self,user_id,book_name,book_isbn):
        flag = True

        query1_Issue_grt_Return = f"Select count(*) from Issue_Status where Issued_Book_Name = {book_name} and Issued_book_ISBN = {book_isbn} ;"
        issue_count = self.sqlEntry(query1_Issue_grt_Return,receive=True)

        query2_Issue_grt_Return = f"Select count(*) from Return_Status where Return_Book_Name = {book_name} and Returned_book_ISBN = {book_isbn} "
        return_count = self.sqlEntry(query2_Issue_grt_Return,receive=True)

        if issue_count[0][0] < return_count[0][0]:
            flag = False
            return flag,'The return cannot be done as you are returning an item that has already been returned'

        return flag,'No Error'







lib_obj = Library()
user_obj = User()
i_and_r_obj = Issue_And_Return_Books()

while True:

    print('\n 1 : Add Book \n 2: Add User \n 3: Issue And Return Book \n 4:Exit')
    choice = int(input('Enter the choice : '))

    if choice == 1:

        while True:
            print("\n For Adding Books \n 1: Add Entry \n2: View ALL \n3:Search Entry  \n4: Delete Entry \n5 : Exit")
            choice = int(input('Enter the choice : '))

            if choice == 1:
                lib_obj.add_entry_into_table()

            if choice == 2:
                lib_obj.viewAll()

            if choice == 3:
                lib_obj.searchEntry()

            if choice == 4:
                lib_obj.del_selected()

            if choice == 5:
                break

    if choice == 2:

        while True:
            print("\n For Adding User \n 1: Add Entry \n2: View ALL \n3:Search Entry  \n4: Delete Entry \n5 : Exit")
            choice = int(input('Enter the choice : '))

            if choice == 1:
                user_obj.add_entry_into_table()

            if choice == 2:
                user_obj.viewAll()

            if choice == 3:
                user_obj.searchEntry()

            if choice == 4:
                user_obj.del_selected()

            if choice == 5:
                break

    if choice == 3:

        while True:
            print("\n For Issuing And Returning Books \n 1: Issue Status \n2: Return Status \n"
                  "3:Issue Book  \n4: Return Book \n5 : Delete Entry from issue or return \n 6: Exit")
            choice = int(input('Enter the choice : '))

            if choice == 1:
                i_and_r_obj.view_Issue()

            if choice == 2:
                i_and_r_obj.view_Return()

            if choice == 3:
                i_and_r_obj.Issue_Book()

            if choice == 4:
                i_and_r_obj.return_Book()

            if choice == 5:
                i_and_r_obj.del_selected()

            if choice == 6:
                break

    if choice == 4:
        break
