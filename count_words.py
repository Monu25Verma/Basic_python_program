# first type (using build in)
def count_word(string_):
    count = 0
    s = string_.replace(" ", '')
    print(len(s))


count_word("my name is monu mjoh mjeo")


#type two

def count_words(string_):
    count = 0
    for i in string_:
        if i.isalpha() and i != " ":
            count = count + 1
    print("the total number of words in the sentence are:",count)


count_words("my name is monu mjoh mjeo")


