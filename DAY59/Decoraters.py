# The decoraters are used to decorate the function with greetings by adding the random text before and after
#  the execution of the function like(Good morning , Thank you)

def greet(fx):      # This will take the function as an Argument

    def message(*args , **kwargs):              # This is custom function for printing the messages
        print("Good Morning")
        fx(*args , **kwargs)
        print("Thank You")
    return message

@greet                    # This was added above the function for which we want to run our custom messages
def hello():
    print("Hello World")

hello()


@greet
def Add(a,b):
    print("The addition is",a+b)

Add(5 , 5)