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
            tag_info = [i + 1, match.group(1)]
            tags_list.append(tag_info)

    if tags_list == []:
        return None
    # Detect errors
    for tag in tags_list:
        if not tag[1].startswith('/'):  # open Tag
            openStack.append(tag)
        elif tag[1].startswith('/'):  # close Tag
            closeTag = tag[1][1:]
            tag_line = tag[0]
            if openStack != []:
                if closeTag == openStack[-1][1]:
                    openStack.pop()
                elif len(openStack) > 1 and closeTag == openStack[-2][1]:
                    updateTags(openStack[-1][0], 'Missing Close tag', openStack[-1][1])
                    openStack.pop() # pop the wrong tag
                    openStack.pop() # pop the right tag
                else:
                    updateTags(tag_line, 'Missing open tag', closeTag)
            else:
                updateTags(tag_line, 'Missing open tag', closeTag)

        closeTag = ''
        tag_line = 0

    if openStack != []:
        while openStack != []:
            updateTags(openStack[-1][0]+1, 'Missing Close tag', openStack[-1][1],len(tags))
            openStack.pop()

    return tags


