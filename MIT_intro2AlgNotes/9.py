# hash with chaining
# m slots
# want m=O(n)
# table doubling  to grow table , amortized runtime of insertion O(1)
#              m=n/4 then shrim to m/2  of deletion       O(1)
# same for list.  list.append list.pot take O(1)


#string matching
   # AAAAAAAAAAAAAAAAAAAAA
   # aaa
   #  aaa
   #   aaa
   #     .......
   #                   aaa
   #
   #compare hash(aaa)  has(i,i+len(aaa)) for i in range(0, len(AAAA...)-len(aaa))

   # Rolling HASH ADT       Karp-Rabin alg     O(n)















