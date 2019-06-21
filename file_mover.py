import shutil
import os
import glob

train_paths = glob.glob('C:/Users/dotd/workspace/facenet-master/DB/Train/*.jpg')# The train directory that you want to separate.

print("start")
# print(train_paths)
for file_name in train_paths:
	# file_name example : C:/Users/dotd/workspace/facenet-master/DB/Train/train_000150-1.jpg,
	#					  C:/Users/dotd/workspace/facenet-master/DB/Train/train_000150-2.jpg,
	#					  C:/Users/dotd/workspace/facenet-master/DB/Train/train_000150-3.jpg,
	#					  C:/Users/dotd/workspace/facenet-master/DB/Train/train_000150-4.jpg,
	#					  C:/Users/dotd/workspace/facenet-master/DB/Train/train_000151-1.jpg,
	#					  C:/Users/dotd/workspace/facenet-master/DB/Train/train_000152-2.jpg

	dirctory_name = file_name.split('/')[-1].split('_')[1].split('-')[0][3:]

	# print("file_name: {}".format(file_name))
	# print("dirctory_name: {}".format(dirctory_name))
	# print("os.path.basename(file_name):{}".format(os.path.basename(file_name)))
	# print("new_path: {}".format(os.path.dirname(file_name)+'/'+dirctory_name+'/'+os.path.basename(file_name)))

	try:# If there is no directory to store, create it.
		if not (os.path.isdir(os.path.dirname(file_name)+'/'+dirctory_name)):
			os.makedirs(os.path.join(os.path.dirname(file_name)+'/'+dirctory_name))
			print("make directory")
	except OSError as e:
		if e.errno != errno.EEXIST:
			print("Failed to create directory!")
			raise

	shutil.move(file_name ,os.path.dirname(file_name)+'/'+dirctory_name+'/'+os.path.basename(file_name))# move file into directory

print("finish")

