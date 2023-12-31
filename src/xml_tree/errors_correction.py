import re

def error_correction(tags, xml_file):
    if len(tags) == 0:
        return 'File is consistent.'
    
    corrected_xml_file = xml_file.copy()
    
    #Reversed the vector to ensure that tags are inserted in the correct order
    for tag in reversed(tags):
        #tag[0] : line of the error, tag[1]: error type, 
        if tag[1] == 'Missing open tag':
            open_tag = f"<{tag[2]}>"
            open_tag_insert_line = find_open_tag_insert_line(tag[0], corrected_xml_file)
            if open_tag_insert_line is not None and open_tag_insert_line>0:
                corrected_xml_file.insert(open_tag_insert_line, open_tag)
            else:
                open_tag_insert_line = 0
                corrected_xml_file.insert(0, open_tag)  # Insert at position 0 if None or 0
            for tag in tags:
                if tag[0] > open_tag_insert_line:
                    tag[0] += 1
        elif tag[1] == 'Missing Close tag':
            close_tag = f"</{tag[2]}>"
            close_tag_insert_line = find_close_tag_insert_line(tag[0]+1, corrected_xml_file)
            if close_tag_insert_line is not None and close_tag_insert_line < len(corrected_xml_file):
                corrected_xml_file.insert(close_tag_insert_line, close_tag)
            else:
                close_tag_insert_line = len(corrected_xml_file)
                corrected_xml_file.append(close_tag)  # Insert at the end if None
            for tag in tags:
                if tag[0] > close_tag_insert_line:
                    tag[0] += 1


    return corrected_xml_file

# Returns None in case the tag_line tag_line < 0 else returns tag_line
def find_open_tag_insert_line(tag_line, xml_file):
    stack = []  # Stack to store encountered closing tags
   
    just_text = False
    # remove white space
    line_content = xml_file[tag_line].strip()
    if line_content[0] != '<':
        just_text = True

    # Decrement the line number as long as the line contains just text        
    while tag_line >= 0 and not just_text:
        line_content = xml_file[tag_line-1].strip()
        tag_line -= 1
        if line_content:
            if line_content[-1] == '>':
                break
            just_text = True
    
    # The line contains just text
    if just_text:
        return tag_line
    else:
        # The tag has children
        while tag_line >= 0:
            
            if line_content:
                if re.match(r'<[a-z]>[a-zA-Z\s]+</[a-z]>',line_content): #detect <tag>text</tag> case
                    continue
                elif line_content[0] == '<' and line_content[1] !='/':
                    if not stack:
                        return tag_line  #Correct line found
                    else:
                        stack.pop()  # Remove the corresponding close tag from the stack
                    
                # Check if the line contains a closing tag
                elif line_content[0:2] == '</':
                    stack.append(line_content) 

            tag_line -= 1
            line_content = xml_file[tag_line-1].strip()
            
        return None


# Returns None in case the tag_line tag_line > len(xml_file) else returns tag_line
def find_close_tag_insert_line(tag_line, xml_file):
    stack = []  # Stack to store encountered closing tags
   
    just_text = False
    # remove white space
    line_content = xml_file[tag_line-1].strip()
    if line_content[-1] != '>':
        just_text = True

    #Increment the line number as long as the line contains just text
    while tag_line < len(xml_file) and not just_text:
        line_content = xml_file[tag_line].strip()
        tag_line += 1
        if line_content:
            if line_content[0] == '<':
                break
            just_text = True

    if just_text:
        return tag_line
    else:
        # The tag has children
        while tag_line < len(xml_file)-1:
            
            if line_content:
                if re.match(r'<[a-z]>[a-zA-Z\s]+</[a-z]>',line_content): #detect <tag>text</tag> case
                    continue
                elif line_content[0:2] == '</':
                    if not stack:
                        return tag_line  #Correct line found
                    else:
                        stack.pop()  # Remove the corresponding close tag from the stack
                    
                # Check if the line contains a closing tag
                elif line_content[0] == '<' and line_content[1] !='/':
                    stack.append(line_content) 

            tag_line += 1
            line_content = xml_file[tag_line].strip()
            
        return None
