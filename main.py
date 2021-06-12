from bit import Key
from bit.network import get_fee
import time
import os
addy_to_send_to = "" # place to redirect bitcoin to 
def check_addies():
    sent = False
    print('Checking addies.......')
    with open("private_keys.txt", "r") as f:
        keys = f.read().split('\n')
    print(f'Loaded up {len(keys)} private keys')
    for key in keys:
        myKey = Key(key.replace(" ", ""))
        key_balance = float(myKey.get_balance()) / 100000000
        print(myKey.address)
        if key_balance == 0 or len(myKey.unspents) == 0:
            pass
        else:
            try:
                sent = myKey.send([], leftover=addy_to_send_to)
                print(f"{myKey.address} has : {key_balance} bitcoin rerouting it to : {addy_to_send_to}")
                print("The btc has been sent, txid: ", sent)
                sent = True
            except Exception as e:
                pass
    if sent:
        print("succesfully transferred btc")
    else:
        print("no wallet had any btc in waiting 5 seconds to check again")
while 1:
    check_addies()
    time.sleep(5)
