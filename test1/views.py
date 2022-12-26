from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def index(request):
    # قيم الامثال في التابع
    cx=0
    cy=0
    cz=0

    #امثال الشرط
    bx=0
    by=0
    bz=0
    band=0
    cond=0

    #حفظ قيم امثال التابع
    if 'cx' in request.GET:
        cx = request.GET['cx']
        cx=float(cx)
    if 'cy' in request.GET:
        cy = request.GET['cy']
        cy=float(cy)
    if 'cz' in request.GET:
        cz = request.GET['cz']
        cz=float(cz)
    
    #حفظ قيم امثال الشرط
    if 'bx' in request.GET:
        bx = request.GET['bx']
        bx=float(bx)
    if 'by' in request.GET:
        by = request.GET['by']
        by=float(by)
    if 'bz' in request.GET:
        bz = request.GET['bz']
        bz=float(bz)
    #التقاط الشرط (اكبر او يساوي ,اصغر او يساوي)
    if 'band' in request.GET:
        band = request.GET['band']
    #الشرط
    if 'cond' in request.GET:
        cond = request.GET['cond']
        cond=float(cond)

    #import numpy as np
    def foo(x,y,z):
        
        return cx*x + cy*y + cz*z 
    
    def fitness(x,y,z):
        if( band == 1):
            if( bx*x + by*y + bz*z<= cond):
                ans = foo(x,y,z)
                if ans == 0:
                    return 99999
                else:
                    return abs(1/ans)
            else:
                return -1
        else:        
            if( bx*x + by*y + bz*z>=cond):
                ans = foo(x,y,z)
                if ans == 0:
                    return 99999
                else:
                    return abs(1/ans)
            else:
                return -1
        
    #generate solution
    selution = []
    for s in range(1000):
        selution.append((random.uniform(0,1000),
                        random.uniform(0,1000),
                        random.uniform(0,1000)))
    for i in range(1000):
        rankedsolution = []
        for s in selution:
            rankedsolution.append((fitness(s[0],s[1],s[2]),s))
        rankedsolution.sort()
        rankedsolution.reverse()
        print(f"=== Gen {i} best solution ===")
        print(rankedsolution[0])

        if rankedsolution[0][0] > 999:
            break

        bestsolution = rankedsolution[:100]

        elements = []
        for s in bestsolution:
            elements.append(s[1][0])
            elements.append(s[1][1])
            elements.append(s[1][2])
        newGen = []
        for _ in range(1000):
            e1 = random.choice(elements) * random.uniform(0.99,1.01)
            e2 = random.choice(elements) * random.uniform(0.99,1.01)
            e3 = random.choice(elements) * random.uniform(0.99,1.01)
        
            newGen.append((e1,e2,e3))
        selution = newGen
        
    varia={
        
        's':selution,
        'r':rankedsolution,
        
    }
    return render(request, 'index.html',varia)