import sys
import unittest
from functools import cmp_to_key

def mysplit(line,id2name):
    '''
    helper function for split line correctly if the normal line.split(',') fails.
    eg:   #1992728315,ZARUBINSKY,BELLA,"PANCRELIPASE 5,000",1227.63
          #1992728315,ZARUBINSKY,,"PANCRELIPASE 5,000",1227.63
    :param line, dict id2name:
    :return: list [id,prescriber_last_name,prescriber_first_name,drug_name,drug_cost]
    '''
    r=[]
    s=[]
    InQuoteFlag=False
    pre=None
    for e in line:
        if not InQuoteFlag and e==",":
            if pre=='"': pre=e;continue
            r.append(''.join(s))
            s=[]
            pre=e
            continue
        if not InQuoteFlag and e=='"':
            InQuoteFlag=True
            pre=e
            continue
        if InQuoteFlag and e=='"':
            r.append(''.join(s))
            s = []
            InQuoteFlag=False
            pre=e
            continue
        if InQuoteFlag and e==',':
            s.append(e)
            pre=e
            continue
        if e!=',':
            s.append(e)
            pre=e
        elif e==',' and pre==',':
            s.append('')
            pre=e
    if not s:
        #drug_price is missing
        s.append('0')
    r.append(''.join(s))

    if s[1] == '' or s[2] == '':
        # name info missing, try find name by ID
        id = s[0]
        if id in id2name:
            s[1] = id2name[id][0]
            s[2] = id2name[id][1]
        else:
            raise Exception('name is missing and can not match name by ID')
    return r



def comparator(record1,record2):
    '''
    comparator for record1 and record2 structured as [drug_name,num_prescriber,total_cost]
    total_cost in descending order and if there is a tie, drug_name in ascending order.
    '''
    if record1[2]<record2[2]:
        return 1
    elif record1[2]==record2[2]:
        if record1[0]<record2[0]:
            return -1
        else:
            return 1
    else:
        return -1

def mapfun4output(record):
    '''
    map record in list to string
    :param record in list format
    :return: string of the record as:
            "drug_name,num_prescriber,total_cost"
    '''

    return record[0]+","+str(record[1])+','+str(int(record[2]))+'\n'

def main():
    '''
    main function for pharmacy_counting
    '''
    if len(sys.argv)==3:
        input=sys.argv[1]
        output=sys.argv[2]
    else:
        input="../input/itcont.txt"
        output="../output/top_cost_drug.txt"

    #dictionary to store drug_name,{prescriber_names},total_cost
    #the structure of dic:
    #dic[drug_name]=[set(name1,name2,name...)),drug_total_cost]
    #Note: the large dataset containing over 24 million records, still datasize< memory
    #      therefore, in memory processing input file.
    dic=dict()

    #since userID and name is a one to one mapping,save the ID to Name mapping when name is missing.
    id2name=dict()
    #read input file data and construct dic for postprocessing
    #Since prescriber is considered the same person if two lines share the same prescriber first and last names
    #name=prescriber_last_name+'_'+prescriber_first_name is used as unique key in set.
    with open(input,'r') as f:
        f.readline() #skip header
        line=f.readline().strip()
        while line:
            try:
                id, prescriber_last_name, prescriber_first_name, drug_name, drug_cost =line.split(',')
            except ValueError:
                id, prescriber_last_name, prescriber_first_name, drug_name, drug_cost=mysplit(line,id2name)

            if id not in id2name:
                id2name[id] = (prescriber_last_name, prescriber_first_name)
            name=prescriber_last_name+'_'+prescriber_first_name

            if drug_name not in dic:
                dic[drug_name]=[set(),0]
            dic[drug_name][0].add(name)
            dic[drug_name][1]+=float(drug_cost)
            line=f.readline().strip()


    #map dict to list of the following format:
    #              [dic.key, len(set(names)),total_cost] i.e. [drug_name,num_prescriber,total_cost]
    result_list=list(map(lambda x: [x[0],len(x[1][0]),x[1][1]], dic.items()))
    #release memory
    del dic
    del id2name
    #sort the result_list based on customized comparator
    result_list.sort(key=cmp_to_key(comparator))


    with open(output,'w') as f:
        f.write("drug_name,num_prescriber,total_cost\n")
        f.write("".join(list(map(mapfun4output,result_list))))

#-----------------------------------------unit tests--------------------------------------------------------------------
class Testing(unittest.TestCase):
    def test_mysplit_1(self):
        #test mysplit function ; when line.split(',') fails. ',' in drug_name
        line='1992728315,ZARUBINSKY,BELLA,"PANCRELIPASE 5,000",1227.63'
        expected=['1992728315','ZARUBINSKY','BELLA','PANCRELIPASE 5,000','1227.63']
        actual=mysplit(line)
        self.assertEqual(expected,actual)
    def test_mysplit_2(self):
        #test mysplit function ; when first name is missing
        line = '1992728315,ZARUBINSKY,,"PANCRELIPASE 5,000",1227.63'
        expected = ['1992728315', 'ZARUBINSKY', '', 'PANCRELIPASE 5,000', '1227.63']
        actual = mysplit(line)
        self.assertEqual(expected, actual)
    def test_mysplit_3(self):
        # test mysplit function ; when Last name is missing
        line = '1992728315,,BELLA,"PANCRELIPASE 5,000",1227.63'
        expected = ['1992728315', '', 'BELLA', 'PANCRELIPASE 5,000', '1227.63']
        actual = mysplit(line)
        self.assertEqual(expected, actual)
    def test_mysplit_4(self):
        #test mysplit function: when price is missing
        line = '1992728315,ZARUBINSKY,,PANCRELIPASE,'
        expected = ['1992728315', 'ZARUBINSKY', '', 'PANCRELIPASE', '0']
        actual = mysplit(line)
        self.assertEqual(expected, actual)
    def test_mysplit_5(self):
        #test mysplit function: when ID is missing
        line = ',ZARUBINSKY,BELLA,"PANCRELIPASE 5,000",1227.63'
        expected = ['', 'ZARUBINSKY', 'BELLA', 'PANCRELIPASE 5,000', '1227.63']
        actual = mysplit(line)
        self.assertEqual(expected, actual)
    def test_mysplit_6(self):
        #test mysplit function: when everything is missing
        line = ',,,,'
        expected = ['', '', '', '', '0']
        actual = mysplit(line)
        self.assertEqual(expected, actual)

    def test_comparator_1(self):
        #test comparator function, compare total_cost
        #record in format [drug_name, num_prescriber, total_cost]
        record1=['name1',2,100]
        record2=['name2',1,200]
        expected =1
        actual=comparator(record1,record2)
        self.assertEqual(expected, actual)
    def test_comparator_2(self):
        #test comparator function, when total_cost is the same, compare drug name
        #record in format [drug_name, num_prescriber, total_cost]
        record1=['name1',2,100]
        record2=['name2',1,100]
        expected =-1
        actual=comparator(record1,record2)
        self.assertEqual(expected, actual)


if __name__=='__main__':
    main()










