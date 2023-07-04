<?php
header('Content-Type: text/html; charset=utf-8');

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
  $targetDirectory = "C:/Users/hp/Desktop/uploaded/"; // Directory where the file will be saved
  $targetFile = $targetDirectory . basename($_FILES["file"]["name"]);
  $uploadOk = 1;
  $fileType = strtolower(pathinfo($targetFile, PATHINFO_EXTENSION));


  // Check if $uploadOk is set to 0 by an error
  if ($uploadOk == 0) {
    echo "Sorry, your file was not uploaded.";
  } else {
    if (move_uploaded_file($_FILES["file"]["tmp_name"], $targetFile)) {
      // File was successfully uploaded and moved to the desired location
      // You can include any additional code or actions here
    } else {
      // Failed to move the uploaded file
      // You can handle the error or display an error message here
    }
  }


  // virustotal 
  $python_script1 = '...........\AndroSight\VirusTotal.py';
  exec("python $python_script1", $output4);

  // run apktool to decompress
  $python_script2 = '...........\AndroSight\apktool.py';
  exec("python $python_script2");


  // run GetPermission to get Permission from manifiest 
  $python_script3 = '...........\AndroSight\GetPermission.py';
  exec("python $python_script3", $output2);
  sleep(20);
  // clear all files in folder
  $python_script4 = '...........\AndroSight\Flush.py';
  exec("python $python_script4 ");

  // Store the outputs in session variables
  session_start();
  $_SESSION['output1'] = $output1;
  $_SESSION['output2'] = $output4;

  // Redirect to the result page
  header("Location: result.php");
  exit();

}

?>