def arithmetic_arranger(problems, sumprint=False):
    #Initial Declarations
    line1 = ''
    line2 = ''
    str_sum = ''
    total = ''
    linesp = ''
    
    # Rule #1
    if len(problems) > 5:
        return "Error: Too many problems."

    for p in problems:
        r = p.split()
        # Rule #3
        if r[0].isnumeric() == False or r[2].isnumeric() == False:
            
            return "Error: Numbers must only contain digits."
        # Rule #4
        if len(r[0]) >4 or len(r[2]) > 4:
            #print(r[0], r[2])
            return "Error: Numbers cannot be more than four digits."
        
        # Rule #2
        if r[1] == '+' or r[1] == '-':
            if r[1] == '+':
                sums = str(int(r[0]) + int(r[2]))
            else:
                sums = str(int(r[0]) - int(r[2]))
            numlen = max(len(r[0]), len(r[2])) + 2
            ltop = str(r[0]).rjust(numlen)
            lbottom = r[1] + r[2].rjust(numlen-1)
            line = ''
            total = str(sums).rjust(numlen)
            line = '-'*numlen
            # Build Individual line strings
            if p != problems[-1]:
                
                line1 += ltop + '    '
                line2 += lbottom + '    '
                linesp += line + '    '
                str_sum += total + '    '
            else:
                line1 += ltop
                line2 += lbottom
                linesp += line
                str_sum += total
            
        else:
            return "Error: Operator must be '+' or '-'."
    line1.rstrip()
    line2.rstrip()
    linesp.rstrip()
    arranged_problems = ''
    # Generate final output string - Conditionally add sum/diff.
    if sumprint == True:
        str_sum.rstrip()
        arranged_problems = line1 + '\n' + line2 +'\n' + linesp + '\n' + str_sum
    else:
        arranged_problems = line1 + '\n' + line2 +'\n' + linesp
    return arranged_problems