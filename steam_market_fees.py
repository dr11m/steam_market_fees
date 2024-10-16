def get_price_minus_fees(name: str, price: float)-> float:
    intervals = [0.02, 0.21, 0.32, 0.43]
    fees = [0.02, 0.03, 0.04, 0.05, 0.07, 0.09]

    while price > intervals[-1]:
        last_element = intervals[-1]
        if len(intervals) % 2 == 0:
            intervals.append(round(last_element + 0.12, 2))
        else:
            intervals.append(round(last_element + 0.11, 2))

    while len(intervals) > len(fees):
        last_element = fees[-1]
        if len(fees) % 2 == 0:
            fees.append(round(last_element + 0.01, 2))
        else:
            fees.append(round(last_element + 0.02, 2))

    first_greater = next(value for value in intervals if value >= price)
    index_of_first_greater = intervals.index(first_greater)
    amount_minus_fee = round(price - fees[index_of_first_greater - 1], 2)
    fee = round(price - amount_minus_fee, 2)
    
    print(f"{name} -  get_price_minus_fees: input: {price}, | fee: {fee} | input - fee: {amount_minus_fee}")

    return amount_minus_fee


def get_price_plus_fees(name: str, input_value: float) -> float:
    """Получаем сумму без комисии, которую получит продавец в стиме"""
    intervals = [0.19]
    fees = [0.02, 0.03, 0.04, 0.06, 0.07, 0.09]

    while input_value > intervals[-1]:
        intervals.append(round(intervals[-1] + 0.1, 2))

    while len(intervals) > len(fees):
        last_element = fees[-1]
        if len(fees) % 2 == 0:
            fees.append(round(last_element + 0.01, 2))
        else:
            fees.append(round(last_element + 0.02, 2))

    index_of_last_element = intervals.index(intervals[-1])
    amount_plus_fee = round(input_value + fees[index_of_last_element], 2)
    
    fee = round(amount_plus_fee - input_value, 2)
    print(f"{name} - get_price_plus_fees: {input_value}| fee: {fee} | input - fee: {amount_plus_fee}")
    
    return amount_plus_fee



if __name__ == "__main__":
    number = 0.65
    price_plus_fee = get_price_plus_fees("test", number)
    price_minus_fee = get_price_minus_fees("test", number)
    print(price_minus_fee, price_plus_fee)
