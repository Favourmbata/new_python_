my_string = ("demigod","write","madam","sales","wrap")

palindrome = list(filter(lambda word: word== word[: : -1],my_string))


print(palindrome)