#import numpy as np

def Main():
    x0 = [0, 0, 1, 1]
    x1 = [0, 1, 0, 1]
    y  = [0, 0, 0, 1]
    
    ypred = [0, 0, 0, 0]

    w0 = 0
    w1 = 0

    alpha = 0.1
    MAX_ITER = 100
    
    it=0
    erro = 1
    while abs(erro) > 0 and it<MAX_ITER:
        
        erro = 0
        acc = 0
        for i in range(len(x0)) :
            acc = ypred[i] + x0[i]*w0+ x1[i]*w1

            ypred[i] = degrau(acc)
        
            erro +=  (y[i] - ypred[i])
        erro = erro /len(x0)


        for i in range(len(x0)):
            w0 = w0 + alpha*erro*x0[i]
            w1 = w1 + alpha*erro*x1[i]

        #print(w0)
            

        print("fim da iteração %d, erro: %f"%(it, erro))
        print(ypred)
        it = it + 1

        #desnecessário, apenas para pausar para ver o erro da iteração atual
        input()
        

    print ("w0 = %f e w1 = %f" %(w0,w1))
    print(ypred)

    

def degrau(x):
    if x >=0.5:
        return 1
    else:
        return 0

if __name__ == "__main__":
    Main()
