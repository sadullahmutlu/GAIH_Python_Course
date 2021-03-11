#global değişkenlerimiz
name = [] #isimler için oluşturduğum liste
notes = [] #girilen notlarla oluşturduğum liste
info_dictionary = {}  #isim ve notları attığım sözlük
sorted_values = [] #sıralama listesi

def main(): #sıralamaları olduğu fonksiyonumuz
    info_dictionary = dict(zip(name, notes)) #sözlüğe zip yöntemiyle isim ve notları ekledik
    sorted_values = sorted(info_dictionary.values()) #sorted metoduyla sıralamasını yaptık

    print("Dictionary elements :", info_dictionary) #sözlük bilgilerini ekrana yazdırdık
    print("Sorted list : ", sorted_values) #sıralanmış listeyi ekrana yazdırdık
    print("List in reverse order :", sorted_values[::-1]) #tersten sıralanmış listeyi ekrana yazdırdık

'''information yani bilgileri girdiğimiz fonksiyonumuz kodu okumak böyle daha kolay geldi bana bende 
o yüzden 2 fonksiyon kullanıp yaptım, direk alt alta da yazdırabilirdik tüm kodu'''

def info():
    for i in range(5): # kullanıcıdan 5 tane öğrenci ismi ve midterm project ve final notlarını aldık
        name.append(input("Enter Your Name :"))
        midterm = float(input("Enter Midterm grade : "))
        project = float(input("Enter Project grade :"))
        final = float(input("Enter Final grade :"))
        passingGrade = float(midterm * 0.3 + project * 0.3 + final * 0.4) #ortalamalarını burada aldık
        '''#Hocam geçme notu ile ilgili bir şey demediniğiniz için sadece ortalamyı yazdırdım eğer
        geçme kalma olayını da istersek
        if passingGrade >= 50:
            print("Geçti")
        else:
            print("kaldı") diyerek geçip kaldığını da görebiliriz.Hatta elif>= 90: print("AA") olarak 
        harf notuda ekleyebiliriz'''
        formatted_passingGrade = '{:.2f}'.format(passingGrade)#float değerlerin . dan sonraki değerleri uzun olmasın diye
        notes.append(formatted_passingGrade) #formatladıpımız grade elemanlarını notes listesine ekledik.
        print("\n", "Names:", name)
        print("Grades:", notes, "\n")

#fonskiyonlarımızı buradan çağırdık
info()
main()

