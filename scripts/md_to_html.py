#!/usr/bin/env python3
import os
import sys
import markdown
import re
from datetime import datetime

def read_metadata(md_content):
    """Extract metadata from markdown front matter."""
    metadata = {}
    if md_content.startswith('---'):
        parts = md_content.split('---', 2)
        if len(parts) >= 3:
            for line in parts[1].strip().split('\n'):
                if ':' in line:
                    key, value = line.split(':', 1)
                    metadata[key.strip()] = value.strip()
            content = parts[2].strip()
        else:
            content = md_content
    else:
        content = md_content
    return metadata, content

def convert_md_to_html(md_file, template_file):
    """Convert markdown file to HTML using the template."""
    with open(md_file, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    metadata, content = read_metadata(md_content)
    html_content = markdown.markdown(content, extensions=['fenced_code', 'tables', 'toc'])
    
    with open(template_file, 'r', encoding='utf-8') as f:
        template = f.read()
    
    # Extract title from metadata or first heading
    title = metadata.get('title')
    if not title:
        title_match = re.search(r'# (.*)', content)
        title = title_match.group(1) if title_match else 'Blog Post'
    
    # Get date from metadata or file modification time
    date = metadata.get('date')
    if not date:
        date = datetime.fromtimestamp(os.path.getmtime(md_file)).strftime('%B %d, %Y')
    
    # Replace placeholders in template
    html = template.replace('{{title}}', title)
    html = html.replace('{{date}}', date)
    html = html.replace('{{content}}', html_content)
    
    # Generate output filename in the same directory
    basename = os.path.splitext(os.path.basename(md_file))[0]
    output_file = os.path.join(os.path.dirname(md_file), f'{basename}.html')
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f'Converted {md_file} to {output_file}')

def main():
    if len(sys.argv) != 3:
        print('Usage: python md_to_html.py <markdown_file> <template_file>')
        sys.exit(1)
    
    md_file = sys.argv[1]
    template_file = sys.argv[2]
    convert_md_to_html(md_file, template_file)

if __name__ == '__main__':
    main()