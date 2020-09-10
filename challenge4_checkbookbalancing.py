import re

def formatTo2dp(number):
    return "{:.2f}".format(round(number, 2))

def balanceCheckbookLine(writer, line, previousBalance):
    cleanedLine = re.sub(r'[^\w^.^\s]', '', line)
    cleanedLine = cleanedLine.split(' ')
    amount = float(cleanedLine[2])
    cleanedLine[2] = formatTo2dp(amount)
    cleanedLine = " ".join(cleanedLine)
    formattedExpense = formatTo2dp(previousBalance-amount)
    cleanedLine += (" Balance "+formattedExpense)
    writer.write(cleanedLine+"\n")
    return float(formattedExpense)

def main():
    r = open('balance.txt', 'r')
    w = open('formatted.txt', 'w')
    counter = 0
    balance = 0
    for line in r:
        line = line.strip('\n')
        if counter == 0:
            balance = float(line)
            originalBalance = balance
            w.write("Original_Balance: "+formatTo2dp(balance)+"\n")
        else:
            balance = balanceCheckbookLine(w, line, balance)
        counter += 1
    w.write("Total expense "+formatTo2dp(originalBalance-balance)+"\n")
    w.write("Average expense "+formatTo2dp((originalBalance-balance)/(counter-1)))
    r.close()
    w.close()
main()
