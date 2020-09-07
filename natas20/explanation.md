# natas20 - all about php sessions and custom sessions handlers
	first php checks for any previous sessions, if found uses that session or creates a new session id and sends that session id as a cookie "PHPSESSID" to
	the client. It created a temporary directory on the server to created the session variables for that user session. In the custon session handler functios, the functions read() and write() are vulnurable.
	first I thought the sequence of execution was; write() and read() but it is quite the opposite because first php checks for any previous sessions and reads from that session file.
	so the vulnurability is in both of those functions:
		in the read function:
		function myread($sid) { 
		    debug("MYREAD $sid"); 
		    if(strspn($sid, "1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM-") != strlen($sid)) { // checks if the sessid is valid
		    debug("Invalid SID"); 
		        return "";
		    }
		    $filename = session_save_path() . "/" . "mysess_" . $sid;
		    if(!file_exists($filename)) {                                // checks if file existe ie if there was any previous sessions
		        debug("Session file doesn't exist");
		        return "";
		    }
		    debug("Reading from ". $filename);         // reads from the file; remember-first read() is executed not write so the file can be empty at first
		    $data = file_get_contents($filename);
		    $_SESSION = array();                      // gets file contents
		    foreach(explode("\n", $data) as $line) {  // splits the contents at every "\n" newline; returns a array
		        debug("Read [$line]");
		    $parts = explode(" ", $line, 2);          //splits at every space char " " 
		    if($parts[0] != "") $_SESSION[$parts[0]] = $parts[1];   //saves it in session varibale; we can inject "somename \nadmin 1"
		    }
		    return session_encode();
		}
		in the write function:
		if(strspn($sid, "1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM-") != strlen($sid)) { // checks if sessid is valid
		    debug("Invalid SID"); 
		        return;
		    }
		    $filename = session_save_path() . "/" . "mysess_" . $sid;   // writes to this file
		    $data = "";
		    debug("Saving in ". $filename);
		    ksort($_SESSION);
		    foreach($_SESSION as $key => $value) {
		        debug("$key => $value");
		        $data .= "$key $value\n";
		    }
		    file_put_contents($filename, $data)


if we inject "somename \nadmin 1"

it will split at \n
and the session varibale $_session['admin'] = 1 is saved
but since write is executed after read, to be more precise; after the output stream is closed we have to make another get request to set ourself as admin