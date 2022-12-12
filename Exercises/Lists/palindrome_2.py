string = input().split()
search_palindrome = input()

palindromes = [word for word in string if word == word[::-1]]
search_palindrome_count = palindromes.count(search_palindrome)
print(palindromes)
print(f"Found palindrome {search_palindrome_count} times")
