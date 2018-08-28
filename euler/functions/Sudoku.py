#!/usr/bin/python

import cgi
import cgitb; cgitb.enable()

print """

<html>
<head>
<title>Sudoku Solver</title>
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




<style type="text/css">

.sudokuformgrey {
	font-size: 16px;
	background-color: #CCCCCC;
	border: 1px solid #666666;
	text-align: center;

}

.sudokuformwhite {
	font-size: 16px;
	background-color: #E6E6E6;
	border: 1px solid #666666;
	text-align: center;

}

table {
	border:2px solid black;
	padding:8px;
	margin:-3px;
}

table.outer {
	border: 0px;
}

</style>



</head>

<body>







<form action="Sudoku.html" method="post" id="input">
<table class="outer">
<tr>
<td><table>
<tr>
<td><input type="text" name="n0" class="sudokuformwhite" maxlength="1" size="1" /></td>
<td><input type="text" name="n1" class="sudokuformwhite" maxlength="1" size="1" /></td>
<td><input type="text" name="n2" class="sudokuformwhite" maxlength="1" size="1" /></td>
</tr>

<tr>
<td><input type="text" name="n9" class="sudokuformwhite" maxlength="1" size="1" /></td>
<td><input type="text" name="n10" class="sudokuformwhite" maxlength="1" size="1" /></td>
<td><input type="text" name="n11" class="sudokuformwhite" maxlength="1" size="1" /></td>
</tr>

<tr>
<td><input type="text" name="n18" class="sudokuformwhite" maxlength="1" size="1" /></td>
<td><input type="text" name="n19" class="sudokuformwhite" maxlength="1" size="1" /></td>
<td><input type="text" name="n20" class="sudokuformwhite" maxlength="1" size="1" /></td>
</tr>
</table></td>
<td><table>
<tr>
<td><input type="text" name="n3" class="sudokuformgrey" maxlength="1" size="1" /></td>
<td><input type="text" name="n4" class="sudokuformgrey" maxlength="1" size="1" /></td>
<td><input type="text" name="n5" class="sudokuformgrey" maxlength="1" size="1" /></td>
</tr>

<tr>
<td><input type="text" name="n12" class="sudokuformgrey" maxlength="1" size="1" /></td>
<td><input type="text" name="n13" class="sudokuformgrey" maxlength="1" size="1" /></td>
<td><input type="text" name="n14" class="sudokuformgrey" maxlength="1" size="1" /></td>
</tr>

<tr>
<td><input type="text" name="n21" class="sudokuformgrey" maxlength="1" size="1" /></td>
<td><input type="text" name="n22" class="sudokuformgrey" maxlength="1" size="1" /></td>
<td><input type="text" name="n23" class="sudokuformgrey" maxlength="1" size="1" /></td>
</tr>
</table></td>
<td><table>
<tr>
<td><input type="text" name="n6" class="sudokuformwhite" maxlength="1" size="1" /></td>
<td><input type="text" name="n7" class="sudokuformwhite" maxlength="1" size="1" /></td>
<td><input type="text" name="n8" class="sudokuformwhite" maxlength="1" size="1" /></td>
</tr>

<tr>
<td><input type="text" name="n15" class="sudokuformwhite" maxlength="1" size="1" /></td>
<td><input type="text" name="n16" class="sudokuformwhite" maxlength="1" size="1" /></td>
<td><input type="text" name="n17" class="sudokuformwhite" maxlength="1" size="1" /></td>
</tr>

<tr>
<td><input type="text" name="n24" class="sudokuformwhite" maxlength="1" size="1" /></td>
<td><input type="text" name="n25" class="sudokuformwhite" maxlength="1" size="1" /></td>
<td><input type="text" name="n26" class="sudokuformwhite" maxlength="1" size="1" /></td>
</tr>
</table></td>
</tr>

<tr>
<td><table>
<tr>
<td><input type="text" name="n27" class="sudokuformgrey" maxlength="1" size="1" /></td>
<td><input type="text" name="n28" class="sudokuformgrey" maxlength="1" size="1" /></td>
<td><input type="text" name="n29" class="sudokuformgrey" maxlength="1" size="1" /></td>
</tr>

<tr>
<td><input type="text" name="n36" class="sudokuformgrey" maxlength="1" size="1" /></td>
<td><input type="text" name="n37" class="sudokuformgrey" maxlength="1" size="1" /></td>
<td><input type="text" name="n38" class="sudokuformgrey" maxlength="1" size="1" /></td>
</tr>

<tr>
<td><input type="text" name="n45" class="sudokuformgrey" maxlength="1" size="1" /></td>
<td><input type="text" name="n46" class="sudokuformgrey" maxlength="1" size="1" /></td>
<td><input type="text" name="n47" class="sudokuformgrey" maxlength="1" size="1" /></td>
</tr>
</table></td>
<td><table>
<tr>
<td><input type="text" name="n30" class="sudokuformwhite" maxlength="1" size="1" /></td>
<td><input type="text" name="n31" class="sudokuformwhite" maxlength="1" size="1" /></td>
<td><input type="text" name="n32" class="sudokuformwhite" maxlength="1" size="1" /></td>
</tr>

<tr>
<td><input type="text" name="n39" class="sudokuformwhite" maxlength="1" size="1" /></td>
<td><input type="text" name="n40" class="sudokuformwhite" maxlength="1" size="1" /></td>
<td><input type="text" name="n41" class="sudokuformwhite" maxlength="1" size="1" /></td>
</tr>

<tr>
<td><input type="text" name="n48" class="sudokuformwhite" maxlength="1" size="1" /></td>
<td><input type="text" name="n49" class="sudokuformwhite" maxlength="1" size="1" /></td>
<td><input type="text" name="n50" class="sudokuformwhite" maxlength="1" size="1" /></td>
</tr>
</table></td>
<td><table>
<tr>
<td><input type="text" name="n33" class="sudokuformgrey" maxlength="1" size="1" /></td>
<td><input type="text" name="n34" class="sudokuformgrey" maxlength="1" size="1" /></td>
<td><input type="text" name="n35" class="sudokuformgrey" maxlength="1" size="1" /></td>
</tr>

<tr>
<td><input type="text" name="n42" class="sudokuformgrey" maxlength="1" size="1" /></td>
<td><input type="text" name="n43" class="sudokuformgrey" maxlength="1" size="1" /></td>
<td><input type="text" name="n44" class="sudokuformgrey" maxlength="1" size="1" /></td>
</tr>

<tr>
<td><input type="text" name="n51" class="sudokuformgrey" maxlength="1" size="1" /></td>
<td><input type="text" name="n52" class="sudokuformgrey" maxlength="1" size="1" /></td>
<td><input type="text" name="n53" class="sudokuformgrey" maxlength="1" size="1" /></td>
</tr>
</table></td>
</tr>

<tr>
<td><table>
<tr>
<td><input type="text" name="n54" class="sudokuformwhite" maxlength="1" size="1" /></td>
<td><input type="text" name="n55" class="sudokuformwhite" maxlength="1" size="1" /></td>
<td><input type="text" name="n56" class="sudokuformwhite" maxlength="1" size="1" /></td>
</tr>

<tr>
<td><input type="text" name="n63" class="sudokuformwhite" maxlength="1" size="1" /></td>
<td><input type="text" name="n64" class="sudokuformwhite" maxlength="1" size="1" /></td>
<td><input type="text" name="n65" class="sudokuformwhite" maxlength="1" size="1" /></td>
</tr>

<tr>
<td><input type="text" name="n72" class="sudokuformwhite" maxlength="1" size="1" /></td>
<td><input type="text" name="n73" class="sudokuformwhite" maxlength="1" size="1" /></td>
<td><input type="text" name="n74" class="sudokuformwhite" maxlength="1" size="1" /></td>
</tr>
</table></td>
<td><table>
<tr>
<td><input type="text" name="n57" class="sudokuformgrey" maxlength="1" size="1" /></td>
<td><input type="text" name="n58" class="sudokuformgrey" maxlength="1" size="1" /></td>
<td><input type="text" name="n59" class="sudokuformgrey" maxlength="1" size="1" /></td>
</tr>

<tr>
<td><input type="text" name="n66" class="sudokuformgrey" maxlength="1" size="1" /></td>
<td><input type="text" name="n67" class="sudokuformgrey" maxlength="1" size="1" /></td>
<td><input type="text" name="n68" class="sudokuformgrey" maxlength="1" size="1" /></td>
</tr>

<tr>
<td><input type="text" name="n75" class="sudokuformgrey" maxlength="1" size="1" /></td>
<td><input type="text" name="n76" class="sudokuformgrey" maxlength="1" size="1" /></td>
<td><input type="text" name="n77" class="sudokuformgrey" maxlength="1" size="1" /></td>
</tr>
</table></td>
<td><table>
<tr>
<td><input type="text" name="n60" class="sudokuformwhite" maxlength="1" size="1" /></td>
<td><input type="text" name="n61" class="sudokuformwhite" maxlength="1" size="1" /></td>
<td><input type="text" name="n62" class="sudokuformwhite" maxlength="1" size="1" /></td>
</tr>

<tr>
<td><input type="text" name="n69" class="sudokuformwhite" maxlength="1" size="1" /></td>
<td><input type="text" name="n70" class="sudokuformwhite" maxlength="1" size="1" /></td>
<td><input type="text" name="n71" class="sudokuformwhite" maxlength="1" size="1" /></td>
</tr>

<tr>
<td><input type="text" name="n78" class="sudokuformwhite" maxlength="1" size="1" /></td>
<td><input type="text" name="n79" class="sudokuformwhite" maxlength="1" size="1" /></td>
<td><input type="text" name="n80" class="sudokuformwhite" maxlength="1" size="1" /></td>
</tr>
</table></td>
</tr>
</table>



<br /><br />
</form>

<button type="button" onclick="solve()">Submit</button>



#	s = string of the numbers from l to r, x's mean not filled yet
#	n = number index for a row, column, box
#	d = digit 1-9

class sudoku:
	
	def __init__(self, s):
		self.part = str()
		whole_list = []
		for d in s:
			whole_list.append(d)
		for i in xrange(len(whole_list)):
			if whole_list[i] == '0':
				whole_list[i] = 'x'
		self.whole = ''.join(map(str, whole_list))
	
	def row(self, n):
		self.part = str()
		for i in xrange(9):
			self.part += self.whole[n*9 + i]
		return self.part
	
	def column(self, n):
		self.part = str()
		for i in xrange(9):
			self.part += self.whole[n + i*9]
		return self.part
	
	def box(self, n):
		self.part = str()
		for i in xrange(3):
			for j in xrange(3):
				self.part += self.whole[(n/3)*18 + n*3 + i*9 + j] # double check
		return self.part
	
	def isSolved(self):
		self.error()
		if 'x' in self.whole:
			return False
		for n in xrange(9):
			this_row = self.row(n)
			this_column = self.column(n)
			this_box = self.box(n)
			for d in xrange(1, 10):
				if (str(d) not in this_row) or (str(d) not in this_column) or (str(d) not in this_box):
					return False
		return True
	
	def box_index(self, n):		# (row, column)
		self.part = dict()
		for i in xrange(3):
			for j in xrange(3):
				self.part[((n/3)*3 + i, (n%3)*3 + j)] = self.whole[(n/3)*18 + n*3 + i*9 + j] # double check
		return self.part
	
	def all_index(self):		# (row, column)
		self.part = dict()
		for n in xrange(9):
			for i in xrange(9):
				self.part[(n, i)] = self.whole[n*9 + i]
		return self.part
	
	def error(self):
		if '0' in self.whole:
			raise Exception('SudokuError: Zero')
		if len(self.whole) != 81:
			raise Exception('SudokuError: Length')
		for n in xrange(9):
			this_row = self.row(n)
			this_column = self.column(n)
			this_box = self.box(n)
			for d in xrange(1, 10):
				if this_row.count(str(d)) > 1 or this_column.count(str(d)) > 1 or this_box.count(str(d)) > 1:
					raise Exception('SudokuError: Double')					
	
	def dict_to_whole(self, s_index):	# does not return, updates self.whole within the method
		new_whole = []
		for i in xrange(9):
			for j in xrange(9):
				new_whole.append(s_index[(i, j)])
		self.whole = ''.join(map(str, new_whole))	
	
	def list_to_whole(self, s_list):	# does not return, updates self.whole within the method
		self.whole = ''.join(map(str, s_list))
	
	def box_reduce(self):				# does not return, updates self.whole within the method
		all_boxes = self.all_index()		
		prev_whole = ''
		
		while self.whole != prev_whole:
			prev_whole = self.whole
			for d in xrange(1, 10):
				for n in xrange(9):
					this_box_index = self.box_index(n)
					if str(d) in self.box(n):
						continue
					for key_value in all_boxes.iteritems():
						if key_value[1] == str(d):
							for i in xrange(9):
								if (key_value[0][0], i) in this_box_index:
									del this_box_index[(key_value[0][0], i)]
								if (i, key_value[0][1]) in this_box_index:
									del this_box_index[(i, key_value[0][1])]
					solo_count = 0
					for i in this_box_index.iterkeys():
						if this_box_index[i] == 'x':
							solo_count += 1
					if solo_count == 1:
						for i in this_box_index.iterkeys():
							if this_box_index[i] == 'x':
								all_boxes[i] = str(d)
					self.dict_to_whole(all_boxes)
			
		self.error()

	def walk(self):

		def x_index_list(s):
			x_list = []
			for i in range(len(list(s))):
				if list(s)[i] == 'x':
					x_list.append(i)
			return x_list
		
		saved_whole = self.whole
		whole_list = list(self.whole)
		x_index = x_index_list(saved_whole)
		
		i = 0
		while True:
			try:
				whole_list[x_index[i]] = str(int(whole_list[x_index[i]]) + 1)
			except:
				whole_list[x_index[i]] = '1'
			if whole_list[x_index[i]] == '10':
				whole_list[x_index[i]] = 'x'
				i -= 1
			else:
				try:
					self.list_to_whole(whole_list)
					if self.isSolved() == True:
						return
					else:
						i += 1
				except:
					pass
		

def nextgrid():
	s = open('sudoku.txt', 'r')
	i = 0
	sud = []
	for row in s:
		i = (i+1)%10
		if i != 1:
			sud.append(str(row)[:9])
		if i == 0:
			sud = ''.join(sud)
			new = []
			for j in sud:
				if j != '0':
					new.append(int(j))
				else:
					new.append('x')
			yield ''.join(map(str, new))
			sud = []
	return		

def main():	
	total = 0
	for s in nextgrid():
		this_sudoku = sudoku(s)
		this_sudoku.box_reduce()
		if this_sudoku.isSolved() == False:
			this_sudoku.walk()
		print this_sudoku.whole, this_sudoku.isSolved(), int(this_sudoku.whole[:3])
		total += int(this_sudoku.whole[:3])
		
	print total

main()




</body>
</html>

"""