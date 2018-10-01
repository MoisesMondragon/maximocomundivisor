__autor__ ='moises mondragon mondragon'


def maximocomun(N,M):
    if (N < M):
        return maximocomun(M,N)
    elif(M == 0):
        return N
    else:
        return maximocomun(M, N%M)
N = int(input('porfavor ingrese el primer numero'))
M = int(input('porfavor ingrese el segundo numero'))
print ('el maximo comun divisor de los dos numeros es:'+str(maximocomun(N,M)))
