def is_match(pattern, s):
    m, n = len(pattern), len(s)

    # dp[i][j] будет True, если первые i символов pattern могут соответствовать первым j символам s
    dp = [[False] * (n + 1) for _ in range(m + 1)]

    # Пустая строка соответствует пустому шаблону
    dp[0][0] = True

    # Инициализация для шаблона, начинающегося с '*'
    for i in range(1, m + 1):
        if pattern[i - 1] == '*':
            dp[i][0] = dp[i - 1][0]

    # Заполнение таблицы dp
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if pattern[i - 1] == s[j - 1] or pattern[i - 1] == '?':
                dp[i][j] = dp[i - 1][j - 1]
            elif pattern[i - 1] == '*':
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]

    # Ответ в правом нижнем углу таблицы
    return dp[m][n]


def main(input_data, output_file):
    lines = input_data.strip().split("\n")
    pattern = lines[0]
    s = lines[1] if len(lines) > 1 else ''

    if is_match(pattern, s):
        output_file.write("YES\n")
    else:
        output_file.write("NO\n")


if __name__ == '__main__':
    import sys
    import os

    input_path = sys.argv[1] if len(sys.argv) > 1 else "../txtf/input.txt"
    output_path = sys.argv[2] if len(sys.argv) > 2 else "../txtf/output.txt"

    if not os.path.exists(input_path):
        print(f"Ошибка: файл '{input_path}' не найден!")
        sys.exit(1)

    try:
        with open(input_path, "r") as input_file:
            input_data = input_file.read()

        with open(output_path, "w") as output_file:
            main(input_data, output_file)

        print(f"Результат успешно записан в файл '{output_path}'")
    except Exception as e:
        print(f"Ошибка при обработке: {e}")




