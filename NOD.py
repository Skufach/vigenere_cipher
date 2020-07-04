import  math

def DecompositionTwo(a):

    kol = 0;

    while ((a > 0) and (a % 2 == 0)):
        kol = kol + 1;
        a = math.floor(a // 2);

    return a, kol;

def NOD(a,b):
    a = int(a);
    b = int(b);

    a, kolA = DecompositionTwo(a);
    b, kolB = DecompositionTwo(b);

    k = min(kolA, kolB);

    while (a != b):

        if (a < b):
            t = b;
            b = a;
            a = t;

        c = a - b;
        c, l = DecompositionTwo(c);
        a = c;

    return 2**k * a;