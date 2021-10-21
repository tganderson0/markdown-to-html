import sys
import re



def main():
    new_page = HTML_START + getMarkdownString(sys.argv[1]) + HTML_END

    # This means a save file was given
    if len(sys.argv) == 3:
        with open(sys.argv[2], "w+") as output_file:
            output_file.write(new_page)
        print("\033[32m" + f"Saved file to {sys.argv[2]}" + "\033[0m")
    else:
        print(new_page)


# Converts the input markdown file into a string
def getMarkdownString(filename):
    all_lines = []
    list_stack = []

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
            if in_code_block:
                output += '<br>'
            elif len(list_stack) > 0:
                output += list_stack.pop(0)
            continue

        
        # Checking for code blocks
        if re.search("```", line):
            output += '</code></div>' if in_code_block else '<div class="code_block"><code>'
            in_code_block = not in_code_block
        
        # If we are in a code block just add whatever is there
        elif in_code_block:
            output += f"<br>{line}"

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
            if (index - 1 < 0 or not is_ol_element(all_lines[index - 1])) and line[0] == "1":  # First element of a list
                output += "<ol>"
                list_stack.insert(0, "</ol>") # Adds a closer for the ol to the stack, used for nested lists
            output += f"<li>{line[2:]}</li>"  # Remove the number and dot, then create an li with it
            if (index + 1 >= len(all_lines)):
                output += "</ol>"  # If this was the last li in the section, close off the ol
    
        # Checking for unordered lists
        elif is_ul_element(line):
            if (index - 1 < 0 or not is_ul_element(all_lines[index - 1])):  # First element of a list
                output += "<ul>"
                list_stack.insert(0, "</ul>")  # Adds a closer for the ul to the stack, used for nested lists
            output += f"<li>{line[1:]}</li>"  # Remove the number and dot, then create an li with it
            if (index + 1 >= len(all_lines)):
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


#####################################
# Constants
#####################################

# Beginning of the HTML, goes up to where new elements are inserted
HTML_START = """
<!DOCTYPE html>

<html lang="en">
	<head>
		<title>My Markdown</title>
		<meta charset="utf-8">
		<link href="autostyle.css" rel="stylesheet">
	</head>

	<body>
"""

# End of the html, goes from where inserts end, to where the true end is
HTML_END = """
	</body>
</html>
"""

AUTO_CSS = """

body {
    font-family: 'helvetica neue', helvetica, sans-serif;
    margin: 8px;
    padding: 4px;
}

.code_block {
    border: 1px solid black;
    padding: 0px;
    font-family: monospace;
}
"""


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("No files were specified")
        exit()
    css_choice = input("Would you like to generate a css file? (y/n)").lower()
    if re.search("y", css_choice):
        with open("autostyle.css", "w+") as css:
            css.write(AUTO_CSS)
        print("\033[32M" +  "Created CSS" + "\033[0m")
    else:
        print("\033[31m" + "Will not create CSS" + "\033[0m")

    print("\n" + "\033[36m" + f"Creating HTML file from {sys.argv[1]}" + "\033[0m")
    main()
