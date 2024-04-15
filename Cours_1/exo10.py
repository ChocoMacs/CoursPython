def testscore(score):
    while True:
        if float(score) < 0 or float(score) > 100:
            score = float(input("Saisir un vrai score... : "))
        else:
            return(score)       
    


scoreA = float(input("Saisire le score du candidat A : "))
scoreA = testscore(scoreA)

scoreB = float(input("Saisire le score du candidat B : "))
scoreB = testscore(scoreB)

scoreC = float(input("Saisire le score du candidat C : "))
scoreC =testscore(scoreC)

scoreD = float(input("Saisire le score du candidat D : "))
scoreD = testscore(scoreD)

print(scoreA,scoreB,scoreC,scoreD)

if scoreA > 50:
    print("Le candidat A est elu au premier tour")
elif scoreA >= 12.5 :
    print("Le candidat A est en balotage favorable")
else:
    print("Le candidat A est en balotage defavorable")



"""     
elif int(scoreB) > 12.5 or int(scoreC) > 12.5 or int(scoreD) > 12.5 :
    if int(scoreB) > int(scoreA) or int(scoreC) > int(scoreA) or int(scoreD) > int(scoreA):
        print("Le candidat A est en balotage defavorable")
else:
        print("Le candidat A est en balotage favorable") """
   