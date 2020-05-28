# Testing script for project2.py

import project2 as p


print("----------------------Sample #1 CSV----------------------")
output = p.main("sample_accounts.csv", 1)
print(f"{output=}")
print(output == [[26, 22, 28, 22, 16, 20, 31, 22, 13, 0]])
output = p.main("sample_accounts.csv",1,True)
print(f"{output=}")
print(output == [[0.13, 0.11, 0.14, 0.11, 0.08, 0.1, 0.155, 0.11, 0.065, 0.0]])
output = p.main("sample_accounts.csv",3)
print(f"{output=}")
print(output == [[26, 22, 28, 22, 16, 20, 31, 22, 13, 0], [17, 21, 23, 15, 15, 23, 30, 18, 14, 23], [14, 12, 23, 22, 22, 8, 21, 24, 25, 28]])

print("Testing with int input instead of boolean")
output = p.main("sample_accounts.csv",1,1)
print(f"{output=}")
print(output == [[0.13, 0.11, 0.14, 0.11, 0.08, 0.1, 0.155, 0.11, 0.065, 0.0]])


print("--------------------Testing with 8")
output = p.main("sample_accounts.csv",8,False)
print(f"{output=}")
print(output == [[26, 22, 28, 22, 16, 20, 31, 22, 13, 0], [17, 21, 23, 15, 15, 23, 30, 18, 14, 23], [14, 12, 23, 22, 22, 8, 21, 24, 25, 28]])
print("----------------------Sample #2 CSV----------------------")
output = p.main("sample_accounts2.csv", 1)
print(f"{output=}")
print("----------------------Sample #3 CSV----------------------")
output = p.main("sample_accounts3.csv", 1)
print(f"{output=}")
print(output == [[26, 22, 28, 22, 16, 20, 31, 22, 13, 0]])
output = p.main("sample_accounts3.csv",1,True)
print(f"{output=}")
print(output == [[0.13, 0.11, 0.14, 0.11, 0.08, 0.1, 0.155, 0.11, 0.065, 0.0]])
output = p.main("sample_accounts3.csv",3)
print(f"{output=}")
print(output == [[26, 22, 28, 22, 16, 20, 31, 22, 13, 0], [17, 21, 23, 15, 15, 23, 30, 18, 14, 23], [14, 12, 23, 22, 22, 8, 21, 24, 25, 28]])