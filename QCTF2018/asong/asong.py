#nothing to import  :)

key=[0xEC,0x29,0xE3,0x41,0xE1,0xF7,0xAA,0x1D,0x29,0xED,0x29,0x99,0x39,0xF3,0xB7,0xA9,0xE7,0xAC,0x2B,0xB7,0xAB,0x40,0x9F,0xA9,0x31,0x35,0x2C,0x29,0xEF,0xA8,0x3D,0x4B,0xB0,0xE9,0xE1,0x68,0x7B,0x41]

table=[0x16,0x0,0x6,0x2,0x1E,0x18,0x9,0x1,0x15,0x7,0x12,0x0A,0x8,0x0C,0x11,0x17,0x0D,0x4,0x3,0x0E,0x13,0x0B,0x14,0x10,0x0F,0x5,0x19,0x24,0x1B,0x1C,0x1D,0x25,0x1F,0x20,0x21,0x1A,0x22,0x23]

dic = {104:'a',30:'b',15:'c',29:'d',169:'e',19:'f',38:'g',67:'h',60:'i',0:'j',20:'k',39:'l',28:'m',118:'n',165:'o',26:'p',0:'p',61:'r',51:'s',133:'t',45:'u',7:'v',34:'w',0:'x',62:'y',0:'z',245:'_'}

#first recover:
recover=[]
recover.append(((key[37]<<5)&0xff)|(key[0]>>3))
for i in range(1,38):
  recover.append((key[i]>>3)|((key[i-1]<<5)&0xff))

#second recover:
i=1
for x in range(0,38):
  recover[table[i]]=recover[i]
  i=table.index(i)

#and return to flag:
flag=''
for i in recover:
  flag+=dic[i]

print 'QCTF{'+flag+'}'
