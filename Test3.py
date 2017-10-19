def main():
    quest = input("Enter a Celsius Temperature :")

    if quest[-1] == 'C':
        celsius = int(quest[:-1])
    else:
        celsius = int(quest)

    final = 9 / 5 * celsius + 32
    print(celsius,"C is",final,"F")
main()