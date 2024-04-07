#len()# ()안에 있는 읽을수 있는 애들의 길이를 숫자로 반환
#print(len([]))


"조건문+"

year=int(input(""))

if  year%4==0 :

    if year%400==0 :
        print("1")
    
    elif year%100==0 :
        print("0")
    
    else :
        print("1")


else :
    print("0")