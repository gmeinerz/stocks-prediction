#!/usr/bin/env python

import sys
import getopt

def readStocks(file_name):

    with open(file_name, mode='r') as sample:
        
        data = list()
        
        next(sample)
        
        for line in sample.readlines():

            data.append(','.join(map(str.strip, [line[0:2], line[2:6]+'-'+line[6:8]+'-'+line[8:10], line[10:12], 
                                                 line[12:24], line[24:27], line[27:39], line[39:49], line[49:52], 
                                                 line[52:56], line[56:67]+'.'+ line[67:69], line[69:80]+'.'+line[80:82], 
                                                 line[82:93]+'.'+line[93:95], line[95:106]+'.'+line[106:108], 
                                                 line[108:119]+'.'+line[119:121], line[121:132]+'.'+line[132:134], 
                                                 line[134:145]+'.'+line[145:147], line[147:152], line[152:170], 
                                                 line[170:186]+'.'+line[186:188], line[188:199]+'.'+line[199:201], 
                                                 line[201:202], line[202:206]+'-'+line[206:208]+'-'+line[208:210], 
                                                 line[210:217], line[217:224]+'.'+line[224:230], line[230:242], line[242:245]])))
            
        data.pop()
    
    return data

def writeCsv(file_name, data):

    with open(file_name, mode='w') as sample:
        
        sample.writelines(','.join(['TIPREG', 'DATA DO PREGAO', 'CODBDI', 'CODNEG', 'TPMERC', 'NOMRES', 
                                    'ESPECI', 'PRAZOT', 'MODREF', 'PREABE', 'PREMAX', 'PREMIN', 'PREMED', 
                                    'PREULT', 'PREOFC', 'PREOFV', 'TOTNEG', 'QUATOT', 'VOLTOT', 'PREEXE', 
                                    'INDOPC', 'DATVEN', 'FATCOT', 'PTOEXE', 'CODISI', 'DISMES\n']))
        
        for line in data:
            sample.writelines(line + '\n')


if __name__ == '__main__':

    try:

        opts, args = getopt.getopt(sys.argv[1:], 'i:o:h', ['input_file_path=', 'output_file_path=', 'help'])

    except getopt.GetoptError as err:

        print(err)
        sys.exit(1)

    data = list()

    for opt, arg in opts:

        if opt in ('-h', '--help'):
            print('txt2csv.py -i --input_file_path -o --output_file_path [-h | --help]')
            sys.exit(2)

        elif opt in ('-i', '--input_file_path'):
            data = readStocks(arg)

        elif opt in ('-o', '--output_file_path'):
            writeCsv(arg, data)