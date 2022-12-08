def arithmetic_arranger(problems):
    arranged_problems = []
    for i in problems:
        arranged_problems = [item.split() for item in problems]

        if len(problems) > 5:
            print ('Error: Too many problems.')
            exit ()

        for i in arranged_problems:
            if i[0].isnumeric() != True or i[2].isnumeric() != True  :
                print ('Error: Numbers must only contain digits.')
                exit()

            num1 = int(i[0])
            num2 = int(i[2])
            sym = i[1]

            if sym != {'+',"-"} and sym != '+' and sym != '-':
                print ('Error: Operator must be "+" or "-".')
                exit()

            if len(i[0]) > 4 or len (i[2]) > 4:
                print ('Error: Numbers cannot be more than four digits.')
                exit()

            if sym == '+':
                ans = num1 + num2

            if sym == '-':
                ans = num1 - num2

            topline = str(num1)
            bottomline = str(num2)
            line = ''
            total= str(ans)

            if len(bottomline) > len(topline):
                for k in range(len(bottomline) + 2):
                    line +='-'
            else:
                for k in range(len(topline) + 2):
                    line +='-'

            space1, space2, space3 = '','',''

            n = len(line) - len(topline)
            for k in range(n):
                space1 += ' '

            if topline > bottomline or bottomline > topline:
                n = len(line) - len(bottomline)
                for j in range(n - 1):
                    space2 += ' '

            n = len(line) - len(total)
            for j in range(n):
                space3 += ' '

            arranged_problems = print (space1 + topline + '\n' + sym + space2 + bottomline + '\n' + line + '\n' + space3 + total + '\n')

        return arranged_problems
