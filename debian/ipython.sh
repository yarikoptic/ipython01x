#! /bin/sh

# determine desired Python version from filename
VERSION="${0##*ipython}"

if [ ! -f /usr/bin/python$VERSION ]
then
	echo "Please install the python$VERSION package." >&2
	exit 1
else
	exec python$VERSION -c "import sys; sys.argv[0] = 'ipython$VERSION'; import IPython; IPython.Shell.start().mainloop()" $@
fi
