#!/usr/bin/python3

def AddHeadFile(blockParms):
    headString=[]
    headString.append('##########################################')
    headString.append('#  Ring parameter file: PET_module.blockparms')
    headString.append('#  Author/Owner:        gsize')
    headString.append('#  Comments:  blockLength:'+ str(blockParms['blockLength']))
    headString.append('#             crystalNumbers:' +str(blockParms['crystalNumbers']) )
    headString.append('#             crystalSize:' +str(blockParms['crystalLenght']) +' unit cm' )
    headString.append('##########################################')

    headString.append('# Reference point on block used for ring position & orientation.')
    headString.append('REAL block_reference_y       =   0.00000000000000')
    headString.append('REAL block_reference_z       =   0.00000000000000')
    headString.append('REAL block_reference_z       =   0.00000000000000')
    headString.append(' ')
    return headString

def AddBlock(blockParms):
    blockString=[]
    blockString.append('# BLOCK OUTER DIMENSIONS')
    blockString.append('# Provides the outer bounds of the block.  The maximum and minimum extent of the block')
    blockString.append('# are given with respect to the reference point.  The coordinates (X,Y,Z) represent the')
    blockString.append('# radial, transaxial, and axial directions, respectively.')

    blockString.append('REAL    block_x_minimum         =  '+str(blockParms['boundary_x'][0])) 
    blockString.append('REAL    block_x_maximum         =  '+str(blockParms['boundary_x'][-1])) 
    blockString.append('REAL    block_y_minimum         =  '+str(blockParms['boundary_y'][1][0])) 
    blockString.append('REAL    block_y_maximum         =  '+str(blockParms['boundary_y'][1][-1])) 
    blockString.append('REAL    block_z_minimum         =  '+str(blockParms['boundary_z'][1][0])) 
    blockString.append('REAL    block_z_maximum         =  '+str(blockParms['boundary_z'][1][-1])) 

    blockString.append('INT    block_num_layers        =   '+str(len(blockParms['boundary_x'])-1)) 
    for n in range(0,len(blockParms['boundary_x'])-1):
        blockString.append(' ')
        blockString.append('NUM_ELEMENTS_IN_LIST    block_layer_info_list = 5')
        blockString.append(' ')
        blockString.append('        REAL           block_layer_inner_x   =  ' +str(blockParms['boundary_x'][n]))
        blockString.append('                       # (must be == to outer x of previous layer)')
        blockString.append('')
        blockString.append('        REAL           block_layer_outer_x   = =  ' +str(blockParms['boundary_x'][n+1]))
        blockString.append('')
        if len(blockParms['boundary_y'][n])>0:
            blockString.append('        NUM_ELEMENTS_IN_LIST    block_layer_num_y_changes = '+str(len(blockParms['boundary_y'][n])-2))
            for i in range(1,len(blockParms['boundary_y'][n])-1):
                blockString.append('        REAL           block_layer_y_change  = '+str(blockParms['boundary_y'][n][i]))
        else:
            blockString.append('        NUM_ELEMENTS_IN_LIST    block_layer_num_y_changes = 0')

        blockString.append('')
        if len(blockParms['boundary_z'][n])>0:
            blockString.append('        NUM_ELEMENTS_IN_LIST    block_layer_num_z_changes = '+str(len(blockParms['boundary_z'][n])-2))
            for i  in range(1,len(blockParms['boundary_z'][n])-1):
                blockString.append('        REAL           block_layer_z_change  = '+str(blockParms['boundary_z'][n][i]))
        else:
            blockString.append('        NUM_ELEMENTS_IN_LIST    block_layer_num_z_changes = 0')

        blockString.append('')
        material_elements=(len(blockParms['material_index'][n]))
        blockString.append('        NUM_ELEMENTS_IN_LIST    block_layer_material_elements  = '+str(material_elements))
        for i in range(material_elements):
            blockString.append('            # Material element  ' +str(i))
            blockString.append('            NUM_ELEMENTS_IN_LIST    block_material_info_list = 2')
            blockString.append('                INT block_material_index = '+str(blockParms['material_index'][n][i]))
            blockString.append('                BOOL    block_material_is_active = ' +blockParms['material_active'][n][i])

    return blockString

def GetBoundary(blockLength,crystalNumber,crystalLen,spacingLen,centraflag=1):
    boundary=[-blockLength/2.]
    step=crystalLen+spacingLen
    firstCrystalOffset=step/2.0*(1-crystalNumber)
    if centraflag !=1 :
        firstCrystalOffset-=boundary[0]
        boundary=[0.0]
    for i in range(crystalNumber):
        boundary.append(firstCrystalOffset+i*step-crystalLen/2.0)
        boundary.append(firstCrystalOffset+i*step+crystalLen/2.0)
    boundary.append(blockLength/2.)
    if centraflag !=1 :
        boundary[-1]=blockLength

    return boundary



if __name__=='__main__':
    blockParms={}
    blockParms.update({'blockLength':(2.001,6.72,10.08)})## crystalLenght (x,y,z),cm unit 
    blockParms.update({'crystalNumbers':(1,16,24)})
    blockParms.update({'crystalLenght':(2.0,0.4,0.4)}) ## crystalLenght (x,y,z),cm unit 
    blockParms.update({'crystalSpacing':(0.02,0.02,0.02)}) ## crystalLenght (x,y,z),cm unit 
    blockParms.update({'crystallMarerial':29}) ## crystalLenght (x,y,z),cm unit 
    blockParms.update({'wrapMarerial':0}) ## crystalLenght (x,y,z),cm unit 
    blockParms.update({'haveGapAroundCrystal':1}) ## crystalLenght (x,y,z),cm unit 

    print(blockParms['crystalNumbers'])

    boundary_x=GetBoundary(blockParms['blockLength'][0],blockParms['crystalNumbers'][0],blockParms['crystalLenght'][0],blockParms['crystalSpacing'][0],0)
    boundary_y=GetBoundary(blockParms['blockLength'][1],blockParms['crystalNumbers'][1],blockParms['crystalLenght'][1],blockParms['crystalSpacing'][1])
    boundary_z=GetBoundary(blockParms['blockLength'][2],blockParms['crystalNumbers'][2],blockParms['crystalLenght'][2],blockParms['crystalSpacing'][2])

    blockParms.update({'boundary_x':boundary_x})  

    material_index0=[]
    material_active0=[]
    boundary_y0=[]
    boundary_z0=[]
    for k in range(len(blockParms['boundary_x'])-1):
        material_index=[]
        material_active=[]
        if k==1:
            boundary_y0.append(boundary_y)
            boundary_z0.append(boundary_z)
            for i in range(len(boundary_z)-1):
                for j in range(len(boundary_y)-1):
                    if j%2==1 and i%2==1:
                        material_index.append( 29)
                        material_active.append('TRUE')
                    else:
                        material_index.append( 0)
                        material_active.append('FALSE')
        else:
            boundary_y0.append([])
            boundary_z0.append([])
            material_index.append( 0)
            material_active.append('FALSE')
        material_index0.append(material_index)
        material_active0.append(material_active)

    blockParms.update({'boundary_y':boundary_y0})  
    blockParms.update({'boundary_z':boundary_z0})  
    blockParms.update({'material_index':material_index0})
    blockParms.update({'material_active':material_active0})

    outfile=r'PET2L_module_new_test.blockparms'
    headStr = AddHeadFile(blockParms)
    blockStr=AddBlock(blockParms)
    #'''
    pf=open(outfile,'w')

    for i in range(0,len(headStr)):
        print(headStr[i])
        pf.write(headStr[i]+'\n')

    for i in range(0,len(blockStr)):
        print(blockStr[i])
        pf.write(blockStr[i]+'\n')

    pf.close()
    #'''

