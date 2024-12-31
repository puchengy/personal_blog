# My Personal Blog

This is my personal blog hosted using GitHub Pages. Visit the blog at [username.github.io/repository-name].

## About

This blog is built using HTML and CSS, hosted directly on GitHub Pages.

## Writing New Posts

1. Create a new markdown file in the `posts/markdown/` directory with a `.md` extension.
2. Add YAML front matter at the top of your markdown file:
   ```yaml
   ---
   title: Your Post Title
   date: Month DD, YYYY
   ---
   ```
3. Write your post content in markdown format below the front matter.
4. Run the conversion script to generate the HTML:
   ```bash
   python3 scripts/md_to_html.py posts/markdown/your-post.md templates/post.html
   ```

### Markdown Features Supported

- Headers (# to ######)
- Bold and italic text (**bold**, *italic*)
- Lists (ordered and unordered)
- Links and images
- Code blocks (fenced with ```)
- Tables
- Blockquotes
- Horizontal rules

### Example Post Structure

```markdown
---
title: My Example Post
date: January 1, 2024
---

# My Example Post

This is a paragraph with **bold** and *italic* text.

## Subheading

- List item 1
- List item 2
  - Nested item

### Code Example

```python
def hello_world():
    print("Hello, World!")
```

For more information about markdown syntax, visit [Markdown Guide](https://www.markdownguide.org/basic-syntax/).