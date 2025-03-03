def sum_even_numbers(start, end):
    return sum(num for num in range(start, end + 1) if num % 2 == 0)
#takes 2 parameters start and end
#Iyo ndo inagenerate sequence ya izo numbers from start to end
#Then from if kuendelea kazi yake ni kufilter even numbers pekeyake by checking if a number is divisible by 2
#Alafu iyo function ya sum inaokota even numbers zote