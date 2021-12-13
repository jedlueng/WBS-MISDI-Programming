#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 01:59:36 2021

@author: vasitach
"""

exchange_rate = input( "What types of currency you want to change? 1.USD 2.CNY 3.EUR 4.NTD 5.HKD").lower()

usd_rate = 1.38

cny_rate = 8.81

eur_rate = 1.19

ntd_rate = 38.44

hkd_rate = 10.72


if exchange_rate == 'USD'.lower():
    print("You have selected {currency} today's exchange rate from 1 GBP to {currency} is {rate}".format(currency=exchange_rate,rate = usd_rate))
if exchange_rate== 'CNY'.lower():
    print("You have selected {currency} today's exchange rate from 1 GBP to {currency} is {rate}".format(currency=exchange_rate,rate=cny_rate))
if exchange_rate == 'EUR'.lower():
    print("You have selected {currency} today's exchange rate from 1 GBP to {currency} is {rate}".format(currency=exchange_rate,rate =eur_rate))
if exchange_rate == 'NTD'.lower():
    print("You have selected {currency} today's exchange rate from 1 GBP to {currency} is {rate}".format(currency=exchange_rate,rate = ntd_rate))
if exchange_rate == 'HKD'.lower():
    print("You have selected {currency} today's exchange rate from 1 GBP to {currency} is {rate}".format(currency=exchange_rate, rate = hkd_rate))

   




