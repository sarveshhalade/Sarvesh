
for i in range(1, 101):
    
    if i % 3 == 0:
        print("fizz:",i)

    
    elif i % 5 == 0:
        print("buzz:",i)
     
    elif i % 5 == 0 and i % 3 == 0:
        print("fizz and buzz:",i)
        
        
        # Get the number of rows from the user
n = int(input("Enter the number of rows: "))

# Upper part of the diamond
for i in range(n):
    # Print leading spaces
    print(' ' * (n - i - 1), end='')
    # Print asterisks
    print('*' * (2 * i + 1))

# Lower part of the diamond
for i in range(n - 2, -1, -1):
    # Print leading spaces
    print(' ' * (n - i - 1), end='')
    # Print asterisks
    print('*' * (2 * i + 1))
