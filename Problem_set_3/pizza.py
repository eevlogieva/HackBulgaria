from time import time
from datetime import datetime


orders = {}
files = []


def main():
    command = input("Enter command> ")
    lst = command.split(" ")
    while True:
        if lst[0] == "take":
            take_orders(lst[1], lst[2])
        elif lst[0] == "status":
            status()
        elif lst[0] == "save":
            save()
        elif lst[0] == "list":
            listing()
        elif lst[0] == "load":
            load(int(lst[1]))
        elif lst[0] == "finnish" and orders:
            print("You have not saved your order." + "\n" +
                  "If you wish to continue, type finish again." +
                  "\n" + "If you want to save your order, type save")
            command = input("Enter command> ")
            lst = command.split(" ")
            if lst[0] == "finnish":
                break
            elif lst[0] == "save":
                save()
            else:
                unknown_command()
        elif lst[0] == "finnish" and not orders:
            break
        else:
            unknown_command()
        command = input("Enter command> ")
        lst = command.split(" ")


def take_orders(name, price):
    print("Taking order from {} for {}".format(name, price))
    if name in orders:
        orders[name] += int(price)
    else:
        orders[name] = int(price)


def status():
    for person in orders:
        print("{} - {}".format(person, orders[person]))


def save():
    ts = time()
    stamp = datetime.fromtimestamp(ts).strftime('%Y_%m_%d_%H_%M_%S')
    file = open("order " + stamp + ".txt", "w")
    for person in orders:
        file.write("{} - {}".format(person, orders[person]) + '\n')
    file.close()
    print("Saved the current order to " + "order " + stamp)
    files.append("order " + stamp)
    orders.clear()


def listing():
    for index, item in enumerate(files):
        print("[" + str(index + 1) + "] " + item)


def load(number):
    if not files:
        print("Use list command before loading")
    if orders:
        print("You have not saved the current order." + "\n" +
              "If you wish to discard it, type load <number> again.")
        command = input("Enter command> ")
        lst = command.split(" ")
        if lst[0] == "load":
            actually_load(int(lst[1]))
    actually_load(number)


def actually_load(number):
    print("Loading " + files[number - 1])
    file = open(files[int(number) - 1] + ".txt", "r")
    for line in file:
        single_order = file.readline().split(" ")
        if single_order[0] in orders:
            orders[single_order[0]] += int(single_order[2])
        else:
            orders[single_order[0]] = int(single_order[2])
    file.close()


def unknown_command():
    print("Unknown command!" + "\n" + "Try one of the following:" +
          "take <name> <price>" + "\n" + "status" + "\n" + "save" +
          "list" + "\n" + "load <number>" + "\n" + "finnish")
if __name__ == "__main__":
    main()
