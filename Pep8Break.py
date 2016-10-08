#!/opt/local/bin/python3.3
import re;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;
def twist ( t ,r  =  '' ,i  =  0 ,u  =  True ,j  =  1 ,k  =  1 , l  =  1 ,  ) :#
 d={';' :':' ,']' :'[' ,'[' :']' ,'@' :'#' ,'!' :'?' ,'' :'' ,'#' :'@' ,',' :'.'
,'.' :',' ,')' :'(' ,'(' :')' ,'5' :'4'  ,'4' :'5' ,'7' :'2' ,'6' :'3' ,'1' :'8'
,'0' :'9' ,'3' :'6' ,'2' :'7' ,'}' :'{' ,'<' :'>' ,'?' :'!' ,'>' :'<' ,'9' :'0'#
,'8' :'1' ,'{' :'}' ,':' :';'};z=[w[: :-1] for w in ''.join( x.isupper () and x.
lower() or x.upper() if x.isalpha() else ' ' for x in t).split()][: :-1];z;z;z;#
 while i<len(t) and u==u and u==u and u==u and u==u and u==u and u==u and u==u:#
  if t[i].isalpha():w=z.pop();r+=w;i+=len(w);t;t;t;t;t;t;t;t;t;t;t;t;t;t;t;t;t;#
  else:r+=d.get(t[i],t[i]);i+=1;t;t;t;t;t;t;t;t;t;t;t;t;t;t;t;t;t;t;t;t;t;t;t;t#
 return re.sub(' +' ,' ' ,r );x;x;x;x;x;x;x;x;x;x;x;x;x;x;x;x;x;x;x;x;x;x;x;x;x#
1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;

if __name__ == '__main__':
    assert twist("Hello World!") == "OLLEh DLROw?"
    assert twist("I'm 1st") == "i'M 8TS"
    assert twist("How are you? 905th.") == "WOh ERA UOY! 094HT,"
    assert twist("The code - ([{<;#>}])") == "EHt EDOC - )]}>:@<{[("
    assert twist("EMAIL        a@b.ru") == "liame A#B,UR"
    assert twist(";-) 0_0 @__@") == ":-( 9_9 #__#"
    assert twist("          ") == " "
