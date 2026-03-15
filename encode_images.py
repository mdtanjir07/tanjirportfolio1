import base64
import re
import os
import mimetypes

html_path = 'c:/Users/mdasa/Downloads/Md_Asad_Iqbal_Portfolio/index.html'

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

def replace_with_b64(match):
    src = match.group(1)
    if src.startswith('http') or src.startswith('data:'):
        return match.group(0)
    
    img_path = os.path.join(os.path.dirname(html_path), src.replace('/', os.sep))
    if os.path.exists(img_path):
        mime_type, _ = mimetypes.guess_type(img_path)
        if not mime_type:
            mime_type = 'image/png'
        with open(img_path, 'rb') as img_f:
            b64_data = base64.b64encode(img_f.read()).decode('utf-8')
        return f'src="data:{mime_type};base64,{b64_data}"'
    return match.group(0)

# Replace <img src="...">
content = re.sub(r'src="([^"]+)"', replace_with_b64, content)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Images encoded successfully.")
