<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Printing Pyramid</title>
    <style>
      @import url("https://fonts.googleapis.com/css2?family=Anta&display=swap");

      * {
        padding: 0;
        margin: 0;
        font-family: "Anta", "sans-serif";
        border-radius: 15px;
        box-sizing: border-box;
        font-weight: 600;
      }

      body {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 30px;
        min-height: 100vh;
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
        padding:6px;
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
        font-size: 40px;
        font-family: sans-serif;
      }

      input::-webkit-outer-spin-button,
      input::-webkit-inner-spin-button {
        -webkit-appearance: none;
        margin: 0;
      }
    </style>
  </head>
  <body>
    <div>
      <h1>Pyramid Printing</h1>
    </div>
    <form method="post">
    <div>
      <label id="label">Enter the length of Pyramid : </label>
      <input type="number" id="inputbox" name="number"/>
        <input id="btn" name="submit" type="submit">
    </div>
</form>

    <div id="result">
        <?php
        if($_POST){
            $number = $_POST['number'];
            for($i = 1; $i<=$number;$i++){
                for($j = 1; $j <= $number - $i; $j++){
                    echo "&nbsp;";
                }
                for($k = 1; $k <= $i; $k++){
                    echo "* ";
                }
                echo "<br>";
                }
            }?>
    </div>
  </body>
</html>
