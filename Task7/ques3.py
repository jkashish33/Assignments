class triple_comb:
    def triple_num(self):
        input_array = input("Enter the numbers:")
        input_split = input_array.split(',')
        result = []
        for i in range(len(input_split)):
            input_split[i] = int(input_split[i])
        for i in range(len(input_split)):
            sum = 0
            for j in range(i + 1, len(input_split)):
                for z in range(j + 1, len(input_split)):
                    sum = input_split[i] + input_split[j] + input_split[z]
                    if sum == 0:
                        temp = [input_split[i], input_split[j], input_split[z]]
                        result.append(temp)
                        break
        return result


a = triple_comb()
print(a.triple_num())