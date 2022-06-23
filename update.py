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

        # Only convert published datas, else ignore.
        if data.get('status') != 'published':
            continue

        # Convert the body to HTML
        # Add the html to the data dictionary
        # Add the data dictionary to the items list
        data['content'] = markdown(body, extensions=['tables', 'codehilite', 'fenced_code'])
        data['slug'] = page.replace('.md', '.html')
        items.append(data)

        # Load the template and write html file
        env = Environment(
            loader=PackageLoader('update'),
            autoescape=select_autoescape()
        )


        blog_template = env.get_template('page.html')
        blog = blog_template.render(data)

        with open(os.path.join('site', data['slug']), "w") as f:
            f.write(blog)

    index_template = env.get_template('index.html')
    index = index_template.render({'items': items})
    with open("site/index.html", "w") as f:
        f.write(index)


if __name__ == '__main__':
    update()

