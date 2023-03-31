import sympy
from sympy import poly

def associative_checker(s, op):
    for i in s:
        for j in s:
            for k in s:
                if(op[(i,op[(j,k)])] != op[(op[(i,j)],k)]):
                    return False
    return True

def identity_elements_search(s,op):
    unit_elements = []
    for i in s:
        flag = True
        for j in s:
            if(not(op[i,j] == op[j,i] == j)):
                flag = False
        if flag:
            unit_elements.append(i)
    
    return unit_elements

def commutative_checker(s,op):
    for i in s:
        for j in s:
            if(op[i,j] != op[j,i]):
                return False
    
    return True

def inverse_checker(s,op,e):
    for i in s:
        flag = False
        for j in s:
            if(op[i,j] == e):
                flag = True
        if(flag != True):
            return False
    
    return True

def alg_props(s,op):

    props = set()

    if associative_checker(s,op):
        props.add('associative')
    else:
        print("not associative")
    
    units = identity_elements_search(s,op)
    if len(units) == 1 :
        e = units[0]
        props.add('identity')
    else:
        print("there is not e")

        
    if commutative_checker(s,op):
        props.add('commutative')
    else:
        print("this is not commutative")
    
    if inverse_checker(s,op,e):
        props.add('inverse')
    else:
        print("there is not add inverse")
        
    return e,props
        

                
def alg_classifier(set,add,mult):
    
    zero, add_props = alg_props(set, add)

    if not {'associative','identity','inverse','commutative'} <= add_props:
        return None, None, None


    for i in set:
        for j in set:
            for k in set:
                if(mult[(i,add[(j,k)])] != add[(mult[(i,j)],mult[(i,k)])]):
                    print("not distributive")
                    return None,None,None
                if(mult[(add[(j,k)],i)] != add[(mult[(j,i)],mult[(k,i)])]):
                    print("not distributive")
                    return None,None,None

    one, mult_props = alg_props(set - {zero},mult)

    if not ({'associative','identity'} <= mult_props):
        return None,None,None

    if not('commutative' in mult_props):
        return zero,one,'ring'

    if 'inverse' in mult_props:
        return zero,one,'field'
    else:
        return zero,one,'commutative ring'

                
class Element:
    def __init__(self, alg,x):
        self.alg = alg
        self.val = x
    
    
    def __add__(self,other):
        return Element(self.alg,self.alg.add(self.val,other.val))

    def __iadd__(self,other):
        return Element(self.alg,self.alg.add(self.val,other.val))
    
    def __str__(self):
        return str(self.val)

    def __mul__(self,other):
        return Element(self.alg,self.alg.mult(self.val,other.val))

    def __imul__(self,other):
        return Element(self.alg,self.alg.mult(self.val,other.val))
    
                
class FiniteAlg:

    def __init__(self,uset,add,mult):
        self.zero,self.one,self.alg =  alg_classifier(uset,add,mult)
        self.uset = uset
        self._add_op = add # dict of {(a,b): a+b, (a,c): a+c, ... }
        self._mult_op = mult # dict
        self.finite =True
        
    def __call__(self, x): 
        if x in self.uset:
            return Element(self,x)
        else: 
            print("error: this element is not in this underlying set")


    def __len__(self):
        return len(self.uset)
    
    def add(self,x,y):
        if(x in self.uset and y in self.uset):
            return self._add_op[(x,y)]
        elif x not in self.uset :
            print(f"error: {x} is not in the field")
            return None
        elif y not in self.uset :
            print(f"error: {y} is not in the field")
            return None

    def mult(self,x,y):
        if(x in self.uset and y in self.uset):
            return self._mult_op[(x,y)]
        elif x not in self.uset :
            print(f"error: {x} is not in the field")
            return None
        elif y not in self.uset :
            print(f"error: {y} is not in the field")
            return None

def comp_sys_rep(alg,ideal):
    """
    get complete system of representatives
    :param alg (FiniteAlg object) : divided finit alg (ring is recomended)
    :param ideal(FiniteAlg object) : dividing finit alg (ideal is recomended)
    :return csr: complete system of representatives of alg/ideal
    """
    print("xxxx")




def factor_ring(expr,field,csr):
    """
    calculate polynomial factor ring
    :param expr (expr) : the generator of a principal ideal domain
    :param csr (list) : complete system of representatives
    :return: None
    """
    print("xxxx")
