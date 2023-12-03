# md-to-anki

Takes Markdown files and turns then into Anki Decks

## Install

In order to install this package, type the following into the command line:

```console
$ python3 setup.py install --user
```

## Usage

Invoking the command is as simple as:

```console
$ md-to-anki PATH_TO_MARKDOWN.md PATH_TO_NEW_DECK.apkg
```

You specify a Markdown file as an input and the desired name of the Anki package
as the output.

### Markdown Formatting

```markdown
# Deck Title 1

## Card Name 1

Card content
```

