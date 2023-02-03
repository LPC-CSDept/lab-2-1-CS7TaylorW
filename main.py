def main():
   ##################################################
   # Comlete your code here
   ##################################################
   
   original_price = int (input("Please enter a price."))
   rate_input = int (input ("Please enter a rate."))
   rate = (rate_input / 100)
   discount_amount = int (original_price * rate)
   print (original_price)
   print (discount_amount)
   print (original_price - discount_amount)
   
   pass


if __name__ == '__main__':
    main()
