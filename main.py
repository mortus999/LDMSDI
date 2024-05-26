from library import Library

def main():
    library = Library()
    print()
    print("Welcome to the LMSDI!")
    
    while True:
        print()
        main_menu_option = input("""Please enter the number assigned to your desired choice:
            Menu:
            1 - Book Operations
            2 - User Operations
            3 - Author Operations 
            4 - Genre Operations 
            5 - Exit
            """)
        print()
        if main_menu_option == "1":    
            book_opp_choice = input("""Please enter the number assigned to your desired choice:
                Menu:
                1 - Add book
                2 - Checkout book
                3 - Return Book
                4 - Search for a book
                5 - Display all books
                6 - Exit
                """)
            try: 
                if book_opp_choice == "1":
                    library.add_book()
                
                elif book_opp_choice == "2":
                    library.checkout_book()
                
                elif book_opp_choice == "3":
                    library.return_book()
                
                elif book_opp_choice == "4":
                    library.search_for_book()
                    
                elif book_opp_choice == "5":
                    library.display_books()
                    
                elif book_opp_choice == "6":
                    print("Returning to main menu.")
                
                else:
                    print("Please enter a valid choice")
            
            except Exception as e:
                print(f"An error occurred: {e}")
        
        elif main_menu_option == "2":
            user_opp_choice = input("""Below is a Menu for you to select from. Please enter the number assigned to your desired choice:
                Menu:
                1 - Add new user
                2 - View user details
                3 - Display all users
                4 - Display user's borrowed books 
                5 - Exit
                """)
            try:
                if user_opp_choice == "1":
                    library.add_user()
                
                elif user_opp_choice == "2":
                    library.view_user_details()
                
                elif user_opp_choice == "3":
                    library.display_users()
                    
                elif user_opp_choice == "4":
                    library.borrowed_books()

                elif user_opp_choice == "5":
                    print("Returning to main menu.")
                
                else:
                    print("Please enter a valid choice")
            
            except Exception as e:
                print(f"An error occurred: {e}")
                
        elif main_menu_option == "3":
            author_opp_choice = input("""Below is a Menu for you to select from. Please enter the number assigned to your desired choice:
                Menu:
                1 - Add new author
                2 - View author details
                3 - Display all authors
                4 - Exit
                """)
            try:
                if author_opp_choice == "1":
                    library.add_author()
                
                elif author_opp_choice == "2":
                    library.view_author_details()
                
                elif author_opp_choice == "3":
                    library.display_authors()

                elif author_opp_choice == "4":
                    print("Returning to main menu.")
                
                else:
                    print("Please enter a valid choice")
            
            except Exception as e:
                print(f"An error occurred: {e}")
                
        elif main_menu_option == "4":
            genre_opp_choice = input("""Below is a Menu for you to select from. Please enter the number assigned to your desired choice:
                Menu:
                1 - Add new genre
                2 - View genre details
                3 - Display all genres
                4 - Exit
                """)
            try:
                
                if genre_opp_choice == "1":
                    library.add_genre()
                
                elif genre_opp_choice == "2":
                    library.view_genre_details()
                
                elif genre_opp_choice == "3":
                    library.display_genres()

                elif genre_opp_choice == "4":
                    print("Returning to main menu.")
                
                else:
                    print("Please enter a valid choice")
            
            except Exception as e:
                print(f"An error occurred: {e}")
                
        elif main_menu_option == "5":
            print("Thanks for supporting your public library! Have a nice day!")
            break
        else:
            print("You entered an invalid selection")

if __name__ == "__main__":
    main()