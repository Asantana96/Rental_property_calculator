import time


class Rental_Property_Cal():
    income = {
        'Income': 0,
        'misc': 0
    }
    expenses = {
        'taxes': 0,
        'utilities': 0,
        'insurance': 0,
    }
    total_i = 0
    total_e = 0
    investment = {
        'down payment': 0,
        'closing cost': 0,
        'rehab budget': 0
    }
    total_invest = 0

    def driver(self):
        # welcome message
        print("""______ _                        ______          _        _              
| ___ (_)                       | ___ \        | |      | |             
| |_/ /_  __ _  __ _  ___ _ __  | |_/ /__   ___| | _____| |_ ___        
| ___ \ |/ _` |/ _` |/ _ \ '__| |  __/ _ \ / __| |/ / _ \ __/ __|       
| |_/ / | (_| | (_| |  __/ |    | | | (_) | (__|   <  __/ |_\__ \       
\____/|_|\__, |\__, |\___|_|    \_|  \___/ \___|_|\_\___|\__|___/       
          __/ | __/ |                                                   
         |___/ |___/                                                    
______           _        _  ______                          _          
| ___ \         | |      | | | ___ \                        | |         
| |_/ /___ _ __ | |_ __ _| | | |_/ / __ ___  _ __   ___ _ __| |_ _   _  
|    // _ \ '_ \| __/ _` | | |  __/ '__/ _ \| '_ \ / _ \ '__| __| | | | 
| |\ \  __/ | | | || (_| | | | |  | | | (_) | |_) |  __/ |  | |_| |_| | 
\_| \_\___|_| |_|\__\__,_|_| \_|  |_|  \___/| .__/ \___|_|   \__|\__, | 
                                            | |                   __/ | 
                                            |_|                  |___/  
 _____       _            _       _                                     
/  __ \     | |          | |     | |                                    
| /  \/ __ _| | ___ _   _| | __ _| |_ ___  _ __                         
| |    / _` | |/ __| | | | |/ _` | __/ _ \| '__|                        
| \__/\ (_| | | (__| |_| | | (_| | || (_) | |                           
 \____/\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|                           
                                                                        
                                                                            """)
        welcome = input(
            'To commence calculating the ROI of your rental property, kindly press enter')

        if welcome.lower() == "":
            name = input(
                'Before we proceed, could you provide me with your first name:\n')
            name = name.capitalize()
            initiation = input(f"\nThank you, {name}. To ensure precise calculation of the ROI of your rental property,\nWe will be asking you a series of questions.\nPlease provide accurate information to obtain the most precise results.\n\nPress enter to continue\nEnter 'back' to return to the previous prompt or enter 'q' to quit:")
            if initiation == '':
                self.pass_income()

            elif initiation.lower() == "back":
                time.sleep(1)
                self.driver()
            elif initiation.lower() == 'q':
                time.sleep(1)
                print('Good-Bye')
                time.sleep(2)
                self.driver()
            else:
                time.sleep(1)
                print('Invalid entry, please try again')
                self.driver()

        elif welcome.lower() == "back":
            time.sleep(1)
            self.driver()

        elif welcome.lower() == 'q':
            time.sleep(1)
            print('Good-Bye')
            self.driver()
        else:
            time.sleep(1)
            print('Invalid entry, please try again')
            self.driver()

    def pass_income(self):
        income_question = input("\nPlease enter your monthly passive income: ")
        if income_question.isdigit():
            Rental_Property_Cal.income['Income'] = int(income_question)
            misc_question = input(
                "\nEnter any other miscellaneous income, if none enter 0: ")
            if income_question.isdigit():
                Rental_Property_Cal.income['misc'] = int(misc_question)
                self.expense()
            else:
                print('\nInvalid input, please try again.')
                self.pass_income
        else:
            print('\nInvalid input, please try again.')
            self.pass_income

    def expense(self):
        print('\nNow that we have determine your monthly passive income, lets take a look at your expenses. ')
        time.sleep(1)
        ex = input('\nPlease enter your monthly taxes: ')
        if ex.isdigit():
            Rental_Property_Cal.expenses['taxes'] = int(ex)
            utilities = input('\nPlease enter the amount of your utilities.')
            if utilities.isdigit():
                Rental_Property_Cal.expenses['utilities'] = int(utilities)
                insurance = input(
                    '\nTo finish with your expenses please provide your monthly insurance cost. ')
                if insurance.isdigit():
                    Rental_Property_Cal.expenses['insurance'] = int(insurance)
                    self.cash_flow()
                else:
                    print('\nInvalid input, please try again.')
                    self.expense()
            else:
                print('\nInvalid input, please try again.')
                self.expense()
        else:
            print('\nInvalid input, please try again.')
            self.expense()

    def cash_flow(self):
        print('\nEverything looks good! We now calculate your Cash Flow.')
        time.sleep(1)
        print('\ncalculating...')
        time.sleep(1)
        total_i = sum(Rental_Property_Cal.income.values())
        total_e = sum(Rental_Property_Cal.expenses.values())
        c_f = total_i - total_e
        print(f'\nYour Cash Flow is {c_f}!')
        self.ROI()

    def ROI(self):
        time.sleep(1)
        print('\nWe\'re almost done!\nLet\'s get some information on your initial investment. ')
        time.sleep(.5)
        down_pay = input(
            '\nHow much did you put down on your rental property? ')
        time.sleep(.5)
        if down_pay.isdigit():
            Rental_Property_Cal.investment['down payment'] = int(down_pay)
            closing = input("\nWhat were your closing cost? ")
            time.sleep(.5)
            if closing.isdigit():
                Rental_Property_Cal.investment['closing cost'] = int(closing)
                rehab = input("\nHow much were your rehab costs? ")
                if rehab.isdigit():
                    Rental_Property_Cal.investment['rehab budget'] = int(rehab)
                    self.calculate()

                else:
                    print('\nInvalid input, please try again.')
                    self.ROI()

            else:
                print('\nInvalid input, please try again.')
                self.ROI()
        else:
            print('\nInvalid input, please try again.')
            self.ROI()

    def calculate(self):
        time.sleep(.5)
        print('\nLets calculate your ROI.')
        time.sleep(1)
        print('\ncalculating...')
        time.sleep(1)
        total_i = sum(Rental_Property_Cal.income.values())
        total_e = sum(Rental_Property_Cal.expenses.values())
        annual_c_f = (total_i - total_e) * 12
        total_invest = sum(Rental_Property_Cal.investment.values())
        roi = annual_c_f/total_invest
        print(f'\nYour ROI is {roi}!!')
        time.sleep(4)
        print('Thank you for using Bigger Pockets Rental Property Calculator!')
        time.sleep(6)
        self.driver()


test = Rental_Property_Cal()
test.driver()
