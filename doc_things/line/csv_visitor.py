from arpeggio import PTNodeVisitor

class CsvVisitor(PTNodeVisitor):

    def visit_csv(self, node, children):
        par_list = []
        for child in children :
            par_list.append(child)
        return par_list
    
    def visit_record(self, node, children):
        in_list = []
        for child in children :
            in_list.append(child)
        return in_list
    
    def visit_field(self, node, children):
        return node.value
    
    
