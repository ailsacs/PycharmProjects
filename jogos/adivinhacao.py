print("****************************************")
print("Bem-vindo ao jogo de adivinhação")
print("welcome to the game of guessing!")
print("****************************************")

from random import randint
secret_number = randint(1,10)
total_try = 3
try_= 1

while(try_ <= total_try):
    print("try", try_, "de", total_try)
    kick = int(input("type your number: "))
    answer = (print("you typed: ", kick))

    right = kick == secret_number
    smaller = kick < secret_number
    more = kick > secret_number

    if(right):
        print("you're right!")
    else:
        if(more):
            print("you missed! the your kick was more than the secret number.")
        elif(smaller):
            print("you missed! the your kick was smaller than the secret number.")

    try_ = try_ + 1

print ("The secret number is ", secret_number)
print("Congratulations!")
print("This is getting fun, haha!")
print("END GAME!!")