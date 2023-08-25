class SubfieldsInAI():
    def Subfields():
        print("Sub-fields in AI are:")
        for temp in ['Machine Learning', 'Neural Networks', 'Vision', 'Robotics', 'Speech Processing', 'Natural Language Processing']:
            print(temp)

    def OddEven():
        num = int(input("Enter a number: "))
        if(num%2==0):
            print("{0} is Even".format(num))
        else:
            print("{0} is Odd". format(num))

    def Eligible():
        gender=input("Your Gender:")
        age=int(input("Your Age:"))
        if(gender=="Male"):
            if(age>=21):
                print("Eligible")
            else:
                print("Not Eligible")
        elif(gender=="Female"):
            if(age>=18):
                print("Eligible")
            else:
                print("Not Eligible")          
        else:
            print("Invalid Data")
            

    def percentage():
        m1=int(input("Subject 1="))
        m2=int(input("Subject 2="))
        m3=int(input("Subject 3="))
        m4=int(input("Subject 4="))
        m5=int(input("Subject 5="))
        print("Total",m1+m2+m3+m4+m5)
        print("Percentage",((m1+m2+m3+m4+m5)/500)*100)


    def triangle():
        Height=int(input("Height="))
        breadth=int(input("breadth="))
        print("Area of the Triangle:", (Height*breadth)/2)
        Height1=int(input("Height1="))
        Height2=int(input("Height2="))
        breadth=int(input("breadth="))
        print("Perimeter of the Triangle:", Height1+Height2+breadth)
