   

def NumbersInWords(num):

    if not isinstance(num, int):
        return "only integers allowed"
    
    if num == None:
        return "Please enter a number"
    
    if num < 0:
        return "Please enter a positive number"
    
    if num > 999999999:
        return "highest number allowed is 999.999.999"

    if num == 0:
        return "zero"

    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    teens = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

    groups = [("million", 1000000), ("thousand", 1000), ("", 1)]
    words = []

    for group_name, group_base in groups:
        if num >= group_base:
            group_num = num // group_base
            num %= group_base

            if group_num >= 100:
                words.append(ones[group_num // 100] + " hundred")
                group_num %= 100
            
            if group_num >= 11 and group_num <= 19:
                words.append(teens[group_num - 10])
            
            elif group_num == 10 or group_num >= 20:
                words.append(tens[group_num // 10])
                
                if group_num % 10:
                    words.append(ones[group_num % 10])
            
            elif group_num > 0:
                words.append(ones[group_num])
            
            if group_name:
                words.append(group_name)

    return " ".join(words)
