from motor_control.height import height

def qnum(value, made):
        q = 0
        w = 0
        for i in made[value]:
            if i.isupper():
                q += 1
            elif i.islower():
                w += 1
        return height(q, w)



def cnum(value, value1):
        q = 0
        w = 0
        if value1[0][value].isupper():
            q += 1
        elif value1[0][value].islower():
            w += 1

        if value1[1][value].isupper():
            q += 1
        elif value1[1][value].islower():
            w += 1

        if value1[2][value].isupper():
            q += 1
        elif value1[2][value].islower():
            w += 1
        return height(q, w)


def abcs(o, f):
    if f == 1:
        coef = 0.075    
    elif f == 2:
        coef = 0.1125
    elif f == 3:
        coef = 0.225
    return(round( int(o/coef),0)*coef)