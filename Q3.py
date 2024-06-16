'''
Max is having a dog . he want  to find the age of the dog  with respect to the age of human.
he came to know that , the age of the  dog is mesured with respect to human  has a formula to proceed. 
example: 1 year of life span of dog is same as seveen years of  life span  of human being
Now , calculate the age of MAX dog.
'''

def calculate_dog_age(dog_age):
    human_age = dog_age * 7
    return human_age

dog_age = int(input("Enter the age of Max's dog: "))
human_age = calculate_dog_age(dog_age)
print("The age of Max's dog in human years is:", human_age)