""" OPPGAVE 2: Konvertering """

#2.1
#tilordner variabel f temperaturen i fahrenheit, gitt av brukeren
f = float(input("oppgi en temperatur i farenheit: "))    
#skriver ut temperaturen i fahrenheit
print("Temperaturen i fahrenheit er: " + str(f) + " grader fahrenheit.")

#finner variabel c for temperaturen i celsius, regner ut basert på f
c = (f - 32) * 5/9      
#skriver ut temperaturen i celsius
print("Temperaturen i celsius er: " + str(round(c,2)) + " grader celsius.") #runder av c til 2 desimaler med kommandoen round()
