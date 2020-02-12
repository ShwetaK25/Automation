############################XML Parsing######################
To find root of a XML


>>> path="S:\\NGP\\TeamMembers\\Shweta\\practise.xml"
>>> import xml.etree.ElementTree as ET
>>> tree = ET.parse(path)
>>> root = tree.getroot()
>>> print root



###################To find all child elements of a root############
>>> for child in root:
	print child.tag


####################################To find all attributes of child elements
for child in root:
	print child.attrib

#####################################To find child of child elements######
root[0][1].text


########To find all attibutes having same tag#######Iter###############
for m in root.iter('neighbor'):
	print m.attrib




################Find All/find##################
for m in root.findall('country'):
	rank = m.find('rank').text
	name = m.get('name')
	print name, rank



###############Modifying XML###############
for rank in root.iter('rank'):
...   new_rank = int(rank.text) + 1
...   rank.text = str(new_rank)
...   rank.set('updated', 'yes')



>>> tree.write('S:\\NGP\\TeamMembers\\Shweta\\practise.xml')


########################Element.remove################
for country in root.findall('country'):
...   rank = int(country.find('rank').text)
...   if rank > 50:
...     root.remove(country)


>>> tree.write('S:\\NGP\\TeamMembers\\Shweta\\practise.xml')


###################################