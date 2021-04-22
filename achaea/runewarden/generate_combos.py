shield_cmds = [
    ("h", "smash high"),
    ("m", "smash mid"),
    ("l", "smash low"),
    ("d", "drive"),
    ("c", "concuss"),
    ("t", "trip"),
    ("b", "club"),
]

venoms = [
    ("a", "aconite"),
    ("c", "curare"),
    ("s", "slike"),
    ("k", "kalmia"),
    ("g", "gecko"),
    ("x", "xentio"),
    ("p", "prefarar"),
    ("d", "digitalis"),
    ("es", "epseth"),
    ("et", "epteth"),
    ("v", "vernalius"),
]


def craft_alias(venom_alias, shield_alias):
    return f"^c{venom_alias}{shield_alias}$"


def craft_cmd(venom, shield_cmd):
    return f"stand;combination &tar slice {venom} {shield_cmd}"


def craft_combo(venom_attacks):
    for venom, shield_cmd in venom_attacks:
        venom_alias, venom_name = venom
        shield_alias, shield_att = shield_cmd
        alias = craft_alias(venom_alias, shield_alias)
        cmd = craft_cmd(venom_name, shield_att)
        yield alias, cmd


def write_weaponmastery(file_path):
    with open(file_path, "w") as f:
        f.write("\n")
        f.write("from achaea.basic import eqbal\n")
        f.write("from achaea.state import s\n")
        f.write("from client import c, send\n")
        f.write("\n")
        f.write("weaponmastery_aliases = [\n")

        venom_attacks = ((v, s) for v in venoms for s in shield_cmds)
        for alias, cmd in craft_combo(venom_attacks):
            f.write("   (\n")
            f.write(f'       "{alias}",\n')
            f.write(f'       "{cmd}"\n')
            f.write(f'       lambda m: eqbal("{cmd}")\n')
            f.write("   ),\n")

        f.write("]\n")
        f.write('c.add_aliases("ab_weaponmastery", weaponmastery_aliases)\n')


if __name__ == "__main__":

    """
    for venom_alias, venom in venoms:
        for shield_alias, shield_cmd in shield_cmds:
            alias = craft_alias(venom_alias, shield_alias)
            cmd = craft_cmd(venom, shield_cmd)

            print(alias)
            print(cmd)
            print()
    """
    write_weaponmastery("test_weaponmastery.py")
