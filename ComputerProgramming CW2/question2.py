#creating a class and it's attributes using a constructer for initializing the parameters
class Book:
    def __init__(self,title,author,year_published):
        self.title=title
        self.author=author
        self.year_published=year_published

    def describe(self,description):#creating a method for output displaywith another variable created in its parethesis description
        print('Book title: ',self.title,'\n','The author:',self.author,'\n','Year_published: ',self. year_published,'\n','Description: ',description)

# class classname:
#     def constructer method(self,parameteres for class):
#         self.title=parameter

#     def method_name(self,varable if needed):
#         print(output desired )

#creating objects and calling the class book so that they can use its attributes/ the class resorces
book1=Book('lifestyle','tino','2024')#creating objects to use the class methods
book2=Book('legendary','akol','2023')
book1.describe('its when i was born')
book2.describe('we either code today or debug forever')#displaying the object description in the output section 
print('................')

#creating a function for sorting books by the year published
def sort_books_by_year(books):
    if books==[]:#checking for an empty list input
        raise TypeError("Input must be a list.")#if above condition is true this should be an output error
    else:
        return sorted(books, key=lambda book: book.year_published)#otherwise this should be output
        
print('here is a sample of books available sorted by year they were published') 
books=[book1,book2]#sample input for a list
sort_books_by_year(books)#calling the sorted function which just creates a duplicate of the original list but in a sorted manner
try: #trying to capture an error  
    sorted_books=sort_books_by_year(books)

except Exception as e:#the error captured should be kept in a variable e
    print('there is an issue with your entries: ',e)#error captured should be concatenated to the print string and e

for book in sorted_books:#using a for loop to print items in a list one at a time
    print(book.title,book.author,book.year_published)

#using the while loop to iterate the books and their description in terminal one at a time
print('sorted by while\n')
book_number=0
while book_number < len(sorted_books):
    book=sorted_books[book_number]
    print(book.title,book.author,book.year_published)
    book_number +=1

#creating a method that prompts a user tho search a book from the existing collection by tittle 
def search_book_by_title(books,title):#function name and variables in parenthesis
    for book in books:#using the foor loop to iterate a single book from the list but it only displays the book description if the user input matches one of the existing books in the list
        if book.title.lower()==title.lower():#the input should be changed to lowercase
            print('book found')
            print(book.describe('this is it'))
        else:
            print('book not found')

while True:#infinite looping to allow the user to have multiple chances to search a book unless the user is no longer interested in searching and inputs exit thats when the loop will be jumped out
    user_search_input=input('would you like to search a book by title to check in our library collection: ')
    if user_search_input=="exit":
        help=input('anything else you would like assistance with: ')
        if help.lower()=='nothing':
            print('i hope we were of help to you')
            print('thankyou for interacting with us\n see you soon')
        break

    search_book_by_title(books,user_search_input)#calling the function for use
    


