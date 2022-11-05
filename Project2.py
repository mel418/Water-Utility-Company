#processing the customer's inputs of information code, beginning meter, ending meter
code = input('Enter the customer\'s code: ')
code = code.lower() #turns the prior input into lower case so both lower and upper case codes can work
bMeter = int(input('Enter the customer\'s beginning meter reading: '))
eMeter = int(input('The customer\'s ending meter reading:          '))
bill = 0

#computing amount of gallons
if bMeter > eMeter:
    gallonsW = (((eMeter + 1000000000) - bMeter) * 0.1)
else:
    gallonsW = ((eMeter - bMeter) * 0.1) 

#selecting which code to use to calculate water bill from the amount of gallons of water
if code == 'r':
    bill = 5 + (gallonsW * 0.0005)
elif code == 'c':
    bill = 1000
    if gallonsW > 4000000:
        bill = bill + ((gallonsW - 4000000) * 0.00025)
elif code == 'i':
    if gallonsW <= 4000000:
        bill = 1000
    elif gallonsW <= 10000000:
        bill = 2000
    else:
        bill = 2000 + ((gallonsW - 10000000) * 0.0025)

#displaying back the customer's code beginning meter, ending meter
print(f'\nCustomer code: {code}')
print('Beginning meter reading: {:0>9}'.format(bMeter))
print('Ending meter reading:    {:0>9}'.format(eMeter))

#if the code is invalid or if the meter is outside the range of 0 to 999999999
if code != 'r' and code != 'i' and code != 'c' or (bMeter or eMeter < 0) or (bMeter or eMeter >= 1_000_000_000):
    gallonsW = 0
    bill = 0
    print('Invalid Entry')

#return amount of gallons of water used and amount billed to the customer
print(f'Gallons of water used: {gallonsW:.1f}')
print(f'Amount billed: ${bill:.2f}')
