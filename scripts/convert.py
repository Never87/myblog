import os
import markdown
from pathlib import Path

# 配置路径
POSTS_DIR = Path("posts")
PUBLIC_DIR = Path("public")
TEMPLATE = Path("templates/post.html").read_text()

# 清空输出目录
os.makedirs(PUBLIC_DIR, exist_ok=True)

# 遍历所有 Markdown 文件
for md_file in POSTS_DIR.glob("*.md"):
    # 转换为 HTML
    html_content = markdown.markdown(md_file.read_text())
    # 插入模板
    final_html = TEMPLATE.replace("{{content}}", html_content)
    # 保存为 HTML
    output_path = PUBLIC_DIR / f"{md_file.stem}.html"
    output_path.write_text(final_html)