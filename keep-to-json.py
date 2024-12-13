import os
import sys
import platform
import glob
import json
from datetime import datetime as dt
import argparse

def clean_title(title) -> str:
    ostype = platform.system()
    if ostype == 'Linux':
        title = title.replace('/', '_')
    elif ostype == 'Darwin':
        title = title.replace(':', ' ')
        title = title.replace('\\', '_').replace('/', '_').replace('|', '_')
    elif ostype == 'Windows':
        title = title.replace('\\', '_').replace('/', '_').replace('|', '_')
        title = title.replace('<', '-').replace('>', '-').replace(':', ' ')
        title = title.replace('?', '').replace('"', '').replace('*', '')
        title = title.replace('\n', '')
    return title

def format_tags(tags):
    return tags

def read_write_notes(args):
    path = args.i
    jsonpath = os.path.join(path, '')
    notes = glob.glob(f'{jsonpath}*.json')

    all_notes = []

    for note in notes:
        with open(note, 'r', encoding='utf-8') as jsonfile:
            data = json.load(jsonfile)
            title = data.get('title', 'Untitled')
            content = data.get('textContent', '')
            labels = [label['name'] for label in data.get('labels', [])]

            cleaned_title = clean_title(title)

            all_notes.append({
                'title': cleaned_title,
                'content': content,
                'labels': labels
            })

    output_file = os.path.join(os.getcwd(), 'exported_notes.json')
    with open(output_file, 'w', encoding='utf-8') as outfile:
        json.dump(all_notes, outfile, ensure_ascii=False, indent=4)

    print(f'Exported notes to {output_file}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Converting Google Keep notes to a single JSON file.')
    parser.add_argument('-i', metavar='PATH', required=True, help='The path to the Takeout folder.')
    args = parser.parse_args()

    try:
        read_write_notes(args)
    except Exception as e:
        print(f'An error occurred: {e}')
