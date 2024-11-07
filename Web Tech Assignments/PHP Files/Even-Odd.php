<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>Even and Odd</title>
<style>
@import url("https://fonts.googleapis.com/css2?family=Anta&display=swap");

  * {
    padding: 0;
    margin: 0;
    font-family: "Anta", sans-serif;
    border-radius: 15px;
    box-sizing: border-box;
    font-weight: 600;
  }

  body {
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    overflow: hidden;
    background-color: #023047;
  }

  .container {
    position: relative;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 36px;
    padding: 40px;
    border-radius: 20px;
    height: 360px;
    background-color: #8ad2f4;
  }

  #label {
    font-size: 27px;
  }

  #inputbox {
    padding: 1px 8px;
    font-size: 22px;
    background-color: #dcebf3;
  }

  #btn {
    padding: 6px;
    font-size: 20px;
    background-color: #026694;
    color: white;
  }

  #btn:active {
    transition: all 100ms ease-in-out;
    transform: scale(85%);
  }

  div > h1 {
    text-decoration: underline;
    font-weight: 600;
    font-size: 50px;
  }

  #result {
    font-size: 25px;
  }

  input::-webkit-outer-spin-button,
  input::-webkit-inner-spin-button {
    -webkit-appearance: none;
    margin: 0;
  }
</style>
</head>
<body>

<form method="post">
<div class="container">
  <div>
    <h1>Check Even or Odd Number</h1>
  </div>

  <div>
    <label id="label">Enter a Number : </label>
    <input type="number" id="inputbox" name="number" />
  </div>

  <div>
    <input type="submit" id="btn" value="Check"/>
  </div>

  <div id="result">
  <?php
    if($_POST){
        $num = $_POST['number'];
        if ($num%2==0){
            echo "$num is an Even Number.";
        }
        else{
            echo "$num is an Odd Number.";
        }
    }
  ?>
  </div>
</div>
</form>

</body>
</html>
