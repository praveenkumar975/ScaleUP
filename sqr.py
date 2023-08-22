from turtle import *

ctr=0
sqd={}

def sqr(sz):
 for i in range(4):
  fd(sz)
  lt(90)

while True:
 s=input('>')
 lst=s.split()
 cmd=lst[0]
 if cmd=='bye':
  break
 if cmd=='square':
  amt=int(lst[1])
  sqid='sq_'+str(ctr)
  sqd[sqid]={
   'xy':pos(),
   's':amt
  }
  print(sqid)
  sqr(amt)
  ctr=ctr+1
 elif cmd=='move':
  x1=int(lst[1])
  y1=int(lst[2])
  print(x1,y1)
  pu()
  goto(x1,y1)
  pd()
 elif cmd=='sqdel':
  sqentry=sqd[lst[1]]
  print(sqentry)
  pu()
  goto(sqentry['xv'])
  pd()
  color('white')
  sqr(sqentry['s'])
  color('silver')
 elif cmd=='sqdir':
  print(sqd)
 elif cmd=='resurrent':
  deadsqid=lst[1]
  deadsquare=sqd[deadsqid]
  print('resurrecting',deadsquare)
  pu()
  goto(deadsquare['xy'])
  pd()
  sqr(deadsquare['s'])