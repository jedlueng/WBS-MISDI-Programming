#Jedlueng 24 OCT 2021  finished 25 OCT 2021

'''  Smart Customer Service has been popular in recent years. 
Today we want you to build a simple Q&A customer service machine to answer the question 
about currency change rate information on GBP with other currency.'''



print('What types of currency you want to change?')
print('1.USD 2.CNY 3.EUR 4.NTD 5.HKD')
cur = str(input())
gbp_usd = 1.38
gbp_cny =  8.79
gbp_eur = 1.18
gbp_ntd = 38.40
gbp_hkd = 10.70


if cur.lower() == 'usd'.lower():
    print(' You have selected USD, todays exchange rate from GBP to USD is 1 GBP = {} usd '.format(gbp_usd))
    print('How many GBP you want to change to {cur}'.format(cur = cur))
    amount = float(input())
    if amount > 0: 
        print(amount*gbp_usd)
    else: 
        print('Sorry you can not input a negative value on currency. Please enter it again.')
elif cur.lower() == 'cny'.lower():
    print(' You have selected USD, todays exchange rate from GBP to CNY is 1 GBP = {} usd '.format(gbp_cny))
    print('How many GBP you want to change to {cur}'.format(cur = cur ))
    amount = float(input())
    if amount > 0:
        print(amount*gbp_cny)
    else: 
        print('Sorry you can not input a negative value on currency. Please enter it again.')
elif cur.lower() == 'eur'.lower():
    print(' You have selected USD, todays exchange rate from GBP to EUR is 1 GBP = {} usd '.format(gbp_eur))
    print('How many GBP you want to change to {cur}'.format(cur = cur))
    amount = float(input())
    if amount > 0:
        print(amount*gbp_eur)
    else: 
        print('Sorry you can not input a negative value on currency. Please enter it again.')
elif cur.lower() == 'ntd'.lower():
    print(' You have selected USD, todays exchange rate from GBP to NTD is 1 GBP = {} usd '.format(gbp_ntd))
    print('How many GBP you want to change to {cur}'.format(cur = cur))
    amount = float(input())
    if amount > 0:
        print(amount*gbp_ntd)
    else: 
        print('Sorry you can not input a negative value on currency. Please enter it again.')
elif cur.lower() == 'hkd'.lower():
    print(' You have selected USD, todays exchange rate from GBP to HKD is 1 GBP = {} usd '.format(gbp_hkd))
    print('How many GBP you want to change to {cur}'.format(cur = cur))
    amount = float(input())
    if amount > 0:
        print(amount*gbp_hkd)
    else: 
        print('Sorry you can not input a negative value on currency. Please enter it again.')
else: 
    print('How many GBP you want to change to {cur}'.format(cur = cur))
    quit()


