import sys
import re

# Beginning of the HTML, goes up to where new elements are inserted
HTML_START = """
<!DOCTYPE html>

<!-- Changes you make to this file will not be reviewed by the grader -->

<html lang="en">
	<head>
		<title>My Markdown</title>
		<meta charset="utf-8">
		<link href="style.css" rel="stylesheet">
	</head>

	<body>
"""

# End of the html, goes from where inserts end, to where the true end is
HTML_END = """
	</body>
</html>
"""


def main():
    new_page = HTML_START + getMarkdownString(sys.argv[1]) + HTML_END

    # This means a save file was given
    if len(sys.argv) == 3:
        with open(sys.argv[2], "w+") as output_file:
            output_file.write(new_page)
    else:
        print(new_page)


# Converts the input markdown file into a string
def getMarkdownString(filename):
    all_lines = []
    
    # Read all lines from markdown into our array
    with open(filename) as f:
        all_lines = f.readlines()
    
    # Now to manipulate the lines
    output = ""
    in_code_block = False
    
    for index, line in enumerate(all_lines):
        
        # Saving original line for code blocks
        original_line = line
        # Strip leading whitespace
        line = line.lstrip()
        if len(line) == 0:
            continue

        
        # Checking for code blocks
        if line == '```':
            output += '<code>' if in_code_block else '</code>'
            in_code_block = not in_code_block
        
        # If we are in a code block just add whatever is there
        elif in_code_block:
            output += line

        # Check for headers
        elif line[0] == '#' and not in_code_block:
            header_count = 0
            # Count the header number
            for character in line:
                if character == '#':
                    header_count += 1
                else:
                    break
            output += f"<h{header_count}>{line[header_count:]}</h{header_count}>"
        
        # Checking for ordered lists
        elif is_ol_element(line):
            if (index - 1 < 0 or not is_ol_element(all_lines[index - 1])):  # First element of a list
                output += "<ol>"
            output += f"<li>{line[2:]}</li>"  # Remove the number and dot, then create an li with it
            if (index + 1 >= len(all_lines) or not is_ol_element(all_lines[index + 1])):
                output += "</ol>"  # If this was the last li in the section, close off the ol
    
        # Checking for unordered lists
        elif is_ul_element(line):
            if (index - 1 < 0 or not is_ul_element(all_lines[index - 1])):  # First element of a list
                output += "<ul>"
            output += f"<li>{line[1:]}</li>"  # Remove the number and dot, then create an li with it
            if (index + 1 >= len(all_lines) or not is_ul_element(all_lines[index + 1])):
                output += "</ul>"  # If this was the last li in the section, close off the ul
    

    
        # Everything else has been tried, so just make a <p>
        else:
            output += f"<p>{line}</p>"

    # Return the output at the end
    return output

# Returns true if the given line matches an ordered list element
def is_ol_element(line):
    line = line.lstrip()
    return len(line) > 1 and line[0].isnumeric() and line[1] == '.'


# Returns true if the given line matches an unordered list element
def is_ul_element(line):
    line = line.lstrip()
    return len(line) > 1 and line[0] == "*"



if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("No files were specified")
        exit()
    main()
