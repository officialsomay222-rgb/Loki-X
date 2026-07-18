import re

with open("src/index.css", "r") as f:
    content = f.read()

# Replace mask-image with border-radius for aura and shine
content = re.sub(r'-webkit-mask-image:\s*url\("/logo\.png"\);', 'border-radius: 25%;', content)
content = re.sub(r'mask-image:\s*url\("/logo\.png"\);', 'border-radius: 25%;', content)
content = re.sub(r'-webkit-mask-size:\s*contain;', 'overflow: hidden;', content)
content = re.sub(r'mask-size:\s*contain;', '', content)
content = re.sub(r'-webkit-mask-repeat:\s*no-repeat;', '', content)
content = re.sub(r'mask-repeat:\s*no-repeat;', '', content)
content = re.sub(r'-webkit-mask-position:\s*center;', '', content)
content = re.sub(r'mask-position:\s*center;', '', content)

with open("src/index.css", "w") as f:
    f.write(content)
