#!/usr/bin/env python3
import requests, time, socket


def is_connected():
    Connected = False

    while Connected == False:
        try:
            # connect to the host -- tells us if the host is actually
            # reachable
            socket.create_connection(("1.1.1.1", 53))
            response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
            data = response.json()
            rate = int(data["bpi"]["USD"]["rate_float"])
            rate = round(rate, 0)
            rate = "{:,}".format(rate)
            print(f"^c#D19A66^[:$"+rate+"]")
            break
            Connected = True    
        except OSError:
            pass
            print("^c#D19A66^[wifi not connected]")
            Connected = False
            time.sleep(1)

is_connected()
