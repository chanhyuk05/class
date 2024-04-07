x=int(input(""))
"""
if x%6==0 :
    print("6의 배수입니다.")
else :
    print("6의 배수가 아닙니다.")"""

"""
if x%6==0 :
    print("6의 배수")
    
elif x%2==0 :
    print("2의 배수")

elif x%3==0 :
    print("3의 배수")
"""


if x%2==0 : #2 4 6 8 10 12
    if x%3==0 : # 6 12 
        print("6의 배수")
    else :
        print("2의 배수")
elif x%3==0 :
    print("3의 배수")
