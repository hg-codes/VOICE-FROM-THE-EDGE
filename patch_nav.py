import os

target_files = [
    'ektara_detailed_labeling.html',
    'ektara_explorer.html',
    'kinnera_3d_explorer.html',
    'kinnera_spatial_story.html',
    'kinnera_vs_world.html',
    'villu_pattu_explorer.html',
    'vanishing_forms_dashboard.html'
]

injection = """
<!-- INJECTED BACK NAVIGATION -->
<div id="exhib-back-btn" style="position:fixed; top:20px; left:20px; z-index:999999;">
<a href="index.html" style="background:rgba(15,10,25,0.75); border:1px solid rgba(232,161,0,0.3); color:#F5ECD7; text-decoration:none; padding:8px 16px; border-radius:100px; font-family:sans-serif; font-size:0.85rem; font-weight:500; backdrop-filter:blur(10px); -webkit-backdrop-filter:blur(10px); display:flex; align-items:center; gap:8px; box-shadow:0 4px 20px rgba(0,0,0,0.5); transition:all 0.3s ease; text-transform:uppercase; letter-spacing:0.1em;" onmouseover="this.style.background='rgba(232,161,0,0.25)'; this.style.borderColor='#E8A100';" onmouseout="this.style.background='rgba(15,10,25,0.75)'; this.style.borderColor='rgba(232,161,0,0.3)';">
   <span style="font-size:1.2em; margin-top:-2px;">&#10229;</span> Exhibition Hub
</a>
</div>
"""

count = 0
for f in target_files:
    if os.path.exists(f):
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Don't inject twice
        if 'id="exhib-back-btn"' not in content:
            # inject right after <body> or <body ...>
            body_idx = content.find('<body')
            if body_idx != -1:
                close_bracket = content.find('>', body_idx)
                if close_bracket != -1:
                    new_content = content[:close_bracket+1] + injection + content[close_bracket+1:]
                    with open(f, 'w', encoding='utf-8') as file:
                        file.write(new_content)
                    print(f'Patched: {f}')
                    count += 1
            else:
                print(f'Error: <body> tag not found in {f}')
        else:
            print(f'Already patched: {f}')
    else:
        print(f'File not found: {f}')

print(f'\nTotal files patched: {count}')
