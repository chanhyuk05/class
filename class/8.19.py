x=input("자신:")
y=input("상대:")

if x=="바위" :
    if y=="가위":
        print("승리")
    elif y=="보" :
        print("패배")
    elif y=="바위" :
        print("무승부")
    else :
        print("※ 잘못된 입력※")

elif x=="가위" :
    if y=="바위" :
        print("패배")
    elif y=="보" :
        print("승리")
    elif y=="가위" :
        print("무승부")
    else :
        print("※ 잘못된 입력※")

elif x=="보" :
    if y=="보" :
        print("무승부")
    elif y=="바위" :
        print("승리")
    elif y=="가위" :
        print("패배")
    else :
        print("※ 잘못된 입력※")

else :
    print("※ 잘못된 입력※")
