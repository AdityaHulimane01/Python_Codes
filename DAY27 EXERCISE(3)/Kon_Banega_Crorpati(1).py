# Questions :- 
# create a program capable for displaying questions to the user like KBC
# use list data type to store the question and their correct answers
# display the final amount the person is taking home after playing the game


Questions = ["Q1) Which for the following festivals is known as the “Festival for Lights”?", 
             "Q2) Which planet is known as the Red Planet?",
             "Q3) Who wrote the Indian National Anthem “Jana Gana Mana”?",
             "Q4) In computers, RAM stands for what?",
             "Q5) Which for the following is the largest ocean in the world?"]

Options = ["          A) Holi , B) Diwali , C) Eid , D) Christmas" , 
           "          A) Venus , B) Saturn , C) Mars , D) Jupiter" ,
           "          A) Bankim Chandra Chatterjee , B) Mahatma Gandhi , C) Rabindranath Tagore , D) Subhas Chandra Bose" ,
           "          A) Random Access Memory , B) Read Any Memory , C) Run Access Mode , D) Random Active Module" ,
           "          A) Indian Ocean , B) Pacific Ocean , C) Arctic Ocean , D) Atlantic Ocean"]

Answers = ["B" , "C" , "C" , "A" , "B"]

Amount = ["5,00,000" , "10,00,000" , "20,00,000" , "30,00,000" , "35,00,000"]

QuestionNum = 0;

for i in Questions:
    print(Questions[QuestionNum])
    print(Options[QuestionNum])
    print()
    UserAns = input("Enter your Answer : ")
    print()
    if(UserAns == Answers[QuestionNum] and QuestionNum == 0):
          print("Congrats! This is correct answer for Amount" , Amount[QuestionNum])
    elif(UserAns == Answers[QuestionNum] and QuestionNum == 1):
         print("Congrats! This is correct answer for Amount" , Amount[QuestionNum])
    elif(UserAns == Answers[QuestionNum] and QuestionNum == 2):
         print("Congrats! This is correct answer for Amount" , Amount[QuestionNum])
    elif(UserAns == Answers[QuestionNum] and QuestionNum == 3):
         print("Congrats! This is correct answer for Amount" , Amount[QuestionNum])
    elif(UserAns == Answers[QuestionNum] and QuestionNum == 4):
         print("Congrats! This is correct answer for Amount" , Amount[QuestionNum])
         print()
         print("Congrats Player you won total 1CR you can take it to your home Bye! ")
    else:
          print("Sorry! but this is wrong answer you lose the game come again with your best version best for luck.")
    if(UserAns == Answers[QuestionNum]):
         QuestionNum += 1
    else:
         break
    

 
    