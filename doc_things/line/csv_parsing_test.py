from csv_grammar_line import *
from csv_visitor import *
from arpeggio import ParserPython, visit_parse_tree


parser = ParserPython(csv, ws = '\t ', debug=True)

test_data = open('test_data.csv', 'r').read()

pars_tree = parser.parse(test_data)

restat = visit_parse_tree(pars_tree, CsvVisitor())

print(restat)