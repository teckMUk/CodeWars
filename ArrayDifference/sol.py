import sys
import ast

def array_diff(a, b):
        for number in b:
            while True:
                if number not in a:
                    break
                a.remove(number)
        return a

def array_diff_better_sol(a,b):
    return [number for number in a if number not in b]

def main(args=None):
    if args is None:
        list1 = ast.literal_eval(sys.argv[1])
        list2 = ast.literal_eval(sys.argv[2])
        result = array_diff(list1,list2)
        print("Array difference of list1 and list2 is:",result)
        result2 = array_diff(list1,list2)
        print("Array difference of list1 and list2 is with better solution:",result2)
        


if __name__ == "__main__":
    main()          