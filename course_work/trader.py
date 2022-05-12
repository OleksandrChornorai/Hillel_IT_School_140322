from argparse import ArgumentParser
import json
import random


class MoneyExchange:
    def __init__(self, config_file, exchange_list):
        self.config_file = config_file
        self.exchanger = exchange_list
        self.read_config()
        self.start_exchange()
        self.exchanger_list()
        self.course = self.exchanger_list()["course"]
        self.uah_acc = self.exchanger_list()["uah_acc"]
        self.usd_acc = self.exchanger_list()["usd_acc"]
        self.delta = self.exchanger_list()["delta"]
        self.change_course()

    def read_config(self):
        with open(self.config_file, 'r') as file:
            config = json.load(file)
            return config

    def start_exchange(self):
        with open(self.exchanger, 'w') as file:
            json.dump(self.read_config(), file, indent=2)

    def exchanger_list(self):
        with open(self.exchanger, 'r') as file:
            exchange = json.load(file)
            return exchange

    def change_course(self):
        new_course = round(random.uniform(self.course - self.delta, self.course + self.delta), 2)
        with open(self.exchanger, 'r') as file:
            data = json.load(file)
            data["course"] = new_course
        with open(self.exchanger, 'w') as file:
            json.dump(data, file)


args = ArgumentParser()
args.add_argument("operation", type=str, nargs='?', default='')
args.add_argument("value", type=float, nargs='?', default='0')
args = vars(args.parse_args())
# print(f'{args["operation"]},{args["value"]}')
config_file = '../Hillel_IT_School_140322/course_work/config.json'
exchange_list = '../Hillel_IT_School_140322/course_work/exchange_list.json'
make_exchange = MoneyExchange(config_file, exchange_list)
result = make_exchange.read_config()
result2 = make_exchange.exchanger_list()
course = make_exchange.exchanger_list()["course"]
uah_acc = make_exchange.exchanger_list()["uah_acc"]
usd_acc = make_exchange.exchanger_list()["usd_acc"]
try:
    moneymaker = MoneyExchange(config_file, exchange_list)
    if args["operation"] == 'RATE':
        print(f'Курс:{course}')
    elif args["operation"] == 'AVAILABLE':
        print(f'UAH:{uah_acc}')
        print(f'USD:{usd_acc}')
    elif args["operation"] == 'NEXT':
        make_exchange.change_course()
    else:
        pass
except ValueError:
    print('ERROR')
# print(result, result2)
# RATE - получение текущего курса (USD/UAH)
# AVAILABLE - получение остатков по счетам
# BUY XXX - покупка xxx долларов. При отсутсвии грвен для покупки выводит сообщение типа UNAVAILABLE, REQUIRED BALANCE UAH 2593.00, AVAILABLE 1000.00
# SELL XXX - продажа xxx долларов. При отсутсвии долларов для продажи выводит сообщение типа UNAVAILABLE, REQUIRED BALANCE USD 200.00, AVAILABLE 135.00
# BUY ALL - покупка долларов на все возможные гривны.
# SELL ALL - продажа всех долларов.
# NEXT - получить следующий курс
# RESTART - начать игру с начала (с начальными условиями)
