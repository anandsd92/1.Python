from functools import reduce
class CombinedClassFunction():
    def Subfields():
        aiFields=['Machine Learning','Neural Networks','Vision','Robotics','Speech Processing','Natural Language Processing']
        print("Sub-fields in AI are:")
        for f in aiFields:
            print(f)
    
    #Check Odd Or Even using List comprehensive function            
    def CheckOddOrEven():
        numbers=[532,248,781,563]
        evenNumbers=[val for val in numbers if val % 2==0]
        print(f"Even Numbers list using comprehensive function: {evenNumbers}")
    #Check Eligibility for Marriage
    def CheckEligibilityMarriage():
        try:
            gender=input("Enter your gender information:")
            age=int(input("Enter your age in numeric :"))
            print(f"Given gender: {gender} and age: is {age} \n")
        except ValueError:
            return "Invalid age. Please enter a valid age & number."
        if(gender.lower()=="male"):    
            if(age >=21):
                message = "Groom is eligible for marriage"
            else:
                message = "Groom is not eligible for marriage"
        elif(gender.lower()=="female"):
            if(age >=18):
                message = "Bride is eligible for marriage"
            else:
                message = "Bride is not eligible for marriage"
        else:
                message = "Given Gender is incorrect"
        return message
    #Check Total & Percentage of student
    def FindPercent():
        marks=[85,86,67,55,92]
        total=reduce(lambda x,y: x+y, marks)
        print(f"Total scores of student: {total}")
        percent = total/ len(marks)
        print(f"Percentile of student: {percent}")
    #Triangle Property
    def FindArea():
        try:
            Height1 = int(input("Enter Height1 of the triangle:"))
            Height2 = int(input("Enter Height2 of the perimeter:"))
            Breadth = int(input("Enter Breadth of the triangle:"))
        except ValueError:
            return "Invalid Height & Breadth of the triangle"
        areaOfTriangle = (Height1*Breadth)/2
        perimeterOfTriangle = Height1+Height2+Breadth
        return f"Area of triangle: {areaOfTriangle}, Perimeter of triangle: {perimeterOfTriangle}"