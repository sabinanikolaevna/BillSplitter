list_of_friends = {}
while True:
    print("Enter the number of friends joining (including you):\n")
    number = int(input())
    if int(number) <= 0:
        print("No one is joining for the party")
        break
    elif int(number) != 0:
        print("Enter the name of every friend (including you), each on a new line:\n")
        for i in range(int(number)):
            name = input()
            list_of_friends[name] = 0
        print("Enter the total bill value:")
        bill = int(input())
        print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
        answer = input()
        if answer == "No":
            print("No one is going to be lucky")
            part = round(int(bill) / int(number), 2)
            for i in list_of_friends:
                list_of_friends[i] = part
            print(list_of_friends)
        elif answer == "Yes":
            number -= 1
            import random
            random_list = list(list_of_friends.keys())
            lucky = random.choice(random_list)
            part = bill / number
            for i in list_of_friends:
                if i == lucky:
                    list_of_friends[i] = 0
                elif i != lucky:
                    list_of_friends[i] = part
            print(f'{lucky} is the lucky one!')
            print(list_of_friends)
        break
