'''with open("data.txt", "w") as file:
    file.write("Hello, World!\n" "python is great!\n" "Let's write some data to a file.\n""file handling is important in programming.\n" "Hello, World!\n" "python is great!\n" "Let's write some data to a file.\n""file handling is important in programming.\n")

with open("data.txt", "r") as file:

    content = file.read()
    count ={} 
    for word in content.split():
        if word in count:
            count[word] += 1
        else:
            count[word] = 1

max_frequency = float('-inf')

for word, frequency in count.items():
     if frequency > max_frequency:
         max_frequency = frequency

print(f"Maximum frequency: {max_frequency} {word}, Word(s) with maximum frequency: ", end="")


with open ("data.txt","r") as file:

    content=file.read()

    count=0

    for line in content.splitlines():
        count+=1

    print(f"Total number of lines in the file: {count}")
    count ={}
    for word in content.split():
        if word in count:
            count[word] += 1
        else:
            count[word] = 1

    print(f"Total number of words in the file: {len(content.split())}")

with open ("myfile.txt","w") as file:

    file.write("python docker kubernetes linux jenkins")

with open("myfile.txt","r") as file:
    content=file.read()
    print(content)

    max_len=0

    for word in content.split():
        if len(word)>max_len:
            max_len=len(word)
            max_word=word

    print(f"Longest word: {max_word}, Length: {max_len}")


with open("myfile.txt", "r") as file:
    content = file.read()

    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0

    for word in content.split():
        for char in word:
            if char.isalpha():
                if char in vowels:
                    vowel_count += 1
                else:
                    consonant_count += 1

    print(f"Total vowels: {vowel_count}")
    print(f"Total consonants: {consonant_count}")


with open("myfile.txt", "r") as file:
    content = file.read()
    print(content)

    max_len=0
    semax_len=0
    max_word=""
    semax_word=""


    for word in content.split():
        if len(word)>max_len:
            semax_len=max_len
            semax_word=max_word
            max_len=len(word)
            max_word=word
        elif len(word)>semax_len:
            semax_len=len(word)
            semax_word=word

            print(f"Longest word: {max_word}, Length: {max_len}")
            print(f"Second longest word: {semax_word}, Length: {semax_len}")'''


'''with open ("content.txt","w") as file:
    file.write("python\n")
    file.write("docker\n")
    file.write("kubernetes\n")
    file.write("linux\n")
    file.write("jenkins\n")'''

with open("content.txt", "r") as file:
    content = file.read()
    print(content)

    for word in content.splitlines():
        reverse_word = word[::-1]

        print(f"Original word: {word}, Reversed word: {reverse_word}")



