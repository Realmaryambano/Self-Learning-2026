# ================================================================
# SCENARIO-BASED PYTHON PROGRAM
# ================================================================
# QUESTION (SCENARIO):
# You are a first-semester Computer Science student.
# Your university wants a simple console-based "University Library
# Management and Student Activity System" to help beginners learn
# Python programming.
#
# The system should:
# 1. Store student information
# 2. Store book information
# 3. Allow issuing and returning books
# 4. Track simple statistics
# 5. Demonstrate use of:
#    - Variables
#    - Lists
#    - Tuples
#    - Dictionaries
#    - Sets
#    - Strings
#    - Functions
#    - Loops
#    - Conditions
#
# The program is divided into multiple parts.
# EACH PART IS EXPLAINED USING COMMENTS AND FUNCTIONS.
# ================================================================

# ================================================================
# PART 1: GLOBAL DATA STORAGE (USING LISTS, DICTIONARIES, SETS)
# ================================================================

# List to store student names
students = []

# Dictionary to store student details
# Key: student_id, Value: dictionary of details
student_details = {}

# List of books available in the library
books = []

# Dictionary to store book information
# Key: book_id, Value: dictionary of details
book_details = {}

# Dictionary to track issued books
# Key: student_id, Value: list of book_ids
issued_books = {}

# Set to keep track of all unique authors
authors = set()


# ================================================================
# PART 2: UTILITY FUNCTION TO PRINT A LINE
# ================================================================

def print_line():
    print("-" * 60)

# ================================================================
# PART 3: FUNCTION TO ADD A STUDENT
# ================================================================

def add_student(student_id, name, department):
    students.append(name)
    student_details[student_id] = {
        "name": name,
        "department": department
    }
    issued_books[student_id] = []


# ================================================================
# PART 4: FUNCTION TO DISPLAY ALL STUDENTS
# ================================================================

def display_students():
    print_line()
    print("STUDENT LIST")
    print_line()
    for sid, info in student_details.items():
        print("ID:", sid, "| Name:", info["name"], "| Dept:", info["department"])
    print_line()


# ================================================================
# PART 5: FUNCTION TO ADD A BOOK
# ================================================================

def add_book(book_id, title, author, copies):
    books.append(title)
    book_details[book_id] = {
        "title": title,
        "author": author,
        "copies": copies
    }
    authors.add(author)

# ================================================================
# PART 6: FUNCTION TO DISPLAY ALL BOOKS
# ================================================================

def display_books():
    print_line()
    print("BOOK LIST")
    print_line()
    for bid, info in book_details.items():
        print("ID:", bid,
              "| Title:", info["title"],
              "| Author:", info["author"],
              "| Copies:", info["copies"])
    print_line()


# ================================================================
# PART 7: FUNCTION TO ISSUE A BOOK
# ================================================================

def issue_book(student_id, book_id):
    if student_id in student_details and book_id in book_details:
        if book_details[book_id]["copies"] > 0:
            issued_books[student_id].append(book_id)
            book_details[book_id]["copies"] -= 1
            print("Book issued successfully.")
        else:
            print("No copies available.")
    else:
        print("Invalid student ID or book ID.")


# ================================================================
# PART 8: FUNCTION TO RETURN A BOOK
# ================================================================

def return_book(student_id, book_id):
    if book_id in issued_books.get(student_id, []):
        issued_books[student_id].remove(book_id)
        book_details[book_id]["copies"] += 1
        print("Book returned successfully.")
    else:
        print("This book was not issued to the student.")


# ================================================================
# PART 9: FUNCTION TO DISPLAY ISSUED BOOKS
# ================================================================

def display_issued_books():
    print_line()
    print("ISSUED BOOKS")
    print_line()
    for sid, books_list in issued_books.items():
        name = student_details[sid]["name"]
        print("Student:", name, "| Books:", books_list)
    print_line()


# ================================================================
# PART 10: FUNCTION TO DISPLAY AUTHORS (USING SET)
# ================================================================

def display_authors():
    print_line()
    print("AUTHORS IN LIBRARY")
    print_line()
    for author in authors:
        print(author)
    print_line()


# ================================================================
# PART 11: FUNCTION TO SEARCH A BOOK BY TITLE (STRING OPERATIONS)
# ================================================================

def search_book_by_title(keyword):
    print_line()
    print("SEARCH RESULTS FOR:", keyword)
    print_line()
    for info in book_details.values():
        if keyword.lower() in info["title"].lower():
            print(info["title"], "by", info["author"])
    print_line()


# ================================================================
# PART 12: FUNCTION TO COUNT TOTAL BOOK COPIES
# ================================================================

def total_book_copies():
    total = 0
    for info in book_details.values():
        total += info["copies"]
    return total


# ================================================================
# PART 13: FUNCTION TO SHOW LIBRARY STATISTICS
# ================================================================

def library_statistics():
    print_line()
    print("LIBRARY STATISTICS")
    print_line()
    print("Total Students:", len(students))
    print("Total Book Titles:", len(books))
    print("Total Book Copies:", total_book_copies())
    print("Total Authors:", len(authors))
    print_line()


# ================================================================
# PART 14: FUNCTION USING TUPLES (DEMO PURPOSE)
# ================================================================

def university_info():
    info = ("ABC University", "Computer Science Department", 2026)
    print_line()
    print("UNIVERSITY INFORMATION")
    print_line()
    print("Name:", info[0])
    print("Department:", info[1])
    print("Year:", info[2])
    print_line()


# ================================================================
# PART 15: INITIAL DATA SETUP
# ================================================================

add_student(1, "Alice", "CS")
add_student(2, "Bob", "CS")
add_student(3, "Charlie", "IT")

add_book(101, "Python Programming", "John Smith", 3)
add_book(102, "Data Structures", "Jane Doe", 2)
add_book(103, "Computer Networks", "Andrew Tanenbaum", 1)



# ================================================================
# PART 16: SIMULATED OPERATIONS
# ================================================================

display_students()
display_books()

issue_book(1, 101)
issue_book(2, 102)
issue_book(1, 102)
issue_book(3, 103)

display_issued_books()
display_books()

return_book(1, 101)
display_books()

search_book_by_title("python")
display_authors()
library_statistics()
university_info()



# ================================================================
# PART 17: LOOP PRACTICE FOR BEGINNERS
# ================================================================

print_line()
print("LOOP PRACTICE: COUNTING NUMBERS")
print_line()
for i in range(1, 11):
    print("Number:", i)
print_line()



# ================================================================
# PART 18: STRING MANIPULATION PRACTICE
# ================================================================

sample_string = "Learning Python is Fun"
print_line()
print("STRING OPERATIONS")
print_line()
print("Original:", sample_string)
print("Uppercase:", sample_string.upper())
print("Lowercase:", sample_string.lower())
print("Word Count:", len(sample_string.split()))
print_line()


# ================================================================
# PART 19: LIST OPERATIONS PRACTICE
# ================================================================

print_line()
print("LIST OPERATIONS")
print_line()
print("Students List:", students)
students.sort()
print("Sorted Students:", students)
students.append("David")
print("After Adding:", students)
print_line()


# ================================================================
# PART 20: DICTIONARY OPERATIONS PRACTICE
# ================================================================

print_line()
print("DICTIONARY OPERATIONS")
print_line()
for sid in student_details:
    print("Student ID:", sid, "Details:", student_details[sid])
print_line()


# ================================================================
# PART 21: SET OPERATIONS PRACTICE
# ================================================================

print_line()
print("SET OPERATIONS")
print_line()
new_authors = {"John Smith", "New Author"}
all_authors = authors.union(new_authors)
print("All Authors:", all_authors)
print_line()


# ================================================================
# PART 22: FUNCTION CALLING ANOTHER FUNCTION
# ================================================================

def full_report():
    university_info()
    library_statistics()
    display_students()
    display_books()

full_report()

