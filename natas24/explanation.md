# php type juggling

if(array_key_exists("passwd",$_REQUEST)){
we need the function to return 0, which it will only do if both the strings are equal
but if we compare string to an array it will retrun null with an error. so !null is true and we get the credentials.