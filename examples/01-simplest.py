TARGET = tsf('cage.aiff', thresh=-26, offsetRise=1.5)

CORPUS = [
csf('lachenmann.aiff'),
] # CORPUS documented in 04-corpus.py

SEARCH = [
spass('ratio_limit', d('effDur-seg'), minratio=0.7, maxratio=1.1),
spass('closest', d('mfccs'))
] # SEARCH documented in 02-searching.py

SUPERIMPOSE = si(maxSegment=8) # SUPERIMPOSE documented in 03-superimposition.py
