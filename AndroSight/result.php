<?php

session_start();

header('Content-Type: text/html; charset=utf-8');

// $output1 = $_SESSION['output1'];
// $output2 = $_SESSION['output2'];
$output4 = isset($_SESSION['output1']) ? $_SESSION['output1'] : [];
$output2 = isset($_SESSION['output4']) ? $_SESSION['output4'] : [];


?>

<!DOCTYPE html>
<html>

<head>
  <title>Result</title>
  <link rel="stylesheet" type="text/css" href="styles.css">
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="Content-Language" content="ar-sa">
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <style>
    body {
      padding-left: 80px;
    }
  </style>
</head>

<body>
  <!-- Navigation bar -->
  <div class="navbar">
    <div class="nav-links">
      <div id="info-link">
        <a href="info.html" class="nav-link">INFO</a>
      </div>
    </div>
    <a href="http://localhost/AndroSightTestRun/main.html" id="logo">Your Logo</a>
  </div>



  <!-- Content area -->
  <div class="content">
    <h1>Result</h1>
    <!-- Display the outputs within the div -->
    <div id="output">
      <p>
        <?php
        echo implode("<br>", $output1);
        echo implode("<br>", $output4); ?>
      </p>
    </div>
  </div>
</body>

</html>

<?php
// Clear the session variables
session_unset();
session_destroy();
?>