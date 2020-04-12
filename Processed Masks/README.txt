There are 2 types of masks present in the training set for the problem.

This folder contains the two types of masks. 

-Processed mask1 : masks obtained from the semantic segmentation of the CT's, using a type of algorithm, 
		which delimits the lungs from one another (one is gray, another is white)
-Processed mask2 : masks obtained from the semantic segmentation of the CT's, using another type of algorithm,
			which only delimits the lungs, no delimitation of lungs is done. 

Each folder contains another 3 folders with masks for the corresponding image on the CT (i.e. MSK1_2d_001, FrontBack, CTR_TRN_001_z2_55 
	corresponds to Processed Cts/CTR_TRN_001/FrontBack/CTR_TRN_001_z255).

Each folders in the MSK1/2  contains 3 folders:

-FrontBack :  it's the mask sliced from the front to the back. (As you would see a person that it's standing in front of you,
		facing you)

-LeftRight : it's the mask sliced from the left arm to the right one (As you would see a person from the side)

-TopBottom : it's the mask sliced from the bottom of the lungs to the top  (from stomach to shoulders)