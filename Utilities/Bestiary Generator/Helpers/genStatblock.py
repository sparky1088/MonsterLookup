################################################################################
#
#	genStatblock.py
#	Generates statblock HTML code for monster using a monster info. file
#	This program is intended to be used as a subsystem for a monster generator.
#
#	Usage: python genStatblock.py [monster name] [monster info file name]
#	
#	This generator is developed by Shunman Tse (RiasKlein)
#		https://github.com/riasklein
#	Statblock5e code is by Val Markovic (Valloric) 
#		https://github.com/Valloric
#
#	Version 0.92
#
################################################################################

import sys

# print_usage_instructions
#	Function prints the usage instructions
def print_usage_instructions ():
	print ("Correct Usage:\tpython genStatblock.py [monster name] [info file name]")
	
def print_ferror ( func_name ):
	print ("Error detected in function: " + func_name)
	print ("Exiting program...")
	sys.exit()
	
# writeCreatureHeading
# 	Function writes the creature heading information into the output file
def writeCreatureHeading (monster_name, rfile, wfile):
	wfile.write ("""
<stat-block>
	<creature-heading>
		<h1>""")	  
	
	wfile.write (monster_name)
	
	wfile.write ("""</h1>
		<h2>
		""")

	while True:
		line = rfile.readline()			# Get a line from the monster info file
		if not line: print_ferror ('writeCreatureHeading')
		
		if 'Tags' in line:
			armor_class = rfile.readline()
			wfile.write (armor_class)
			wfile.write ("""		</h2>
	</creature-heading>
	""")
			return

# writeTopStats
# 	Function writes the top stats of a monster into the output file
def writeTopStats (rfile, wfile):
	wfile.write ("""
	<top-stats>""")

	while True:
		line = rfile.readline()
		if not line: print_ferror ('writeTopStats')
		
		# Armor Class 
		if 'armor class' in line.lower():
			wfile.write("""		
		<property-line>
			<h4>Armor Class</h4>
			<p>
			""")
			wfile.write (line [len ('armor class '):])
			wfile.write ("""			</p>
		</property-line>""")
	
		# Hit Points
		if 'hit points' in line.lower():
			wfile.write("""
			
		<property-line>
			<h4>Hit Points</h4>
			<p>
			""")
			wfile.write (line [len ('hit points '):])
			wfile.write ("""			</p>
		</property-line>""")

		# Speed and 'Basic' Stats
		if 'speed' in line.lower():
			wfile.write("""
			
		<property-line>
			<h4>Speed</h4>
			<p>
			""")
			wfile.write (line [len ('speed '):])
			wfile.write ("""			</p>
		</property-line>""")
		
		# Monster Attributes
		if 'str' in line.lower() and 'dex' in line.lower() and 'con' in line.lower() and 'int' in line.lower() and 'wis' in line.lower() and 'cha' in line.lower():
			line = rfile.readline()
			line = line.split()
			
			# This is for a line break in the generated output file
			wfile.write ("""
			
		""")
			
			# Let's fill in our stats!!
			wfile.write ('<abilities-block data-str="')
			wfile.write (line[0])
			wfile.write ('" data-dex="')
			wfile.write (line[2])
			wfile.write ('" data-con="')
			wfile.write (line[4])
			wfile.write ('" data-int="')
			wfile.write (line[6])
			wfile.write ('" data-wis="')
			wfile.write (line[8])
			wfile.write ('" data-cha="')
			wfile.write (line[10])
			wfile.write ('" ></abilities-block>')
			line = line[0]
			
		# Saving Throws
		if 'saving throws' in line.lower():
			wfile.write("""	
			
		<property-line>
			<h4>Saving Throws</h4>
			<p>
			""")
			wfile.write (line [len ('saving throws '):])
			wfile.write ("""			</p>
		</property-line>""")
		
		# Skills
		if 'skills' in line.lower():
			wfile.write("""	
			
		<property-line>
			<h4>Skills</h4>
			<p>
			""")
			wfile.write (line [len ('skills '):])
			wfile.write ("""			</p>
		</property-line>""")
		
		# Immunities
		if 'immunities' in line.lower() and (line[:6].lower() != 'damage' and line[:9].lower() != 'condition'):
			wfile.write("""
			
		<property-line>
			<h4>Immunities</h4>
			<p>
			""")
			wfile.write (line [len ('immunities '):])
			wfile.write ("""			</p>
		</property-line>""")
		
		# Damage Resistances
		if 'damage resistances' in line.lower():
			wfile.write("""	
			
		<property-line>
			<h4>Damage Resistances</h4>
			<p>
			""")
			wfile.write (line [len ('damage resistances '):])
			wfile.write ("""			</p>
		</property-line>""")
		
		# Damage Immunities
		if 'damage immunities' in line.lower():
			wfile.write("""	
			
		<property-line>
			<h4>Damage Immunities</h4>
			<p>
			""")
			wfile.write (line [len ('damage immunities '):])
			wfile.write ("""			</p>
		</property-line>""")
		
		# Damage Vulnerabilities
		if 'damage vulnerabilities' in line.lower():
			wfile.write("""	
			
		<property-line>
			<h4>Damage Vulnerabilities</h4>
			<p>
			""")
			wfile.write (line [len ('damage vulnerabilities '):])
			wfile.write ("""			</p>
		</property-line>""")
		
		# Condition Immunities
		if 'condition immunities' in line.lower():
			wfile.write("""	
			
		<property-line>
			<h4>Condition Immunities</h4>
			<p>
			""")
			wfile.write (line [len ('condition immunities '):])
			wfile.write ("""			</p>
		</property-line>""")
		
		# Senses
		if 'senses' in line.lower():
			wfile.write("""	
			
		<property-line>
			<h4>Senses</h4>
			<p>
			""")
			wfile.write (line [len ('senses '):])
			wfile.write ("""			</p>
		</property-line>""")
		
		# Languages
		if 'languages' in line.lower():
			wfile.write("""	
			
		<property-line>
			<h4>Languages</h4>
			<p>
			""")
			wfile.write (line [len ('languages '):])
			wfile.write ("""			</p>
		</property-line>""")
	
		# Challenge - this marks the end of the top stats
		if 'challenge' in line.lower():
			wfile.write("""	
			
		<property-line>
			<h4>Challenge</h4>
			<p>
			""")
			wfile.write (line [len ('challenge '):])
			wfile.write ("""			</p>
		</property-line>
	</top-stats>""")
			return
	
# writeAbilities
# 	Function writes the abilities of the monster into the output file
def writeAbilities (rfile, wfile):
	while True:
		line = rfile.readline()
		if not line: print_ferror ('writeAbilities')
		
		# Ending condition is seeing the start of the Actions category
		if line.strip().lower() == 'actions' or line.strip().lower() == 'reactions':
			return
		elif line.strip().lower() == 'bestiary':
			return
			
		# Write valid properties into the output file
		line = line.split ('.', 1)
		
		# A valid property has a . to name the ability
		if len(line) > 1:
			wfile.write("""
			
	<property-block>
		<h4>
		""")
			
			wfile.write(line[0] + '.')
			
			wfile.write("""
		</h4>
		<p>""")
			
			wfile.write (line[1])
			
			wfile.write("""		</p>
	</property-block>""")
	
def writeActions (rfile, wfile):
	wfile.write ("""
	
	<h3>Actions</h3>""")

	while True:
		line = rfile.readline()
		if not line: return
		
		# Ending condition is seeing the start of the Legendary Actions Category
		if line.strip().lower() == 'legendary actions':
			writeLegendaryActions(rfile, wfile)
			return
		elif line.strip().lower() == 'bestiary':
			return
			
		# Adding in Reactions label
		if line.strip().lower() == 'reactions':
			wfile.write("""
			
	<h3>Reactions</h3>""")
		
		# Splitting off the name of the action
		line = line.split ('.')
		
		# A valid property has a . to name the ability
		if len(line) > 1:
			wfile.write("""
			
	<property-block>
		<h4>
		""")

			wfile.write (line[0] + '.')
			
			wfile.write("""
		</h4>
		<p>""")

			for i in range ( 1, len(line)):
				if line[i] != '\n' and line[i] != ' \n':
					if ':' in line[i] and line[0] != 'Multiattack':		# Make sure that the ability isn't multiattack
						italics = line[i].split(':', 1)					# Use ':' as condition to apply italics
						wfile.write ( '<i>' )							# Add start tag for HTML italics
						wfile.write (italics[0] + ':')					# Include the : that we removed before
						wfile.write ( '</i>' )							# Add end tag for HTML italics
						wfile.write (italics[1] + '.')					# Add in the '.' that we removed before
					else:
						wfile.write (line[i] + '.')
			
			wfile.write("""		
		</p>
	</property-block>""")
	
def writeLegendaryActions (rfile, wfile):
	wfile.write ("""
	
	<h3>Legendary Actions</h3>""")
	
	while True:
		line = rfile.readline()
		if not line: break
		
		# Ending condition is seeing the term 'bestiary'
		if line.strip().lower() == 'bestiary':
			return
			
		# Splitting off the name of the action
		line = line.split ('.', 1)
		
		# A valid property has a . to name the ability
		if len(line) > 1:
			wfile.write ("""
			
	<property-block>
		<p>""")
		
			wfile.write(line[0] + '.')
			wfile.write(line[1])
			
			wfile.write("""		</p>
	</property-block>""")
	
			break
	
	while True:
		line = rfile.readline()
		if not line: return
		
		# Ending condition is seeing the term 'bestiary'
		if line.strip().lower() == 'bestiary':
			return
		
		# Splitting off the name of the action
		line = line.split ('.', 1)
		
		# A valid property has a . to name the ability
		if len(line) > 1:
			wfile.write("""
			
	<property-block>
		<h4>
		""")
		
			wfile.write (line[0] + '.')
			
			wfile.write("""
		</h4>
		<p>""")
			
			wfile.write (line[1])
			
			wfile.write("""		</p>
	</property-block>""")
	
def writeClosing (wfile):
	wfile.write ("""
</stat-block>
""")
	
def genStatblock( monster_name, input_file ):
	if len(sys.argv) < 3:
		print ("Usage Error: genStatblock.py cannot run properly")
		print_usage_instructions()
		sys.exit()

	# According to the usage instructions, the monster name is the second argument
	#monster_name = sys.argv[1]				# Get the monster name from arguments

	# Convert periods to spaces
	monster_name = monster_name.replace ('.', ' ')

	# Capitalize the first letter of every word in monster name
	list = [word[0].upper() + word[1:] for word in monster_name.split()]
	monster_name = " ".join(list)

	# We will write statblock code into the monster file
	wfile = open (monster_name.lower() + ".html", 'a+')
	rfile = open (input_file, 'r')

	############################################################################
	# Writing the statblock code
	############################################################################

	writeCreatureHeading (monster_name, rfile, wfile)
	writeTopStats (rfile, wfile)
	writeAbilities (rfile, wfile)
	writeActions (rfile, wfile)
	writeClosing (wfile)

	# Close the files now that we are done
	rfile.close()
	wfile.close()
