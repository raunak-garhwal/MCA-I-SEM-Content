<?php

$server = "localhost";
$username = "root";
$pwd = "";
$dbname = "user_data";

$conn = mysqli_connect($server,$username,$pwd,$dbname);

if (!$conn){
    die("Database Not Connected : " . mysqli_connect_error());
}

if(isset($_POST['register'])){
    $fullname = $_POST['fullname'];
    $email = $_POST['email'];
    $password = $_POST['password'];
    $mobileno = $_POST['mobileno'];

    $sql = "INSERT INTO `registered_users`(`Username`,`E-mail`,`Password`,`Mobile_no.`) VALUES ('$fullname','$email','$password','$mobileno');";

    $result = mysqli_query($conn, $sql);

    if ($result) {
        echo "<script>alert('Congratulations, You have successfully registered with our Website.\\nPlease come back soon.')</script>";
        exit();   
    }

    else {
        echo "Some error occurred, data cannot be submitted: " . mysqli_error($conn);
    }
}

mysqli_close($conn);
?>

<!-- 
  Run this query in Xampp.  

CREATE DATABASE user_data;
USE user_data;
CREATE TABLE registered_users (`S_no` INT NOT NULL AUTO_INCREMENT , `Username` VARCHAR(40) NOT NULL , `E-mail` VARCHAR(30) NOT NULL , `Password` VARCHAR(20) NOT NULL , `Mobile_no.` BIGINT(15) NOT NULL , `Registered_on` TIMESTAMP NOT NULL , PRIMARY KEY (`S_no`));

 -->
