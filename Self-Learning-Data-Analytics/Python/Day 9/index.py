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
