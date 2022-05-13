from argparse import ArgumentParser
import json
import random


def read_config(config_file):
    with open(config_file, 'r') as file:
        config = json.load(file)
        return config


def read_exchange_list(exchange_list):
    with open(exchange_list, 'r') as file:
        exchange = json.load(file)
        return exchange


def change_course(exchange_list):
    with open(exchange_list, 'r') as file:
        data = json.load(file)
        course = data["course"]
        delta = data["delta"]
        new_course = round(random.uniform(course - delta, course + delta), 2)
        data["course"] = new_course
    with open(exchange_list, 'w') as file:
        json.dump(data, file, indent=2)


def buy_sell(exchange_list, args, operation):
    with open(exchange_list, 'r') as file:
        data = json.load(file)
        new_uah = data["uah_acc"]
        new_usd = data["usd_acc"]
        if operation == 'BUY':
            if data["uah_acc"] >= float(args["value"]) * data["course"]:
                buyer = float(args["value"]) * data["course"]
                new_uah = data["uah_acc"] - buyer
                new_usd = data["usd_acc"] + float(args["value"])
            else:
                print(f'UNAVAILABLE, REQUIRED BALANCE UAH {args["value"] * data["course"]}, AVAILABLE {data["uah_acc"]}')
        elif operation == 'SELL':
            if data["usd_acc"] >= float(args["value"]):
                buyer = float(args["value"]) * data["course"]
                new_uah = data["uah_acc"] + buyer
                new_usd = data["usd_acc"] - float(args["value"])
            else:
                print(f'UNAVAILABLE, REQUIRED BALANCE USD {args["value"]}, AVAILABLE {data["usd_acc"]}')
        data["uah_acc"] = new_uah
        data["usd_acc"] = new_usd
    with open(exchange_list, 'w') as file:
        json.dump(data, file, indent=2)


def buy_sell_all(exchange_list, operation):
    with open(exchange_list, 'r') as file:
        data = json.load(file)
        new_uah = data["uah_acc"]
        new_usd = data["usd_acc"]
        if operation == 'BUY':
            new_usd = data["uah_acc"] / data["course"]
            new_uah = 0
        elif operation == 'SELL':
            new_uah = data["usd_acc"] * data["course"]
            new_usd = 0
        data["uah_acc"] = new_uah
        data["usd_acc"] = new_usd
    with open(exchange_list, 'w') as file:
        json.dump(data, file, indent=2)


def restart_exchange(config_file, exchange_list):
    with open(config_file, 'r') as file:
        config = json.load(file)
    with open(exchange_list, 'w') as file:
        json.dump(config, file, indent=2)


args = ArgumentParser()
args.add_argument("operation", type=str, nargs='?', default='')
args.add_argument("value", nargs='?', default='0')
args = vars(args.parse_args())
config_file = '../Hillel_IT_School_140322/course_work/config.json'
exchange_list = '/Users/AleksandrCh/PycharmProjects/Hillel_IT_School_140322/course_work/exchange_list.json'
read_list = read_exchange_list(exchange_list)
real_course = read_exchange_list(exchange_list)["course"]
uah_acc = read_exchange_list(exchange_list)["uah_acc"]
usd_acc = read_exchange_list(exchange_list)["usd_acc"]
if args["operation"] == 'RATE':
    print(f'Курс: {real_course}')
elif args["operation"] == 'AVAILABLE':
    print(f'UAH: {uah_acc}')
    print(f'USD: {usd_acc}')
elif args["operation"] == 'BUY':
    if args["value"] == 'ALL':
        buy_sell_all(exchange_list, 'BUY')
    elif float(args["value"]) > 0:
        buy_sell(exchange_list, args, 'BUY')
elif args["operation"] == 'SELL':
    if args["value"] == 'ALL':
        buy_sell_all(exchange_list, 'SELL')
    elif float(args["value"]) > 0:
        buy_sell(exchange_list, args, 'SELL')
elif args["operation"] == 'NEXT':
    change_course(exchange_list)
elif args["operation"] == 'RESTART':
    restart_exchange(config_file, exchange_list)
else:
    pass
