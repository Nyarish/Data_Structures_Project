
class Group(object):
    
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name



def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    
    # check if user is available in group
    users = group.get_users()
    if user in users:
        return True
    
    # check in is user is in groups
    else:
        group_list = group.get_groups()
        for item in group_list:
            if is_user_in_group(user, item):
                return True 
    
    return False


# Test 1
print("Test case 1: group with sub group and user")
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")


sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

print("Check Group:{} ".format(parent.get_name()),      "Check if user:{} is in group ?".format(sub_child_user),      is_user_in_group(sub_child_user, parent))


print("Check Group:{} ".format(child.get_name()),      "Check if user:{} is in group ?".format(sub_child_user),      is_user_in_group(sub_child_user, child))

print("Check Group:{} ".format(sub_child.get_name()),      "Check if user:{} is in group ?".format(sub_child_user),      is_user_in_group(sub_child_user, sub_child))



print()
# Test 2
print("Test case 2: group with no user")
empty = Group("Empty")
empty_user = "user"


print("Check Group:{} ".format(parent.get_name()),      "Check if user:{} is in group ?".format(empty_user),      is_user_in_group(empty_user, empty))


print()
# Test 3
print("Test case 3: group with users and sub group without user")

# add groups
udacity = Group("Udacity_online_students")
chat_udacity = Group("Online_chat")

# add users
user1 = "Nyaribo"
user2 = "Juma"
user3 = "karimi"
user4 = "James"
user5 = "Makena"

udacity.add_user(user1)
udacity.add_user(user2)
udacity.add_user(user3)
udacity.add_user(user4)
udacity.add_user(user5)

chat_udacity.add_user(user1)
chat_udacity.add_user(user4)

print("Check Group:{} ".format(udacity.get_name()),      "Check if user:{} is in group ?".format(user1),      is_user_in_group(user1, udacity))

print("Check Group:{} ".format(udacity.get_name()),      "Check if user:{} is in group ?".format(user2),      is_user_in_group(user2, udacity))

print("Check Group:{} ".format(udacity.get_name()),      "Check if user:{} is in group ?".format(user5),      is_user_in_group(user5, udacity))

print("Check Group:{} ".format(chat_udacity.get_name()),      "Check if user:{} is in group ?".format(user3),      is_user_in_group(user3, chat_udacity))
print("Check Group:{} ".format(chat_udacity.get_name()),      "Check if user:{} is in group ?".format(user4),      is_user_in_group(user4, chat_udacity))



"""OUTPUT
Test case 1: group with sub group and user
Check Group:parent  Check if user:sub_child_user is in group ? True
Check Group:child  Check if user:sub_child_user is in group ? True
Check Group:subchild  Check if user:sub_child_user is in group ? True

Test case 2: group with no user
Check Group:parent  Check if user:user is in group ? False

Test case 3: group with users and sub group without user
Check Group:Udacity_online_students  Check if user:Nyaribo is in group ? True
Check Group:Udacity_online_students  Check if user:Juma is in group ? True
Check Group:Udacity_online_students  Check if user:Makena is in group ? True
Check Group:Online_chat  Check if user:karimi is in group ? False
Check Group:Online_chat  Check if user:James is in group ? True

"""





