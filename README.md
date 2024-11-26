# EGM96Swift

Port of EGM96 Repo to Swift

Original EGM96 repo Java code can be found [here](https://github.com/matthiaszimmermann/EGM96).

We ported to Swift with the help of ChatGPT-4 and then fixed and
enhanced what ChatGPT-4 broke.  Plus, we switched from gzip to zlib
since iOS has built in support for zlib compression and decompression.

Refer to original EGM96 repo for disclaimers and more information.  We
also tested and audited the offsets for various cities on each
continent and compared those offsets against an online GeoID
calculator located
[here.](https://geographiclib.sourceforge.io/cgi-bin/GeoidEval?input=33.7490+-84.3880&option=Reset)

The uncompressed Geoid data is in the file EGM96complete.
Zlib-compressed Geoid data is in the file EGM96complete.bin

WGS84 models earth as a squished sphere; GPS uses this model for
altitude or vertical datum.  EGM96 earth gravitional model accounts
for variations and irregularties in earth's gravity.  Mean sea level
(MSL) is artificial construct and is used interchangeably with EGM96.

alt(WGS84) - offset = alt(MSL)
