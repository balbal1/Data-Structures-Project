import re

def error_detection(xml_file):
    filter = r'<(/?\w+)>'
    tags_list = []
    openStack = []
    tags = []  # line: , status: correct/missing tag

    def updateTags(line, status, name):
        tag_info = [line, status, name]
        tags.append(tag_info)

    # Get the tags and their corresponding line
    for i in range(len(xml_file)):
        matches = re.finditer(filter, xml_file[i])
        for match in matches:
            tag_info = [i, match.group(1)]
            tags_list.append(tag_info)

    if tags_list == []:
        return None
    
    found_text = False
    # Detect errors
    flag = None
    for tag in tags_list:
        if not tag[1].startswith('/'):  # open Tag
            flag = tag
            if found_text:
                updateTags(openStack[-1][0], 'Missing close tag', openStack[-1][1])
                openStack.pop()
                found_text = False
            openStack.append(tag)
            if xml_file[tag[0]].strip()[-1] != '>' or ((len(xml_file) > tag[0]+1) and xml_file[tag[0]+1].strip() and re.findall(r'<(/?\w+)>', xml_file[tag[0]+1]) == []):
                found_text = True
        elif tag[1].startswith('/'):  # close Tag
            closeTag = tag[1][1:]
            tag_line = tag[0]
            if openStack != []:
                if closeTag == openStack[-1][1]:
                    openStack.pop()
                    found_text = False
                else:
                    if len(openStack) > 1 and closeTag == openStack[-2][1]:
                        updateTags(openStack[-1][0], 'Missing close tag', openStack[-1][1])
                        openStack.pop() # pop the wrong tag
                        openStack.pop() 
                        # pop the right tag
                    elif found_text or flag and flag[0] == tag_line:
                        updateTags(tag_line, "Mismatching tags", [closeTag, flag[1], flag[0]])
                        openStack.pop()
                    else:
                        updateTags(tag_line, 'Missing open tag', closeTag)
                    if found_text:
                        found_text = False
            else:
                updateTags(tag_line, 'Missing open tag', closeTag)

        closeTag = ''
        tag_line = 0

    if openStack != []:
        while openStack != []:
            updateTags(openStack[-1][0], 'Missing close tag', openStack[-1][1])
            openStack.pop()

    tags.sort(key=lambda x: int(x[0]))
    
    return tags


