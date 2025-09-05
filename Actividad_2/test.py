import sys
from antlr4 import *
from WhileLangLexer import WhileLangLexer
from WhileLangParser import WhileLangParser


code = """
i = 0;
while (i < 10) {
  if (i == 5) {
    break;
  }
  i = i + 1;
  continue;
}
"""


input_stream = InputStream(code)


lexer = WhileLangLexer(input_stream)
tokens = CommonTokenStream(lexer)


parser = WhileLangParser(tokens)
tree = parser.program()



tokens.fill()
print("## 🔤 TOKENS")
for token in tokens.getTokens(0, len(tokens.tokens) - 1):
    print(f"  - {lexer.symbolicNames[token.type]} ('{token.text}') @line {token.line}:{token.column}")



print("\n## 🌳 ÁRBOL SINTÁCTICO (toStringTree)")
print(tree.toStringTree(recog=parser))


def print_tree(node, indent=0):
    if node.getChildCount() == 0:
        print("  " * indent + f"TOKEN({node.getText()})")
    else:
        print("  " * indent + type(node).__name__.replace("Context",""))
        for i in range(node.getChildCount()):
            print_tree(node.getChild(i), indent + 1)

print("\n## 🌲 ÁRBOL SINTÁCTICO (Indentado)")
print_tree(tree)
