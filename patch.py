import re

with open("src/components/ChatInput.tsx", "r") as f:
    content = f.read()

target = """                <div className={`relative rounded-[32px] transition-all duration-500 ${isAwakened || effectInputBox ? 'p-[2px] shadow-[0_0_40px_rgba(0,242,255,0.3)]' : 'p-0 bg-transparent'}`}>
                  {(isAwakened || effectInputBox) && (
                    <div className="absolute inset-0 rounded-[32px] overflow-hidden pointer-events-none">
                      <div 
                        className="absolute top-1/2 left-1/2 w-[300%] sm:w-[250%] aspect-square -translate-x-1/2 -translate-y-1/2 animate-[spin_3s_linear_infinite]" 
                        style={{ background: 'conic-gradient(from 0deg at 50% 50%, transparent 0%, rgba(0, 242, 255, 0.4) 15%, #00f2ff 30%, transparent 30%, transparent 50%, rgba(189, 0, 255, 0.4) 65%, #bd00ff 80%, transparent 80%, transparent 100%)' }}
                      />
                      <div className="absolute inset-0 rounded-[32px] shadow-[inset_0_0_20px_rgba(0,242,255,0.5)] animate-pulse" style={{ animationDuration: '2s' }} />
                    </div>
                  )}
                  <div
                    className={`relative z-10 rounded-[30px] transition-all duration-500 flex flex-col p-2 sm:p-3 backdrop-blur-xl border-transparent shadow-sm dark:shadow-none ${
                      isAwakened || effectInputBox
                        ? `bg-white/60 dark:bg-[#050505]/90 transition-shadow duration-300 shadow-[inset_0_0_30px_rgba(0,242,255,0.1)] focus-within:shadow-[inset_0_0_50px_rgba(0,242,255,0.25)]`
                        : "bg-transparent"
                    } ${
                      isSuccessFlash
                        ? "shadow-[0_0_30px_rgba(255,255,255,0.5)] border-white/50"
                        : isRecording
                          ? "shadow-[0_0_20px_rgba(255,255,255,0.5)] animate-pulse border-white/50"
                          : ""
                    }`}
                  >"""

replacement = """                <div className={`relative rounded-[32px] transition-all duration-500 ${isAwakened || effectInputBox ? 'p-[2px] shadow-[0_0_40px_rgba(0,242,255,0.4)]' : 'p-[1px] bg-gradient-to-br from-slate-300 to-slate-200 dark:from-white/20 dark:to-white/5 shadow-md'}`}>
                  {(isAwakened || effectInputBox) && (
                    <div className="absolute inset-0 rounded-[32px] overflow-hidden pointer-events-none">
                      <div 
                        className="absolute top-1/2 left-1/2 w-[300%] sm:w-[250%] aspect-square -translate-x-1/2 -translate-y-1/2 animate-[spin_4s_linear_infinite]" 
                        style={{ background: 'conic-gradient(from 0deg at 50% 50%, #ff007a 0%, #bd00ff 25%, #00f2ff 50%, #bd00ff 75%, #ff007a 100%)', opacity: 0.9 }}
                      />
                      <div className="absolute inset-0 rounded-[32px] shadow-[inset_0_0_30px_rgba(0,242,255,0.6)] animate-[pulse_2s_ease-in-out_infinite]" />
                    </div>
                  )}
                  <div
                    className={`relative z-10 rounded-[30px] transition-all duration-500 flex flex-col p-2 sm:p-3 backdrop-blur-xl border border-transparent ${
                      isAwakened || effectInputBox
                        ? `bg-white/80 dark:bg-[#050505]/80 transition-shadow duration-300 shadow-[inset_0_0_40px_rgba(0,242,255,0.15)] focus-within:shadow-[inset_0_0_60px_rgba(0,242,255,0.3)]`
                        : "bg-white dark:bg-[#1E1F20] shadow-sm"
                    } ${
                      isSuccessFlash
                        ? "shadow-[0_0_30px_rgba(255,255,255,0.5)] border-white/50"
                        : isRecording
                          ? "shadow-[0_0_20px_rgba(255,255,255,0.5)] animate-pulse border-white/50"
                          : ""
                    }`}
                  >"""

if target in content:
    content = content.replace(target, replacement)
    with open("src/components/ChatInput.tsx", "w") as f:
        f.write(content)
    print("Success")
else:
    print("Target not found. Doing fuzzy search...")
