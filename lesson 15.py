def save_scores(path: str, scores: dict[str, int]) -> None:
    with open(path, "w", encoding="utf-8") as file:
        for name, score in scores.items():
            file.write(f"{name}:{score}\n")
save_scores("data/scores.txt", {"ნინო": 92, "გიორგი": 78, "ანა": 85})
def add_score(path: str, name: str, score: int) -> None:
    with open(path, "a", encoding="utf-8") as file:
        file.write(f"{name}:{score}\n")
add_score("data/scores.txt", "დათო", 64)
add_score("data/scores.txt", "მარიამი", 97)

def read_scores(path: str) -> dict[str, int]:
    scores = {}

    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            name, score = line.strip().split(":")
            scores[name] = int(score)

    return scores
scores = read_scores("data/scores.txt")
print(scores)

print("სტუდენტები:", len(scores))

average = sum(scores.values()) / len(scores)
print("საშუალო ქულა:", round(average, 1))
best_name = max(scores, key=scores.get)
print("საუკეთესო:", best_name, scores[best_name])

with open("data/passed.txt", "w", encoding="utf-8") as file:
    for name, score in scores.items():
        if score >= 80:
            file.write(f"{name}\n")

with open("data/passed.txt", "r", encoding="utf-8") as file:
    passed = [line.strip() for line in file]

print("ჩააბარეს (80+):", passed)