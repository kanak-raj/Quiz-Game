Bank = { 
    "python": { 
        "question": [ 
            "Q1. How do you insert comments in Python code?", 
            "Q2. Which of the following is ternary operator used in python?",  
            "Q3. Which method is used for taking inputs from user?",  
            "Q4. Who developed Python?", 
            "Q5. What is the method inside the class in python language?",
            "Q6. Which of the following declarations is incorrect in python language? ",
            "Q7. Which of the following operators is the correct option for power ?" ], 
        "answer": [ 1, 
                    1, 
                    3, 
                    2, 
                    2, 
                    2, 
                    4 
                    ], 
        "options": [ 
                    ["#This is a comment", 
                    "/*This is a comment*/", 
                    "//This is a comment", 
                    "//This is a comment#" 
                    ], 
                    ["!", 
                    "$", 
                    "&", 
                    "*" 
                    ], 
                    ["range()", 
                    "print()", 
                    "input()", 
                    "sorted()" 
                    ], 
                    ["Zim Den", 
                    "Guido van Rossum", 
                    "Niene Stom", 
                    "Wick van Rossum" 
                    ], 
                    ["Object", 
                    "Function", 
                    "Attribute", 
                    "Argument"], 
                    ["xyzp = 5,000,000", 
                    "x y z p = 5000 6000 7000 8000", 
                    "x,y,z,p = 5000, 6000, 7000, 8000", 
                    "x_y_z_p = 5,000,000"], 
                    ["a^b", 
                    "a^*b", 
                    "a^^b", 
                    "a**b" 
                    ] 
                   ]
              }, 
    "java": { 
            "question": [ 
                        "Q1. Which of the following is not a Java features?", 
                        "Q2. ____ is used to find and fix bugs in the Java programs.",  
                        "Q3. What is the return type of the hashCode() method in the Object c  ",
                        "Q4. Evaluate the following Java expression, if x=3, y=5, and z=10:  ++z + y - y + z + x++", 
                        "Q5. Which package contains the Random class?", 
                        ], 
            "answer": [3, 4, 2, 4, 1], 
            "options": [ 
                            ["Dynamic", 
                            "Architecture Neutral", 
                            "Use of pointers", 
                            "Object-oriented", 
                            ], 
                            ["JVM", 
                            "JRE", 
                            "JDK", 
                            "JDB" 
                            ], 
                            ["Object", 
                            "int", 
                            "long", 
                            "void" 
                            ], 
                            ["24", 
                            "23", 
                            "20", 
                            "25" 
                            ], 
                            ["java.util package", 
                            "java.lang package", 
                            "java.awt package", 
                            "java.io package" 
                            ] 
                        ] 
             }, 
    "javascript": { 
                    "question": [ 
                            "Q1. Which of the following option is used as hexadecimal literal beg  ",
                            "Q2. Which of the following type of a variable is volatile?",  
                            "Q3. When there is an indefinite or an infinite value during an arith  ",
                            "Q4. Which of the following number object function returns the value   ",
                            "Q5. Which of the following function of the String object returns the  ",
                            "Q6. In JavaScript the x===y statement implies that:",  
                            """Q7. Choose the correct snippet from the following to check if the   """,
                            """Q8. What will be the output of the following JavaScript code?  
                                        functioncomparison() 
                                        { 
                                        int number= 10 
                                        if(number ==="10") 
                                        returntrue 
                                        else 
                                        returnfalse 
                                        }""",
                            "Q9. Which one of the following operator is used to check weather as  ",
                            "Q10. Which one of the following is an ternary operator:"  ], 
                    "answer": [4, 1, 3, 2, 3, 3, 1, 1, 4, 1], 
                    "options": [ 
                                ["00", 
                                "0x", 
                                "0X", 
                                "Both 0x and 0X"], 
                                [ 
                                "Mutable variable", 
                                "Dynamic variable", 
                                "Volatile variable", 
                                "Immutable variable"], 
                                ["Prints an exception error", 
                                "Prints an overflow error", 
                                """Displays 'Infinity'""", 
                                "Prints the value as such"], 
                                [ 
                                "toString()", 
                                "valueOf()", 
                                "toLocaleString()", 
                                "toPrecision()"], 
                                [ 
                                "slice()", 
                                "split()", 
                                "substr()", 
                                "search()"], 
                                [ 
                                "Both x and y are equal in value, type and reference address as w  ","Both are x and y are equal in value only.", 
                                "Both are equal in the value and data type.",  "Both are not same at all."], 
                                [ 
                                "if(a !==null)", 
                                "if (a!)", 
                                "if(a!null)", 
                                "if(a != null)"], 
                                [ 
                                "True", 
                                "false", 
                                "runtime error", 
                                "compilation error"], 
                                [ 
                                "Exists", 
                                "exist", 
                                "within", 
                                "in"], 
                                ["?", 
                                ":", 
                                "-", 
                                "+"]
                                ] 
                   } 
    } 
registered = {'kanak': "12asQW", 'aman': "ajklQW153"} 
def login(student, password): 
    if student not in registered: 
         print(f"There is no {student} registered.Register first.") 
         return 
    if registered[student] == password: 
        score = 0 
        try_again = 'yes' 
        while try_again != 'no': 
            Selection = input("Which type of quiz you want?(Python/Java/Javascript)")
            Selection = Selection.lower() 
            if Selection in Bank: 
                for count in range(len(Bank[Selection]["question"])):  
                    print(Bank[Selection]["question"][count])
                    for order in range(4): 
                        print(f"{order+1}."+Bank[Selection]["options"][count][order])
                    user_input = int(input("Enter your answer: ")) 
                    # print(python["answer"][0]) 
                    if user_input == Bank[Selection]["answer"][count]: 
                        score += 1 
                    else: 
                        pass 
                percentage = int((score/len(Bank[Selection]["answer"]))*100)
                if percentage >= 80: 
                    print("Excellent") 
                elif percentage >= 70 and percentage < 80:
                    print("good") 
                else: 
                    print("Bad") 
                print(f"Your score is: {int(percentage)} %")
                try_again = input("Do you want to try again?(yes or no) ") 
                try_again = try_again.lower() 
            else: 
                 print("Wrong choice.Try again.") 
    else: 
        print("Wrong credentials.Try again..") 
def register(student): 
  if student in registered: 
        print("This username is already registered.Try Login")
        return 
  success = 0 
  while success != 1: 
    pas = input("Enter the password:") 
    numeric = upper = lower = 0 
    if len(pas) >= 6 and pas.find(" ") == -1 and pas.find("/")==-1:
         for digits in pas: 
           if digits.isnumeric():  
               numeric = 1 
           if digits.isupper(): 
             upper = 1 
           if digits.islower(): 
               lower = 1 
           if numeric == upper == lower == 1:  
               success = 1 
               break 
    if numeric == 0 or upper == 0 or lower == 0:
        print("Weak password.Try something else") 
  registered[student] = pas 
  print("You are registered.You can login now..") 
choice = 0 
while choice != "3": 
    choice = input("""Enter your choice:
    1.Registration. 
    2.Login. 
    3.Exit 
    """) 
    if choice == '1': 
        student = input("enter id: ") 
        register(student) 
    elif choice == '2': 
        student = input("enter id: ") 
        password = input("Enter password: ")
        login(student, password) 
        break 
    elif choice == '3': 
        break 
    else: 
     print("Choose again.")
