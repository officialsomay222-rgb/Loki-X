import re

with open("src/components/ChatInput.tsx", "r") as f:
    content = f.read()

# target: <img src={att.url} alt={`attachment-${index}`} className="w-full h-full object-cover" />
# replace with: <img src={att.data ? `data:${att.mimeType};base64,${att.data}` : att.url} alt={`attachment-${index}`} className="w-full h-full object-cover" />

target = '<img src={att.url} alt={`attachment-${index}`} className="w-full h-full object-cover" />'
replacement = '<img src={att.data ? `data:${att.mimeType};base64,${att.data}` : att.url} alt={`attachment-${index}`} className="w-full h-full object-cover" />'

if target in content:
    content = content.replace(target, replacement)
    with open("src/components/ChatInput.tsx", "w") as f:
        f.write(content)
    print("Success")
else:
    print("Target not found.")
