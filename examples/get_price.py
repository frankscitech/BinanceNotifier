'''
	:breif: Simple Example of Get Price of X Currency
	:author: @frankscitech
'''

'''
	Get API Key from Binance
'''


import os
import sys
from binance.client import Client

def testnet(client):
	client.API_URL = 'https://testnet.binance.vision/api'

def print_acc_info(client):
	print(client.get_account())


def conn_client(key,secret):
	client = Client(key, secret)
	if not client:
		print("Failed Connection to Client")
		return 0
	else:
		return client 

def get_balance(client,curr_name):
	return client.get_asset_balance(asset=curr_name)

def get_price(client,currs_name):
	price = client.get_symbol_ticker(symbol=currs_name)
	return price

def calc_delta(cp,pp):
	return ((cp-pp)/pp)*100

if __name__ == '__main__':

	api_key = sys.argv[1] # Get them from Binance.com
	api_secret = sys.argv[2]

	client=conn_client(api_key,api_secret)

	print(get_price(client,'BTCUSDT'))