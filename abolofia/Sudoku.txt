#!/usr/bin/python


print 'Content-Type: text/html\n\n'

print """
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
    background-color: #BE81F7;
    }
    
    table.outer {
    border: 0px;
    background-color: white;
    }
    
    table.topleft {
    -webkit-border-top-left-radius: 20px;
    -moz-border-radius-topleft: 20px;
    border-top-left-radius: 20px;
    background-color: #E3CEF6;
    }
    
    table.topright {
    -webkit-border-top-right-radius: 20px;
    -moz-border-radius-topright: 20px;
    border-top-right-radius: 20px;
    background-color: #E3CEF6;
    }
    
    table.bottomright {
    -webkit-border-bottom-right-radius: 20px;
    -moz-border-radius-bottomright: 20px;
    border-bottom-right-radius: 20px;
    background-color: #E3CEF6;
    }
    
    table.bottomleft {
    -webkit-border-bottom-left-radius: 20px;
    -moz-border-radius-bottomleft: 20px;
    border-bottom-left-radius: 20px;
    background-color: #E3CEF6;
    }
    
    table.middle {
    background-color: #E3CEF6;
    }
    
    
    body {
    margin:0;
    padding:10;
    height:100%;
    }
    #container {
    min-height:100%;
    position:relative;
    }
    #footer {
    position:fixed;
    bottom:10;
    width:100%;
    height:20px;
    font-size:0.75em;
    text-align:center;
    }
    
    #source {
    color: black;
    border: 0px;
    background: white;
    text-decoration:underline;
    }
    
    #source:hover {
    color:blue;
    }
    
    #source:active {
    text-decoration:none;
    }
    
    </style>
    
    
    
    </head>
    
    <body>
    
    <form action="Sudoku.py" method="GET" id="input">
    <table class="outer">
    <tr>
    <td><table class="topleft">
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
    <td><table class="topright">
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
    <td><table class="middle">
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
    <td><table class="bottomleft">
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
    <td><table class="bottomright">
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
    <input type="submit" value="Solve" />
    </form>
    
    
    
    
    <div id="container">
    <div id="footer">
    <a href="sudoku.txt" id="source">view source</a>
    </div>
    </div>
    """



import cgi

class sudoku:
	
	def __init__(self, s):
		self.part = str()
		self.whole = ''.join(map(str, s))

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

	def all_index(self):		# (row, column)
		self.part = dict()
		for n in xrange(9):
			for i in xrange(9):
				self.part[(n, i)] = self.whole[n*9 + i]
		return self.part

	def box_index(self, n):		# (row, column)
		self.part = dict()
		for i in xrange(3):
			for j in xrange(3):
				self.part[((n/3)*3 + i, (n%3)*3 + j)] = self.whole[(n/3)*18 + n*3 + i*9 + j] # double check
		return self.part

	def box(self, n):
		self.part = str()
		for i in xrange(3):
			for j in xrange(3):
				self.part += self.whole[(n/3)*18 + n*3 + i*9 + j] # double check
		return self.part

	def dict_to_whole(self, s_index):	# does not return, updates self.whole within the method
		new_whole = []
		for i in xrange(9):
			for j in xrange(9):
				new_whole.append(s_index[(i, j)])
		self.whole = ''.join(map(str, new_whole))

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

	def walk(self):
		
		if self.isSolved() == True:
			return

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

	def list_to_whole(self, s_list):	# does not return, updates self.whole within the method
		self.whole = ''.join(map(str, s_list))



def sudoku_solve():

	form = cgi.FieldStorage()
    
	form_input = list()
	for i in xrange(81):
		form_input.append(form.getvalue('n'+str(i), 'x'))

	this_sudoku = sudoku(form_input)
	
	if this_sudoku.whole != 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx':
		try:
			this_sudoku.box_reduce()
			this_sudoku.walk()
			return this_sudoku.whole
		except:
			print 'You made a mistake in your entry, please try again.'
	else:
		return None
		




Solution = sudoku_solve()

if Solution != None:
	i = 0
	for n in Solution:
		if i % 9 == 0:
			print '<br />'
		print n, ' '
		i += 1


