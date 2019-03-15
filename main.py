import random,os,time
class guys:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    @property
    def pos(self):
        return (self.x,self.y)
    def move(self):
        em=[]
        for i in range(-1,2):
            for j in range(-1,2):
                if l[(self.x+i,self.y+j)]==" ":
                    em.append((self.x+i,self.y+j))
        if em==[]:
            return
        else:
            h=em[random.randint(0,len(em)-1)]
            self.x=h[0]
            self.y=h[1]
def render(l):
    os.system("clear")
    n=1
    for i in l:
        print(l[i],end="")
        if n%51==0:
            print("\n",end="")
        n+=1
l={}
for i in range(0,51):
    for j in range(0,51):
        if i==0 or j==0 or i==50 or j==50:
            l[(i,j)]="#"
        else:
            l[(i,j)]=" "
while True:
    try:
        n=int(input("Please enter the number of guys: "))
        break
    except:
        print("Error!")
g=[]
for i in range(n):
    g.append(guys(i+2,i+2))
while True:
    for i in g:
        l[i.pos] = " "
        i.move()
        l[i.pos]="X"
    render(l)
    time.sleep(0.05)