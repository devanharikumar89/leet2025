class PythonCheatSheet:
    """
    A Python cheat sheet class that demonstrates common Python syntax and constructs.
    Use this class as a quick reference for Python basics.
    """

    def data_types(self):
        # Basic data types
        integer = 10
        floating_point = 3.14
        string = "Hello, Python!"
        boolean = True
        none_type = None

    def collections(self):
        # Common collections
        my_list = [1, 2, 3]          # List
        my_tuple = (1, 2, 3)        # Tuple
        my_set = {1, 2, 3}          # Set
        my_dict = {"key": "value"}  # Dictionary

    def data_structures(self):
        # Priority Queue
        import heapq
        pq = []
        heapq.heappush(pq, 10)
        heapq.heappush(pq, 5)
        heapq.heappush(pq, 15)
        print(heapq.heappop(pq))  # Output: 5 (smallest element)

        # Stack
        stack = []
        stack.append(1)  # Push
        stack.append(2)
        stack.append(3)
        print(stack.pop())  # Output: 3 (Last in, first out)

        # Queue
        from collections import deque
        queue = deque()
        queue.append(1)  # Enqueue
        queue.append(2)
        queue.append(3)
        print(queue.popleft())  # Output: 1 (First in, first out)

        # Linked List
        class Node:
            def __init__(self, value):
                self.value = value
                self.next = None

        class LinkedList:
            def __init__(self):
                self.head = None

            def append(self, value):
                if not self.head:
                    self.head = Node(value)
                    return
                current = self.head
                while current.next:
                    current = current.next
                current.next = Node(value)

            def display(self):
                current = self.head
                while current:
                    print(current.value, end=" -> ")
                    current = current.next
                print("None")

        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)
        ll.display()  # Output: 1 -> 2 -> 3 -> None

        # HashMap
        hashmap = {}
        hashmap["key1"] = "value1"
        hashmap["key2"] = "value2"
        print(hashmap["key1"])  # Output: value1
        print("key2" in hashmap)  # Check existence (Output: True)

    def control_structures(self):
        # If-else
        x = 10
        if x > 5:
            print("x is greater than 5")
        elif x == 5:
            print("x is 5")
        else:
            print("x is less than 5")

        # Loops
        for i in range(5):
            print(i)

        while x > 0:
            print(x)
            x -= 1

    def functions(self):
        # Function definition
        def add(a, b):
            return a + b

        # Lambda function
        square = lambda x: x ** 2
        print(square(5))  # Output: 25

        # Lambda with multiple parameters
        multiply = lambda a, b: a * b
        print(multiply(3, 4))  # Output: 12

        # Using lambda with filter, map, and reduce
        nums = [1, 2, 3, 4, 5]

        # Filter: Keep only even numbers
        even_nums = list(filter(lambda x: x % 2 == 0, nums))
        print(even_nums)  # Output: [2, 4]

        # Map: Square each number
        squared_nums = list(map(lambda x: x ** 2, nums))
        print(squared_nums)  # Output: [1, 4, 9, 16, 25]

        # Reduce: Sum all numbers (requires functools)
        from functools import reduce
        total = reduce(lambda x, y: x + y, nums)
        print(total)  # Output: 15

    def classes(self):
        # Class and object example
        class MyClass:
            def __init__(self, name):
                self.name = name

            def greet(self):
                return f"Hello, {self.name}!"

        obj = MyClass("Python")
        print(obj.greet())

    def comprehensions(self):
        # List comprehension
        squares = [x ** 2 for x in range(10)]

        # Dictionary comprehension
        square_dict = {x: x ** 2 for x in range(10)}

        # Set comprehension
        square_set = {x ** 2 for x in range(10)}

    def file_operations(self):
        # File handling
        with open("example.txt", "w") as f:
            f.write("Hello, file!")

        with open("example.txt", "r") as f:
            content = f.read()
            print(content)

    def error_handling(self):
        # Try-except
        try:
            result = 10 / 0
        except ZeroDivisionError as e:
            print("Error:", e)
        finally:
            print("Execution finished.")

    def miscellaneous(self):
        # Importing modules
        import math
        print(math.sqrt(16))

        # Using decorators
        def decorator(func):
            def wrapper(*args, **kwargs):
                print("Before function call")
                result = func(*args, **kwargs)
                print("After function call")
                return result
            return wrapper

        @decorator
        def say_hello():
            print("Hello!")

        @decorator
        def add_numbers(a, b):
            return a + b

        say_hello()
        result = add_numbers(5, 10)
        print(f"Result of add_numbers: {result}")

        # Decorators with arguments
        def repeat(times):
            def decorator(func):
                def wrapper(*args, **kwargs):
                    for _ in range(times):
                        func(*args, **kwargs)
                return wrapper
            return decorator

        @repeat(3)
        def greet():
            print("Greetings!")

        greet()

    def string_manipulation(self):
        # String basics
        s = "   Hello, Python!   "
        print(s.lower())            # Convert to lowercase
        print(s.upper())            # Convert to uppercase
        print(s.title())            # Title case
        print(s.strip())            # Remove leading and trailing whitespace
        print(s.lstrip())           # Remove leading whitespace
        print(s.rstrip())           # Remove trailing whitespace
        print(s.strip("!"))         # Remove specific character from ends

        # String formatting
        name = "Alice"
        age = 30
        print(f"My name is {name} and I am {age} years old.")  # f-string
        print("My name is {} and I am {} years old.".format(name, age))  # format method

        # Splitting and joining
        words = s.split()           # Split into list
        print(words)
        print(" ".join(words))      # Join list into string

        # String searching and replacing
        print(s.find("Python"))     # Find substring
        print(s.replace("Python", "World"))  # Replace substring

        # Checking string content
        print(s.startswith("Hello"))  # Check if starts with substring
        print(s.endswith("Python!"))  # Check if ends with substring
        print(s.strip().isdigit())  # Check if the stripped string is numeric

        # Multi-line strings
        multi_line = """This is a
        multi-line string."""
        print(multi_line)

        # String slicing
        print(s[0:5])              # Slice from index 0 to 4 (inclusive)
        print(s[:5])               # Slice from start to index 4 (inclusive)
        print(s[7:])               # Slice from index 7 to the end
        print(s[-6:])              # Slice the last 6 characters
        print(s[::2])              # Slice with a step of 2
        print(s[::-1])             # Reverse the string

    def datetime_stuff(self):
        # Prints today's date with help
        # of datetime library
        import datetime
        today = datetime.datetime.today()
        print(f"{today:%B %d, %Y}")

# Example usage
if __name__ == "__main__":
    cheat_sheet = PythonCheatSheet()
    cheat_sheet.data_types()
    cheat_sheet.collections()
    cheat_sheet.data_structures()
    cheat_sheet.control_structures()
    cheat_sheet.functions()
    cheat_sheet.classes()
    cheat_sheet.comprehensions()
    cheat_sheet.file_operations()
    cheat_sheet.error_handling()
    cheat_sheet.miscellaneous()
    cheat_sheet.string_manipulation()
    cheat_sheet.datetime_stuff()
