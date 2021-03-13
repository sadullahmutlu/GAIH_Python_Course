### BİLGİ YARIŞMASI
# =============================================================================
#__init__ methodu her sorunun cevabı farklı diye kullandım.
#Aşağıdaki örnekte Questions adında bir class oluşturduk. 
#Genel olarak her soruda bulunan fakat sorudan soruya değişiklik gösteren şıklar
#ve girilen değerler gibi ayırt edeci özellikleri class’ımıza atadık.
# =============================================================================

# =============================================================================
# __init__ metodunun yapısına baktığımızda parantez içinde self kavramı dikkatimizi çekmektedir. 
#self anahtar sözcüğü (keyword) __init__ metodu ile gelen ve class içinden türetmiş
#olduğumuz nesnelere ulaşmamızı sağlayan bir kavramdır. 
#Bizim burada prompt ve answerimiz yani 2 tane keyword değerimiz bulunmaktadır.
# =============================================================================

class Question:
     def __init__(self, prompt, answer):
          self.prompt = prompt
          self.answer = answer
          
#soru listemiz
entered_questions = [
     "1-)Türkiyenin Başkenti Neresidir\n a)İstanbul\n b)İzmir\n c)Ankara\n d)Rize\n\nEnter Answer: ",
     "2-)Üçgenin İç Açıları Toplamı Kaçtır?\n a)180\n b)90\n c)270\n d)360\n\nEnter Answer: ",
     "3-)Python'ın Tasarımcısı Kimdir?\n a)Guido Van Rossum \n b)Dennis Ritchie\n c)James Gosling\n d)Linus Torvalds\n\nEnter Answer:",
     "4-)Python Hangi Senede Geliştirildi?\n a)1989\n b)1990\n c)1991\n d)1992\n\nEnter Answer:",
     "5-)TBMM Hangi Yılda Açılmıştır?\n a)1923\n b)1921\n c)1920\n d)1919\n\nEnter Answer: ",
     "6-)Malazgirt Meydan Muharebesi Hangi Tarihinde Yaşanmıştır\n a)1023\n b)1299\n c)1037\n d)1071\n\nEnter Answer:",
     "7-)Mehmet Akif İstiklal Marşını nerede yazmıştır?\n a)Ankara-Ayasofya\n b)Ankara-Keçiören Camii\n c)Ankara-Ayaş Dergahı\n d)Ankara-Taceddin Dergahı\n\nEnter Answer:",
     "8-)Türkiye'nin ilk Safari Parkı hangi ilimizde açılmıştır?\n a)Gaziantep\n b)İzmir\n c)Bursa\n d)Balıkesir\n\n Enter Answer:",
     "9-)Türkiye'nin en büyük kış ve doğa sporları merkezi olan Uludağ'ın eski adı nedir?\n a)Ulu Kuş Dağı\n b)Buz Dağı\n c)Keşiş Dağı\n d)Yeşil Dağ\n\nEnter Answer:",
     "10-)Tarihte Codex Cumanicus adıyla bilinen Sözlük hangi Türk devletine aittir?\n a)Hazarlar\n b)Kıpçaklar\n c)Göktürkler\n d)Avarlar\n\n Enter Answer:"
     ]
#cevap listemiz
question_answers = [
     Question(entered_questions[0], "c"),
     Question(entered_questions[1], "a"),
     Question(entered_questions[2], "a"),
     Question(entered_questions[3], "b"),
     Question(entered_questions[4], "c"),
     Question(entered_questions[5], "d"),
     Question(entered_questions[6], "d"),
     Question(entered_questions[7], "a"),
     Question(entered_questions[8], "c"),
     Question(entered_questions[9], "b")
     ]
#soruların cevapları doğru ve yanlış olmasına göre score vericek fonksiyonumuz
def knowledge_competition(question_answers):
    score = 0
    for i in question_answers: # soru miktarı kadar döndürmesi için range'i soru miktarı yaptık
        answer = input(i.prompt)# girilen değerimi alıp answer'a atadık 
        answer = answer.lower() # büyük küçük harfe duyarlı hale getirdik
        if answer == i.answer: #girilen değer cevap ile aynı mı kontrol ettirdik
            score += 10 #doğruysa 10 puan verip score değişkenimize ekledik
        else:
            score += 0 #yanlışsa 5 puan verip score değişkenimize ekledik
    #kullanıcı 5 soru üstüne doğru cevap verirse başarılı olucak.
    #Eğer 5 soru ve üstü yapmak istersek score >=50 diyerek yapabiliriz
    if score > 50:
        print("\n=================================================")
        print("Congratulations !! You know more than 5 questions \nToplam Score: ", score) # Toplam Score muzu yazdırdık
        print("=================================================")
    else:
        print("\n==============================================")
        print("Unsuccessful !! You know less than 5 questions \nToplam Score: ",score) # 5 sorudan az bilirse bunu yazdırdık
        print("==============================================")
     
knowledge_competition(question_answers) #fonksiyonumuzu çağırdık