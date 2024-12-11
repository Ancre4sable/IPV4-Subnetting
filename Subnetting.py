import sys


def main():
    IP = input("Enter your IP address:")
    slash = input("/ write the number:")
    print(f"Your IP address: {IP}/{slash} ")
    
    isTruth(IP,slash)




def isTruth(ip,slash):
    a,b,c,d=ip.split(".")

    okt1=int(a)
    okt2=int(b)
    okt3=int(c)
    okt4=int(d)
    slash=int(slash)

    if okt1<0 or okt1>255:
        sys.exit("Error!")
    if okt2<0 or okt2>255:
        sys.exit("Error!")
    if okt3<0 or okt3>255:
        sys.exit("Error!")
    if okt4<0 or okt4>255:
        sys.exit("Error!")    
    if slash<0 or slash>32:
        sys.exit("Error!") 
        
    Calculate(okt1,okt2,okt3,okt4,slash)


def Calculate(okt1,okt2,okt3,okt4,slash):
    
    b_okt1 = okt1
    b_okt2 = okt2
    b_okt3 = okt3
    b_okt4 = okt4
    
    remainder = 32-slash
    Counter = 0
    while(remainder >= 8):
        remainder -= 8
        Counter += 1
        
    if Counter == 0:
        exponent = pow(2, remainder)
        temp = exponent
        while(exponent < okt4):
            exponent += temp
            
        b_okt4 = exponent-1
        
        exponent -= temp
        okt4 = exponent
        
    elif Counter == 1:
        exponent = pow(2, remainder)
        temp = exponent
        while(exponent < okt3):
            exponent += temp
        b_okt4 = 255
        b_okt3 = exponent-1
        
        exponent -= temp
        okt4 = 0
        okt3 = exponent
        
    elif Counter == 2:
        exponent = pow(2, remainder)
        temp = exponent
        while(exponent < okt2):
            exponent += temp
        b_okt4 = 255
        b_okt3 = 255
        b_okt2 = exponent-1
            
        exponent -= temp
        okt4 = 0
        okt3 = 0
        okt2 = exponent
        
    else:
        exponent = pow(2, remainder)
        temp = exponent
        while(exponent < okt1):
            exponent += temp
        b_okt4 = 255
        b_okt3 = 255
        b_okt2 = 255
        b_okt1 = exponent-1
        
        exponent -= temp
        okt4 = 0
        okt3 = 0
        okt2 = 0
        okt1 = exponent

    print(f"Network address: {okt1}.{okt2}.{okt3}.{okt4}")
    print(f"Broadcast address: {b_okt1}.{b_okt2}.{b_okt3}.{b_okt4}")
        
main()