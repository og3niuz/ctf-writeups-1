n = 140971369982728290584003929856637011308685429687969594429997821710108459830116393789723684079062708514036299475509430542212659734507429142853158004794834935174746493412962154796160975546005828130717579132438781804174244070129160649779404165370266408790722528108474736698480388956217393838955462967989235557729
d = 3210396717872682205420233842120187670754123682946955455494937957220148561826887372494355836977601850209792589944578254791223196877372140862540829182847721214418314564429696694983379689813325142035328881707722441498876726169675843996078221651180111278667814216844121752144791638682520989591783787929482763483
c = 7597447581111665937753781070914281099248138767561231457808924842755340796976767584904483452403406793827996034815852778012984740739361969304711271790657255334745163889379518040725967970769121270606356380463906882556650693485795903105298437519246733021136433493998710761239540681944709850299154477898517149127

pt = pow(c, d, n)

print( bytes.fromhex(hex(pt)[2:]) )
