class CoffeeMachine:

    def __init__(self, water, milk, beans, cups, cash):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.cash = cash

    def get_status(self):
        return """The coffee machine has:
{} of water
{} of milk
{} of coffee beans
{} of disposable cups
${} of money """.format(self.water, self.milk, self.beans, self.cups, self.cash)

    def buy_espresso(self):
        if self.water < 250:
            print('I have enough resources, making you a coffee!')
        elif self.beans < 16:
            print('I have enough resources, making you a coffee!')
        elif self.cups < 1:
            print('I have enough resources, making you a coffee!')
        else:
            self.water -= 250
            self.beans -= 16
            self.cups -= 1
            self.cash += 4

    def buy_latte(self):
        if self.water < 350:
            print('I have enough resources, making you a coffee!')
        elif self.milk < 75:
            print('I have enough resources, making you a coffee!')
        elif self.beans < 20:
            print('I have enough resources, making you a coffee!')
        elif self.cups < 1:
            print('I have enough resources, making you a coffee!')
        else:
            self.water -= 350
            self.milk -= 75
            self.beans -= 20
            self.cups -= 1
            self.cash += 7

    def buy_cappuccino(self):
        if self.water < 200:
            print('I have enough resources, making you a coffee!')
        elif self.milk < 100:
            print('I have enough resources, making you a coffee!')
        elif self.beans < 12:
            print('I have enough resources, making you a coffee!')
        elif self.cups < 1:
            print('I have enough resources, making you a coffee!')
        else:
            self.water -= 200
            self.milk -= 100
            self.beans -= 12
            self.cups -= 1
            self.cash += 6

    def fill(self):
        print('Write how many ml of water do you want to add:')
        water_fill = int(input())
        self.water = self.water + water_fill
        print('Write how many ml of milk do you want to add:')
        milk_fill = int(input())
        self.milk = self.milk + milk_fill
        print('Write how many grams of coffee beans do you want to add:')
        beans_fill = int(input())
        self.beans = self.beans + beans_fill
        print('Write how many disposable cups of coffee do you want to add:')
        cups_fill = int(input())
        self.cups = self.cups + cups_fill

    def take(self):
        print('I gave you ${}'.format(self.cash))
        self.cash = 0


coffee_machine1 = CoffeeMachine(400, 540, 120, 9, 550)

#print(coffee_machine1.get_status())


while True:
    print('Write action (buy, fill, take, remaining, exit):')
    action = str(input())
    print()
    if action == 'buy':
        print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:')
        coffee_type = str(input())
        if coffee_type == '1':
            coffee_machine1.buy_espresso()
            print()
            continue
        elif coffee_type == '2':
            coffee_machine1.buy_latte()
            print()
            continue
        elif coffee_type == '3':
            coffee_machine1.buy_cappuccino()
            print()
            continue

    elif action == 'fill':
        coffee_machine1.fill()
        print()
        continue

    elif action == 'take':
        coffee_machine1.take()
        print()
        continue

    elif action == 'exit':
        break

    elif action == 'remaining':
        print(coffee_machine1.get_status())
        print()
        continue
