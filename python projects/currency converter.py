def main():
    print ("This program converts US dollars to pounds sterling")
    print()
    
    dollars = eval(input("Enter amount in dollars: "))
    
    ppounds = convert_to_pounds(dollars)
    
    print("That is", pounds, "pounds. ")
    
convert_to_pounds = lambda dollars: dollars * 0.82

main()