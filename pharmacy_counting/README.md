# approach
The datafile size is in the computer's memory range.
Therefore,the data processing can all be done in memory.

1)A dictionary is created to store drug_name,{prescriber_names} and total_cost
the structure of dic as follow:

dic[drug_name]=[set([name1,name2,name...]),drug_total_cost]

Above is the original design, since in the description, UNIQUE is defined by FIRSTNAME+LASTNAME.
It could be the case that A Unique person with FIRSTNAME+LASTNAME has multiple IDs. They are counted as different person.
However, I can not pass the testcase for large dataset.Then I change my design as follow:

dic[drug_name]=[set([id1,id2,id3...]),drug_total_cost]

2)Then the dic is convert to a result_list with entry fommat:

[dic.key, len(set([id1,id2,id3...]),total_cost]

3)Then sort the result_list by customized comparater:

sort totalcost in descending order first, if there is a tie. 
Sort drug_name  in ascending order.(Here I also got a misunderstanding, what's the ascending order? I modify my customized comparator so that I can pass the testcase for big dataset )

Note: when the drug_total_cost smaller than 1.0, the drug_total_cost is round to 0
      if multiple such drug_name exits, sort drug_name in ascending order.

# instructions

python3 is used.


For normal run:

 execute run.sh  or   python3 pharmacy_counting.py inputfile outputfile
  

For unittest please run:

 python3 -m unittest pharmacy_counting.Testing


# SQL   (identified by ID  or  First+LastName)
SELECT drug_name, COUNT(DISTINCT id) as num_prescriber , FLOOR(SUM(drug_cost)) as total_cost FROM data GROUP BY drug_name ORDER BY total_cost DESC,drug_name ASC;

or

SELECT drug_name, COUNT(DISTINCT CONCAT(prescriber_last_name,',', prescriber_first_name)) as num_prescriber , FLOOR(SUM(drug_cost)) as total_cost FROM data GROUP BY drug_name ORDER BY total_cost DESC,drug_name ASC;



