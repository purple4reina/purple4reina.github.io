<html>
<head>
<title>Neo-Riemannian Theory</title>
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

<style type="text/css">
 body{
  margin:10;
  padding:0 <length> 0 0;
 }
 div#right-sidebar{
  position:absolute;
  top:10;
  right:10;
  width:360;
  height:100%;
 }
 @media screen{
  <body>div#right-sidebar{
   position:fixed;
  }
 }
 * html body{
  overflow:hidden;
 } 
 * html div#content{
  height:100%;
  overflow:auto;
 }

#footer {
position:fixed;
bottom:0;
width:100%;
height:30px;
text-align:center;
font-size:small;
background-color:white;
	}


</style>
<div id="right-sidebar">
<b>P (Parallel):</b><br />
Transforms a triad to its parallel Major/Minor.<br />
<i>ex. C Major --> C Minor and C Minor --> C Major</i><br /><br />
<b>R (Relative):</b><br />
Transforms a triad to its relative Major/Minor.<br />
<i>ex. C Major --> A Minor and C Minor --> E&#9837 Major</i><br /><br />
<b>L (Leading-Tone Exchange):</b><br />
For a Major triad, transforms the root down a semi-tone. For a Minor triad, transforms the fifth up a semi-tone<br />
<i>ex. C Major --> E Minor and C Minor --> A&#9837 Major</i><br /><br />
<b>N (Nebenverwandt):</b><br />
Transforms a Major triad to its Minor subdominant and a Minor triad to its Major dominant. Also obtained through applying R, L, and P successively.<br />
<i>ex. C Major --> F Minor and C Minor --> G Major</i><br /><br />
<b>S (Slide):</b><br />
Transforms a triad by successively applying L, P, and R.<br />
<i>ex. C Major --> C&#9839 Minor and C Minor --> B Major</i><br /><br />
<b>H (Hexatonic):</b><br />
Transforms a triad by successively applying L, P, and L.<br />
<i>ex. C Major --> G&#9839 Minor and C Minor --> E Major</i><br /><br />




</div>
<div id="content">

<form action="Riemann.php" method="post">
Enter Starting Triad: <br />

<select name="pitch">
<option value="C">C</option>
<option value="D">D</option>
<option value="E">E</option>
<option value="F">F</option>
<option value="G">G</option>
<option value="A">A</option>
<option value="B">B</option></select>

<select name="accidental">
<option value="flat">&#9837</option>
<option value="natural" selected="selected">&#9838</option>
<option value="sharp">&#9839</option></select>

<input type="radio" name="quality" value="Major" checked="yes" />Major
<input type="radio" name="quality" value="Minor" />Minor<br /><br />

Neo-Riemannian Transformations to apply (in order):<br />

<select name="tran_1">
<option value="P">P</option>
<option value="R">R</option>
<option value="L">L</option>
<option value="N">N</option>
<option value="S">S</option>
<option value="H">H</option>
<option value="">None</option>
</select><br />

<select name="tran_2">
<option value="P">P</option>
<option value="R">R</option>
<option value="L">L</option>
<option value="N">N</option>
<option value="S">S</option>
<option value="H">H</option>
<option value="">None</option>
</select><br />

<select name="tran_3">
<option value="P">P</option>
<option value="R">R</option>
<option value="L">L</option>
<option value="N">N</option>
<option value="S">S</option>
<option value="H">H</option>
<option value="">None</option>
</select><br /><br />

<input type="hidden" name="submitted" value="true" />
<input type="submit" />
</form>

<?php 

function P($pc, $q)
{
if ($q == Major) $q_new = Minor;
elseif ($q == Minor) $q_new = Major;
return array($pc, $q_new);
}

function R($pc, $q)
{
if ($q == Major)
	{
	return array(($pc + 9)%12, Minor);
	}
elseif ($q == Minor)
	{
	return array(($pc + 3)%12, Major);
	}
}

function L($pc, $q)
{
if ($q == Major)
	{
	return array(($pc + 4)%12, Minor);
	}
elseif ($q == Minor)
	{
	return array(($pc + 8)%12, Major);
	}
}

function N($pc, $q)
{
$Rchord = R($pc, $q);
$Lchord = L($Rchord[0], $Rchord[1]);
$Pchord = P($Lchord[0], $Lchord[1]);
return array($Pchord[0], $Pchord[1]);
}

function S($pc, $q)
{

$Lchord = L($pc, $q);
$Pchord = P($Lchord[0], $Lchord[1]);
$Rchord = R($Pchord[0], $Pchord[1]);
return array($Rchord[0], $Rchord[1]);
}

function H($pc, $q)
{

$Lchord = L($pc, $q);
$Pchord = P($Lchord[0], $Lchord[1]);
$Lchord = L($Pchord[0], $Pchord[1]);
return array($Lchord[0], $Lchord[1]);
}

function None_($pc, $q)
{
return array($pc, $q);
}


function chord_to_number($p, $a)
{

if ($a == "&#9837") $a = flat;
elseif ($a == "&#9838") $a = natural;
elseif ($a == "&#9839") $a = sharp;

if ((($p == C) && ($a == natural)) || (($p == B) && ($a == sharp)))
	{
	return 0;
	}
elseif ((($p == D) && ($a == flat)) || (($p == C) && ($a == sharp)))
	{
	return 1;
	}
elseif (($p == D) && ($a == natural))
	{
	return 2;
	}
elseif ((($p == D) && ($a == sharp)) || (($p == E) && ($a == flat)))
	{
	return 3;
	}
elseif ((($p == E) && ($a == natural)) || (($p == F) && ($a == flat)))
	{
	return 4;
	}
elseif ((($p == F) && ($a == natural)) || (($p == E) && ($a == sharp)))
	{
	return 5;
	}
elseif ((($p == F) && ($a == sharp)) || (($p == G) && ($a == flat)))
	{
	return 6;
	}
elseif (($p == G) && ($a == natural))
	{
	return 7;
	}
elseif ((($p == G) && ($a == sharp)) || (($p == A) && ($a == flat)))
	{
	return 8;
	}
elseif (($p == A) && ($a == natural))
	{
	return 9;
	}
elseif ((($p == A) && ($a == sharp)) || (($p == B) && ($a == flat)))
	{
	return 10;
	}
elseif ((($p == B) && ($a == natural)) || (($p == C) && ($a == flat)))
	{
	return 11;
	}
}


function number_to_chord($pc, $q)
{

$flat = "&#9837";
$natural = "&#9838";
$sharp = "&#9839";

if ($pc == 0)
	{
	return array(C, $natural);
	}
elseif ($pc == 1)
	{
	if ($q == Major) return array(D, $flat);
	elseif ($q == Minor) return array(C, $sharp);
	}
elseif ($pc == 2)
	{
	return array(D, $natural);
	}
elseif ($pc == 3)
	{
	return array(E, $flat);
	}
elseif ($pc == 4)
	{
	return array(E, $natural);
	}
elseif ($pc == 5)
	{
	return array(F, $natural);
	}
elseif ($pc == 6)
	{
	if ($q == Major) return array(G, $flat);
	elseif ($q == Minor) return array(F, $sharp);
	}
elseif ($pc == 7)
	{
	return array(G, $natural);
	}
elseif ($pc == 8)
	{
	if ($q == Major) return array(A, $flat);
	elseif ($q == Minor) return array(G, $sharp);
	}
elseif ($pc == 9)
	{
	return array(A, $natural);
	}
elseif ($pc == 10)
	{
	return array(B, $flat);
	}
elseif ($pc == 11)
	{
	return array(B, $natural);
	}
}



function printTransform($p, $a, $q, $t1, $t2, $t3)
{

$pitch_class = chord_to_number($p, $a);

echo $p;

if ($a == flat) echo "&#9837";
elseif ($a == natural) echo "&#9838";
elseif ($a == sharp) echo "&#9839";

echo $q . " under ";

if (($t1 == "") && ($t2 == "") && ($t3 == "")) echo "no ";

echo "transformation";

if (($t1 == "") && ($t2 == "") && ($t3 == "")) echo "s";

echo " " . $t1 . $t2 . $t3 . " is ";

if ($t1 == P) $chord1 = P($pitch_class, $q);
elseif ($t1 == R) $chord1 = R($pitch_class, $q);
elseif ($t1 == L) $chord1 = L($pitch_class, $q);
elseif ($t1 == N) $chord1 = N($pitch_class, $q);
elseif ($t1 == S) $chord1 = S($pitch_class, $q);
elseif ($t1 == H) $chord1 = H($pitch_class, $q);
elseif ($t1 == "") $chord1 = None_($pitch_class, $q);

if ($t2 == P) $chord2 = P($chord1[0], $chord1[1]);
elseif ($t2 == R) $chord2 = R($chord1[0], $chord1[1]);
elseif ($t2 == L) $chord2 = L($chord1[0], $chord1[1]);
elseif ($t2 == N) $chord2 = N($chord1[0], $chord1[1]);
elseif ($t2 == S) $chord2 = S($chord1[0], $chord1[1]);
elseif ($t2 == H) $chord2 = H($chord1[0], $chord1[1]);
elseif ($t2 == "") $chord2 = None_($chord1[0], $chord1[1]);

if ($t3 == P) $chord3 = P($chord2[0], $chord2[1]);
elseif ($t3 == R) $chord3 = R($chord2[0], $chord2[1]);
elseif ($t3 == L) $chord3 = L($chord2[0], $chord2[1]);
elseif ($t3 == N) $chord3 = N($chord2[0], $chord2[1]);
elseif ($t3 == S) $chord3 = S($chord2[0], $chord2[1]);
elseif ($t3 == H) $chord3 = H($chord2[0], $chord2[1]);
elseif ($t3 == "") $chord3 = None_($chord2[0], $chord2[1]);

$pitch_accidental = number_to_chord($chord3[0], $chord3[1]);
$pitch = $pitch_accidental[0];
$accidental = $pitch_accidental[1];

echo $pitch . $accidental . $chord3[1];

}

if ($_POST['submitted'] == true) 
	{
	printTransform($_POST['pitch'], $_POST['accidental'], $_POST['quality'], $_POST['tran_1'], $_POST['tran_2'], $_POST['tran_3']);
	}
?>

</div>
</body>
<div id="footer">
<a href="http://euler.clarinetcat.com/">project euler</a>
*
<a href="http://euler.clarinetcat.com/functions/functions">functions</a>
*
<a href="http://abolofia.net/">reina abolofia</a>
*
<a href="http://clarinetcat.com">tie swabs</a>
</div>
</html>