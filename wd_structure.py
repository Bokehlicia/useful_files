import os

# Content ignored with .gitignore file
ignore_content = """/scss"""

# Content inside the index.html file
html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    
</body>
</html>"""

# Reset all
reset_content = """// SCSS Reset

// Reset box model
html, body, div, span, applet, object, iframe,
h1, h2, h3, h4, h5, h6, p, blockquote, pre,
a, abbr, acronym, address, big, cite, code,
del, dfn, em, img, ins, kbd, q, s, samp,
small, strike, strong, sub, sup, tt, var,
b, u, i, center,
dl, dt, dd, ol, ul, li,
fieldset, form, label, legend,
table, caption, tbody, tfoot, thead, tr, th, td,
article, aside, canvas, details, embed,
figure, figcaption, footer, header, hgroup,
menu, nav, output, ruby, section, summary,
time, mark, audio, video {
    margin: 0;
    padding: 0;
    border: 0;
    font-size: 100%;
    font: inherit;
    vertical-align: baseline;
}

// Reset HTML5 display-role for older browsers
article, aside, details, figcaption, figure,
footer, header, hgroup, menu, nav, section {
    display: block;
}

// Reset body line-height
body {
    line-height: 1;
}

// Remove list styles
ol, ul {
    list-style: none;
}

// Remove quotes from blockquote and q
blockquote, q {
    quotes: none;
}

blockquote:before, blockquote:after,
q:before, q:after {
    content: '';
    content: none;
}

// Reset table layout
table {
    border-collapse: collapse;
    border-spacing: 0;
}"""

# Content inside the main.scss file
scss_content = """@import "./base/mixin.scss";
@import "./base/placeholder.scss";
@import "./base/reset.scss";
@import "./base/variable.scss";"""

def create_web_dev_structure(project_name):
    # Define the project structure
    project_structure = {
        '.gitignore': ignore_content,
        'index.html': html_content,
        'css': {},
        'scss': {
            'main.scss': scss_content,
            'base': {                
                '_mixin.scss': '',
                '_placeholder.scss': '',
                '_reset.scss': reset_content,
                '_variable.scss': ''
            }
        },
        'js': {
            'main.js': ''
        },
        'img': {},
        'fonts': {},
        'html': {
            'about.html': html_content,
            'contact.html': html_content
        },
    }

    # Create the project folder
    project_path = os.path.join(os.getcwd(), project_name)
    os.makedirs(project_path)

    # Recursively create folders and files
    create_folders_and_files(project_structure, project_path)

def create_folders_and_files(structure, current_path):
    for item, content in structure.items():
        item_path = os.path.join(current_path, item)

        if isinstance(content, dict):
            # Create folder
            os.makedirs(item_path)
            # Recursively create contents
            create_folders_and_files(content, item_path)
        else:
            # Create file
            with open(item_path, 'w') as file:
                file.write(content)

# Example usage:
project_name = 'my_web_project'
create_web_dev_structure(project_name)