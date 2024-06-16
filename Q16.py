'''You work in the message encoding department of a national security agency. Every message
that is sent from or received in your office is encoded. you have a string containing , alpha numeric characters.
of N is squared and the squares are concatenated together to encode the original number.
Your task is to find and return an integer value representing the encoded value of the
number.
input1: An a string  representing the number and chracters 
Output :
Return an integer value representing the encoded value of the number
input format:
"hello 123 good morning"
output:
149  '''

def encode_number(s):
    num_str = ''.join(filter(str.isdigit, s))
    num = int(num_str)
    encoded_num = int(str(num ** 2))
    return encoded_num

input_str = "hello 123 good morning"
print(encode_number(input_str))  # Output: 149
   