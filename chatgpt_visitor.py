from arpeggio import PTNodeVisitor


class CalcVisitor(PTNodeVisitor):
    def __init__(self, parser, debug=False):
        super().__init__(parser, debug=debug)

    def visit_number(self, node, children):
        return float(node.value)

    def visit_factor(self, node, children):
        if len(children) == 1:
            return float(children[0])
        sign = -1 if children[0] == '-' else 1
        return float(sign * children[-1])

    def visit_term(self, node, children):
        if len(children) == 1:
            return float(children[0])
        child = self.visit(children[0])
        if children[1] == '*':
            return float(child * self.visit(children[-1]))
        if children[1] == '/':
            return float(child / self.visit(children[-1]))

    def visit_expression(self, node, children):
        terms = self.visit(children[0])
        n = len(children) // 2
        for i in range(0, n):
            if children[2*i+1] == '+':
                terms += self.visit(children[2*i + 2])
            if children[2*i+1] == '-':
                terms -= self.visit(children[2*i + 2])
        return float(terms)
