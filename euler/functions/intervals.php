<html>
<head>
<title>Musical Intervals</title>
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

<form action="intervals.php" method="post">
Find the interval between two pitchs<br /><br />
Lower Pitch: <select name="pitch_1">
<option value="C">C</option>
<option value="D">D</option>
<option value="E">E</option>
<option value="F">F</option>
<option value="G">G</option>
<option value="A">A</option>
<option value="B">B</option></select>&nbsp&nbsp&nbsp
<input type="radio" name="accidental_1" value="2" />&#9837&#9837&nbsp&nbsp&nbsp
<input type="radio" name="accidental_1" value="1" />&#9837&nbsp&nbsp&nbsp
<input type="radio" name="accidental_1" value="0" checked="yes" />&#9838&nbsp&nbsp&nbsp
<input type="radio" name="accidental_1" value="-1" />&#9839&nbsp&nbsp&nbsp
<input type="radio" name="accidental_1" value="-2" />&#9839&#9839<br /><br />
Upper Pitch: <select name="pitch_2">
<option value="C">C</option>
<option value="D">D</option>
<option value="E">E</option>
<option value="F">F</option>
<option value="G">G</option>
<option value="A">A</option>
<option value="B">B</option></select>&nbsp&nbsp&nbsp
<input type="radio" name="accidental_2" value="-2" />&#9837&#9837&nbsp&nbsp&nbsp
<input type="radio" name="accidental_2" value="-1" />&#9837&nbsp&nbsp&nbsp
<input type="radio" name="accidental_2" value="0" checked="yes" />&#9838&nbsp&nbsp&nbsp
<input type="radio" name="accidental_2" value="1" />&#9839&nbsp&nbsp&nbsp
<input type="radio" name="accidental_2" value="2" />&#9839&#9839<br /><br />
<input type="submit" />
</form>





<?php 

function getinterval($p1, $a1, $p2, $a2)
{

//interval
$interval = ($p2 - $p1) % 7;
if ($interval < 0)
	{
	$interval = 7 - abs($interval + 1);
	}
else
	{	
	$interval = abs($interval + 1);
	}
if ($interval == 1) $interval = "Octave";
elseif ($interval == 2) $interval = "2nd";
elseif ($interval == 3) $interval = "3rd";
elseif ($interval == 4) $interval = "4th";
elseif ($interval == 5) $interval = "5th";
elseif ($interval == 6) $interval = "6th";
elseif ($interval == 7) $interval = "7th";


//quality step one
if (($p1 == 0 && $p2 == 1) || ($p1 == 0 && $p2 == 2) || ($p1 == 0 && $p2 == 5) || ($p1 == 0 && $p2 == 6) || ($p1 == 1 && $p2 == 2) || ($p1 == 1 && $p2 == 6) || ($p1 == 3 && $p2 == 4) || ($p1 == 3 && $p2 == 5) || ($p1 == 3 && $p2 == 1) || ($p1 == 3 && $p2 == 2) || ($p1 == 4 && $p2 == 5) || ($p1 == 4 && $p2 == 6) || ($p1 == 4 && $p2 == 2) || ($p1 == 5 && $p2 == 6))
	{
	$quality = "major";
	}

elseif (($p1 == 1 && $p2 == 3) || ($p1 == 1 && $p2 == 0) || ($p1 == 2 && $p2 == 3) || ($p1 == 2 && $p2 == 4) || ($p1 == 2 && $p2 == 0) || ($p1 == 2 && $p2 == 1) || ($p1 == 4 && $p2 == 3) || ($p1 == 5 && $p2 == 0) || ($p1 == 5 && $p2 == 3) || ($p1 == 5 && $p2 == 4) || ($p1 == 6 && $p2 == 0) || ($p1 == 6 && $p2 == 1) || ($p1 == 6 && $p2 == 4) || ($p1 == 6 && $p2 == 5))
	{
	$quality = "minor";
	}

elseif (($p1 == 0 && $p2 == 3) || ($p1 == 0 && $p2 == 4) || ($p1 == 1 && $p2 == 4) || ($p1 == 1 && $p2 == 5) || ($p1 == 2 && $p2 == 5) || ($p1 == 2 && $p2 == 6) || ($p1 == 3 && $p2 == 0) || ($p1 == 4 && $p2 == 0) || ($p1 == 4 && $p2 == 0) || ($p1 == 4 && $p2 == 1) || ($p1 == 5 && $p2 == 1) || ($p1 == 5 && $p2 == 2) || ($p1 == 6 && $p2 == 2) || ($p1 == $p2))
	{
	$quality = "perfect";
	}

elseif ($p1 == 3 && $p2 == 6)
	{
	$quality = "augmented";
	}

elseif ($p1 == 6 && $p2 == 3)
	{
	$quality = "diminished";
	}


//quality step two
$qual_change = $a1 + $a2;

if ($quality == major)
	{
	if ($qual_change == -4) $qual_final = "Triply Diminished";
	if ($qual_change == -3) $qual_final = "Doubly Diminished";
	if ($qual_change == -2) $qual_final = "Diminished";
	if ($qual_change == -1) $qual_final = "Minor";
	if ($qual_change == 0) $qual_final = "Major";
	if ($qual_change == 1) $qual_final = "Augmented";
	if ($qual_change == 2) $qual_final = "Doubly Augmented";
	if ($qual_change == 3) $qual_final = "Triply Augmented";
	if ($qual_change == 4) $qual_final = "Quadruply Augmented";
	}

elseif ($quality == minor)
	{
	if ($qual_change == -4) $qual_final = "Quadriply Diminished";
	if ($qual_change == -3) $qual_final = "Triply Diminished";
	if ($qual_change == -2) $qual_final = "Doubly Diminished";
	if ($qual_change == -1) $qual_final = "Diminished";
	if ($qual_change == 0) $qual_final = "Minor";
	if ($qual_change == 1) $qual_final = "Major";
	if ($qual_change == 2) $qual_final = "Augmented";
	if ($qual_change == 3) $qual_final = "Doubly Augmented";
	if ($qual_change == 4) $qual_final = "Triply Augmented";
	}

elseif ($quality == perfect)
	{
	if ($qual_change == -4) $qual_final = "Quadriply Diminished";
	if ($qual_change == -3) $qual_final = "Triply Diminished";
	if ($qual_change == -2) $qual_final = "Doubly Diminished";
	if ($qual_change == -1) $qual_final = "Diminished";
	if ($qual_change == 0) $qual_final = "Perfect";
	if ($qual_change == 1) $qual_final = "Augmented";
	if ($qual_change == 2) $qual_final = "Doubly Augmented";
	if ($qual_change == 3) $qual_final = "Triply Augmented";
	if ($qual_change == 4) $qual_final = "Quadruply Augmented";
	}

elseif ($quality == augmented)
	{
	if ($qual_change == -4) $qual_final = "Triply Diminished";
	if ($qual_change == -3) $qual_final = "Doubly Diminished";
	if ($qual_change == -2) $qual_final = "Diminished";
	if ($qual_change == -1) $qual_final = "Perfect";
	if ($qual_change == 0) $qual_final = "Augmented";
	if ($qual_change == 1) $qual_final = "Doubly Augmented";
	if ($qual_change == 2) $qual_final = "Triply Augmented";
	if ($qual_change == 3) $qual_final = "Quadruply Augmented";
	if ($qual_change == 4) $qual_final = "Quintuply Augmented";
	}

elseif ($quality == diminished)
	{
	if ($qual_change == -4) $qual_final = "Quintuply Diminished";
	if ($qual_change == -3) $qual_final = "Quadruply Diminished";
	if ($qual_change == -2) $qual_final = "Triply Diminished";
	if ($qual_change == -1) $qual_final = "Doubly Diminished";
	if ($qual_change == 0) $qual_final = "Diminished";
	if ($qual_change == 1) $qual_final = "Perfect";
	if ($qual_change == 2) $qual_final = "Augmented";
	if ($qual_change == 3) $qual_final = "Doubly Augmented";
	if ($qual_change == 4) $qual_final = "Triply Augmented";
	}

return $qual_final . " " . $interval;
}


function printinterval()
{
if ($_POST["pitch_1"] == C) $p1 = 0;
if ($_POST["pitch_1"] == D) $p1 = 1;
if ($_POST["pitch_1"] == E) $p1 = 2;
if ($_POST["pitch_1"] == F) $p1 = 3;
if ($_POST["pitch_1"] == G) $p1 = 4;
if ($_POST["pitch_1"] == A) $p1 = 5;
if ($_POST["pitch_1"] == B) $p1 = 6;

if ($_POST["pitch_2"] == C) $p2 = 0;
if ($_POST["pitch_2"] == D) $p2 = 1;
if ($_POST["pitch_2"] == E) $p2 = 2;
if ($_POST["pitch_2"] == F) $p2 = 3;
if ($_POST["pitch_2"] == G) $p2 = 4;
if ($_POST["pitch_2"] == A) $p2 = 5;
if ($_POST["pitch_2"] == B) $p2 = 6;

if ($_POST["accidental_1"] == 2) $a1 = "&#9837&#9837";
if ($_POST["accidental_1"] == 1) $a1 = "&#9837";
if ($_POST["accidental_1"] == 0) $a1 = "&#9838";
if ($_POST["accidental_1"] == -1) $a1 = "&#9839";
if ($_POST["accidental_1"] == -2) $a1 = "&#9839&#9839";

if ($_POST["accidental_2"] == -2) $a2 = "&#9837&#9837";
if ($_POST["accidental_2"] == -1) $a2 = "&#9837";
if ($_POST["accidental_2"] == 0) $a2 = "&#9838";
if ($_POST["accidental_2"] == 1) $a2 = "&#9839";
if ($_POST["accidental_2"] == 2) $a2 = "&#9839&#9839";

if ($_POST["pitch_1"] == "");
else
	{
	echo "The interval from " . $_POST["pitch_1"] . $a1 . " to " . $_POST["pitch_2"] . $a2 . " is: <br />";
	echo getinterval($p1, $_POST["accidental_1"], $p2, $_POST["accidental_2"]);
	}
}

printinterval();

?>

</body>
</html>