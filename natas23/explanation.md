# php type juggling 
	PHP does not require (or support) explicit type definition in variable declaration; a variable's type is determined by the context in which the variable is used. That is to say, if a string value is assigned to variable $var, $var becomes a string. If an integer value is then assigned to $var, it becomes an integer.(from php manual page)
	so php will convert the variable type as necessary
binary safe functions: process strings as stream of bytes.. which simply means that the function is case sensitive


<form name="input" method="get">
    <input type="text" name="passwd" size=20>
    <input type="submit" value="Login">
</form>

<?php
    if(array_key_exists("passwd",$_REQUEST)){
        if(strstr($_REQUEST["passwd"],"iloveyou") && ($_REQUEST["passwd"] > 10 )){
            echo "<br>The credentials for the next level are:<br>";
            echo "<pre>Username: natas24 Password: <censored></pre>";
        }
        else{
            echo "<br>Wrong!<br>";
        }
    }
    // morla / 10111
?>  

The strstr() function compares the 2 strings and returns the part of the first string which contains the 2nd string, False if the 1st string doenot contain 2nd string
if(strstr($_REQUEST["passwd"],"iloveyou") && ($_REQUEST["passwd"] > 10 )){
here we can see we are first comparing string and then a integer,
php converts variable type as necessary
so if we submit "12 iloveyoubaby", 
strtsr() will return "iloveyoubaby" and teh 2nd part will also be true as pho will convert the string "12 iloveyoubab" to integer 12 which is greater than 10
and hence we get the password.

