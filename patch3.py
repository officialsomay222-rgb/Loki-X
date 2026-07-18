import re

with open("src/App.tsx", "r") as f:
    content = f.read()

target = """                  <div className="w-full h-full rounded-full overflow-hidden z-[2] border-2 border-white dark:border-[#08080c] relative">
                    <img
                      src="/logo.png"
                      className="w-full h-full object-cover"
                      alt="Commander"
                    />
                  </div>"""

replacement = """                  <div className="w-full h-full rounded-full overflow-hidden z-[2] border-2 border-white dark:border-[#08080c] relative">
                    <img
                      src={avatarUrl || "/logo.png"}
                      className="w-full h-full object-cover"
                      alt="Commander"
                    />
                  </div>"""

if target in content:
    content = content.replace(target, replacement)
    with open("src/App.tsx", "w") as f:
        f.write(content)
    print("Success")
else:
    print("Target not found.")
