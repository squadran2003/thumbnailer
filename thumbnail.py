from PIL import Image
import os


dir_path=os.path.join(os.getcwd(),'created_thumbnails')
if os.path.exists(dir_path)==False: # if a folder called created_thumbnails is not there create it
	os.mkdir('created_thumbnails')
	
# Introduction to the app with help text
def help_text():
	print("""
	Welcome to THUMBNAILER. 
	The command line app that lets you create thumbnails of your images. 
	You can create a thumbnail of one image or ccreate thumbnails of 
	all images in a directory
	""")

# menu

def menu():
	input_text = """
	To create a thumbnail of a single image its [A].
	To create thumbnails or images in an entire directory its [B].
	And its [Q] to quite the app >> 
	"""
	return  raw_input(input_text).lower()
	
#clear the prompt for all enviroments
def clear_prompt():
	os.system('cls' if os.name == 'nt' else 'clear')
		
# create one image at a time
def created_thumbnail_image(file,width,height):
	try:
		img = Image.open(file)
		img.thumbnail((width,height))
		img.save(os.path.join(dir_path,file))
		clear_prompt()
		print('Thumbnail for image {} was created in the directory created_thumbnails !!'.format(file))
	except Exception as e:
		print("Following erro {} occured".format(str(e)))
		clear_prompt()
		

def dimentions():
	width= raw_input("Enter Thumbnail width >> ")
	height= raw_input("Enter Thumbnail height >> ")
	if width =="" or height=="":
		print("You must supply values for the width and height")
		return ValueError
	else:
		try:
			width = int(width)
			height = int(height)
		except ValueError:
			return ValueError
		return width,height
	
#create multiple images at a time
def create_multiple_thumbnail_images(width,height):
	# remove all files from the created_thumbnails folder
	filenames = next(os.walk(dir_path))[2] # only effects current directory
	if filenames !=[]: # if there are files in the created_thumbnails folder
		for i in filenames:
			os.remove(os.path.join(dir_path,i)) # empty the folder
	else:
		for i in os.listdir(os.getcwd()): # loop through and convert each image and place in created_thumbnails folder 
			if i.endswith(".jpg"):
				try:
					img = Image.open(i)
					img.thumbnail((width,height))
					img.save(os.path.join(dir_path,i))
					print('Thumbnail for image {} was created in the directory created_thumbnails !!'.format(i))
				except Exception as e:
					print("Following error {} occured".format(str(e)))
				
				
		
		
help_text()	

while True:
	user_input = menu()
	if user_input=='a':
		infile = raw_input("Image name ??  ")
		print("Enter width and height of your thumbnail image !")
		width,height = dimentions()
		created_thumbnail_image(infile,width,height)
	elif user_input=='b':
		width,height = dimentions()
		create_multiple_thumbnail_images(width,height)
	elif user_input=='q':
		break
	else:
		print("Did not recognisze your input !!!!".upper())
		continue
			
