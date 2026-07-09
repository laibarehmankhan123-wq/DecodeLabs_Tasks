total =0
print("ஜ۩۞۩ஜ|𝙴𝚇𝙿𝙴𝙽𝚂𝙴 𝚃𝚁𝙰𝙲𝙺𝙴𝚁| ஜ۩۞۩ஜ")
print("Enter your expenses one by one")
print("Type 'done' when you're finished.\n")

while True:
    expense=input("Enter an expense (or 'done' to finish): ")
    if expense.lower()=="done": 
        break
    try:
        expense=float(expense)
    except ValueError:
        print("Invalid input! Enter the valid number")
        continue
    if expense <0:
        print("Expense cannot be negative")
        continue

    total+=expense
    print(f"Current total expenses: {total}")
print("======================")
print("𝓔𝓧𝓟𝓔𝓝𝓢𝓔 𝓢𝓤𝓜𝓜𝓐𝓡𝓨")
print("======================")
print(f"Total Spent: ${total:.2f}")
print("𝘛𝘩𝘢𝘯𝘬 𝘺𝘰𝘶 𝘧𝘰𝘳 𝘶𝘴𝘪𝘯𝘨 𝘵𝘩𝘦 𝘌𝘹𝘱𝘦𝘯𝘴𝘦 𝘛𝘳𝘢𝘤𝘬𝘦𝘳!")
