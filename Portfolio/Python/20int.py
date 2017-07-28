#Write a program that computes the sum of the first 20 positive integers
#def sumInts():
#  Your code here
#for i in range(21):
    #sum = sum + i
    #print(sum)
#def main():
#sum = sumInts()
#1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,

#main()
y = int(input("What do you want you range to be?"))

def sumInts(r):
    x = 0
    for i in range(r):
        x += i
    return x
def main():
        print(sumInts(y))


main()
