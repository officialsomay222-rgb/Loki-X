import re

with open("src/index.css", "r") as f:
    content = f.read()

content = content.replace('.awakened-logo-image {\n', '.awakened-logo-image {\n  border-radius: 25%;\n')

with open("src/index.css", "w") as f:
    f.write(content)
