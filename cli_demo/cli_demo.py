import os
import stat
import argparse
import sys

def is_file(pth):
	st = os.stat(pth)
	return stat.S_ISREG(st.st_mode)

def is_dir(pth):
	st = os.stat(pth)
	return stat.S_ISDIR(st.st_mode)

def sum_directory(pth):
	local_files = []
	local_directories = []
	local_total_size = 0
	local_file_count = 0
	local_directory_count = 0

	for f in os.listdir(pth):
		if os.path.isfile(f): 
			local_files.append(f)
			local_file_count += 1
		elif os.path.isdir(f): 
			local_directories.append(f)
			local_directory_count += 1

	for f in local_files:
		file_size = os.stat(f).st_size
		local_total_size += file_size

	return (local_total_size, local_file_count, local_directory_count)


def main():
	parser = argparse.ArgumentParser()

	parser.add_argument('--summary', action='store_true', default=False, help='show summary')
	parser.add_argument('--countdir', action='store_true', default=False, help='show directory count')

	args = parser.parse_args(sys.argv[1:])

	(total_size, file_count, directory_count) = sum_directory('.')

	if args.countdir:
		if not args.summary:
			print 'Must specify --summary with --countdir'
		else:
			print 'Found total of %d bytes, %d files, %d directories' % (total_size, file_count, directory_count)
	elif args.summary and not args.countdir:
		print 'Found total of %d bytes, %d files' % (total_size, file_count)

if __name__ == '__main__':
	main()