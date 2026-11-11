def energy_per_day(kwh, days):
    if days <= 0:
        return "Кол-во дней должно быть больше нуля."
    return kwh / days

assert energy_per_day(100, 5) == 20
assert energy_per_day(50, 0) == "Кол-во дней должно быть больше нуля."
assert energy_per_day(0, 10) == 0

words = ["ход", "партия", "чемпионат"]
sorted_words = sorted(words, key=lambda word: len(word))
print(sorted_words)
        