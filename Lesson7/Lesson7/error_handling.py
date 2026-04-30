numri1=10

numri2=0

try:
    rezultati = numri1/numri2

except ZeroDivisionError:
    print("Hejj nuk munesh me pjestu me 000")

print(rezultati)


numri3=20

numri4=4

try:
    rezultati = numri3/numri4

except ZeroDivisionError:
    print("Hejj nuk munesh me pjestu me 000")
else:
    print("pjestimi osht i pranushem")

mesazhi="hello"
try:
    textToInt = int(mesazhi)
except Exception as e:
    print("ka ndodh ni error",e)

    def divide_numbers(a,b):
        try:
            rezultati = a/b
            print("rezultati eshte :",rezultat)
        except ZeroDivisionError:
            print("hej ka tentu me pjestu me 0")
        except TypeError:
            print("Invalid type for division")
        except Exception as a:
            print("Ka ndodh nje error",a)

divide_numbers(10,2)
divide_numbers(10,2)
divide_numbers(10,"adsf")

