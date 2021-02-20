midterm=[15,86,79,55,76]
homework=[100,0,28,76,49]
final=[59,28,85,46,14]
isimler=["Ahmet Öztekin","Mehmet Aslan","Aslı Yen","Kerem Aktürkoğlu","Büşra Alp"]


print("1.Öğrenci",
      "\nİsim ve Soyisim:",isimler[0],
      "\nÖdev Notu:",homework[0],
      "\nArasınav Notu:",midterm[0],
      "\nFinal Notu:",final[0],
      "\n------------------------")
print("2.Öğrenci",
      "\nİsim ve Soyisim:",isimler[1],
      "\nÖdev Notu:",homework[1],
      "\nArasınav Notu:",midterm[1],
      "\nFinal Notu:",final[1],
      "\n------------------------")
print("3.Öğrenci",
      "\nİsim ve Soyisim:",isimler[2],
      "\nÖdev Notu:",homework[2],
      "\nArasınav Notu:",midterm[2],
      "\nFinal Notu:",final[2],
      "\n------------------------")
print("4.Öğrenci",
      "\nİsim ve Soyisim:",isimler[3],
      "\nÖdev Notu:",homework[3],
      "\nArasınav Notu:",midterm[3],
      "\nFinal Notu:",final[3],
      "\n------------------------")
print("5.Öğrenci",
      "\nİsim ve Soyisim:",isimler[4],
      "\nÖdev Notu:",homework[4],
      "\nArasınav Notu:",midterm[4],
      "\nFinal Notu:",final[4],
      "\n------------------------")

info= {"İsimler":[isimler],"Notlar":[midterm,homework,final],}

midterm.sort(reverse=True)
homework.sort(reverse=True)
final.sort(reverse=True)

print("Ara sınavdan en yüksek puanı alan öğrencimizi tebrik ederiz.\nİsim:",isimler[1],
      "\nPuan:",midterm[0],
      "\n-------------------")

print("Ödevden en yüksek puanı alan öğrencimizi tebrik ederiz..\nİsim:",isimler[0],
      "\nPuan:",homework[0],
      "\n-------------------")

print("Final sınavından en yüksek puanı alan öğrencimizi tebrik ederiz.\nİsim:",isimler[2],
      "\nPuan:",final[0],
      "\n-----------------")
