import os
import glob
import shutil
from jinja2 import Environment, PackageLoader, select_autoescape
from markdown import markdown
from datetime import datetime


def move_images():
    '''
    Move images to the 'images' directory
    '''
    # Get all images in the 'pages' directory
    exts = ('jpg', 'png', 'gif')
    images = []
    for ext in exts:
        images.extend(glob.glob(f'pages/**/*.{ext}', recursive=True))
    print(f'Found {len(images)} images')

    # Copy images to the 'images/blog' directory
    for image in images:
        dest = os.path.join('images', 'blogs', os.path.basename(image))
        shutil.copy(image, dest)





def move_markdown():
    '''
    Convert published markdown files to html files
    Iterate over all the markdown files in the 'pages' directory
    For each markdown file,
    1. Read in the markdown file
    2. Parse out the content and metadata
    2. Create a dictionary containing content and metadata
    4. Output to html as blog page and to the index page
    '''

    # Get all markdown files in the 'pages' directory
    pages = glob.glob('pages/**/*.md', recursive=True)
    print(f'Found {len(pages)} markdown files')


    items = []
    for page in pages:

        print(f"Processing{os.path.basename(page):.>40}", end = '')
        # Read in markdown
        with open(page, "r", encoding='utf-8') as f:
            md = f.read()

        # Split the metadata and body
        meta, body = md.strip().split('\n\n', maxsplit=1)

        # Replace image paths
        body = body.replace('images/', '/images/blogs/')



        # Create a dictionary of metadata
        if ':' not in meta:
            raise ValueError(
                'Metadata must be in "key:value" format. Got "{}"'.format(meta))

        data = {item.split(':')[0].strip(): item.split(':')[1].strip()
                for item in meta.split('\n')}
        
        # Only convert published datas, else ignore.
        if data.get('status') != 'published':
            print(f"{'Not published':.>40}")
            continue
        


        # The list of extensions are available here https://python-markdown.github.io/extensions/
        extensions = ['codehilite', 'toc', 'extra', 'admonition'] 
        # Use `pip install pymdown-extensions` for extras - https://facelessuser.github.io/pymdown-extensions/
        extensions += ['pymdownx.tilde', 'pymdownx.emoji']
        # Convert the body to HTML and add to data dictionary
        data['content'] = markdown(body, extensions=extensions)


        # Add the path to blog
        folder = data.get('category', 'blog')
        if 'url' in data:
            data['url'] = os.path.join(folder, data['url'] + '.html')
        else:
            data['url'] = os.path.join(folder, os.path.basename(page).replace('.md', '.html'))

        # Set defaults
        data.setdefault('category', 'miscellaneous')
        data.setdefault('author', 'Philip')
        data.setdefault('date', datetime.today())
        # Convert date to date type object
        data['date'] = datetime.strptime(data['date'], '%Y-%m-%d')

        # Add the data dictionary to the items list
        items.append(data)

        # Load the template and write html file
        env = Environment(
            loader=PackageLoader('update'),
            autoescape=select_autoescape()
        )


        blog_template = env.get_template('page.html')
        blog = blog_template.render(data)

        # Create category folder
        if not os.path.exists(folder):
            os.mkdir(folder)

        # Write the html file
        with open(data['url'], "w", encoding='utf-8') as f:
            f.write(blog)
            print(f"{'Published':.>40}")

    index_template = env.get_template('index.html')
    index = index_template.render({'items': items})
    with open("index.html", "w", encoding='utf-8') as f:
        f.write(index)


if __name__ == '__main__':
    move_images()
    move_markdown()

