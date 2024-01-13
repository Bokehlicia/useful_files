## File organizer

Keep clean your directories with this little python script **file_organizer.py**.

### Create a directory

```py
program_dir = os.path.join(current_directory, "programs")
```

### Add extensions

```py
program_extensions = [".exe", ".msi", ".app", ".deb"]
```

### Move files into program directory

```py
shutil.move(file, os.path.join(music_dir, file))
    elif extension in program_extensions:
```

## Website dev directories and files structure

Create a nice Web Dev structure for your directories and files in one click **wb_structure.py**.

### Directory and files structure example

```py
project_structure = {
        '.gitignore': ignore_content, #.gitignore file created
        'index.html': html_content,  #index.html file created
        'css': {}, #css directory created
        'scss': { #scss directory created
            'main.scss': scss_content, #main.scss file created
            'base': { #base directory created
                '_mixin.scss': '', #_mixin.scss file created
                '_placeholder.scss': '', #and so on...
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
```
