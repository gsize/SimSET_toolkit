
#include <fstream>

int generateRing()
{
	float blockLen=3.38; // unit cm
	int rsectorNumbers=38;
	double radialPos_0 =41.5000;
	double pi=3.14159265358979323846264338;
	double angularTransaxialOrient = TMath::ATan(blockLen/2./radialPos_0)*180/pi;
	double radialPos=sqrt(pow(radialPos_0,2)+pow(blockLen/2.0,2));
	double angStep = 360./(rsectorNumbers);
	double angStart=0.;

	std::stringstream strstream;
	strstream<<"##########################################"<<endl;
	strstream<<"#"<<endl;
	strstream<<"#  Ring parameter file: PET.ringparms"<<endl;
	strstream<<"#  Author/Owner:        gsize"<<endl;
	strstream<<"#  Comments:            38 blocks per ring"<<endl;
	strstream<<"#                       ok"<<endl;
	strstream<<"##########################################"<<endl;
	strstream<<" "<<endl;
	strstream<<"# RING OUTER DIMENSIONS"<<endl;
	strstream<<"# Provides the outer dimensions of the ring: all the blocks must fall entirely"<<endl;
	strstream<<"# within these boundaries.  The ring is bounded with a maximum and minimum"<<endl;
	strstream<<"# z value axially and by elliptical cylinders transaxially.  These bounds are not"<<endl;
	strstream<<"# in tomograph coordinates: the ring can shifted up or down axially or rotated"<<endl;
	strstream<<"# transaxially when placing it in the tomograph."<<endl;
	strstream<<"REAL	ring_x_inner_radius     =   41.00000000000000"<<endl;
	strstream<<"REAL	ring_x_outer_radius     =   45.00000000000000"<<endl;
	strstream<<"REAL	ring_y_inner_radius     =   41.00000000000000"<<endl;
	strstream<<"REAL	ring_y_outer_radius     =   45.00000000000000"<<endl;
	strstream<<"REAL	ring_z_minimum          =   -1.69000000000000"<<endl;
	strstream<<"REAL	ring_z_maximum          =   1.69000000000000"<<endl;
	strstream<<""<<endl;
strstream<<"NUM_ELEMENTS_IN_LIST   ring_num_blocks_in_ring  = "<<rsectorNumbers*2<<endl;
//	strstream<<"NUM_ELEMENTS_IN_LIST   ring_num_blocks_in_ring  = "<<rsectorNumbers<<endl;

	for(int i=0;i<rsectorNumbers;i++)
	{
		double angPos1=angStart+i*angStep +angularTransaxialOrient ;
		double angPos2=angStart +(i+1)*angStep -angularTransaxialOrient;
		strstream<<"	 "<<endl;
		strstream<<"# Block    "<<i*2<<endl;
	//	strstream<<"# Block    "<<i<<endl;
		strstream<<"NUM_ELEMENTS_IN_LIST   ring_block_description_list  = 5"<<endl;
		strstream<<"STR      ring_block_parameter_file                  = \"PET.blocparms\""<<endl;
		strstream<<"REAL     ring_block_radial_position                 = "<<setprecision(13)<<radialPos <<endl;
		strstream<<"REAL     ring_block_angular_position                = "<<angPos1 <<endl;
		strstream<<"REAL     ring_block_z_position                      = 0.00000000000000"<<endl;
		strstream<<"REAL     ring_block_transaxial_orientation          = "<< -angularTransaxialOrient<<endl;
		strstream<<"	 "<<endl;
		strstream<<"# Block    "<<i*2+1<<endl;
		strstream<<"NUM_ELEMENTS_IN_LIST   ring_block_description_list  = 5"<<endl;
		strstream<<"STR      ring_block_parameter_file                  = \"PET.blocparms\""<<endl;
		strstream<<"REAL     ring_block_radial_position                 = "<<radialPos <<endl;
		strstream<<"REAL     ring_block_angular_position                = "<<angPos2 <<endl;
		strstream<<"REAL     ring_block_z_position                      = 0.00000000000000"<<endl;
		strstream<<"REAL     ring_block_transaxial_orientation          = "<< angularTransaxialOrient<<endl;
	}

	ofstream fout("PET.ringparms",ios::out);
	fout<<strstream.str();
	fout.close();
	return 0;
}
