class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        total_combos = 0
        existing_combos = []
        for i, a in enumerate(digits):
            for v, b in enumerate(digits):
                if i == v:
                    continue
                for j, c in enumerate(digits):
                    if i == j or v == j:
                        continue
                    new_combo = str(a) + str(b) + str(c)

                    if (int(new_combo) % 2 == 0) and (a != 0):
                        existing_combos.append(new_combo)

        removed_duplicates = set(existing_combos)
        # print(removed_duplicates)
        for combo in removed_duplicates:
            print(combo)
            total_combos += 1

        return total_combos
