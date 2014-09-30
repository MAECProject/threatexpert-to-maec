#****************************************************#
#                                                    #
#      ThreatExpert -> MAEC XML Converter Script     #
#                                                    #
#      Copyright (c) 2014 - The MITRE Corporation    #
#                                                    #
#****************************************************#

#BY USING THE THREATEXPERT TO MAEC SCRIPT, YOU SIGNIFY YOUR ACCEPTANCE OF THE TERMS AND 
#CONDITIONS OF USE.  IF YOU DO NOT AGREE TO THESE TERMS, DO NOT USE THE THREATEXPERT
#TO MAEC SCRIPT.

#For more information, please refer to the LICENSE.txt file.

#ThreatExpert Converter Script
#Copyright 2014, MITRE Corp
#v0.95 - BETA
#Updated 02/24/2014 for MAEC v4.1 and CybOX v2.1

from __init__ import generate_package_from_report_filepath
import sys
import os
import traceback

#Create a MAEC output file from a ThreatExpert input file
def create_maec(inputfile, outpath, verbose_error_mode):
    stat_actions = 0

    if os.path.isfile(inputfile):
        
        try:
            package = generate_package_from_report_filepath(inputfile)
  
            #Finally, Export the results
            package.to_xml_file(outpath, {"https://github.com/MAECProject/threatexpert-to-maec":"ThreatExpertToMAEC"})
            
            print "Wrote to " + outpath
            
        except Exception, err:
           print('\nError: %s\n' % str(err))
           if verbose_error_mode:
                traceback.print_exc()
    else:
        print('\nError: Input file not found or inaccessible.')
        return

#Print the usage text    
def usage():
    print USAGE_TEXT
    sys.exit(1)
    
USAGE_TEXT = """
ThreatExpert XML Output --> MAEC XML Converter Utility
v0.95 BETA // Supports MAEC v4.1 and CybOX v2.1

Usage: python threatexpert_to_maec.py <special arguments> -i <input threatexpert xml output> -o <output maec xml file> 
       OR python threatexpert_to_maec.py <special arguments> -d <directory>

Special arguments are as follows (all are optional):
-v : verbose error mode (prints tracebacks of any errors during execution).

"""    
def main():
    verbose_error_mode = 0
    infilename = ''
    outfilename = ''
    directoryname = ''
    
    #Get the command-line arguments
    args = sys.argv[1:]
    
    if len(args) < 2:
        usage()
        sys.exit(1)
        
    for i in range(0,len(args)):
        if args[i] == '-v':
            verbose_error_mode = 1
        elif args[i] == '-i':
            infilename = args[i+1]
        elif args[i] == '-o':
            outfilename = args[i+1]
        elif args[i] == '-d':
            directoryname = args[i+1]

    if directoryname != '':
        for filename in os.listdir(directoryname):
            if '.xml' not in filename:
                pass
            else:
                outfilename = filename.rstrip('.xml') + '_maec.xml'
                create_maec(os.path.join(directoryname, filename), outfilename, verbose_error_mode)
    #Basic input file checking
    elif infilename != '' and outfilename != '':
        create_maec(infilename, outfilename, verbose_error_mode)
        
if __name__ == "__main__":
    main()    
