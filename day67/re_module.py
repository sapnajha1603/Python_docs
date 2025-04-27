import re


paragraph1 = "Hello, I am Sapna! And i am very excited to learn about substitution function, in the re module."


cleaned_para = re.sub(r'[^\w\s]', " ", paragraph1.lower())


print(f"\n{cleaned_para}")