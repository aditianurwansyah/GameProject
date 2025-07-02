import random
  
while True:   
 pilihan = input('Apakah ingin memutar dadu? (y/n) :').lower()
 if pilihan == 'y':
   die1 = random.randint(1, 6)
   die2 = random.randint(1, 6)
   print(f'({die1},{die2})')  
 elif pilihan == 'n': 
    print('hello')  
    break 
else:  
    print('gagal code') 

def heybang() :
  print("Yooo")  
  print("Saya masih pemula banget")
  print("asli reall 100%")   
heybang()    


          