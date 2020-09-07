# playing with cookies: cross-site session hijaking
	we get this note:
	Note: this website is colocated with http://natas21-experimenter.natas.labs.overthewire.org
	check the source code in both webpages
	the main vulnurable code is:
	This code is in the second website
	if(array_key_exists("submit", $_REQUEST)) {
    foreach($_REQUEST as $key => $val) {
    $_SESSION[$key] = $val;
    }
	}
	so whatever we submit through the form is stored in the session array
	so we can submit "admin": "1"

	the main print_credentials() page is in the orignal webiste

	websites are colocated: never heard of it
	googled it: co-located
	sharing same location
	so session cookies might also be stored on the sa,e computer I guess
	post "admin": "1"
	from the second website and get the "PHPSESSID" and perform a get request to the orignal website submitting the same session cookie and wohhal you are the admin
	bacause we at first set the array or the session variable $_session['array'] = 1
	and used the same session cookie 2nd time which will access the same file for the seeion on the server.