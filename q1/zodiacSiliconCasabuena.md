[zodiacSiliconCasabuena.txt](https://github.com/user-attachments/files/31071665/zodiacSiliconCasabuena.txt)

[zodiacSiliconCasabuena.py](https://github.com/user-attachments/files/31071530/zodiacSiliconCasabuena.py)

#asks the user to input their birth year.
birth_year=int(input("Enter your birth year: "))

#creates an infiinite loop where the user is asked to put a birth year no later than 1900 repeatedly until compliance.
while birth_year<1900:
    print("Invalid Year, it should not be earlier than 1900")
    birth_year=int(input("Enter your birth year: "))
    if birth_year>=1900:
          break
          
#computes the remainder of the computed birth year which then serve as the index for a specific zodiac sign in the list zodiac_sign[].        
zodiac_sol= (birth_year-1900)%12 

#creates a list of Chinese zodiac signs which will serve as placeholders for the value of zodiac_sol[]
zodiac_sign=["Rat (鼠 / Shǔ)", "Ox (牛 / Niú)", "Tiger (虎 / Hǔ)", "Rabbit (兔 / Tù)", "Dragon (龙 / Lóng)", "Snake (蛇 / Shé)", "Horse (马 / Mǎ)", "Goat (羊 / Yáng)", "Monkey (猴 / Hóu)", "Rooster (鸡 / Jī)", "Dog (狗 / Gǒu)", "Pig (猪 / Zhū)"]

print(f"Your Chinese Zodiac Sign is: {zodiac_sign[zodiac_sol]}")
input("")

<img width="503" height="452" alt="image" src="https://github.com/user-attachments/assets/945c46c0-4975-422b-ad56-6fa5ee009095" />
    
    




    
