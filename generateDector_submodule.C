
#include <fstream>

void AddHeader(stringstream &strstream,int rings)
{
strstream<<"##############################################################################"<<endl;
strstream<<"#"<<endl;
strstream<<"#       PARAMETER FILE FOR THE PHG SIMULATION"<<endl;
strstream<<"#"<<endl;
strstream<<"#       RUN NAME:	PET"<<endl;
strstream<<"#       CREATED:	2018 -8-30"<<endl;
strstream<<"#       OWNER:		gsize"<<endl;
strstream<<"#"<<endl;
strstream<<"#	This file gives parameters for PET block-based detectors."<<endl;
strstream<<"#	It is intended for use with the fastTest suite."<<endl;
strstream<<"#"<<endl;
strstream<<"#	This parameter file uses the block detector module."<<endl;
strstream<<"#"<<endl;
strstream<<"##############################################################################"<<endl;
strstream<<""<<endl;
strstream<<"# GENERAL DETECTOR MODULE PARAMETERS"<<endl;
strstream<<"	# DETECTOR TYPE"<<endl;
strstream<<"	# detector_type can be simple_pet or simple_spect (these just apply Gaussian"<<endl;
strstream<<"	# blurring to the energy with no tracking through the detector), or planar,"<<endl;
strstream<<"	# dual-headed, cylindrical, or block (these are photon-tracking simulations)"<<endl;
strstream<<"	ENUM detector_type = block"<<endl;
strstream<<""<<endl;
strstream<<"	# FORCED INTERACTION"<<endl;
strstream<<"	# Photons can be forced to interact at least once in the detector array.  This"<<endl;
strstream<<"	# is an importance sampling feature.  It often slows down block detector simulations."<<endl;
strstream<<"	BOOL do_forced_interaction = false"<<endl;
strstream<<""<<endl;
strstream<<"	# ENERGY RESOLUTION"<<endl;
strstream<<"	# Energy resolution is specified as a \% full-width-half-maximum of a"<<endl;
strstream<<"	# reference energy."<<endl;
strstream<<"	REAL    reference_energy_keV = 511.0"<<endl;
strstream<<"	REAL    energy_resolution_percentage = 16"<<endl;
strstream<<""<<endl;
strstream<<"	# HISTORY FILE"<<endl;
strstream<<"	# If a file pathname is given below, a list-mode (or history) file is created"<<endl;
strstream<<"	# giving all the photon information needed to continue the simulation"<<endl;
strstream<<"	# after the detector module.  Such a file is very big!"<<endl;
strstream<<"	# STR	history_file = \"\""<<endl;
strstream<<"	# The file can be made somewhat smaller by reducing the number of"<<endl;
strstream<<"	# parameters recorded per photon--however, the file can no longer be used"<<endl;
strstream<<"	# as input to the binning module."<<endl;
strstream<<"	#STR history_params_file = \"\""<<endl;
strstream<<""<<endl;
strstream<<"# POSITIONING ALGORITHM:  WHERE TO PLACE THE DETECTED POSITION WITHIN BLOCK"<<endl;
strstream<<"	# BLOCKTOMO_POSITION_ALGORITHM"<<endl;
strstream<<"	# what algorithm should be used to convert the interactions within a"<<endl;
strstream<<"	# block into a detected position?  The current default is"<<endl;
strstream<<"	# = snap_centroid_to_crystal_center"<<endl;
strstream<<"	# which takes uses the center of the crystal nearest to the"<<endl;
strstream<<"	# energy-weighted centroid of the interactions in active areas"<<endl;
strstream<<"	# of the block as the detected position.  The other option is"<<endl;
strstream<<"	# = use_energy_weighted_centroid"<<endl;
strstream<<"	# which will just use the energy-weighted centroid as the detected"<<endl;
strstream<<"	# position - note the latter does not guarantee that the detected"<<endl;
strstream<<"	# position will fall within an active area in the block!"<<endl;
strstream<<"	ENUM blocktomo_position_algorithm = snap_centroid_to_crystal_center"<<endl;
strstream<<"  "<<endl;
strstream<<"# DEFINITION OF RING POSITIONS"<<endl;
strstream<<"# Rings are stacked axially.  The axial extent of one ring cannot"<<endl;
strstream<<"# overlap that of another.  (If such an arrangement of blocks is"<<endl;
strstream<<"# desired, it can be achieved in a single ring.)"<<endl;
strstream<<"NUM_ELEMENTS_IN_LIST blocktomo_num_rings = "<<rings <<endl;
strstream<<""<<endl;
strstream<<"	# PLACEMENT AND DEFINITION OF RING 0"<<endl;
strstream<<"	# The rings must be listed by increasing axial position."<<endl;
strstream<<"	# A list of items must be given for each ring: the name of"<<endl;
strstream<<"	# the ring parameters file that defines it; the axial shift"<<endl;
strstream<<"	# (i.e., the axial position to shift the z=0 point of the slice"<<endl;
strstream<<"	# to); and the transaxial rotation, a counterclockwise"<<endl;
strstream<<"	# rotation between 0 and 360 degrees."<<endl;
strstream<<" "<<endl;
}
int generateDector()
{
	ofstream fout("PET_axial96.detparms",ios::out);
	float blockLen=3.38; // unit cm
	int submoduleNumbersTrans=12;

	stringstream header;
	AddHeader(header,submoduleNumbersTrans);
	fout<<header.str()<<endl;

	for(int i=0;i<submoduleNumbersTrans;i++)
	{
		float  zOffset1st=0.5*(1-submoduleNumbersTrans)*blockLen;
		float  zOffset=zOffset1st+i*blockLen;
		fout<<"	# Ring "<<i<<endl;
		fout<<"	NUM_ELEMENTS_IN_LIST	blocktomo_ring_description_list = 3"<<endl;
		fout<<"		STR		blocktomo_ring_parameter_file = \"PET.ringparms\""<<endl;
		fout<<"		REAL	blocktomo_ring_axial_shift = "<<zOffset  <<endl;
		fout<<"		REAL	blocktomo_ring_transaxial_rotation =  90"<<endl;
	}
	fout.close();
	return 0;
}
