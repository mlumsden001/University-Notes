class Calc:

    var_A = 0
    var_B = 0
    var_C = 0

    def set_A(num):
        var_A = num

    def set_B(num):
        var_B = num

    def set_C(num):
        var_C = num

    def add(nums):
        i = 0
        sum = 0
        while i < len(nums):
            sum += nums[i]
            i += 1
        return sum

    def subtract(num1, num2):
        sub = num1 - num2
        return sub

    def multiply(nums):
        i = 0
        sum = 0
        while i < len(nums):
            if nums[i] == 'A':
                sum *= var_A
            if nums[i] == 'B':
                sum *= var_B
            if nums[i] == 'C':
                sum *= var_C
            sum *= nums[i]
            i += 1
        return sum

    def divide(n1, n2):
        if n1 == 'A':
            n1 = var_A
        if n1 == 'B':
            n1 = var_B
        if n1 == 'C':
            n1 == var_C
        if n2 == 'A':
            n2 = var_A
        if n2 == 'B':
            n2 = var_B
        if n2 == 'C':
            n2 == var_C
        div = n1/n2
        return div
