import numpy as np
import matplotlib.pyplot as plt
def search(x2,y2,a):
#     пошук точки перетину
    k0=180*np.arctan2(y2-y0, x2-x0)/np.pi
    if k0<0:
        k0=k0+360                
    k0=round(k0,de)
    for i in range(m):        
        if k0 in K0[i]:
            ix=K0[i].index(k0)
            iy=i
#             print('k0=',k0,'; (', ix,';', iy,');','(', x1[ix],y1[iy],')', a)
            L=round(((x1[ix]-x0)**2+(y1[iy]-y0)**2)**0.5,2)
            L0.append([x1[ix],y1[iy],k0,L])
#             plt.annotate(str(x1[ix])+';'+str(y1[iy])+'/'+str(k0), xy=(x1[ix],y1[iy]), fontsize=7)
        
def K1():
#     кут для кожної точки
    ii=0
    for i in y1: #рядки,        
        for j in x1: #стовпчики,
            k=180*np.arctan2(i-y0, j-x0)/np.pi
            if k<0:
                k=k+360
            K0[ii].append(round(k,de))  #m-ii-1      
#             plt.annotate(str(j)+';'+str(i)+'/'+str(round(k,2)), xy=(j,i), fontsize=7)
#             plt.annotate(str(j-x0)+';'+str(i-y0)+'/'+str(round(k,2)), xy=(j,i), fontsize=7)
#             print(round(k,3), end=' ')
#         print('///',len(K0[ii]))
        ii=ii+1
        

def lin1(x0,y0,e):
#     лінії усіх напрямків
    a=0
    while a<360:
        tg=np.tan(a*np.pi/180)        
        xm=x1[-1]
        ym=y1[-1]
        dy1=(xm-x0)*tg
        dy2=(-xm-x0)*tg
        
        if y0+dy1<=ym:            
            y2=y0+dy1
            if a>=0 and a<=90:            
                plt.plot([x0,xm],[y0,y2],'-ob',markersize=w)
                search(xm,y2,a)
                #print(a,180*np.arctan2(y2-y0, xm-x0)/np.pi)        
        if y0+dy2<=ym:
            y2=y0+dy2
            if a>90 and a<=180:
                plt.plot([x0,-xm],[y0,y2],'-ob',markersize=w)
                search(-xm,y2,a)
                #print(a,180*np.arctan2(y2-y0, -xm-x0)/np.pi)
        if y0+dy2>=-ym:
            y2=y0+dy2
            if a>180 and a<=270:
                plt.plot([x0,-xm],[y0,y2],'-ob',markersize=w)
                search(-xm,y2,a)
                #print(a,360+180*np.arctan2(y2-y0, -xm-x0)/np.pi)
        if y0+dy1>=-ym:
            y2=y0+dy1
            if a>270 and a<360:
                plt.plot([x0,xm],[y0,y2],'-ob',markersize=w)
                search(xm,y2,a)
                #print(a,360+180*np.arctan2(y2-y0, xm-x0)/np.pi)
            
        if tg!=0:
            dx1=(ym-y0)/tg
            dx2=(-ym-y0)/tg
            
        else:
            if ym-y0>0:
                dx1=np.inf
            if -ym-y0<0:
                dx2=-np.inf        

        if x0+dx1<=xm:
            x2=x0+dx1
            if a>=0 and a<=90:            
                plt.plot([x0,x2],[y0,ym],'-ob',markersize=w)
                search(x2,ym,a)
                #print(a,180*np.arctan2(ym-y0, x2-x0)/np.pi)
        if x0+dx1>=-xm:
            x2=x0+dx1
            if a>90 and a<=180:            
                plt.plot([x0,x2],[y0,ym],'-ob',markersize=w)
                search(x2,ym,a)
                #print(a,180*np.arctan2(ym-y0, x2-x0)/np.pi)
        if x0+dx2>=-xm:
            x2=x0+dx2
            if a>180 and a<=270:            
                plt.plot([x0,x2],[y0,-ym],'-ob',markersize=w)
                search(x2,-ym,a)
                #print(a,360+180*np.arctan2(-ym-y0, x2-x0)/np.pi)
        if x0+dx2<=xm:
            x2=x0+dx2
            if a>270 and a<360:            
                plt.plot([x0,x2],[y0,-ym],'-ob',markersize=w)
                search(x2,-ym,a)
                #print(a,360+180*np.arctan2(-ym-y0, x2-x0)/np.pi)
        a=a+e            
Sn=20
Sm=20
x1 = np.linspace(-Sn, Sn, 2*Sn+1)
y1 = np.linspace(-Sm, Sm, 2*Sm+1)
m=len(y1)
w=0.1 #ширина лінії
#Функція отримує два одновимірних масиви
#повертає два двовимірних -  із усіма можливими парами у кожному
X, Y = np.meshgrid(x1,y1)
plt.axis('equal')

# точка
x0=0.5
y0=-0.5
plt.plot(x0,y0,'-om', markersize=2)
plt.annotate(str(x0)+';'+str(y0), xy=(x0,y0), fontsize=7)
K0=[[] for i in range(m)]
L0=[]
# точність; ціле число; к-ть цифр після коми для k
de=1
# крок кута
e=0.1
K1()
lin1(x0,y0,e)
# print(L0,len(L0))
# сортуємо по куту
L0.sort(key = lambda x: x[2])
# print(L0,len(L0))
# сортуємо по куту, а потім по довжині 
L0.sort(key = lambda x: (x[2],x[3]))
# print(L0,len(L0))
# залишаємо лише мінімальні значення для даного кута
L1=[]
L1.append(L0[0])
# plt.annotate(str(L1[0][0])+';'+str(L1[0][1])+'/'+str(L1[0][2]), xy=(L1[0][0],L1[0][1]), fontsize=7)
plt.plot([x0,L1[0][0]],[y0,L1[0][1]],'-or',markersize=w)
p=0
s=L1[0][3]
for i in range(1,len(L0)):
    if L1[p][2]!=L0[i][2]:
        L1.append(L0[i])        
        p=p+1
        s=s+L1[p][3]
#         plt.annotate(str(L1[p][0])+';'+str(L1[p][1])+'/'+str(L1[p][2]), xy=(L1[p][0],L1[p][1]), fontsize=7)
        plt.plot([x0,L1[p][0]],[y0,L1[p][1]],'-or',markersize=w)
        
print(L1, len(L1))
# L*d=S/N
N=(2*Sn+1)*(2*Sm+1) #кількість точок
S=2*Sn*2*Sm #площа
d=10**(-de)/2 #розмір точки
print(d)
s1=round(s/len(L1),2) #довжина вільного пробігу з моделі
s2=round(S/N/d,2) #довжина вільного пробігу з теорії
ds=round(100*(s2-s1)/s2,2) #відносна похибка
print('sм=',s1, 'sт=',s2, ds,'%')
# сітка з точок розміром x×y
plt.plot(X,Y, '-ok', markersize=1, linewidth=0)
plt.show()

# 'b' blue
# 'g' green
# 'r' red
# 'c' cyan
# 'm' magenta
# 'y' yellow
# 'k' black
# 'w' white