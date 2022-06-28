# %%
import os
import sys
from jinja2 import Environment, PackageLoader, select_autoescape
from markdown import markdown


def update():
    '''
    Convert published markdown files to html files
    Iterate over all the markdown files in the 'pages' directory
    For each markdown file,
    1. Read in the file
    2. Split the content into metadata and body
    '''

    items = []

    pages = os.listdir('pages')
    for page in pages:
        print(f'Reading page {page}')
        with open(os.path.join('pages', page), "r") as f:
            md = f.read()

        # Split the metadata and body
        meta, body = md.strip().split('\n\n', maxsplit=1)

        # Create a dictionary of metadata
        if ':' not in meta:
            raise ValueError(
                'Metadata must be in "key:value" format. Got "{}"'.format(meta))

        data = {item.split(':')[0].strip(): item.split(':')[1].strip()
                for item in meta.split('\n')}
        print(data)
        # Only convert published datas, else ignore.
        if data.get('status') != 'published':
            continue

        # Convert the body to HTML
        # Add the html to the data dictionary
        data['content'] = markdown(body, extensions=['tables', 'codehilite', 'fenced_code'])
        # Add the path to blog
        data['url'] = os.path.join('blog', page.replace('.md', '.html'))
        # data.setdefault('category', 'other')
        # Add the data dictionary to the items list
        items.append(data)

        # Load the template and write html file
        env = Environment(
            loader=PackageLoader('update'),
            autoescape=select_autoescape()
        )


        blog_template = env.get_template('page.html')
        blog = blog_template.render(data)

        with open(data['url'], "w") as f:
            f.write(blog)

    index_template = env.get_template('index.html')
    index = index_template.render({'items': items})
    with open("index.html", "w") as f:
        f.write(index)


if __name__ == '__main__':
    update()

