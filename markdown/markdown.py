import re

def parse(markdown : str) -> str:

    # Convert markdown string to a list; one item per line of markdown
    lines = markdown.split('\n')

    # Each line of markdown is converted to html, and added to html_list
    html_list = []

    # Initially, you are not in a list
    list_is_open = False

    # Iterate over each line of markdown
    for line in lines:

        html_line = ''

        '''
        1 BLOCK: signalled at the start of a line
            A. List items are indicated by a *
                - <li> and </li> tags around each item of the list
                - <ul> and </ul> tags around the entire list
            B. Headings are indicated by one or more #
                - <hx> tag at the start of the heading
                - x = number of hashes
            C. Neither a list nor a heading
                - <p> and </p>

        2. SPAN: can occur anywhere in the line
            A. Bold
            B. Italics

        * and # NOT at the start of a line are ignored
        '''

        # 1A. List: if the line starts with a *
        line_is_list_item = re.match(r'\* (.*)', line)

        # If this is a list item,
        if line_is_list_item:
            # Get the item
            current = line_is_list_item.group(1)
            
            # If it's the first item in the list, add the opening <ul> tag
            if list_is_open == False:
                html_line += '<ul>'
                list_is_open = True
                
            # Wrap the item in <li> tags
            html_line += '<li>' + current + '</li>'
        
        else:
            # If the list has ended i.e. line_is_list_item == False (current item is not a list item) and 
            # list_is_open == True (last item was a list and list is not closed), 
            # close it with a </ul>
            if list_is_open:
                html_list[-1] += '</ul>'
                list_is_open = False

        # 1B. Headings: if the line starts with one or more #
        heading = re.match('#+ ', line)
        if heading is not None:
            html_line += '<h' + str(heading.end() - 1) + '>' + line[heading.end():] +  '</h'+ str(heading.end() - 1) + '>'

        # 1C. Neither list nor heading: the line is a string (empty or non-empty)
        if html_line == '':
            html_line += line

        # 2A. Bold: if the line contains __
        bold = re.search('(.*)__(.*)__(.*)', html_line)
        if bold is not None:
            html_line = bold.group(1) + '<strong>' + bold.group(2) + '</strong>' + bold.group(3)

        # 2B. Italics: if the line contains _
        italic = re.search('(.*)_(.*)_(.*)', html_line)
        if italic is not None:
            html_line = italic.group(1) + '<em>' + italic.group(2) + '</em>' + italic.group(3)

        # Add each html_line to a list
        html_list.append(html_line)

    # Handle edge case where the last item of the markdown string was a list item
    if list_is_open:
        html_list[-1] += '</ul>'

    html = ""
    for l in html_list:
        # If there are no tags, add <p> tag
        if re.match('<h|<ul|<p|<li', l) is None:
            l = '<p>' + l + '</p>'
        html += l

    return html


'''
Code to be refactored


import re


def parse(markdown):
    lines = markdown.split('\n')
    res = ''
    list_is_open = False
    list_is_open_append = False
    for i in lines:
        if re.match('###### (.*)', i) is not None:
            i = '<h6>' + i[7:] + '</h6>'
        elif re.match('## (.*)', i) is not None:
            i = '<h2>' + i[3:] + '</h2>'
        elif re.match('# (.*)', i) is not None:
            i = '<h1>' + i[2:] + '</h1>'
        m = re.match(r'\* (.*)', i)
        if m:
            if not list_is_open:
                list_is_open = True
                is_bold = False
                is_italic = False
                curr = m.group(1)
                m1 = re.match('(.*)__(.*)__(.*)', curr)
                if m1:
                    curr = m1.group(1) + '<strong>' + \
                        m1.group(2) + '</strong>' + m1.group(3)
                    is_bold = True
                m1 = re.match('(.*)_(.*)_(.*)', curr)
                if m1:
                    curr = m1.group(1) + '<em>' + m1.group(2) + \
                        '</em>' + m1.group(3)
                    is_italic = True
                i = '<ul><li>' + curr + '</li>'
            else:
                is_bold = False
                is_italic = False
                curr = m.group(1)
                m1 = re.match('(.*)__(.*)__(.*)', curr)
                if m1:
                    is_bold = True
                m1 = re.match('(.*)_(.*)_(.*)', curr)
                if m1:
                    is_italic = True
                if is_bold:
                    curr = m1.group(1) + '<strong>' + \
                        m1.group(2) + '</strong>' + m1.group(3)
                if is_italic:
                    curr = m1.group(1) + '<em>' + m1.group(2) + \
                        '</em>' + m1.group(3)
                i = '<li>' + curr + '</li>'
        else:
            if list_is_open:
                list_is_open_append = True
                list_is_open = False

        m = re.match('<h|<ul|<p|<li', i)
        if not m:
            i = '<p>' + i + '</p>'
        m = re.match('(.*)__(.*)__(.*)', i)
        if m:
            i = m.group(1) + '<strong>' + m.group(2) + '</strong>' + m.group(3)
        m = re.match('(.*)_(.*)_(.*)', i)
        if m:
            i = m.group(1) + '<em>' + m.group(2) + '</em>' + m.group(3)
        if list_is_open_append:
            i = '</ul>' + i
            list_is_open_append = False
        res += i
    if list_is_open:
        res += '</ul>'
    return res
'''