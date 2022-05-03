<?php
$host = "127.0.0.1";
$port = 20205;
$sock = socket_create(AF_INET, SOCK_STREAM, 0);
socket_connect($sock, $host, $port);
?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <div align="center"></div>
    <form method="post">
        <table>
            <tr>
                <td>
                    <label for="name">Name</label>
                    <input type="text" name="name" id="name" placeholder="Enter your name" />
                    <input type="submit" name="BtnSend" value="Send">
                </td>
            </tr>

            <?php
            if (isset($_POST['name'])) {

                $msg = $_REQUEST['name'];
                $len = strlen($msg);
                //send message to server
                socket_write($sock, $msg, $len);
                //receive message from server
                $serv = "oi"; # socket_read($sock, 1024);

                echo "Server: \t" . trim($serv);
            }

            ?>
            <tr>
                <td>
                    <?php echo trim(@$serv); ?>
            </tr>
        </table>
    </form>
</body>

</html>