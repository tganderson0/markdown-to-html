# Phase 0: Requirements Specification (10%)



I will be writing a calculator using vanilla javascript, adding all elements solely through javascript and not using an html document. (Other than the most basic valid page that I can)

1. Title of page should be changed by the script upon load
2. Div will contain instructions to create an expression, as well as inputs for creating one
    * Numeric inputs for binary arithmetic operations (has a placeholder value to begin)
    * Drop down menu to select operation to perform
        1. +
        2. -
        3. /
        4. *
        5. %
        6. **
    * Input for color lets user pick the output div's color
    * Button with label 'compute', which will then evaluate input and output a new div below the input interface (NOTE: color will be taken from input) Should verify input before evaluating
3. Newest output should be at the TOP, pushing the older ones downward

### Output format

* String representation of the current time of evaluation, regardless of operation success
* Output div should be REMOVED when CLICKED
* Red output div if there is an error, place error message
* Color should be what was picked if operation was successful

### What I know and what I will need to learn

* Already know how to create elements through javascript, the main one I will need to look into is telling which div was clicked, but if memory serves me right, there is some form of click listener that I can use

* Will need to review how to use the 'color' input


# Phase 1: System Analysis (10%)


### Inputs

1. Inputted numeric value 1 (numeric input)
2. Inputted numeric value 2 (numeric input)
3. Selected operation (drop-down selector)
4. Output div color (color selector)
5. Output div that was clicked
6. Compute button clicked
7. Current time of browser (from js)


### Outputs

1. New div according to design (red for error, their color for other)
2. Removal of a output div if clicked
3. No formulae, can just use eval()

# Phase 2: Design (30%)
Deliver:


(Pseudocode in python-ish)

```
# numericX is the input sliders, operation is the currently selected operation
# This will be used to validate input, as well as creating the text content for the the divs
# Note: I originally had this function checking for divide by 0 errors, but it seems javascript is totally cool with it
def evaluateInputs(numeric1, numeric2, operation): --> Returns a tuple, string with result or error message, along with boolean if operation was successful

    # Bad inputs
    if numeric1 is null or numeric2 is null:
        return ("Error! One of more Operands are missing", false)
    if numeric1 is not numeric or numeric2 is not numeric:
        return ("Error! One or or more Operands are not valid inputs - you dirty hacker")
    
    # Inputs are good
    result = eval(numeric1, operation, numeric2)
    return (f"{numeric1} {operation} {numeric2} = {result}", true)


# values are the same as evaluateInputs, but the color is the color they selected with the input
# Used for actually creating the divs, creates the correct color as well
def createOutput(numeric1, numeric2, operation, color): --> Creates and returns a div with the proper form
	
	output = div() # Create a div, obviously this will be javascript rather than python in implementation
	
	outputText, valid = evaluateInputs(numeric1, numeric2, operation)
	
	output.text = f"{currentTime} {outputText}"
	if valid:
		output.color = color
	else:
	
		output.color = red
	
	return output


```

Good and bad inputs are handled by the functions, including if the user does some hackery with changing the input types.

Created a separate html file for getting the designs down, to reference later

# Phase 3: Implementation (15%)

I realized that the plan could have gone a bit better with the functions, I did not think about the click listeners. I ended up creating 2 extra functions, that pretty much just added the original input, as well as a single output box.


# Phase 4: Testing & Debugging (30%)

## Tested

1. Empty input box on one or both should create a red error output
	* PASSED
2. Extra test, if user changes input type to non-numeric, and enters a non-numeric value, should output red error
	* PASSED
3. Output box should match color input
	* PASSED
4. Output order should be newest to oldest
	* PASSED
5. Output should be removed when clicked, and the correct one should be removed
	* PASSED
6. Proper output for each selection (perform each operation on a set of numbers, should match expected output)
	* PASSED
7. Testing one and both negative outputs expected number
	* PASSED
8. Testing one and both very small numbers gives expected output
	* PASSED
9. Testing one and both very large numbers gives expected output
	* PASSED


# Phase 5: Deployment (5%)
Deliver:

* Your repository pushed to GitLab.

# Phase 6: Maintenance
Deliver:

* What parts of your program are sloppily written and hard to understand?
	* Creation of the element functions could have been organized a lot better, as well as eliminating some redundancies

* Are there parts of your program which you aren’t quite sure how/why they work?
	* The program all made sense, it is pretty much just like the first assignments of GUIs, with slightly different syntax for doing things

* If a bug is reported in a few months, how long would it take you to find the cause?
	* Bugs should be really quick to find, as it is a very short and simple program. Not a large amount of connected parts

* Will your documentation make sense to
anybody besides yourself?
	* The documentation needs a bit of work to be better understood by other people, I plan on going back and making it better after I finish answering these questions.

* How easy will it be to add a new feature to this program in a year?
	* New features would be really easy to add, as I feel I separated the sections out approriately. The setup function handles adding original parts to the page on load, everything else is just a function to create an element


* Will your program continue to work after upgrading your computer’s hardware? the operating system? to the next version of Python?
	* Since this is javascript running in my browser, my computer's hardware and the operating system would not have an effect on my program. I don't take advantage of anything specific to a computer either. For the next version of javascript, it should be fine, since I did not use any deprecated functions, although I can't gurantee that my work will last forever, just at least to the next version
