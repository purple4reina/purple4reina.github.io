<html>
<head>
<title>Factor Generator</title>
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

<form action="factors.php" method="post">
Generate a list of factors: <input type="text" name="num" />
<input type="submit" />
</form>

<?php 

function factors($n)
{
$factor_list = array();
for ($i = 1; $i <= sqrt($n); $i++)
	{
	if (is_int($n / $i))
		{
		array_push($factor_list, $i);
		if ($i != $n / $i)
			{
			array_push($factor_list, $n / $i);
			}
		}
	}
asort($factor_list);
return $factor_list;
}


function printfactors()
{
$number = $_POST["num"];
if (is_numeric($number) == false && !($number == ""))
	echo "\"" . $number . "\" is not a number. Please enter a number.";

elseif (strlen($number) > 9)
	echo "Number too large.";

elseif ($number < 1)
	echo "Please input a number greater than zero.";

elseif ($number != "")
	{
	$facts = factors($number);
	echo "The factors of " . $number . " are:<br />";
	foreach ($facts as $f)
		{
		echo $f . "<br />";
		}
	}
elseif ($number == "");

}

printfactors();

?>

</body>
</html>