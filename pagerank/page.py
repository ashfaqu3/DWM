import numpy as np
x=int(input('Enter the number of input'))
d=0.85
eps=1.0e-8
print("\Enter the adjacency matrix for network")
print("\Type 1 if there is a link from a page i to j else type 0")
links=[]
for i in range(0,x):
    l =[]
    for j in range(0,x):
        l.append(int(input('page'+str(i+1)+'to page '+str(j+1)+': ')))
    links.append(l)
        
        
outboundL=np.zeros((x,),dtype=int)

for i in range(0,x):
    
    for j in range(0,x):
        if links[i][j]==1:
            outboundL[i] = outboundL+1

M= np.zeros((x,x))
for i in range(0,x):
    
    for j in range(0,x):
        if links[j][i]==1:
            M[i][j]=1/outboundL[j]

M=np.matrix(M)
oneColMat=np.matrix(np.ones((x,1),dtype=int))

R=np.matrix(np.full((x,1),1/x))

while True:
    Rnext=d*np.dot(M,R)+((1-d)/x)*oneColMat
    diff=np.subtract(Rnext,R)
    if np.linalg.norm(diff)<eps:
        break
    R=Rnext
    