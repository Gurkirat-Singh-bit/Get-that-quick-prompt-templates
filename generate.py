#!/usr/bin/env python3
import re, os, json
from datetime import datetime

README = "engineering-prompts-main/README.md"
BASE = "/home/mavaligamerz/code/Personal/GetThatQuick-Templates"
NOW = "2026-03-01T00:00:00Z"

CATEGORY_MAP = {
    "1. Code Refactoring & Development": "development",
    "2. CI/CD & DevOps": "development/devops",
    "3. Database Management": "development/database",
    "4. Cloud & Kubernetes": "development/cloud",
    "5. Full-Stack Development": "development/fullstack",
    "6. UX/UI & Design": "creative/design",
    "7. Security & Authentication": "development/security",
    "8. Event-Driven Architecture & Integration": "development/architecture",
    "9. Content Creation & Marketing": "writing/marketing",
    "10. Infrastructure & System Administration": "development/infrastructure",
    "11. System Monitoring & Debugging": "development/debugging",
    "12. Web Development": "development/frontend",
    "13. API Development": "development/api",
    "14. AI/ML Integration": "development/ai-ml",
    "15. Testing & Quality Assurance": "development/testing",
    "16. Agentic AI": "development/ai-ml",
    "17. RAG Application Development": "development/ai-ml",
}

def slugify(title):
    s = title.lower().strip()
    s = re.sub(r'[^a-z0-9\s-]', '', s)
    s = re.sub(r'[\s]+', '-', s)
    s = re.sub(r'-+', '-', s)
    return s.strip('-')[:60]

def extract_variables(text):
    matches = re.findall(r'\{([^}]+)\}', text)
    seen = set()
    variables = []
    for m in matches:
        name = slugify(m).replace('-', '_')
        if name and name not in seen:
            seen.add(name)
            label = m.strip().replace('_', ' ').title()
            variables.append({"name": name, "label": label})
    return variables

def make_tags(title, category):
    words = re.sub(r'[^a-z0-9\s]', '', title.lower()).split()
    stop = {'a','an','the','for','and','or','in','on','to','of','with','using','from','after','how','set','up','based','create','build','implement','generate','write','provide','design','develop','integrate','explain','suggest','optimize','automate','configure','deploy','test'}
    tags = [w for w in words if w not in stop and len(w) > 2][:5]
    if len(tags) < 2:
        tags.append(category.split('/')[-1])
    return tags[:5]

def convert_prompt_to_system(text):
    text = text.strip().strip('"').strip()
    # Convert {var} to {{var}}
    text = re.sub(r'(?<!\{)\{([^{}]+)\}(?!\})', r'{{\1}}', text)
    # Clean variable names inside {{ }}
    def clean_var(m):
        inner = m.group(1).strip()
        name = re.sub(r'[^a-zA-Z0-9_ ]', '', inner).strip().replace(' ', '_').lower()
        return '{{' + name + '}}'
    text = re.sub(r'\{\{([^}]+)\}\}', clean_var, text)
    return text

def parse_readme(path):
    with open(path, 'r') as f:
        content = f.read()
    
    prompts = []
    current_category = "general"
    
    # Split by section headers
    lines = content.split('\n')
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Detect category headers like ### **1. Code Refactoring...**
        cat_match = re.match(r'^###\s+\*?\*?(\d+\.\s+.+?)\*?\*?\s*$', line)
        if cat_match:
            cat_name = cat_match.group(1).strip('* ')
            for key, val in CATEGORY_MAP.items():
                if key in cat_name or cat_name in key:
                    current_category = val
                    break
        
        # Detect prompt title like * **Title**
        title_match = re.match(r'^\*\s+\*\*(.+?)\*\*', line)
        if title_match:
            title = title_match.group(1).strip()
            # Find the next code block
            j = i + 1
            prompt_text = ""
            while j < len(lines):
                if lines[j].strip().startswith('```text') or lines[j].strip().startswith('```'):
                    if 'text' in lines[j] or (j > i and j < i + 5):
                        k = j + 1
                        block_lines = []
                        while k < len(lines) and not lines[k].strip().startswith('```'):
                            block_lines.append(lines[k])
                            k += 1
                        prompt_text = '\n'.join(block_lines).strip()
                        break
                elif re.match(r'^\*\s+\*\*', lines[j]) or lines[j].startswith('###') or lines[j].startswith('---'):
                    break
                j += 1
            
            if prompt_text:
                prompts.append({
                    'title': title,
                    'category': current_category,
                    'prompt': prompt_text
                })
        i += 1
    
    return prompts

def write_template(prompt_data, output_dir):
    title = prompt_data['title']
    category = prompt_data['category']
    raw_prompt = prompt_data['prompt']
    
    slug = slugify(title)
    if not slug:
        return
    
    body = convert_prompt_to_system(raw_prompt)
    variables = extract_variables(raw_prompt)
    tags = make_tags(title, category)
    
    # Build description
    desc_text = body.split('.')[0].strip()[:120]
    if not desc_text.endswith('.'):
        desc_text += '.'
    desc_text = desc_text.replace('"', "'")
    
    # Build frontmatter
    fm = f'---\n'
    fm += f'id: "{slug}"\n'
    fm += f'title: "{title}"\n'
    fm += f'description: "{desc_text}"\n'
    fm += f'category: "{category}"\n'
    fm += f'tags: {json.dumps(tags)}\n'
    
    if variables:
        fm += 'variables:\n'
        for v in variables:
            fm += f'  - name: "{v["name"]}"\n'
            fm += f'    label: "{v["label"]}"\n'
            fm += f'    required: true\n'
    
    fm += f'createdAt: "{NOW}"\n'
    fm += f'updatedAt: "{NOW}"\n'
    fm += f'---\n\n'
    
    # Rewrite as system prompt if needed
    if body.lower().startswith(("help me", "guide me", "teach me", "show me")):
        body = "You are an expert assistant. " + body
    
    full = fm + body + '\n'
    
    # Write to category subfolder
    cat_dir = os.path.join(output_dir, "templates", category.replace('/', os.sep))
    os.makedirs(cat_dir, exist_ok=True)
    
    filepath = os.path.join(cat_dir, f"{slug}.md")
    # Handle duplicates
    counter = 1
    while os.path.exists(filepath):
        filepath = os.path.join(cat_dir, f"{slug}-{counter}.md")
        counter += 1
    
    with open(filepath, 'w') as f:
        f.write(full)
    
    return filepath

def main():
    prompts = parse_readme(os.path.join(BASE, README))
    print(f"Found {len(prompts)} prompts")
    
    for p in prompts:
        fp = write_template(p, BASE)
        if fp:
            print(f"  -> {os.path.relpath(fp, BASE)}")
    
    print(f"\nDone! Generated {len(prompts)} templates.")

if __name__ == '__main__':
    main()
