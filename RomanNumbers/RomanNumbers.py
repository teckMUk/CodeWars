import sys



def solution(n):
    # TODO convert int to roman string
    roman_dict = {1:"I",5:"V",10:"X",50:"L",100:"C",500:"D",1000:"M"}
    x = str(n)
    roman_value = ""
    for num in reversed(range(len(x))):
        postion = pow(10,num)
        res = int(n/postion)
        res = res*postion
        if res==0:
            continue
        n = int(n%postion)
        if res in roman_dict.keys():
            roman_value += roman_dict[res]
        else:
            prevkey,nextkey = findsymbolkey(roman_dict,res)
            counter = 0
            if prevkey==postion:
                counter+=1
            z = prevkey
            while z!=res:
                z+=postion
                counter+=1    
            if counter>3:
                differnce = int((nextkey-res)/postion)
                roman_value += roman_dict[postion]*differnce
                roman_value+= roman_dict[nextkey]
            else:
                roman_value += roman_dict[prevkey]
                if prevkey==postion:
                    counter-=1
                roman_value += roman_dict[postion]*(counter)           
    return roman_value

def findsymbolkey(x,value):
    prev = 0
    for num in x.keys():
        if value < num:
            return (prev,num)
        prev = num
    return (prev,prev)

#takes argument from cmd
def main(args=None):
    if args is None:
        args = int(sys.argv[1])
    print("Your Roman Numeric is: ",solution(args))   
    

if __name__ == "__main__":
    main()