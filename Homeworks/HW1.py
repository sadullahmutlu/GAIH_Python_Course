
odd_num = [0,2,4,6,8]
even_num = [1,3,5,7,9]
print("Odd Numbers: " , odd_num) #burayı tek satırda da aralarına \n koyarak da yazılabilir.
print("Even Numbers: " , even_num, "\n")

numbers = odd_num + even_num #İki listeyi birleştirdik.
print("All Numbers:",numbers, "\n")

new_list = [i*2 for i in numbers] #İki Listenin elemanlarını birleştirip 2 ile çarptık
print("Multiplication list :",new_list, "\n")
new_list.sort() #listeyi sıralayın demiyordu fakat daha düzgün gözükmesi açısından listeyi sıraladık.
print("Sorted list :", new_list, "\n")

for i in new_list:
    print(i, ": data type of", type(new_list))