# keep-to-json

A script to convert Google Keep notes from Google Takeout into a single json file, for Linux, Mac, and Windows.
Forked from https://github.com/erikelisath/keep-to-markdown

**Requirements**

- Python 3.x
- Google Takeout notes (See [How to download your Google data](https://support.google.com/accounts/answer/3024190))

**Example**

```
> python keep-to-markdown.py -i Takeout/Keep/

arguments:
  -i PATH       Relative path to the Google Keep data folder

optional arguments:
  -h, --help    Show this help message and exit
```

The script outputs to a file `exported_notes.json`. Images will be stored in `notes/resources`.

Export format: 
```typescript
{
  title: string,
  content: string,
  labels: string[]
}[]
```
