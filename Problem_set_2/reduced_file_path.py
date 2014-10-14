def reduce_file_path(path):
    list_of_files = path.split('/')
    result_list = list_of_files[:]
    #print(list_of_files)
    for item in list_of_files:
        if item == '' or item == '.':
            result_list.remove(item)
        if item == '..':
            result_list.pop(result_list.index(item) - 1)
            result_list.remove(item)
    print(result_list)
    return "/" + "/".join(result_list)
print(reduce_file_path("/rado/fds///fds/../fds"))
