def parse_source(path):
    parsedLines = list()
    with open(path, 'r') as f:
        sourceLines = f.readlines()
        for line in sourceLines: #TODO: Don't extend, but allocate the wires to different containers
            parsedLines.extend(line.split(','))
        for listLines in sourceLines:
            print("Parsing of source finished...")
    return parsedLines