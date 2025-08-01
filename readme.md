# **The `.tear` File Format**
**Text-based archive format for humans**

> [!CAUTION]
> Please, don't use it yet. The format is highly unstable and might drastically change at any moment.

The `.tear` (**Te**xt **Ar**chive) file format is a simple, human-readable way to bundle multiple text files (scripts, configs, texts) into a single file while maintaining readability and ease of editing.
This format has been under development since November 2020, evolving through multiple name changes and structural refinements as it progressed toward its current form.

The format was created with following goals:
- be trivial enough to create and edit manually in a text editor.
- be powerful enough to be used as general archive format.
- support symbolic links, binary files and some metadata.
- diff nicely in git history and code reviews.

## **Example `.tear` File**
```shell
#!/usr/bin/env tear
=index.html/t
<!doctype html>
<html lang="en-US">
  <head>
    <meta charset="utf-8" />
    <title>Some web page</title>
    <link rel="stylesheet" href="style.css" />
  </head>
  <body>
    <p>Bulbalka Red</p>
  </body>
</html>
=@

=style.css/t
html, body {
  color-scheme: dark light;
}
=@

=server.sh/s
#!/bin/sh
SCRIPT_DIR="$(dirname "$(readlink -f "$0")")"
python3 -m http.server -d "$SCRIPT_DIR" 8000
=@
```

## **Tools & Libraries**
| Language | Library |
|----------|---------|
| TODO     | `TODO`  |
| TODO     | `TODO`  |

## **Specification**
### TODO
TODO

## **Usage Examples**
### TODO
TODO

## **Alternatives**
There is txtar, which is far simpler format with similar goals. It can't store symbolic links, file modes, filenames with spaces and other exotic things, but it is easier to read and edit manually. Also it has good support by many libraries for different programming languages. 
[txtar golang package](https://pkg.go.dev/golang.org/x/tools/txtar) 
[txtar Rust crate](https://crates.io/crates/txtar) 
[txtar Zig package](https://abhinav.github.io/txtar.zig/)
