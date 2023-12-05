import re

def error_detection(text):
    xml_file=text

    filter1='(?<=\<)[^/].*(?=\>)'
    filter2='(?<=\</).*(?=\>)'

    openning_list=[]
    closing_list=[]
    count_open=0
    count_close=0

    for i in range(len(xml_file)):
        text=re.findall(filter1,xml_file[i])
        closin=re.findall(filter2,xml_file[i])
        openning= ' '.join(text).split('>')[0]
        closing=''.join(closin)
        if openning !='':
            openning_list.append(openning)
            count_open+=1
        if closing !='':
            if closing ==openning_list[-1]:
                openning_list.pop()
            else :
                closing_list.append(closing)
    #             closing_list.append(f'</{openning_list[-1]}>')

            count_close+=1

            




    print(openning_list)
    print(closing_list)











