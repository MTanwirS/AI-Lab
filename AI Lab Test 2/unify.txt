
def main():
    ch = 'y'
    while(ch == 'y'):
        npred = 0
        npred = int(input("Enter N of predicates:"))
        predicate = [None for i in range(npred)]
        narg = [None for i in range(npred)]

        for i in range(npred):
            print("Enter ", (i+1), "predicate :")
            predicate[i] = input()

        for i in range(npred):
            print("Enter N of arguments for predicate ", predicate[i], (i+1))
            narg[i] = int(input())

        argument = [[None for i in range(narg[i])] for i in range(npred)]

        for i in range(npred):
            for j in range(narg[i]):
                print("Enter ", j+1, "argument for", (i+1), "predicate" )
                argument[i][j] = input()

        display(npred , narg, predicate, argument )
        check_arg_pred(npred , narg, predicate, argument)
        ch = input("Continue (y/n)")


def display(npred , narg, predicate, argument):

    print("Predicates :")
    for i in range(npred):
        print(predicate[i], "(", end="")
        for j in range(narg[i]):
            print(argument[i][j], end="")
            if(j != narg[i]-1):
                print(",", end="")
        print(")")


def unify(npred , narg, predicate, argument):
    for i in range(npred-1):
        for j in range(narg[i]):
            if(argument[i][j] != argument[i+1][j]):
                if(isinstance(argument[i][j], int) and isinstance(argument[i+1][j], int)):
                    
                    print("Constant found not similar, unification not possible")
                    
                print("Substitution Θ{} = ".format(j+1), argument[i+1][j], "/", argument[i][j])
            else:
                print("Arguments are Identical...")
        


def check_arg_pred(npred , narg, predicate, argument):
    flagp = 0
    flaga = 0

    for i in range(npred-1):
        if(predicate[i] != predicate[i+1]):
            print("Unification not possible as predicates are different")
            flagp = 1
            break

    if(flagp != 1):
        for i in range(0, npred-1):
            if(narg[i] != narg[i+1]):
                print("Arguments Not Same..!")
                flaga = 1
                break            

        if(flaga == 0 and flagp != 1):
            unify(npred , narg, predicate, argument)



main()