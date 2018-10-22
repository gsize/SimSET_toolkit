#!/usr/bin/python3

def AddHeadFile(ringParms):
    headString=[]
    headString.append('##########################################')
    headString.append('#  Ring parameter file: PET_module.ringparms')
    headString.append('#  Author/Owner:        gsize')
    headString.append('#  Comments:            '+str(ringParms['rsector_numbers']) + ' blocks per ring')
    headString.append('##########################################')

    headString.append('# RING OUTER DIMENSIONS')
    headString.append('# Provides the outer dimensions of the ring: all the blocks must fall entirely')
    headString.append('# within these boundaries.  The ring is bounded with a maximum and minimum')
    headString.append('# z value axially and by elliptical cylinders transaxially.  These bounds are not')
    headString.append('# in tomograph coordinates: the ring can shifted up or down axially or rotated')
    headString.append('# transaxially when placing it in the tomograph.')
    headString.append('REAL	ring_x_inner_radius     =   '+ str(ringParms['ring_x_inner_radius']))
    headString.append('REAL	ring_x_outer_radius     =   '+ str(ringParms['ring_x_outer_radius']))
    headString.append('REAL	ring_y_inner_radius     =   '+ str(ringParms['ring_y_inner_radius']))
    headString.append('REAL	ring_y_outer_radius     =   '+ str(ringParms['ring_y_outer_radius']))
    headString.append('REAL	ring_z_minimum          =   '+ str(ringParms['ring_z_minimum']))
    headString.append('REAL	ring_z_maximum          =   '+ str(ringParms['ring_z_maximum']))

    return headString

def AddRing(ringParms):
    rsectorNumbers=ringParms['rsector_numbers'];
    radialPos =ringParms['ring_block_radial_position'];
    angStep = 360./(rsectorNumbers);
    angStart=0.;
    ringString=[]
    ringString.append('NUM_ELEMENTS_IN_LIST   ring_num_blocks_in_ring  = '+ str(rsectorNumbers))

    for i in range(rsectorNumbers):
        angPos=angStart+i*angStep;
        ringString.append(' ')
        ringString.append('# Block    ' +str(i))
        ringString.append('NUM_ELEMENTS_IN_LIST   ring_block_description_list  = 5')
        ringString.append('STR      ring_block_parameter_file                  = "'+ringParms['ring_block_parameter_file'] +'"')
        ringString.append('REAL     ring_block_radial_position                 = ' + str(radialPos))
        ringString.append('REAL     ring_block_angular_position                = '+ str(angPos))
        ringString.append('REAL     ring_block_z_position                      = '+ str(ringParms['ring_block_z_position']))
        ringString.append('REAL     ring_block_transaxial_orientation          =  ' +  str(ringParms['ring_block_transaxial_orientation']))

    return ringString


if __name__=='__main__':
    ringParms={}
    ringParms.update({'ring_x_inner_radius':41.0})
    ringParms.update({'ring_x_outer_radius':45.0})
    ringParms.update({'ring_y_inner_radius':41.0})
    ringParms.update({'ring_y_outer_radius':45.0})
    ringParms.update({'ring_z_minimum':-5.04})
    ringParms.update({'ring_z_maximum':5.04})
    ringParms.update({'rsector_numbers':38})
    ringParms.update({'ring_block_parameter_file':"PET2L_module.blocparms"})
    ringParms.update({'ring_block_radial_position':41.5})
    ringParms.update({'ring_block_z_position':0.00000})
    ringParms.update({'ring_block_transaxial_orientation':0.00000})

    outfile=r'PET2L_module.ringparms'
    headStr = AddHeadFile(ringParms)
    ringStr=AddRing(ringParms)

    pf=open(outfile,'w')

    for i in range(0,len(headStr)):
        print(headStr[i])
        pf.write(headStr[i]+'\n')

    for i in range(0,len(ringStr)):
        print(ringStr[i])
        pf.write(ringStr[i]+'\n')

    pf.close()
