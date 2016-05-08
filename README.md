## Thumbnailer
Thumbnailer is a command line app that lets you create thumbnail copies of your original image.

## Example

```python

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


```

## Motivation

No real motivation as such, apart from wanting to experiment with the package pillow or PIL


## Installation

For the script to run, you will need to install pillow. You can install it using the command pip install pillow.
1. place the script thumbnail.py in the same folder as the images you wont to covert into thumbnails.
2. The scrpit will create a folder called created_thumbnails where the converted images are placed.

## License 
The repo is licensed under MIT.






