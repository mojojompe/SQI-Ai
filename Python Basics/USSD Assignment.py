#A Complete MTN USSD Application

code = (input("Enter your USSD code: "))
if code == '*312#':
    print('''
          1. Data Plans
          2. Enjoy 4.5GB for N1000
          3. Enjoy 7GB for N1500
          4. Business Plans
          5. Roaming/Int'l
          6. Borrow Credit/Recharge
          99. Next
    ''')
    choice = (input("Choice: "))
    if choice == '1':
        print('''
              1. Daily
              2. 2-3 Days
              3. Weekly
              4. Monthly
              5. 2 Months+
              6. Social Bundles
              7. Broadband
              8. Binge Bundles
              9. Family Share
              10. Hot Deals
              0. Back
        ''')
        plan = input('Pick your plan: ')
        if plan == '1':
            print("You are about to buy a daily plan")
        elif plan == '2':
            print("You are about to buy a 2-3 days plan")
        elif plan == '3':
            print("You are about to buy a weekly plan")
        elif plan == '4':
            print("You are about to buy a monthly plan")
        elif plan == '5':
            print("You are about to buy a 2months+ plan")  
        elif plan == '6':
            print("You are about to buy a Social Bundle")
        elif plan == '7':
            print("You are about to buy a Broadband plan")
        elif plan == '8':
            print("You are about to buy a Binge Bundle")
        elif plan == '9':
            print("You are about to buy a Family Share plan")
        elif plan == '10':
            print("You are about to buy a Hot deal")
        elif plan == '0':
            print('''
          1. Data Plans
          2. Enjoy 4.5GB for N1000
          3. Enjoy 7GB for N1500
          4. Business Plans
          5. Roaming/Int'l
          6. Borrow Credit/Recharge
          99. Next
        ''')           
        
    elif choice == '2':
        print('''
              Special Offer for you! Get 4.5GB for N1000
              Valid for 1day
        ''')
        
    elif choice == '3':
        print('''
              Special Offer for you! Get 7GB for N1500
              Valid for 1day
        ''')
        
    elif choice == '4':
        print('''
              1. BizPlus Bundles & VAS
              2. Broadband Bundles
              3. Enterprise Bundles
              4. Data Coupon
              5. Check Balances
        ''')
        BizPlan = input('Pick your Business plan: ')
        if BizPlan == '1':
            print("You are about to buy a BizPlus Bundle")
        elif BizPlan == '2':
            print("You are about to buy a Broadband Bundle")
        elif BizPlan == '3':
            print("You are about to buy an Enterprise Bundle")
        elif BizPlan == '4':
            print("You are about to buy a Data Coupon")
        elif BizPlan == '5':
            print("You are about to Check your Balance")
        
    elif choice == '5':
        print('''
              1. TravelPass Plans
              2. Data Hybrid
              3. Free incoming roaming call
              4. Int'l Calling Bundles
              5. Roaming Balance Check
        ''')
        BizPlan = input('Pick your Business plan: ')
        if BizPlan == '1':
            print("You are about to buy a TravelPass Plan")
        elif BizPlan == '2':
            print("You are about to buy a Data Hybrid Bundle")
        elif BizPlan == '3':
            print("You are about to opt in for free roaming call")
        elif BizPlan == '4':
            print("You are about to buy an Int'l Bundle")
        elif BizPlan == '5':
            print("You are about to Check your Roaming Balance")
            
    elif choice == '6':
        print("You are not eligible to borrow Credit or Data")
    
    elif choice == '99':
        print("Next...")
    
    else:
        print("Wrong Input")

else:
    print("Wrong Code!")