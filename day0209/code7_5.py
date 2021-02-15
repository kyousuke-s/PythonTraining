#特定の変数や関数だけを取り込む
from math import pi #変数
from math import floor #関数
#from math import pi,floor でも良い

print('円周率は{}です'.format(pi))
print('小数点以下を切り捨てれば{}です'.format(floor(pi)))
