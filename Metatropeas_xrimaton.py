import time
class Questions:
    def __init__(self, prompt):
        self.prompt=prompt
f = input("Pes onoma: ")
print(f"O Pornometanastis se kalosorizi {f}! ")
time.sleep(3)
a = ["Arxika pes mou ti thes na metatrepsis: (Πρέπει να διαλέξεις μεταξύ του : a του b του c του d και του e) \n a.USD\n b.Euro\n c.Yuan\n d.Aggliki lira\n e.Roupia Indias\n"]
c = ["Epita pes mou se ti thes na ta metatrepsis: (Πρέπει πάλι να διαλέξεις μεταξύ του : a του b του c του d και του e) \n a.USD\n b.Euro\n c.Yuan\n d.Aggliki lira\n e.Roupia Indias\n "]


Question=Questions(a[0])
Question1=Questions(c[0])


def arxizo():
    b = input(Question.prompt)
    if b != "a" and b != "b" and b != "c" and  b != "d" and b != "e":
        print("Ipame! Times  metaji tou a tou b tou c tou d kai tou e")
        return
    else:
        d = input(Question1.prompt)
        if d != "a" and d != "b" and d != "c" and d != "d" and d != "e":
            print("Ipame! Times  metaji tou a tou b tou c tou d kai tou e")
            return
        else:
            try:
                q=int(input("Pes posothta: "))
            except ValueError:
                print("Den mporis na balis mi arithmitiki timh.Arxise jana to programma apo thn arxh")
                return

            if b =="a":
                if d =="b":
                     print("Ine: ", q*0.86, "Euro")
                elif d =="c":
                    print("Ine :", q*6.69, "Yuan")
                elif d =="d":
                    print("Ine :", q*0.77, "English Pound")
                elif d == "e":
                    print("Ine :", q*(1/0.013), "Roupies Indias")
            elif b == "b":
                if d =="a":
                    print("Ine :", q*1.162790697674419, "USD")
                elif d == "c":
                    print("Ine", q*7.81, "Yuan")
                elif d == "d":
                    print("Ine :", q*0.90, "English Pound")
                elif d == "e":
                    print("Ine :", q*(1/0.011), "Roupies Indias")
            elif b == "c":
                if d=="a":
                    print("Ine :", q*(1/6.69), "USD")
                elif d=="b":
                    print("Ine :", q*(1/7.81), "Euro")
                elif d=="d":
                    print("Ine :", q*0.12, "English pound")
                elif d=="e":
                    print("Ine :", q*(1/0.088), "Roupies Indias")
            elif b=="d":
                if d=="a":
                    print("Ine :", q*(1/0.77), "USD")
                elif d=="b":
                    print("Ine :",q*(1/0.90), "Euro" )
                elif d=="c":
                    print("Ine :",q*(1/0.12), "Yuan" )
                elif d=="e":
                    print("Ine :", q*(1/0.010), "Roupies Indias")
            elif b == "e":
                if d == "a":
                    print("Ine :", q*0.013, "USD")
                elif d == "b":
                    print("Ine :", q*0.011, "Euro")
                elif d == "c":
                    print("Ine :", q*0.088, "Yuan")
                elif d == "d":
                    print("Ine :", q*0.010, "Agglikes lires")










arxizo()











