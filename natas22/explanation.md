# disallow redirects
	<?
	session_start();

	if(array_key_exists("revelio", $_GET)) {
	    // only admins can reveal the password
	    if(!($_SESSION and array_key_exists("admin", $_SESSION) and $_SESSION["admin"] == 1)) {// if we are not admin, we ll be redirected to the root page again
	    header("Location: /");
	    }
	}
?>

<?
    if(array_key_exists("revelio", $_GET)) {
    print "You are an admin. The credentials for the next level are:<br>";
    print "<pre>Username: natas23\n";
    print "Password: <censored></pre>";
    }
?>

<div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
</div>
</body>
</html>

we can disallow the redirect:
	response = session.get(url, params=payload, auth=(username, password), allow_redirects = False) # as the parameter name says, it ll disallow any redirects.
	