def converttobinary(num):

    #Decimal-->Binary
    if num >=1:
        converttobinary(num // 2)

    print(num%2,end="")


def converttohexa(num1):
    print("\n",hex(num1))

def converttooct(num2):
    value=1
    octnum=0
    while(num2 !=0):
        reminder= num2%8
        octnum = octnum + reminder * value

        value = value * 10
        num2 = num2 // 8
    print(octnum)

converttobinary(344)
converttohexa(10)
converttooct(33)