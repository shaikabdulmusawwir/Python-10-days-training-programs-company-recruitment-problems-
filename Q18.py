'''input: hello programmers how are you
   output: the number of Spaces are at indices: [5, 6]'''

''''input_string = input("Enter a string: ")

spaces = [i for i, char in enumerate(input_string) if char == ' ']

print("Spaces are at indices:", spaces)'''

def countOfSpace(string):
    count = 0
    for i in string:
        if i == ' ':
            count +=1
    return count
string = input()
print(countOfSpace(string)) 