def error_correction(tags, xml_file):
    if len(tags) == 0:
        return 'File is consistent.'
    
    corrected_open_tags = 1
    corrected_xml_file = xml_file.copy()
    
    #Reversed the vector to ensure that tags are inserted in the correct order
    for tag in reversed(tags):
        #tag[0] : line of the error, tag[1]: error type, 
        if tag[1] == 'Missing open tag':
            open_tag = f"<{tag[2]}>"
            open_tag_insert_line = find_open_tag_insert_line(tag, corrected_xml_file,corrected_open_tags)
            corrected_open_tags +=1
            if open_tag_insert_line is not None and open_tag_insert_line>0:
                corrected_xml_file.insert(open_tag_insert_line, open_tag)
                
            else:
                corrected_xml_file.insert(0, open_tag)  # Insert at position 0 if None or 0
        elif tag[1] == 'Missing Close tag':
            close_tag = f"</{tag[2]}>"
            close_tag_insert_line = find_close_tag_insert_line(tag[0], corrected_xml_file)
            if close_tag_insert_line is not None and close_tag_insert_line < len(corrected_xml_file):
                corrected_xml_file.insert(close_tag_insert_line, close_tag)
            else:
                corrected_xml_file.append(close_tag)  # Insert at the end if None
                

    return corrected_xml_file

# Returns None in case the tag_line tag_line < 0 else returns tag_line
def find_open_tag_insert_line(tag, xml_file, count):
    stack = []  # Stack to store encountered closing tags
    tag_line = tag[0]
   
    # Decrement the line number as long as the line contains just text or closing tags
        # remove white space
    line_content = xml_file[tag_line- count].strip().rstrip()

    if line_content and all(char not in line_content for char in ['<', '/', '>']):
        
        # The line contains just text
        while tag_line > 0:
            if line_content and line_content[-1] == '>': 
                return tag_line 
            tag_line -= 1
            line_content = xml_file[tag_line-1].strip().rstrip()
        return None
        
    if line_content and line_content[-1] == '>':
        if not '/' in line_content:
            #Open tag encountered"
            return tag_line - count
        
        # The tag has children
        while tag_line > 0:
            
            if re.match(r'<[a-z]>[a-zA-Z\s]+</[a-z]>',line_content): #detect <tag>text</tag> case
                continue
            elif line_content[0] == '<' and line_content[1] !='/'  :
                if not stack:
                      return tag_line  #Correct line found
                else:
                    stack.pop()  # Remove the corresponding close tag from the stack
            
                
        # Check if the line contains a closing tag
            elif line_content[0:2] == '</':
                stack.append(line_content) 

            tag_line -= 1
            line_content = xml_file[tag_line-1].strip().rstrip()

    return None  


# Returns None in case the tag_line tag_line > len(xml_file) else returns tag_line
def find_close_tag_insert_line(tag_line, xml_file):
    # Find the appropriate line number to insert the close tag
    tag_line += 1

 #Increment the line number as long as the line contains just text
    while tag_line < len(xml_file):
        line_content = xml_file[tag_line].strip()
        if line_content and line_content[0] == '<':
            return tag_line
        tag_line += 1
    return None
