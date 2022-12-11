def add_document (name_doc, content_doc):
    sort_name_doc = ''.join(sorted(name_doc))
    sort_content_doc = ''.join(sorted(content_doc))
    if len(name_doc) != len(content_doc):
        return False
    for index in range(len(sort_name_doc)):
        if sort_content_doc[index] != sort_content_doc[index]:
            return False
    else:
        return True


charachter = "abcabc"
document = "aabbccc"
print(add_document(charachter, document))
