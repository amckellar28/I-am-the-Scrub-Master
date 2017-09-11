<!DOCTYPE php>
<?php
$usernameErr = $passwordErr = "";
$username = $password = "";


if ($_SERVER["REQUEST_METHOD"] == "POST") {
  if (empty($_POST["username"])) {
    $usernameErr = "Username is required";
  } else {
    $username = test_input($_POST["username"]);
  }
  if (empty($_POST["password"])) {
    $passwordErr = "Password is required";
  } else {
    $password = test_input($_POST["password"]);
  }
  if (isset($_POST['username'], $_POST['password'])){
	$db = new PDO('mysql:host=localhost;dbname=security', 'min', '123');
	$query = $db->prepare('SELECT *, FROM admins WHERE username = :username');
	if($query->fetchColumn() === $_POST['password']){
        // starts the session created if login info is correct
        session_start();
        $_SESSION['username'] = $_POST['username'];
        echo 'WORKINGGIGNIGNGING';
        exit;
    }else {
		echo 'gg didnt work';
	}
  }
}




function test_input($data) {
  $data = trim($data);
  $data = stripslashes($data);
  $data = htmlspecialchars($data);
  return $data;
}
?>
<html>
<head> 
	<title> PLEY Account </title>
	<link href='form.css' rel='stylesheet'>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<meta http-equiv="X-UA-Compatible" content="ie=edge">
</head>
<body>    
	<header>
		PLEY
	</header>
<!-- Login Form. -->
	<h4>Login</h4>
	<form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>" novalidate> 
		<label class="labform">
		Username:<br> 
		<input type="text" name="username" placeholder="xXxQikScopes84xXx" required 
			value="<?php echo @$_POST['username']; ?>"
			oninvalid="this.setCustomValidity('Enter Username here')"
			oninput="setCustomValidity('')"><br>
			<span class="error"><?php echo $usernameErr;?></span><br>
		</label>
		<label class="labform">
		Password:<br>
		<input type="password" name="password" placeholder="••••••••••••••••" required
			oninvalid="this.setCustomValidity('Enter Password here')"
			oninput="setCustomValidity('')"><br>
			<span class="error"><?php echo $passwordErr;?><a href="logout.php">----Logout----</a></span><br><br>
		</label>
	<input type="submit" name="login" value="Login">
	</form>

<footer>
&#169;2017 PLEY Corporation
</footer>
</body>
</html>