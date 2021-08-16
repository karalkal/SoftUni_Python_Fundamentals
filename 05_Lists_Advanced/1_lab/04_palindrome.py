words_list = input().split()
find_this = input()
palindrome_list = []
for w in range(len(words_list)):
    if words_list[w] == words_list[w][::-1]:
        palindrome_list.append(words_list[w])
print(palindrome_list)
counted = palindrome_list.count(find_this)
print(f"Found palindrome {counted} times")
