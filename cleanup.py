import os
import sys

def remove_links(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    # Find the start and end of the YAML configuration block
    start_index, end_index = 0, 0
    for i, line in enumerate(lines):
        if line.strip() == '---':
            if start_index == 0:
                start_index = i
            else:
                end_index = i
                break

    # Remove links from lines outside the YAML block
    new_lines = lines[:start_index+1]
    for line in lines[start_index+1:]:
        if line.strip() == '---':
            break
        link_start = line.find('[[')
        while link_start != -1:
            link_end = line.find(']]', link_start)
            link_text = line[link_start+2:link_end].split('|')[-1]
            line = line[:link_start] + link_text + line[link_end+2:]
            link_start = line.find('[[')

        if line.strip() != '':
            new_lines.append(line +"\n")

    # Remove any extra newline characters from the end of the file
    if new_lines and new_lines[-1].strip() == '':
        new_lines.pop()

    # Write the modified content to a temporary file
    with open(filename + '.tmp', 'w') as f:
        f.writelines(new_lines)

    # Replace the old file with the temporary file
    os.remove(filename)
    os.rename(filename + '.tmp', filename)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python remove_links.py <filename>')
        sys.exit(1)
    remove_links(sys.argv[1])
