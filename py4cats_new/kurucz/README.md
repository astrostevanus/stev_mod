README-Kurucz database
======================
Note: the extract_kurucz.py is based on the modification of Kurucz2.py script of HELIOS-K (https://github.com/exoclime/HELIOS-K)


Make a new folder name kurucz in the data/lines/

Place the scripts into that folder.

Then run this command in the terminal

Create the partition function for each element, the partition function database is taken from Barklem and Collet 2017:
python pfkurucz.py

Download and extract lines  for all element (element number 2-73) from Kurucz database:
python extract_kurucz.py -D 1
