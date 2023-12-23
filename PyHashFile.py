End = None


def istr_c(a, b):
    c = "%s" % b
    d = '%s' % b
    if a == c or a == d:
        return True
    else:
        return False


class HashMap(object):
    def __init__(self, File_path, 
                 encode = "utf-8", 
                 File_pathile_info = {"suffix": {"name": "HashMap", "len_lie": [-7, End]}}) -> None:
        self.File_path = File_path
        self.encode = encode
        self.File_pathile_info = File_pathile_info
    def creat(self, matter) -> None:
        with open(self.File_path, 'wb') as w:
            mid_list = list()
            for i in matter.keys():
                mid_str = "%s: %s\n" % (i, matter[i])
                mid_list.append(mid_str.encode())
            w.writelines(mid_list)
