import sys

sys.path.append('/usr/local/lib/python2.7/site-packages')

import cv2
import os
import string
import os
import moviepy.video.io.ImageSequenceClip
from PIL import Image
import glob





def makeMovie_GWcatalogSize(fps=20, duration=60, name_images='none', number_images=400, image_folder='./GW_visualization_detection_number/'):
	'''
	whichRate = 'intrinsic' or 'observed'
	fps=0.4, frames per second
	duration = duration of the movie 
	'''

	

	images = []

	for ind_im  in range(number_images):
			images.append(image_folder +   name_images  + str(ind_im) + '.png')



	image_files = images
	clip = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(image_files, fps=fps)
	clip.write_videofile(image_folder+'movie_'+ name_images  + '.mp4')



	print('done')
	return 



def makeMovie_GWcatalogSizeJustConfirmed(fps=20, duration=60, name_images='none', image_folder='/Users/floorbroekgaarden/Projects/GitHub/GW_visualization_detection_number/GWcatalogFigures/'):
	'''
	whichRate = 'intrinsic' or 'observed'
	fps=0.4, frames per second
	duration = duration of the movie 
	'''



	images = []

	for ind_im  in range(5):
			images.append(image_folder +   name_images  + str(ind_im) + '.png')



	image_files = images
	clip = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(image_files, fps=fps)
	clip.write_videofile(image_folder+'movie_'+ name_images  + '.mp4')


	print('done')
	return 




def makeMovie_GWcatalogSizeO4(fps=60, duration=50, image_folder = '/Users/floorbroekgaarden/Projects/GitHub/GW_visualization_detection_number/GWcatalogMovieFigures/'):
	'''
	whichRate = 'intrinsic' or 'observed'
	fps=0.4, frames per second
	duration = duration of the movie 
	'''

	

	images = []

	for ind_im  in range(400):
			images.append(image_folder +   'O4GWcatalogSize_'  + str(ind_im) + '.png')

	image_files = images
	clip = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(image_files, fps=fps)
	clip.write_videofile(image_folder+'movie_'+ 'O4GWcatalogSize'  + '.mp4')

	# make also gif:
	# Create the frames
	frames = []
	# imgs = glob.glob("*.png")
	for i in images:
	    new_frame = Image.open(i)
	    frames.append(new_frame)
	 
	# Save into a GIF file that loops forever
	frames[0].save(image_folder+'gif_'+ 'O4GWcatalogSize' +  '.gif', format='GIF',
	               append_images=frames[1:],
	               save_all=True,
	               duration=duration, loop=0)

	print('done')
	return 







#####




Movie_GWcatalogSize=True


# Run this using python 3!! 
if Movie_GWcatalogSize==True:
	
	# # this just makes a slide show (slow movie) of the 5 catalogs 
	# image_folder='/Users/floorbroekgaarden/Projects/GitHub/GW_visualization_detection_number/GWcatalogFigures/'
	# makeMovie_GWcatalogSizeJustConfirmed(fps=1.2, duration=200, name_images='knownDetectionsGWcatalogSize_', image_folder=image_folder)
	
	image_folder = '/Users/floorbroekgaarden/Projects/GitHub/GW_visualization_detection_number/GWcatalogMovieFigures/'
	makeMovie_GWcatalogSize(fps=45, duration=40, name_images='knownDetectionsGWcatalogSizeMovie_', image_folder=image_folder) # make movie different O1-O3 catalogs 
	# makes movie lineaer y-scale and without uncertainties:
	makeMovie_GWcatalogSize(fps=20, duration=60, name_images='GWcatalogSize_withUpdatedCE_', number_images=200, image_folder=image_folder)
	# makes movie lineaer y-scale and with uncertainties:
	makeMovie_GWcatalogSize(fps=20, duration=60, name_images='GWcatalogSize_UncertaintyLin_', number_images=200, image_folder=image_folder)
	# make movies log y-scale and with uncertainties:
	makeMovie_GWcatalogSize(fps=20, duration=60, name_images='GWcatalogSize_withUncertainty_', number_images=200, image_folder=image_folder)
	# make movie for O4
	makeMovie_GWcatalogSizeO4(image_folder=image_folder)




