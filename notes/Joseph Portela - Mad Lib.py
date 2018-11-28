print("Welcome to Your Very Own Mad Lib, otherwise known as YVOML! Please answer each prompt.")
print()

# Inputs


responses = [input("Enter a plural noun. "), input("Enter another plural noun. "), int(input("Enter a number. ")),
             input("Enter another plural noun. "), input("Enter a verb ending in ing. "),
             input("Enter another plural noun. "), input("Enter a name. "), input("Enter an adjective. "),
             input("Enter a noun. "), input("Enter yet another plural noun. "), input("Enter another noun. "),
             int(input("Enter another number. ")), input("Enter another plural noun. ")]

# Story

print("Great! YVOML is now complete, here is the result:")
print("Welcome to the Cult of %s, we believe that %s are really gods in disguise!" % (responses[0], responses[1]))
print("We hold services %d days a week, and each service we hold a holy %s." % (responses[2], responses[3]))
print("If you're interested, read our holy book, written by the God of %s." % responses[4])
print("I highly recommend the book of %s, it includes the famous story of the %s %s." % (responses[5], responses[6],
                                                                                         responses[7]))
print("In the cult of %s, our goal is eternal dedication to the one great god of %s." % (responses[8], responses[9]))
print("All who follow him will receive a %s in the afterlife, as well as %d %s." % (responses[10], responses[11],
                                                                                    responses[12]))
print("Wait, Where are you going? Please stay! I have... so much more to tell you... *sigh* Next house then...")
