#!/bin/python
class bead:
    ''' class bead contains all info about bead in chain: global number, 
    the remaining valence, type of the bead and coordinates '''
    numbd=int()
    valence=int()
    typep=int()
    x=float()
    y=float()
    z=float()
    
class bond:
    '''class bond contains all info about bond: which beads connected by this bond'''
    first=int()
    last=int()
    
class chain:
    '''class chain has two lists of beads and bonds and general info about system such as total number of particles, density and box size along each axis'''
    def __init__(self):
        self.bd=[]
        self.bnd=[]
        self.number_of_beads=float()
        self.number_of_bonds=float()
        self.density=float()
        self.xbox=float()
        self.ybox=float()
        self.zbox=float()
    
def read_rst (f, polymer):
    '''function to read the restart file to the class chain, get path to file and name of chain'''
    one=bead()
    sb=bond()
    bnd=False
    for i,line in enumerate(f):
        if i==0:
            head,tail=line.split()
            polymer.number_of_beads = float(head)
            polymer.density = float(tail)
        elif i==1:
            xbox, ybox, zbox=line.split()
            polymer.xbox=float(xbox)
            polymer.ybox=float(ybox)
            polymer.zbox=float(zbox)
        elif 'bonds:' in line:
            bnd=True
        elif i>1 & bnd==False:
            one=bead()
            numbd,valence,typep,x,y,z=line.split()
            one.numbd=int(numbd)
            one.valence=int(valence)
            one.typep=int(typep)
            one.x=float(x)
            one.y=float(y)
            one.z=float(z)
            if one.typep==2:
                polymer.bd.append(one)
        elif 'angles' in line:
            print ('Reading finished')
        elif bnd:
            sb=bond()
            head,tail=line.split()
            sb.first=int(head)
            sb.last=int(tail)
            polymer.bnd.append(sb)

def sortcl (polymer):
    '''function sorts the chain class, only beads'''
    emp=bead();
    for i in range(len(polymer.bd)-1):
        for j in range (len(polymer.bd)-i-1):
            if polymer.bd[j].numbd > polymer.bd[j+1].numbd:
                #polymer.bd[i], polymer.bd[j] = polymer.bd[j], polymer.bd[i]
                emp=polymer.bd[j]
                polymer.bd[j]=polymer.bd[j+1]
                polymer.bd[j+1]=emp

def removePBC (polymer):
    '''revome periodic boundary conditions in case of single chain and numbers of beads corresspond to the global numbers and start from 1'''
    itx=0
    ity=0
    itz=0
    for i in range(len(polymer.bd)-1):
        if polymer.bd[i].x - itx * polymer.xbox - polymer.bd[i+1].x > polymer.xbox / 2:
            itx = itx + 1
            polymer.bd[i+1].x = polymer.bd[i+1].x + itx*polymer.xbox
        elif polymer.bd[i].x - itx * polymer.xbox - polymer.bd[i+1].x < -polymer.xbox / 2:
            itx = itx - 1
            polymer.bd[i+1].x = polymer.bd[i+1].x + itx*polymer.xbox
        else:
            polymer.bd[i+1].x = polymer.bd[i+1].x + itx*polymer.xbox
            
        if polymer.bd[i].y - ity * polymer.ybox - polymer.bd[i+1].y > polymer.ybox / 2:
            ity = ity + 1
            polymer.bd[i+1].y = polymer.bd[i+1].y + ity*polymer.ybox
        elif polymer.bd[i].y - ity * polymer.ybox - polymer.bd[i+1].y < -polymer.ybox / 2:
            ity = ity - 1
            polymer.bd[i+1].y = polymer.bd[i+1].y + ity*polymer.ybox
        else:
            polymer.bd[i+1].y = polymer.bd[i+1].y + ity*polymer.ybox
            
        if polymer.bd[i].z - itz * polymer.zbox - polymer.bd[i+1].z > polymer.zbox / 2:
            itz = itz + 1
            polymer.bd[i+1].z = polymer.bd[i+1].z + itz*polymer.zbox
        elif polymer.bd[i].z - itz * polymer.zbox - polymer.bd[i+1].z < -polymer.zbox / 2:
            itz = itz - 1
            polymer.bd[i+1].z = polymer.bd[i+1].z + itz*polymer.zbox
        else:
            polymer.bd[i+1].z = polymer.bd[i+1].z + itz * polymer.zbox
            
def writeMol2 (polymer, path):
    bstr='1  ala'
    with open(path, 'w') as the_file:
        the_file.write('@<TRIPOS>MOLECULE\n')
    with open(path, 'a') as the_file:
        the_file.write('mol_name\n')
    with open(path, 'a') as the_file:
        the_file.write('\t %d \t %d \t %s \t %s \t %s \n' %(len(polymer.bd), len(polymer.bnd), '0', '0', '0'))
    with open(path, 'a') as the_file:
        the_file.write('SMALL\n')
    with open(path, 'a') as the_file:
        the_file.write('USER_CHARGES\n')
    with open(path, 'a') as the_file:
        the_file.write('@<TRIPOS>ATOM\n')
    for i in range(len(polymer.bd)):
        ty='O'
        if polymer.bd[i].typep==1:
            ty='C'
        with open(path, 'a') as the_file:
            the_file.write('%d \t %s \t %f \t %f \t %f \t %s \t %s \t %f \n' %(i+1, ty, polymer.bd[i].x, polymer.bd[i].y, polymer.bd[i].z, ty, bstr, float(i)))
    with open(path, 'a') as the_file:
        the_file.write('@<TRIPOS>BOND\n')
    for i in range(len(polymer.bnd)):
        with open(path, 'a') as the_file:
            the_file.write('%d \t %d \t %d \t %s \n' %(i+1, polymer.bnd[i].first, polymer.bnd[i].last, '1'))
            
def main():
    for i in range(2,103):
        path = 'restart'+str(i)+'.dat'
        f0=open(path)
        polymer0=chain()
        read_rst(f0,polymer0)
        sortcl (polymer0)
        removePBC (polymer0)
        writeMol2(polymer0, 'restart'+str(i)+'.mol2')
main()