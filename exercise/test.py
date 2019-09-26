import requests
name = requests.get("http://10.36.145.100:5000/v2/_catalog")
name = name.json()
images = {}
print("{:<30}".format("NAME"),"{:>20}".format('TAG'))
for element in name.values():
    for i in range(len(element)):
        tags = requests.get("http://10.36.145.100:5000/v2/{}/tags/list".format(element[i]))
        image = tags.json()
        # print(image)
        names = image['name']
        # for tag in image.values():
        #     if type(tag) == list:
        #         for t in tag:
        #             print("{:<30}".format(names.upper()),"{:>20}".format(t))
        #             images.setdefault("{:<30}".format(names.upper()), "{:>20}".format(t))

        tag = image['tags']
        for t in tag:
            print("{:<30}".format(names.upper()),"{:>20}".format(t))