import random
def the_game():
    x = random.randint(0,500)
    count = 0
    while True:
        try:
            y = int(input("guess a number "))
            count += 1
            if x == y:
                print("good")
                print(count)
                break
            elif x > y:
                print("low")
                continue
            elif x < y:
                print("high")
                continue
            return count
        except Exception as error:
            print(error,"pleas enter a number")

the_game()
