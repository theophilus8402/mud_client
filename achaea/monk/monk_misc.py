from client import c, send

misc_aliases = [
    (
        "^he$",
        "say house phrase",
        lambda matches: send("speak cyrenese;say Open the gate."),
    ),
]
c.add_aliases("sarmenti_misc", misc_aliases)
