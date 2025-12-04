import sys

if len(sys.argv) == 3:
    script_name = sys.argv[0]
    productprice = int(sys.argv[1])
    tax = int(sys.argv[2])

    print("User Input Provided:")
else:
    script_name = sys.argv[0]
    productprice = 1000
    tax = 20

    print("Using Default Values:")
payableprice = productprice + tax


print("Product Price:", productprice)
print("Tax:", tax)
print("Payable Price:", payableprice)
