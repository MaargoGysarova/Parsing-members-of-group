import vk_api

import json
import pandas as pd


def getter(group_id):
    vk_session = vk_api.VkApi("login", "password")
    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return
    # get members of group
    members = vk_session.method('groups.getMembers', {'group_id': group_id})
    print('Posts count:', members['count'])
    members = members["items"]
    for row in members:
        with open(r"wall_{}.csv".format(group_id), "a", encoding="utf-8") as f:
            f.write(str(row))
            f.write("\n")
    member_list = []
    for member in members:
        member_list.append(member)
    return member_list


getter(69812)


def get_properly_members(member_list):
    vk_session = vk_api.VkApi("gysarova.elena@mail.ru", "zabolockaielena1979")
    member_list_true = []
    i = 0

    for member_id in member_list:
        if i < 20:
            try:
                vk_session.auth(token_only=True)
            except vk_api.AuthError as error_msg:
                print(error_msg)
                return
            # check if member not deleted
            try:
                status = vk_session.method('users.get', {'user_ids': member_id})
                status = status[0]["deactivated"]
                if status == "deleted" or status == "banned":
                    print("deleted")
                    with open(r"deleted.csv", "a", encoding="utf-8") as f:
                        f.write(str(member_id))
                        f.write("\n")

            except:
                print("not deleted")
                with open(r"not_deleted.csv", "a", encoding="utf-8") as f:
                    f.write(str(member_id))
                    f.write("\n")
                    member_list_true.append(member_id)

            i = i + 1

        else:
            break
    for member_id in member_list_true:
        status = vk_session.method('status.get', {'user_id': member_id})
        # check if status is not empty
        if status["text"] != "":
            with open(r"status.csv", "a", encoding="utf-8") as f:
                f.write(str(status))
                f.write("\n")
        else:
            with open(r"status.csv", "a", encoding="utf-8") as f:
                f.write("No status")
                f.write("\n")
        print(status)









get_properly_members(getter(69812))
