pass: 8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw
<html>
<body>
/*
CREATE TABLE `users` (
  `username` varchar(64) DEFAULT NULL,
  `password` varchar(64) DEFAULT NULL
);
*/
'''
	here table name and the column name iside it is given
	we can use it
'''


<?php
if(array_key_exists("username", $_REQUEST)) {
    $link = mysql_connect('localhost', 'natas17', '<censored>');
    mysql_select_db('natas17', $link);
    
    $query = "SELECT * from users where username=\"".$_REQUEST["username"]."\"";
    if(array_key_exists("debug", $_GET)) {
        echo "Executing query: $query<br>";
    }

    $res = mysql_query($query, $link);
    if($res) {
    if(mysql_num_rows($res) > 0) {
        //echo "This user exists.<br>";
    } else {
        //echo "This user doesn't exist.<br>";
    }
    } else {
        //echo "Error in query.<br>";
    }

    mysql_close($link);
} else {
?>

<form action="index.php" method="POST">
Username: <input name="username"><br>
<input type="submit" value="Check existence" />
</form>
<? } ?>
<div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
</div>
</body>
</html>

'''
	notice post request is made
	and in the php code, all response texts are commented out
	we have to perform a time based sql injection
	we can use sleep(seconds) like: natas18" and sleep(5) #
	so if the user natas18 exists, the sql server will sleep for 5 seconds before sending the response
	we can use this injection method to find out the password
'''