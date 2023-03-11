# Sunse

![](https://img.shields.io/pypi/v/sunse)
![](https://img.shields.io/pypi/pyversions/sunse)
![](https://img.shields.io/github/issues/wirehaiku/Sunse)
![](https://img.shields.io/github/license/wirehaiku/Sunse)

**Sunse** (*Stephen's Unseen Servant*, pronounced *sun·zee*) is a plaintext command-line note manager, written in Python 3.10.

Give Sunse a directory full of text files and it'll give you a complete management CLI, allowing you to read and manipulate your notes with ease.

```bash
# List all your files:
$ sunse list
future-projects
groceries
party-guest-list

# Show their contents:
$ sunse show party-guest-list
- Todd Chavez
- Princess Carolyn
- Diane Nguyen
- Mr. Peanutbutter (why)

# And manipulate them in all kinds of ways:
$ sunse append groceries vodka
$ sunse delete future-projects
$ sunse edit party-guest-list --command="vim -y"
```

## Installation

You can install Sunse from PyPi...

```
pip install sunse
```

...or download a build from the [latest release][bugs].

## Configuration

Sunse requires two environment variables to operate:

- Set `SUNSE_DIR` to the path of your notes directory:

```fish
set SUNSE_DIR "~/path/to/notes"
```

- Set `SUNSE_EXT` to the file extension your notes use:

```fish
set SUNSE_EXT ".txt"
```

That's it! That's all you need.

## Usage

Run `sunse --help` to see interactive help for all commands.

### List all notes

Use `sunse list` to list all existing note files in your directory (in alphabetical order):

```fish
$ sunse list
future-projects
groceries
party-guest-list
```

## Contributions

- Please submit all bug reports and feature suggestions to the [issue tracker][bugs].
- Run `pip install sunse[test]` to install additional testing dependencies.

[bugs]: https://github.com/wirehaiku/Sunse/issues
[rels]: https://github.com/wirehaiku/Sunse/releases
