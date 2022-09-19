
def compareDict(left_dict: dict, right_dict: dict):
    """compare two dict, will return three list in a tuple.

    Args:
        left_dict (dict): left dict which will be compared
        right_dict (dict): right dict with will be compared

    Returns:
        list: returns keys in left dict which not exists in the right dict
        list: returns keys in right dict which not exists in the left dict
        list: returns [key, left_item, right_item] lists which contains the key and both different items in one list.
    """
    only_left_exists = []
    only_right_exists = []
    differents = []

    for left_key, left_item in left_dict.items():
        # 看元素是否只在左边存在
        if left_key not in right_dict:
            only_left_exists.append(left_key)
            continue

        # 比较是否不同
        right_item = right_dict.get(left_key)
        if left_item != right_item:
            differents.append([left_key, left_item, right_item])
            continue

    for right_key in right_dict.keys():
        if right_key not in left_dict:
            only_right_exists.append(right_key)
            continue

    return only_left_exists, only_right_exists, differents


left_dict = {
    1: "abc",
    2: "cde",
    3: "efg"
}
right_dict = {
    1: "cde",
    4: "abc",
    3: "efg"
}
print(compareDict(left_dict, right_dict))
