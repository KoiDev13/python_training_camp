from emailSlicer import validateEmail
from emailSlicer import emailProcessing
from emailSlicer import printMsg
from sqlalchemy import false, true

def main():
    """This is main function."""
    emails = [
        'akn@gmail.com',
        'python@df',
        'pulmap@xinhdep.vn',
    ]
    try:
        for email in emails:
            valid = validateEmail(email)
            if valid == true:
                print("Valid email!")
                user_name, domain_name = emailProcessing(email)
                printMsg(user_name, domain_name)
            else: 
                print(f"Email {email} is invalid!")
    except:
        print("Debug please!")

if __name__ == "__main__":
    main()