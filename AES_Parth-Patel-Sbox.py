import math

data=raw_input('Enter the data:')
key=raw_input('Enter the key:')
sbox=[['63','7c','77','7b','f2','6b','6f','c5','30','01','67','2b','fe','d7','ab','76'],['ca','82','c9','7d','fa','59','47','f0','ad','d4','a2','af','9c','a4','72','c0'],['b7','fd','93','26','36','3f','f7','cc','34','a5','e5','f1','71','d8','31','15'],['04','c7','23','c3','18','96','05','9a','07','12','80','e2','eb','27','b2','75'],['09','83','2c','1a','1b','6e','5a','a0','52','3b','d6','b3','29','e3','2f','84'],['53','d1','00','ed','20','fc','b1','5b','6a','cb','be','39','4a','4c','58','cf'],['d0','ef','aa','fb','43','4d','33','85','45','f9','02','7f','50','3c','9f','a8'],['51','a3','40','8f','92','9d','38','f5','bc','b6','da','21','10','ff','f3','d2'],['cd','0c','13','ec','5f','97','44','17','c4','a7','7e','3d','64','5d','19','73'],['60','81','4f','dc','22','2a','90','88','46','ee','b8','14','de','5e','0b','db'],['e0','32','3a','0a','49','06','24','5c','c2','d3','ac','62','91','95','e4','79'],['e7','c8','37','6d','8d','d5','4e','a9','6c','56','f4','ea','65','7a','ae','08'],['ba','78','25','2e','1c','a6','b4','c6','e8','dd','74','1f','4b','bd','8b','8a'],['70','3e','b5','66','48','03','f6','0e','61','35','57','b9','86','c1','1d','9e'],['e1','f8','98','11','69','d9','8e','94','9b','1e','87','e9','ce','55','28','df'],['8c','a1','89','0d','bf','e6','42','68','41','99','2d','0f','b0','54','bb','16']]
const=['0','0','0','1','1','0','1','1']
def binary(N):# hex(string) to binary(string) conversion 
    log=int(math.log(16,2))
    bits=len(N)*log
    return str(bin(int(N,16))[2:].zfill(bits))
def hexa(N):# binary(string) to hex conversion
    N=int(N,2)
    return hex(N).split('x')[1]
def seg(N):
    oseg=[]
    for i in N:
        oseg.append(i)
    return oseg
def xor(N,N2):# N2(string) xor N3(string)[bitlevel]; output e is string list
    e=[]
    for i,j in zip(N,N2):
        if i==j:
            c='0'
        else:
            c='1'
        e.append(c)
    return e
def nonlst(N):
    s1=map(str,N)
    s1=''.join(s1)
    return s1
def fix(N):
    if N=='0':
        tempfix='00'
    elif N=='1':
        tempfix='01'
    elif N=='2':
        tempfix='02'
    elif N=='3':
        tempfix='03'
    elif N=='4':
        tempfix='04'
    elif N=='5':
        tempfix='05'
    elif N=='6':
        tempfix='06'
    elif N=='7':
        tempfix='07'
    elif N=='8':
        tempfix='08'
    elif N=='9':
        tempfix='09'
    elif N=='a':
        tempfix='0a'
    elif N=='b':
        tempfix='0b'
    elif N=='c':
        tempfix='0c'
    elif N=='d':
        tempfix='0d'
    elif N=='e':
        tempfix='0e'
    elif N=='f':
        tempfix='0f'
    else:
        tempfix=N
    return tempfix
def shift(l2,n2): # for left shift operation
    return l2[n2:] + l2[:n2]
def lshift(N,N1):return N[(len(N)-N1):]+N[:(len(N)-N1)]
def left(N):
    lft=N[1:]
    lft.append('0')
    return lft
def poly(N,N1):#input:N-strings(4 hex nos.) N1-required shift for mc, output:strings(4 hex nos.)
    rpt=0
    opoly=[]
    mc=['2','3','1','1']
    mc=lshift(mc,N1)
    while rpt<len(N):
        num=N[rpt]
        num=binary(num)###converts hex(string) to binary(string)
        num=seg(num)# converts '1110 0001' in to '1','1','1','0','0','0','0','1'
        if mc[rpt]=='2':
            buf=num
            num=left(num)#left shift operation; '1','1','1','0','0','0','0','1'==>'1','1','0','0','0','0','1','0'
            if buf[0]=='1':
                num=xor(num,const)# bitwise xor operation; both in:string, one out: string
            num=nonlst(num)
            num=hexa(num)
            num=fix(num)
            opoly.append(num)

        if mc[rpt]=='3':
            buf=num
            num=left(num)
            
            if buf[0]=='1':
                num=xor(num,const)# bitwise xor operation; both in:string, one out: string
            num=xor(num,buf)
            num=nonlst(num)
            num=hexa(num)
            num=fix(num)
            opoly.append(num)
            
        if mc[rpt]=='1':
            num=nonlst(num)
            num=hexa(num)
            num=fix(num)
            opoly.append(num)
        rpt+=1
    otemp=[]
    for i in opoly:
        num=binary(i)
        otemp.append(num)
    omc=xor(otemp[0],otemp[1])
    omc=xor(omc,otemp[2])
    omc=xor(omc,otemp[3])
    omc=nonlst(omc)
    omc=fix(hexa(omc))
    return omc
def devide(N):
    rpt1=0
    w=[]
    w1=[]
    w2=[]
    w3=[]
    w4=[]
    while rpt1<len(N):
        w.append(N[rpt1:(rpt1+2)])
        rpt1+=2
#    print w
    w1.append(w[0])
    w1.append(w[1])
    w1.append(w[2])
    w1.append(w[3])
    w2.append(w[4])
    w2.append(w[5])
    w2.append(w[6])
    w2.append(w[7])
    w3.append(w[8])
    w3.append(w[9])
    w3.append(w[10])
    w3.append(w[11])
    w4.append(w[12])
    w4.append(w[13])
    w4.append(w[14])
    w4.append(w[15])
    return [w1,w2,w3,w4]
def XOR(N,N1):#input:N=['11','22','33','44'],N1=['aa','bb','cc','dd'],output: xor of(N,N1)
    xora=[]
    rpt=0
    while rpt<4:
        bxor=seg(binary(N[rpt]))#converts '10' to '0','0','0','1','0','0','0','0'
        bxor1=seg(binary(N1[rpt]))#converts '10' to '0','0','0','1','0','0','0','0'
        oxor=xor(bxor,bxor1)#x oring gives binary out
        oxor=fix(hexa(nonlst(oxor)))# converts segmented binary to hex
        xora.append(oxor)
        rpt+=1
    return xora
def lbyte(N):#input:['11','22','33','44'],output:['22','33','44','11']
    return N[1:]+N[:1]
def ri(N,N1):##for e xor r(i)##input:N: i.e.'1b',N1:integer(range(4,8,16,..,40)),output:string(hex(r of input))
    if N1==4:
        eri='01'

    if N1==8:
        eri='02'

    if N1==12:
        eri='04'

    if N1==16:
        eri='08'

    if N1==20:
        eri='10'

    if N1==24:
        eri='20'

    if N1==28:
        eri='40'

    if N1==32:
        eri='80'

    if N1==36:
        eri='1b'

    if N1==40:
        eri='36'
    rio= fix(hexa(nonlst(xor(seg(binary(eri)),seg(binary(N))))))# e xor r(i):output:i.e.'1b'
    return rio
def transform(N,N1):#input:['11','22','33','44'], output:transform of['11','22','33','44']
    tf=bs(lbyte(N))
    tf1=ri(tf[0],N1)
    del tf[0]
    tf.insert(0,tf1)
    return tf
def step(N):# make a word of 2 hex digits
    t=0
    din=[]
    while t<len(N):
        a1=N[t]+N[t+1]
        din.append(a1)
        t+=2
    return din
    ######################### ARK Module #############################
def ark(N,N1):##N:data,N1: key
    d=step(N)
    k=step(N1)
    t=0
    out=[]
    while t<len(d):
        d1=d[t]
        k1=k[t]
        d1=binary(d1)
        k1=binary(k1)
        d1=seg(d1)
        k1=seg(k1)
        temp0=xor(d1,k1)
        temp0=nonlst(temp0)
        temp0=hexa(temp0)
        temp0=fix(temp0)
        out.append(temp0)
        t+=1
    return out
########################## BS Module ##############################
def bs(r1):#input:['11','22','33','44'];variable, output: bs of ['11','22','33','44']
    r2=[]
    for i1 in r1:
        temp1=binary(i1)
        t1=temp1[0:4]
        t2=temp1[4:8]
        t1=int(t1,2)
        t2=int(t2,2)
        k2=sbox[t1][t2]
        r2.append(k2)
    return r2
########################## SR Module ##############################
def sr(r3):
    rpt=0
    r4=[]
    while rpt<(len(r3)/4):
        for i in xrange(rpt,len(r3),4):
            r4.append(r3[i])
        rpt+=1
#    print r4####column results
    r5=[]
    temp=[]
    rpt=rpt1=gain=0
    var2=len(r4)/4
    while rpt<(var2):
        for i in xrange(rpt1,(var2+gain)):
            temp.append(r4[i])
        temp=shift(temp,rpt)
        r5=r5+temp
        temp=[]
        rpt1+=var2
        gain+=var2
        rpt+=1
#    print r5
    rpt=0
    out=[]
    while rpt<(len(r5)/4):
        for i in xrange(rpt,len(r5),4):
            out.append(r5[i])
        rpt+=1
    return out
########################### MC Module #############################
def MC(N):
    mcf=[]
    rpt=gain=0
    jump=len(N)/4
    while rpt<(len(N)):
        idnn=N[rpt:(jump+gain)]
        idnn1=poly(idnn,0)
        mcf.append(idnn1)
        idnn1=poly(idnn,1)
        mcf.append(idnn1)
        idnn1=poly(idnn,2)
        mcf.append(idnn1)
        idnn1=poly(idnn,3)
        mcf.append(idnn1)
        rpt+=jump
        gain+=jump
    return mcf
########################### KS Module #############################
########### gives list W that has key for round 0 to 10 ###########
def ks(N):
    Win=devide(N)
    indx=4
    while indx<44:
        if (indx%4)==0:
            tempks=XOR(Win[(indx-4)],transform(Win[(indx-1)],indx))
            Win.append(tempks)
        else:
            tempks=XOR(Win[(indx-4)],Win[(indx-1)])
            Win.append(tempks)
        indx+=1
    rpt=rpt1=0
    Roundin=[]
    while rpt<11:
        tround=Win[rpt1]+Win[rpt1+1]+Win[rpt1+2]+Win[rpt1+3]
        Roundin.append(tround)
        rpt+=1
        rpt1+=4
    return Roundin
########################### ASE Implementation ####################
print'Original Plaintext and Key:'
print'Input:',data
print'Key:  ',key
print'=========================================================================================================='
print'Key Schedule Results for Each Round:'
print'=========================================================================================================='
Round=ks(key)
rpt=0
while rpt<11:
    print 'Round',rpt,':'
    print '     Key:',Round[rpt],'\n'
    rpt+=1
print'==========================================================================================================='
print'Intermediate Results at Each Round:'
print'==========================================================================================================='
print'Round 0 : '
print'----Start:',step(data)
outr1=ark(data,key)
print'---Output:',outr1,'\n'
rpt=1
while rpt<10:
    print'Round',rpt,':'
    print'----Start:',outr1
    outr1=bs(outr1)
    print'-----SBox:',outr1
    outr1=sr(outr1)
    print'-ShiftRow:',outr1
    outr1=MC(outr1)
    print'MixColumn:',outr1
    outr1=ark(nonlst(outr1),nonlst(Round[rpt]))
    print'---Output:',outr1,'\n'
    rpt+=1
print'Round 10:'
print'----Start:',outr1
outr1=bs(outr1)
print'-----SBox:',outr1
outr1=sr(outr1)
print'-ShiftRow:',outr1
outr1=ark(nonlst(outr1),nonlst(Round[10]))
print'---Output:',outr1

