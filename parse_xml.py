import xml.etree.ElementTree as ET

def parse_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()

    users = []

    for user_elem in root.findall('user'):
        user = {
            'id': user_elem.find('id').text,
            'name': user_elem.find('name').text,
            'posts': [],
            'followers': []
        }

        for post_elem in user_elem.findall('posts/post'):
            post = {
                'body': post_elem.find('body').text,
                'topics': [topic.text.strip() for topic in post_elem.findall('topics/topic')]
            }
            user['posts'].append(post)

        for follower_elem in user_elem.findall('followers/follower'):
            follower_id = follower_elem.find('id').text
            user['followers'].append({'id': follower_id})

        users.append(user)

    return users

if __name__ == "__main__":
    file_path = "sample.xml"
    parsed_data = parse_xml(file_path)

    # Print the parsed data in a structured format
    for user in parsed_data:
        print(f"User ID: {user['id']}")
        print(f"User Name: {user['name']}")
        print("Posts:")
        for post in user['posts']:
            print(f"  - Body: {post['body']}")
            print(f"    Topics: {', '.join(post['topics'])}")
        print("Followers:")
        for follower in user['followers']:
            print(f"  - Follower ID: {follower['id']}")
        print("\n")
