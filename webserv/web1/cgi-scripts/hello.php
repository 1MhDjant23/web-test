#!/usr/bin/env php
<?php
// CGI must output HTTP headers first
header("Content-Type: text/plain");
header("Cache-Control: no-cache");

// Optional: custom status
// header("HTTP/1.1 200 OK");

// Body of the response
echo "Hello from PHP CGI!\n";
echo "Current time: " . date('Y-m-d H:i:s') . "\n";

// You can also read query parameters (from environment variable QUERY_STRING)
if (isset($_SERVER['QUERY_STRING']) && !empty($_SERVER['QUERY_STRING'])) {
    echo "Query: " . $_SERVER['QUERY_STRING'] . "\n";
}
?>
