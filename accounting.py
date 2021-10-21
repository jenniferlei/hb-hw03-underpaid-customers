MELON_COST = 1.00

def paid_vs_expected(path):
    '''
    takes a report
    calculates how much the amount customer is expected to pay
    prints the comparison between expected amount and customer's payment if payment is incorrect
    '''

    # open file
    accounting_report = open(path)

    # for each line in the file
    for line in accounting_report:
        line = line.rstrip()
        words = line.split('|') # split text by | and assign strings to words variable

        # assign new variables to words
        customer_name = words[1]
        melon_count = int(words[2])
        customer_paid = float(words[3])
    
        # calculate the expected payment for each customer
        customer_expected = melon_count * MELON_COST

        # if the customer expect payment is not equal to customer payment,
        # print the comparison
        if customer_expected != customer_paid:
            print(f"{customer_name} paid ${customer_paid:.2f},",
                f"expected ${customer_expected:.2f}"
                )
            if customer_expected > customer_paid:
                print(f"{customer_name} underpaid ${customer_expected - customer_paid:.2f}.\n")
            elif customer_expected < customer_paid:
                print(f"{customer_name} overpaid ${customer_paid - customer_expected:.2f}.\n")
            
    # close the report
    accounting_report.close()

# call the function
paid_vs_expected("customer-orders.txt")

# melon_cost = 1.00

# customer1_name = "Joe"
# customer1_melons = 5
# customer1_paid = 5.00

# customer2_name = "Frank"
# customer2_melons = 6
# customer2_paid = 6.00

# customer3_name = "Sally"
# customer3_melons = 3
# customer3_paid = 3.00

# customer4_name = "Sean"
# customer4_melons = 9
# customer4_paid = 9.50

# customer5_name = "David"
# customer5_melons = 4
# customer5_paid = 4.00

# customer6_name = "Ashley"
# customer6_melons = 3
# customer6_paid = 2.00


# customer1_expected = customer1_melons * melon_cost
# if customer1_expected != customer1_paid:
#     print(f"{customer1_name} paid ${customer1_paid:.2f},",
#           f"expected ${customer1_expected:.2f}"
#           )

# customer2_expected = customer2_melons * melon_cost
# if customer2_expected != customer2_paid:
#     print(f"{customer2_name} paid ${customer2_paid:.2f},",
#           f"expected ${customer2_expected:.2f}"
#           )

# customer3_expected = customer3_melons * melon_cost
# if customer3_expected != customer3_paid:
#     print(f"{customer3_name} paid ${customer3_paid:.2f},",
#           f"expected ${customer3_expected:.2f}"
#           )

# customer4_expected = customer4_melons * melon_cost
# if customer4_expected != customer4_paid:
#     print(f"{customer4_name} paid ${customer4_paid:.2f},",
#           f"expected ${customer4_expected:.2f}"
#           )

# customer5_expected = customer5_melons * melon_cost
# if customer5_expected != customer5_paid:
#     print(f"{customer5_name} paid ${customer5_paid:.2f},",
#           f"expected ${customer5_expected:.2f}"
#           )

# customer6_expected = customer6_melons * melon_cost
# if customer6_expected != customer6_paid:
#     print(f"{customer6_name} paid ${customer6_paid:.2f},",
#           f"expected ${customer6_expected:.2f}"
#           )
