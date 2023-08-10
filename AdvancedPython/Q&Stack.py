# Raj Shah CIST005B Queue & Stack Palindromes
# Will check if a word is a palindrome using stack and queue

word = input("Enter a word here: ")
queue = []
stack = []
is_palindrome = True

for letter in word:
    queue.append(letter)
    stack.append(letter)

for i in range(len(word)):
    if (queue[i] != stack[len(word) - i - 1]):
        is_palindrome = False
        break

if (is_palindrome):
    print(word + " is a palindrome.")
else:
    print(word + " is not a palindrome.")

'''
Enter a word here: racecar
racecar is a palindrome.

Process finished with exit code 0

Enter a word here: palindrome
palindrome is not a palindrome.

Process finished with exit code 0
'''
