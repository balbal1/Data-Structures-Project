import re
def error_detection(text):
    xml_file = text
    filter = r'<(/?\w+)>'
    tags_list=[]
    openStack = []
    tags = [] # line: , status: correct/missing tag

    def updateTags(line,status,name):
        tag_info = []
        tag_info[0] = line
        tag_info[1] = status
        tag_info[2] = name
        tags.append(tag_info)

    # Get the tags and its corresponding line
    for i in range(len(xml_file)): 
        matches=re.finditer(filter,xml_file[i])
        for match in matches:
            tag_info = []
            tag_info[0] = i + 1
            tag_info[1] = match.group(1)
            tags_list.append(tag_info)
            
    # Detect errors
    for tag in tags_list:
        if not tag[1].startswith('/'): # open Tag
            openStack.append(tag)
        elif tag[1].startswith('/'): # close Tag
            closeTag = tag[1][1:]
            tag_line = tag[0]
            if openStack != []:
                if closeTag == openStack[-1][1]:
                    updateTags(tag_line,'valid',openStack[-1][1])
                    openStack.pop()
                elif len(openStack) > 1 and closeTag == openStack[-2][1]:
                    updateTags(openStack[-1][0],'Missing Close tag',openStack[-1][1])
                    openStack.pop()
                    updateTags(tag_line, 'Valid',openStack[-1][1])
                    openStack.pop()
                else:
                    updateTags(tag_line,'Missing open tag',closeTag)
            else :
                updateTags(tag_line,'Missing open tag',closeTag)
                
        closeTag = ''
        tag_line =0

    if openStack != []:
        while openStack != []:
            updateTags(openStack[-1][0],'Missing Close tag',openStack[-1][1])
            openStack.pop()
    print(tags)
        
    return tags
