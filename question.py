#counts no of corrected and un corrected
marks=0
correct=0
questions=["who is your fav cricketer",
           "who is ur ds teacher",
           "what is the capital of ap",
           "what sport do u like much",
           "how many colours are there in rainbow "]
ans=["ViratKohli",
     "omkar sir",
     "god must know",
     "cricket",
     "seven"]
for i in range(len(questions)):
    
    print(questions[i])
    answer=input("enter the ans for question:")
    print("the ans in list is=",{ans[i]})
    if  answer.lower()==ans[i].lower():
        marks=marks+1
        correct=correct+1
print("no of marks=",marks)
print("no of correct ans=",correct)
