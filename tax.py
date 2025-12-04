import sys


if len(sys.argv) == 4:
    script_name = sys.argv[0]
    productprice = int(sys.argv[1])
    tax = int(sys.argv[2])
    payableprice = int(sys.argv[3])

    print("User Input:")
else:
    
    script_name = sys.argv[0]
    productprice = 1000
    tax = 20   
    payableprice = productprice + tax

    print("Using Default Values:")


payableprice = productprice + tax

print("Payable Price:", payableprice)
