import re

def error_detection(text):
    xml_file=text
    # filter1='(?<=\<)[^/].*(?=\>)'
    # filter2='(?<=\</).*(?=\>)'

    # openning_list=[]
    # closing_list=[]
    # count_open=0
    # count_close=0

    # for i in range(len(xml_file)):
    #     text=re.findall(filter1,xml_file[i])
    #     closin=re.findall(filter2,xml_file[i])
    #     openning= ' '.join(text).split('>')[0]
    #     closing=''.join(closin)
    #     if openning !='':
    #         openning_list.append(openning)
    #         count_open+=1
    #     if closing !='':
    #         if closing ==openning_list[-1]:
    #             openning_list.pop()
    #         else :
    #             closing_list.append(closing)
    # #             closing_list.append(f'</{openning_list[-1]}>')

    #         count_close+=1
    # print(openning_list)
    # print(closing_list)
    
filter = r'<(/?\w+)>' #Get open and close tags
tags_list=[]
line_Count = 1;

for i in range(len(xml_file)):
    matches=re.finditer(filter2,xml_file[i])

    # To flat the array
    for match in matches: 
        tags_list.append(match.group(1))
        
def updateTags(line,status,name):
    tag_info = {}
    tag_info['line'] = line
    tag_info['status'] = status
    tag_info['name'] = name
    tags.append(tag_info)

for tag in tags_list:
    tag_info = {}
    if not tag.startswith('/'):
        openStack.append(tag)
    elif tag.startswith('/'):
        closeTag = tag[1:]
        if len(openStack) > 0:
            if closeTag == openStack[-1]:
                updateTags(line_Count,'valid',openStack[-1])
                openStack.pop()
            elif closeTag == openStack[-2]:
                updateTags(line_Count,'Missing Close tag',openStack[-1])
                
                openStack.pop()
                updateTags(line_Count, 'Valid',openStack[-1])
                openStack.pop()
            else:
                updateTags(line_Count,'Missing open tag',closeTag)
        elif len(openStack) == 0 and closeTag != '':
            updateTags(line_Count,'Missing open tag',closeTag)

    line_Count += 1
    closeTag = ''
    
if openStack != []:

    while openStack != []:
        updateTags(line_Count,'Missing Close tag',openStack[-1])
        openStack.pop()
        
return tags
