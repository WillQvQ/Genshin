def process(character: dict):
    character["ATK_0"] = character["ATK_0_0"] + character["ATK_0_1"]
    if "ATK_1_0" not in character and "ATK" in character:
        character["ATK_1_0"] = round(100 * (character["ATK"] - character["ATK_0"]) / character["ATK_0"], 1)
    if "CRIT_rate_0" not in character and "CRIT_rate" in character:
        character["CRIT_rate_0"] = character["CRIT_rate"] - (
            character["CRIT_rate_1"] if "CRIT_rate_1" in character else 0)
    if "CRIT_DMG_0" not in character and "CRIT_DMG" in character:
        character["CRIT_DMG_0"] = character["CRIT_DMG"] - (character["CRIT_DMG_1"] if "CRIT_DMG_1" in character else 0)
    
    character["ATK_1"] = character["ATK_1_0"] + (character["ATK_1_1"] if "ATK_1_1" in character else 0)
    character["CRIT_rate"] = character["CRIT_rate_0"] + (character["CRIT_rate_1"] if "CRIT_rate_1" in character else 0)
    character["CRIT_DMG"] = character["CRIT_DMG_0"] + (character["CRIT_DMG_1"] if "CRIT_DMG_1" in character else 0)
    
    if "name" in character:
        length = len(character["name"])
        print("*" * (24 - length // 2), character["name"], "*" * (24 - (length + 1) // 2))
    final_value = character["ATK_0"]
    GR_ATK_1 = (100 + character["ATK_1"] + 4.64) / (100 + character["ATK_1"]) * 100 - 100
    GR_DMG_bonus = (100 + character["DMG_bonus"] + 4.66) / (100 + character["DMG_bonus"]) * 100 - 100
    GR_CRIT_rate = (10000 + (character["CRIT_rate"] + 3.11) * character["CRIT_DMG"]) / (
        10000 + character["CRIT_rate"] * character["CRIT_DMG"]) * 100 - 100
    GR_CRIT_DMG = (10000 + character["CRIT_rate"] * (character["CRIT_DMG"] + 6.22)) / (
        10000 + character["CRIT_rate"] * character["CRIT_DMG"]) * 100 - 100
    print("基础攻击力", character["ATK_0"])
    print("攻击区倍率", character["ATK_1"])
    final_value *= 1 + character["ATK_1"] / 100
    print("增伤区倍率", character["DMG_bonus"])
    final_value *= 1 + character["DMG_bonus"] / 100
    print("暴击率", character["CRIT_rate"])
    print("暴击伤害", character["CRIT_DMG"])
    final_value *= 1 + character["CRIT_rate"] * character["CRIT_DMG"] / 10000
    print("基础攻击力*总倍率", round(final_value, 1))
    print(
        "词条推荐(与2%之间的差距):", round(GR_ATK_1 - 2, 2), round(GR_DMG_bonus - 2, 2), round(GR_CRIT_rate - 2, 2),
        round(GR_CRIT_DMG - 2, 2)
    )
    return final_value, character


def process_health(character: dict):
    if "CRIT_rate_0" not in character and "CRIT_rate" in character:
        character["CRIT_rate_0"] = character["CRIT_rate"] - (
            character["CRIT_rate_1"] if "CRIT_rate_1" in character else 0)
    if "CRIT_DMG_0" not in character and "CRIT_DMG" in character:
        character["CRIT_DMG_0"] = character["CRIT_DMG"] - (character["CRIT_DMG_1"] if "CRIT_DMG_1" in character else 0)
    if "HP_1_0" not in character and "HP" in character:
        character["HP_1_0"] = round((character["HP"] - character["HP_0"]) / character["HP_0"] * 100, 2)
    
    character["HP_1"] = character["HP_1_0"] + (character["HP_1_1"] if "HP_1_1" in character else 0)
    character["CRIT_rate"] = character["CRIT_rate_0"] + (character["CRIT_rate_1"] if "CRIT_rate_1" in character else 0)
    character["CRIT_DMG"] = character["CRIT_DMG_0"] + (character["CRIT_DMG_1"] if "CRIT_DMG_1" in character else 0)
    
    if "name" in character:
        length = len(character["name"])
        print("*" * (24 - length // 2), character["name"], "*" * (24 - (length + 1) // 2))
    final_value = character["HP_0"]
    GR_HP_1 = (100 + character["HP_1"] + 4.64) / (100 + character["HP_1"]) * 100 - 100
    GR_DMG_bonus = (100 + character["DMG_bonus"] + 4.66) / (100 + character["DMG_bonus"]) * 100 - 100
    GR_CRIT_rate = (10000 + (character["CRIT_rate"] + 3.11) * character["CRIT_DMG"]) / (
        10000 + character["CRIT_rate"] * character["CRIT_DMG"]) * 100 - 100
    GR_CRIT_DMG = (10000 + character["CRIT_rate"] * (character["CRIT_DMG"] + 6.22)) / (
        10000 + character["CRIT_rate"] * character["CRIT_DMG"]) * 100 - 100
    print("基础生命值", character["HP_0"])
    print("生命区倍率", character["HP_1"])
    final_value *= 1 + character["HP_1"] / 100
    print("增伤区倍率", character["DMG_bonus"])
    final_value *= 1 + character["DMG_bonus"] / 100
    print("暴击率", character["CRIT_rate"])
    print("暴击伤害", character["CRIT_DMG"])
    final_value *= 1 + character["CRIT_rate"] * character["CRIT_DMG"] / 10000
    print("基础攻击力*总倍率", round(final_value, 1))
    print(
        "词条推荐(与2%之间的差距):\n 生命  增伤  暴击  爆伤\n", round(GR_HP_1 - 2, 2), round(GR_DMG_bonus - 2, 2), round(GR_CRIT_rate - 2, 2),
        round(GR_CRIT_DMG - 2, 2)
    )
    return final_value, character


def calc_demo(*characters: dict, hp=False):
    base = characters[0]
    f = 0
    for i, character in enumerate(characters):
        base.update(character)
        if hp:
            v, _ = process_health(base)
        else:
            v, _ = process(base)
        if f == 0:
            f = v
        print("[={}=] {}%".format(i, round(v / f * 100, 2)))


if __name__ == "__main__":
    calc_demo(
        {
            "name": "Neuvillette + Sacrificial Jade",
            "HP_0": 12965,
            "HP": 40312,
            "HP_1_1": 32,
            "DMG_bonus": 0 + 15 + 30,
            "CRIT_rate": 51.4,
            "CRIT_DMG": 178.3
        },{
            "name": "Neuvillette + Sacrificial Jade",
            "HP_0": 12965,
            "HP": 40312,
            "HP_1_1": 32-46.6,
            "DMG_bonus": 0 + 15 + 30 + 34.8,
            "CRIT_rate": 51.4,
            "CRIT_DMG": 178.3
        }, hp=True
    )
    # calc_demo({
    #     "name": "NG+Winds",
    #     "ATK_0_0": 212,
    #     "ATK_0_1": 608,
    #     "ATK": 1835,
    #     "DMG_bonus": 46.6 + 15 + 16,
    #     "CRIT_rate_1": 33.1,
    #     "CRIT_rate": 80,
    #     "CRIT_DMG": 160,
    # }, {
    #     "name": "NG+NEW",
    #     "ATK_0_1": 674,
    #     # "ATK_1_1": 12,
    #     "DMG_bonus": 46.6 + 15 + 26,
    #     "CRIT_rate_1": 22.1,
    # })
    #
    # print()
    # print("*"*50)
    # print()
    # calc_demo({
    #     "name": "GY+Magic",
    #     "ATK_0_0": 922-608,
    #     "ATK_0_1": 608,
    #     "ATK": 2430,
    #     "DMG_bonus": 46.6 + 15,
    #     "CRIT_rate": 50.1+30,
    #     "CRIT_DMG": 223.7,
    #     "CRIT_DMG_1": 66.2,
    # }, {
    #     "name": "GY+Water",
    #     "ATK_0_1": 542,
    #     "ATK_1_1": -48,
    #     "DMG_bonus": 46.6 + 15 + 20,
    #     "CRIT_DMG_1": 88.2,
    # })
