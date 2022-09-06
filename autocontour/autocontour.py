import os
import argparse
import SimpleITK as sitk
from AutocontourKnee import *
from ..util.scanco_rescale import convert_hu_to_bmd

if __name__ == '__main__':
    # Parse input arguments
    parser = argparse.ArgumentParser()
    parser.add_argument( 'image_path', type=str, help='Image (path + filename)' )
    args = parser.parse_args()

    image_path = args.image_path

    # Create a new folder to hold the output images
    image_dir = os.path.dirname(image_path)
    basename = os.path.splitext(os.path.basename(image_path))[0]

    prx_mask_path = os.path.join(image_dir, basename + '_PRX_MASK.nii')
    dst_mask_path = os.path.join(image_dir, basename + '_DST_MASK.nii')
    mask_path = os.path.join(image_dir, basename + '_MASK.nii')

    # Read in images as floats to increase precision
    image = sitk.ReadImage(image_path, sitk.sitkFloat32)
    image_bmd = convert_hu_to_bmd(image, 0.2409, 1603.51904, -391.209015)

    # Run the autocontour method for each bone
    auto_contour = AutocontourKnee()
    prx_mask = auto_contour.get_periosteal_mask(image_bmd, 1)
    dst_mask = auto_contour.get_periosteal_mask(image_bmd, 2)

    # Create a mask for the entire joint
    mask = prx_mask + dst_mask

    sitk.WriteImage(mask, mask_path)
    sitk.WriteImage(prx_mask, prx_mask_path)
    sitk.WriteImage(dst_mask, dst_mask_path)

