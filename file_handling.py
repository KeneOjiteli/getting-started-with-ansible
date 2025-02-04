# with open("inventory.txt", "r") as f:
#     for line in f:
#         print(line, end="")

    # f_content = f.readlines()
    # print(f_content, end="")

    # f_content = f.readline()
    # print(f_content)

# this opens an inventory file in the read mode and copies its content to test file in write mode
# with open("inventory.txt", "r") as f:
#     with open("test.txt", "w") as wf:
#        write = wf.write(f.read())
#        print(write)

def update_server_config(file_path, key, value):
    with open(file_path, "r") as file:
        read_file = file.readlines() 

    with open(file_path, "w") as file:
        for each_file in read_file:
            if key in each_file:
                file.write(f"{key} = {value} \n")
            else:
                file.write(each_file)



# file_path = "server.conf"
# key = "MAX_CONNECTIONS"
# value = "100"
# update_server_config(file_path, key, value)

update_server_config("server.conf", "MAX_CONNECTIONS", "300")
