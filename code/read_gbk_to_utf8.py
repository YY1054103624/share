def gbk_to_utf8(gbkfilepath, utf8filepath):
    """
    file of gbk to file of utf8
    :param gbkfilepath: input file, charset is gbk
    :param utf8filepath: output file, charset is utf8
    :return:
    """
    outputfile = open(utf8filepath, 'w', encoding='utf8')
    for line in open(gbkfilepath, encoding='gbk'):
        outputfile.write(line)


gbk_to_utf8("./diary.txt", "output.txt")
