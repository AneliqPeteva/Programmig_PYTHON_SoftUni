import re

sentence = input()
pattern = r"\s(([a-z0-9]+[a-z0-9\.\-\_]*)@([a-z\-]+)(\.[a-z]+)+)\b"
extracted_emails = re.findall(pattern, sentence)
for extracted_email in extracted_emails:
    print(extracted_email[0])


# import re
#
# text = input()
#
# pattern = r"(^|(?<=\s))([A-Za-z0-9])+([\.\-\_][A-Za-z0-9]+)*@([A-Za-z-]+)\.([A-Za-z-]+)([\.A-Za-z-])*(\b|(?=\s))"
#
# matches = re.finditer(pattern, text)
#
# for match in matches:
#     print(match[0])
