
def error_detection(text):
    xml_file = text
    filter = r'<(/?\w+)>'
    tags_list=[]
    openStack = []
    tags = [] # line: , status: correct/missing tag

    def updateTags(line,status,name):
        tag_info = {}
        tag_info['line'] = line
        tag_info['status'] = status
        tag_info['name'] = name
        tags.append(tag_info)

    # Get the tags and its corresponding line
    for i in range(len(xml_file)): 
        matches=re.finditer(filter,xml_file[i])
        for match in matches:
            tag_info = {}
            tag_info['line'] = i + 1
            tag_info['tag'] = match.group(1)
            tags_list.append(tag_info)
            
    # Detect errors
    for tag in tags_list:
        if not tag['tag'].startswith('/'): # open Tag
            openStack.append(tag)
        elif tag['tag'].startswith('/'): # close Tag
            closeTag = tag['tag'][1:]
            tag_line = tag['line']
            if openStack != []:
                if closeTag == openStack[-1]['tag']:
                    updateTags(tag_line,'valid',openStack[-1]['tag'])
                    openStack.pop()
                elif len(openStack) > 1 and closeTag == openStack[-2]['tag']:
                    updateTags(openStack[-1]['line'],'Missing Close tag',openStack[-1]['tag'])
                    openStack.pop()
                    updateTags(tag_line, 'Valid',openStack[-1]['tag'])
                    openStack.pop()
                else:
                    updateTags(tag_line,'Missing open tag',closeTag)
            else :
                updateTags(tag_line,'Missing open tag',closeTag)
                
        closeTag = ''
        tag_line =0

    if openStack != []:
        while openStack != []:
            updateTags(openStack[-1]['line'],'Missing Close tag',openStack[-1]['tag'])
            openStack.pop()
    print(tags)
        
    return tags
