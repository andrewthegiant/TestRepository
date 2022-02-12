from flask import Flask
app = Flask(__name__)

first_var = ""
second_var = ""

# count = 0
# while count < 10:
#     if count == 3:
#         continue
#         count = count+1
#     first_var += "<p>User count is {}</p></br>".format(count)
#     count = count+1




dataset = {
    "Jon": {
        "age": 35,
        "kids": 1
    },
    "andrew":{
        "age": 25,
        "kids": 0
    }
}



for person in dataset:
    # print person
    # print dataset[person]
    if dataset[person]['age'] > 18:
        print('{} is an adult').format(person)
    # for k, v in person:
    #     print k
    #     print v


my_list = ['apples', 'oranges', 'pickles']


# for fruit in my_list:
#     print fruit

# my_list.append('pineapple')

# print "Now...."

# for fruit in my_list:
#     print fruit




#server/flask website creation:


# @app.route("/")
# def hello():
#     return """
#     <html>
#     <head>
#     </head>
#     <body>
#     {}
#     </br>
#     </Br>
#     {}
#     <body/>
#     </html>
#     """.format(first_var, second_var)

# if __name__ == "__main__":
#     app.run()
    