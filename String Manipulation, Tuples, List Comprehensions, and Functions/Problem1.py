def process_email(email):
    clean_email = email.strip().lower()
    username, domain = clean_email.split("@")
    return (username, domain)


email = "  USER123@Gmail.com  "
result = process_email(email)
print(result)
