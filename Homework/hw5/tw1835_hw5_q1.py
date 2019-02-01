from ArrayStack import ArrayStack

def eval_postfix_exp(exp_str):
    operators = "+-*/"
    args_stack = ArrayStack()
    exp_tokens = exp_str.split()

    for token in exp_tokens:
        if(token not in operators): #token is a number or variable
            try: # token is a number
                args_stack.push(int(token))
            except: # token is a variable
                var_val = vars_dict[token]
                args_stack.push(var_val)


        else: # if operator, do the arithmetic operation
            arg2 = args_stack.pop()
            arg1 = args_stack.pop()
            if (token == '+'):
                res = arg1 + arg2
            elif (token == '-'):
                res = arg1 - arg2
            elif (token == '*'):
                res = arg1 * arg2
            else: #token == '/'
                if(arg2 == 0):
                    raise ZeroDivisionError
                else:
                    res = arg1 / arg2
            args_stack.push(res)

    return args_stack.pop()

# val = eval_postfix_exp('2 3 4 + 3 * 4 6 - + *')
# print(val)


#------------ main --------------

# uncomment later

vars_dict = {}
input_exp = input('--> ')

while (input_exp != 'done()'):
    # if variable assignment -- first arg starts with a letter (and therefore is a variable) and there is a =
    input_exp_split = input_exp.split()
    if (input_exp_split[0][0].isalpha() and input_exp_split[1] == '='):
        arith_str = input_exp.split('= ')[1] # just string of the arithmetic expression
        arith_val = eval_postfix_exp(arith_str) # evaluation arith expression
        var_name = input_exp.split()[0]
        vars_dict[var_name] = arith_val # putting the variable and its value in the dictionary
        print(arith_val)
        input_exp = input('--> ')

    else: # regular arithmetic calculation
        print(eval_postfix_exp(input_exp))
        input_exp = input('--> ')
