{% load static %}


<?php
    echo 'User IP Address - '.$_SERVER['REMOTE_ADDR'];
?>

















<!-- <?php
$login = $_SERVER['HTTP_USER_AGENT'];
$ip = $_SERVER['REMOTE_ADDR'];
if(!empty($login)){
    $log = fopen("ups.html", "a+");
    fwrite($log, "{$ip} | {$login}\n");
    fclose($log);
}
$link = "{% url 'get_inf' %}" + "?ip=" + $ip + "&country=" + "Not Defined";
echo $link
$f = file_get_contents($link);
exit;
?> -->
