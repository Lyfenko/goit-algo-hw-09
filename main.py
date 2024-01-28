import time
from find_coins_greedy import find_coins_greedy
from find_min_coins import find_min_coins


def main():
    try:
        amount = int(input("Введіть суму для видачі решти: "))

        # Тестування жадібного алгоритму
        start_time = time.time()
        result_greedy = find_coins_greedy(amount)
        end_time = time.time()
        print("\nРезультат жадібного алгоритму:")
        print_coins(result_greedy)
        print(f"Час виконання жадібного алгоритму: {end_time - start_time:.10f} секунд")

        # Тестування алгоритму динамічного програмування
        start_time = time.time()
        result_dynamic = find_min_coins(amount)
        end_time = time.time()
        print("\nРезультат алгоритму динамічного програмування:")
        print_coins(result_dynamic)
        print(f"Час виконання алгоритму динамічного програмування: {end_time - start_time:.10f} секунд")

    except ValueError:
        print("Будь ласка, введіть коректне число для суми.")


def print_coins(coins_dict):
    for coin, count in coins_dict.items():
        print(f"{count} монет{' по' if count == 1 else 'ів по'} {coin} грн")


if __name__ == "__main__":
    main()
