<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Calculator</title>
    <style>
        @import url("https://fonts.googleapis.com/css2?family=Anta&display=swap");
      * {
        font-family: "Anta", sans-serif;
        margin: 0;
        padding: 0;
        font-weight: 600;
      }
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            background-color: #02323f;
            height:100vh;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .container {
            width: 300px;
            margin: 50px auto;
            padding: 20px;
            border-radius: 30px;
            border: 1px solid white;
            background-color: #112245;
            display: flex;
            flex-direction:column;
            justify-content: center;
            align-items: center;
        }
        input[type="number"], select{
            width: 100%;
            margin: 10px 0;
            padding: 8px;
            font-size: 16px;
            box-sizing: border-box;
            border-radius:30px;
        }
        input[type="submit"] {
            cursor: pointer;
            display: inline;
            font-size:16px;
            padding:8px;
            margin:4px 0 0 0;
            background-color: #00d1f5;
            color: #14213d;
            font-weight: 700;
            border-radius: 15px;
        }
        .result {
            border: 1px solid white;
            padding: 5px; 
            margin: 15px 0 0 0; 
            display: inline-block;  
            background-color: yellow;
            border-radius: 10px;
        }
        #title{
            color:white;
            padding:5px;
        }
    </style>
</head>
<body>
    <div class="container">
        <div><h1 id="title">CALCULATOR</h1></div>
        <form method="post">
            <div>
            <input type="number" name="num1" placeholder="Enter number 1" step="0.000000000001" />
            <input type="number" name="num2" placeholder="Enter number 2" step="0.000000000001" />
            <select name="operations">
                <option value="add">Addition</option>
                <option value="subtract">Subtraction</option>
                <option value="multiply">Multiplication</option>
                <option value="divide">Division</option>
                <option value="min">Minimum</option>
                <option value="max">Maximum</option>
                <option value="pow">Exponentiation</option>
                <option value="mod">Modulus</option>
                <option value="round">Rounded</option>
                <option value="ceil">Ceiling</option>
                <option value="floor">Floor</option>
                <option value="sqrt">Square Root</option>
                <option value="cbrt">Cube Root</option>
            </select>
            <input type="submit" name="submit" value="Calculate">
            </div>
            <div class="result">
                <?php
                if ($_POST) {
                    $num1 = $_POST['num1'];
                    $num2 = $_POST['num2'];
                    $selectedOperation = $_POST['operations'];
                    $result = 0;

                    switch ($selectedOperation) {
                        case 'add':
                            $result = $num1 + $num2;
                            break;
                        case 'subtract':
                            $result = $num1 - $num2;
                            break;
                        case 'multiply':
                            $result = $num1 * $num2;
                            break;
                        case 'divide':
                            $result = $num1 / $num2;
                            break;
                        case 'min':
                            $result = min($num1, $num2);
                            break;
                        case 'max':
                            $result = max($num1, $num2);
                            break;
                        case 'pow':
                            $result = pow($num1, $num2);
                            break;
                        case 'mod':
                            $result = $num1 % $num2;
                            break;
                        case 'round':
                            $result = round($num1);
                            break;
                        case 'ceil':
                            $result = ceil($num1);
                            break;
                        case 'floor':
                            $result = floor($num1);
                            break;
                        case 'sqrt':
                            $result = sqrt($num1);
                            break;
                        case 'cbrt':
                            $result = $num1**(1/3);
                            break;
                        default:
                            echo 'Invalid operation';
                    }
                    echo 'Result: ' . $result;
                }
                ?>
            </div>
        </form>
    </div>
</body>
</html>
