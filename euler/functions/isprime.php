<html>
<head>
<title>Primality Test</title>
<script type="text/javascript">

  var _gaq = _gaq || [];
  _gaq.push(['_setAccount', 'UA-16960753-5']);
  _gaq.push(['_trackPageview']);

  (function() {
    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
  })();

</script>
</head>

<body>

<form action="isprime.php" method="post">
Test for primality: <input type="text" name="num" />
<input type="submit" />
</form>

<?php 

function isprime($n)
{
$prime = "a";
if ($n == 2)
	return $prime;
elseif ($n < 2 || $n%2 == 0)
	{
	$prime = "not a";
	return $prime;
	}
else
	for ($i = 3; $i < (sqrt($n) + 1); $i += 2)
		{
		if ($n%$i == 0)
			{
			$prime = "not a";
			return $prime;
			}
		}
return $prime;
}


function printprime()
{
$number = $_POST["num"];
if (is_numeric($number) == false && !($number == ""))
	echo "\"" . $number . "\" is not a number. Please enter a number.";
elseif (strlen($number) > 9)
	echo "Number too large.";
elseif ($number != "")
	echo $number . " is " . isprime($number) . " prime number.";
elseif ($number == "");

}

printprime();

?>

</body>
</html>