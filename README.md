# baseimage-python3.9

An impulse chamber baseimage for python-3.9. Builds a container that contains a minimal OS, the python runtime, and the skyhook wrapper that handles requests and invokes client functions. 

This currently uses SimpleHTTPServer, which can only handle one request at a time. This is acceptable for now, as scaling can be acheived by adding more chambers horizontally.

## Building the baseimage

run `./exportrootfs.sh <path-to-image>`

## Related projects:

Sample guest function: https://github.com/izaaklauer/guestimage-python3.9

Impulse: https://github.com/izaaklauer/impulse
