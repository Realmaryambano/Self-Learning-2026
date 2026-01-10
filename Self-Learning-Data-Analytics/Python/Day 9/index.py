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
