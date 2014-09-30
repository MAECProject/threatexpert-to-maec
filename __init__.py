import threatexpert_parser as teparser
from maec.package.package import Package

def generate_package_from_parser(input_parser):
    #Parse the file to get the actions and processes
    input_parser.parse_document()

    #Create the MAEC Package
    package = Package()
    
    #Add the analysis
    for subject in input_parser.maec_subjects:
        package.add_malware_subject(subject)
        
    return package
    
def generate_package_from_report_filepath(input_path):
    parser = teparser.parser()
    open_file = parser.open_file(input_path)
    
    if not open_file:
        print('\nError: Error in parsing input file. Please check to ensure that it is valid XML and conforms to the ThreatExpert output schema.')
        return
    
    return generate_package_from_parser(parser)

def generate_package_from_binary_filepath(input_path):
    import hashlib
    # create MD5
    blocksize = 65536
    fd = open(input_path, "rb")
    hasher = hashlib.md5()
    buf = fd.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = fd.read(blocksize)
    
    return generate_package_from_md5(hasher.hexdigest())

def generate_package_from_md5(input_md5):
    import requests
    parameters = { "md5": input_md5, "xml": 1 }
    response = requests.get("http://www.virustotal.com/vtapi/v2/file/report", params=parameters)
    
    return generate_package_from_report_string(response.text)

def generate_package_from_report_string(input_string):
    parser = teparser.parser()
    parser.use_input_string(input_string)
    
    return generate_package_from_parser(parser)

