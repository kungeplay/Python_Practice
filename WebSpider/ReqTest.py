#!/usr/bin/python
#coding=utf-8
import urllib
import urllib2
import re

str=u"""<p> 妩媚姐姐听到佟晓雅的话吃惊地张大了嘴巴，脸上显出难以置信的表情，
看向一旁的傲娇姐姐。相比之下傲娇姐姐要冷静许多，依然用不屑的眼神俯视我，对我上下打量，
让我感觉很不自在。<br /> 过了挺大一会，佟晓雅总算出了厕所，慵懒地要做引荐，我这才知道傲娇姐姐的名字是李冰，杨思瑶自然是妩媚姐姐的名字，倒真是人如其名。 </p>"""
res=re.sub(r'<p>','  ',str)
print res 
